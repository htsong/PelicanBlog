Title: 正式开始使用 Pelican
Date: 2020-09-14 11:10
Category: 开发

今早为Blog加了评论插件，可以hello中看到效果，但与原先设想相差较大。

测试一下嵌入卡片插件， 还不能正常工作，原因是没有办法获取到已经安装的docutils模块，似乎是该模块安装到env时动作不正确，会被默认安装到root所致。

卡片插件当前效果如下，仅仅被解释为普通的链接：

[!embedlycard](http://physics.stackexchange.com/questions/5265/cooling-a-cup-of-coffee-with-help-of-a-spoon)

[!embedlycard?chrome=1](https://www.youtube.com/watch?v=E43-CfukEgs)

Youtube

[!embedlycard?chrome=1](http://www.baidu.com)

这引发了我的好奇心，Pelican的架构和插件体系是怎样的呢？ 
