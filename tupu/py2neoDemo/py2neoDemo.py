# -*- coding: utf-8 -*-
import os
import pandas as pd
# -*- coding: utf-8 -*-
from py2neo import Node, Graph, Relationship, NodeMatcher
import sys

invoice_data = pd.read_excel('Invoice_data_Demo.xls', header=0)


class DataToNeo4j(object):
    """将excel中数据存入neo4j"""

    def __init__(self):
        """建立连接"""
        link = Graph("http://localhost:7474", username="neo4j", password="123456")
        self.graph = link
        # self.graph = NodeMatcher(link)
        # 定义label
        self.buy = 'buy'
        self.sell = 'sell'
        self.graph.delete_all()
        self.matcher = NodeMatcher(link)

    def create_node(self, node_buy_key, node_sell_key):
        """建立节点"""
        for name in node_buy_key:
            buy_node = Node(self.buy, name=name)
            self.graph.create(buy_node)
        for name in node_sell_key:
            sell_node = Node(self.sell, name=name)
            self.graph.create(sell_node)

    def create_relation(self, df_data):
        """建立联系"""
        m = 0
        for m in range(0, len(df_data)):
            try:
                print(list(self.matcher.match(self.buy).where("_.name=" + "'" + df_data['buy'][m] + "'")))
                print(list(self.matcher.match(self.sell).where("_.name=" + "'" + df_data['sell'][m] + "'")))
                rel = Relationship(
                    self.matcher.match(self.buy).where("_.name=" + "'" + df_data['buy'][m] + "'").first(),
                    df_data['money'][m],
                    self.matcher.match(self.sell).where("_.name=" + "'" + df_data['sell'][m] + "'").first())

                self.graph.create(rel)
            except AttributeError as e:
                print(e, m)


# print(invoice_data)

# 可以先阅读下文档：https://py2neo.org/v4/index.html

def data_extraction():
    """节点数据抽取"""
    # 取出购买方名称到list
    node_buy_key = []
    for i in range(0, len(invoice_data)):
        node_buy_key.append(invoice_data['购买方名称'][i])

    node_sell_key = []
    for i in range(0, len(invoice_data)):
        node_sell_key.append(invoice_data['销售方名称'][i])

    # 去除重复的发票名称
    node_buy_key = list(set(node_buy_key))
    node_sell_key = list(set(node_sell_key))

    # value抽出作node
    node_list_value = []
    for i in range(0, len(invoice_data)):
        for n in range(1, len(invoice_data.columns)):
            # 取出表头名称invoice_data.columns[i]
            node_list_value.append(invoice_data[invoice_data.columns[n]][i])
    # 去重
    node_list_value = list(set(node_list_value))
    # 将list中浮点及整数类型全部转成string类型
    node_list_value = [str(i) for i in node_list_value]

    return node_buy_key, node_sell_key, node_list_value


def relation_extraction():
    """联系数据抽取"""
    links_dict = {}
    sell_list = []
    money_list = []
    buy_list = []

    for i in range(0, len(invoice_data)):
        money_list.append(invoice_data[invoice_data.columns[19]][i])  # 金额
        sell_list.append(invoice_data[invoice_data.columns[10]][i])  # 销售方方名称
        buy_list.append(invoice_data[invoice_data.columns[6]][i])  # 购买方名称

    # 将数据中int类型全部转成string
    sell_list = [str(i) for i in sell_list]
    buy_list = [str(i) for i in buy_list]
    money_list = [str(i) for i in money_list]

    # 整合数据，将三个list整合成一个dict
    links_dict['buy'] = buy_list
    links_dict['money'] = money_list
    links_dict['sell'] = sell_list
    # 将数据转成DataFrame
    df_data = pd.DataFrame(links_dict)
    print(df_data)
    return df_data


relation_extraction()
try:
    create_data = DataToNeo4j()
except:
    print("连接图数据库失败哦")
    sys.exit(0)

create_data.create_node(data_extraction()[0], data_extraction()[1])
create_data.create_relation(relation_extraction())
