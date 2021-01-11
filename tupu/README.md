## 知识图谱笔记

> 推荐b站课程“[2020年最新知识图谱（python） 机器学习 深度学习进阶](https://www.bilibili.com/video/BV14a4y1j7mg)”

neo4j基本语句
- 创建节点`create(n:Person{name:"我",age:12})`
- 创建一个关系`create(p:Person{name:"我",age:12})-[:包工程{金额:100}]->(n:Person{name:"好大哥",age:22})`
- 删除节点`match(n:Person{name:"张三"}) delete n`
- 删除关系`match(p:Person{name:"我",age:12})-[f:包工程{金额:100}]->(n:Person{name:"好大哥",age:22}) delete f`
- 加标签`match(t:Person) where id(t)=173 set t:好人 return t`
- 添加属性`match(t:好人) where id(t)=173 set t.战斗力=200 return t`
- 修改属性`match(t:好人) where id(t)=173 set t.战斗力=500 return t`
- 查询一个关系`match(p:Person)-[:包工程]->(n:Person) return p,n`
- 清空数据`MATCH (n) DETACH DELETE n`