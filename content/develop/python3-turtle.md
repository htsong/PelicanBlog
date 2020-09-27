Title: Python3 中内置的海龟语言 (turtle module)
Date: 2020-09-27 11:18
Category: 开发

Python内置了turtle库，基本上100%复制了原始的Turtle Graphics的所有功能。Turtle 概念来自于1966年 Seymour Papert 
（西摩尔·帕普特）和 Wally Feurzig发明的一种专门给儿童学习编程的语言——LOGO语言，它的特色就是通过编程指挥一个小海龟
（turtle）在屏幕上绘图。

# 西摩尔·帕普特

![Seymour Papert](http://www.kidscode.cn/Uploads/Editor/2016-08-04/57a2a01bc4b3a.jpg)

西摩尔·帕普特（Seymour Papert，1928.2.29~2016.7.31）驾鹤西归，麻省理工学院（MIT）校长拉斐尔·赖夫（Rafael Reif）
在 MIT 官网的讣告文里总结说，西摩尔·帕普特至少给三个领域带来了革命，分别是儿童发展、人工智能，以及科技与教育之融合。
能够在上述任何一个领域做出一点成绩都不容易了，而帕普特则横跨三个领域，而且对这三个领域的发展都带来了极为深远的影响。
尼古拉斯·尼葛洛庞帝（Nicholas Negreponte）在 TED 上做过个演讲，是介绍他2006年启动的名为 “One Laptop Per Child” 
的教育项目的，演讲中Negreponte深情地回忆起西摩尔·帕普特，“每一台 OLPC 电脑里其实都印刻着帕普特的思想”。

对此有兴趣可以看一下帕普特1981年写的 《Mindstorms》[链接](https://pan.baidu.com/s/1jGoiCmy)，这本书1993年再版，
去年还出了个[中译本](https://book.douban.com/subject/30418117/)，加了个副标题，“计算机如何改变我们的思考与学习”。
试摘录一段：
>慢慢地，我开始领会到学习的真谛：一件事情，如果你能把它融会贯通到自己的思维方式中，那它就会变得异常简单；如果不能，
>那它就比登天还难。 在这里我提出的是一个和皮亚杰的理论有共通之处的想法：对学习的理解必须是缘起性的。这就是说，它必
>须追溯到知识的缘起。

帕普特发明 LOGO 是希望小孩能够通过学编程，接触到「有力量的」数学概念，而编程则是实现这一目标的极佳手段。《Mindstorms》
一书的1981年原版的副标题是 “Children, Computers, and Powerful Ideas”，其实 powerful ideas 才是帕普特最为关注的东西。
编程本身并不能使你成为更懂得思考的人，只有当你通过编程，在与电脑上交互中加深了对世界的理解和认识之后，才真正接触到了帕普
特说的 powerful ideas。

# Turtle in Python3

廖雪峰的Python3站点上有关于Turtle模块的入门[介绍](https://www.liaoxuefeng.com/wiki/1016959663602400/1249593505347328)
但廖的介绍比较粗略，知乎上有个还不错的入门[Turtle指南](https://zhuanlan.zhihu.com/p/64594462)。

如果说到权威，还是得看Python3的[Turtle官方文档](https://docs.python.org/zh-cn/3/library/turtle.html)。

以我的经验，如果有初步的python基础后，只要花上5到10分钟搞清楚下面三点，就可以快速开始使用turtle：

1.海龟绘图的坐标系；

2.海龟的基本运动控制，如移动、转角、……

3.海龟的基本绘图指令，如抬笔、落笔、颜色、……

看一段turtle的代码，自己也尝试一下：

![turtle-sample](http://www.kidscode.cn/Uploads/Editor/2016-08-04/57a2a0cf8bd03.jpg)

看到海龟的杰作了吧？你是不是也有点小兴奋呢？

-----------
【参考文献】

1.尼古拉斯·尼葛洛庞帝，每个儿童一台笔记本电脑，[DB/OL] https://www.youtube.com/watch?v=W5ySOqtxhbw，20070116

2.尼古拉斯·尼葛洛庞帝，每童一电脑计划的两年进展，[DB/OL] https://www.youtube.com/watch?v=y_TKjfgjiQs，20080627

3.LOGO（小海龟）编程之父留给我们的思想遗产，[EB/OL] http://www.kidscode.cn/archives/3720，20160804
