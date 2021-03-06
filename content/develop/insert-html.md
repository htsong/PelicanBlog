Title: 用 html 扩展 Pelican 的 Markdown
Date: 2020-09-15 16:01
Category: 开发
Tags: pelican, markdown, blog

测试字体和特殊格式，参考了 [markdown种嵌入html标签，实现自定义样式](https://my.oschina.net/u/4404259/blog/3330517)。
<span style='color:red'>This is red</span> //字体颜色 <ruby> 漢 <rt> ㄏㄢˋ </rt> </ruby> // 特殊字 <kbd>Ctrl</kbd>+<kbd>F9</kbd> // 按键标识 <span style="font-size:2rem; background:yellow;">**Bigger**</span> //字体大小和背景 <font face="微软雅黑" color="red" size="6">字体及字体颜色和大小</font> <font color="#0000ff">字体颜色</font> <p align="left">居左文本</p> <p align="center">居中文本</p> <p align="right">居右文本</p>

测试插入数学公式：

Markdown 中 LaTex 语法可以参考 [MarkDown 中使用 LaTeX 数学式](https://www.cnblogs.com/kikochz/p/13570585.html)

* 方法1：用 http://latex.codecogs.com 的根据 latex 生成图片的功能

<img src="http://latex.codecogs.com/png.latex?\dpi{110}&space;E=mc^2&space;" title="http://latex.codecogs.com/png.latex?\dpi{110} E=mc^2 " />

感觉装载速度比较慢。

* 方法2：用 [render math](https://github.com/pelican-plugins/render-math) 插件 [官网](https://pypi.org/project/pelican-render-math/)

Inline Math
Math between $..$, for example, $x^2$, will be rendered inline with respect to the current HTML block. Note: To use inline math, there must not be any whitespace before the ending $. So for example: ${f(x)=a_nx^n+a_{n-1}x^{n-1}+a_{n-2}x^{n-2}}+\cdots$

Relevant inline math: $e=mc^2$
Will not render as inline math: $40 vs $50
Displayed Math
Math between $$..$$ will be rendered "block style", for example, $$x^2$$, will be rendered centered in a new paragraph.

$${f(x)=a_nx^n+a_{n-1}x^{n-1}+a_{n-2}x^{n-2}}+\cdots \tag{1.1}$$


测试插入图片：

![堆肥机外观](../images/20200916堆肥机.png)

再试试用 img 标签, 参考了 [Markdown-图片设置（大小，居中）](https://blog.csdn.net/qq_35451572/article/details/79443467)， 注意其中有错误，下面代码中已更正。
<div align="center">
  <img src="https://github.com/htsong/PelicanBlog/blob/master/content/business/20200916%E5%A0%86%E8%82%A5%E6%9C%BA.png?raw=true" 
       width = "400" height = "200" />
  <p align="center">堆肥机外观</p>
</div>

测试一下嵌入 YOUTUBE 视频， 参考了 [Pelican YouTube](https://github.com/kura/pelican_youtube/tree/407b97b49112345ea3dfe76f1a5ae41586c4ffb1)。
<div class="youtube youtube-16x9">
<iframe src="https://www.youtube.com/embed/VIDEO_ID" allowfullscreen seamless frameBorder="0"></iframe>
</div>

如果只看到个灰色块，也别气馁，再试试B站呗，参考了 [博客页面嵌入bilibili视频（iframe框架）推荐比例](https://www.deeplearn.site/daily-life/85.html)。
<iframe src="//player.bilibili.com/player.html?aid=370583020&page=1"  
  scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" 
  style="width:330px; height:200px"> 
</iframe>

这里面的视频地址可以在B站视频的下方分享窗口获取，可在 [在网页中使用iframe嵌入B站视频（腾讯视频同理）](https://blog.csdn.net/DSH964/article/details/80961598) 中看到具体的操作指引。

测试表格插入：
<table> 
  <tr> <td>1</td> <td>2</td> </tr> 
  <tr> <td>3</td> <td>4</td> </tr>
</table>

<h3> 嵌入一段 StackOverflow 的 post: </h3>
<p>
   <a class=embedly-card data-card-chrome=0 href=http://physics.stackexchange.com/questions/5265/cooling-a-cup-of-coffee-with-help-of-a-spoon></a> 
   <script>
            !function(a){
                var b="embedly-platform",c="script";
                if(!a.getElementById(b)){
                    var d=a.createElement(c);
                    d.id=b;
                    d.src=("https:"===document.location.protocol?"https":"http")+"://cdn.embedly.com/widgets/platform.js";
                    var e=document.getElementsByTagName(c)[0];e.parentNode.insertBefore(d,e)}
                }(document);
   </script> 
</p> 

### 按照 Embdely_Cards 插件的方法嵌入Youtube视频:
<h3>Embedding a YouTube video <em>with</em> card border:</h3>
<p>
  <a class=embedly-card data-card-chrome=1 href="https://www.youtube.com/watch?v=E43-CfukEgs"></a>
  <script>
            !function(a){
                var b="embedly-platform",c="script";
                if(!a.getElementById(b)){
                    var d=a.createElement(c);
                    d.id=b;
                    d.src=("https:"===document.location.protocol?"https":"http")+"://cdn.embedly.com/widgets/platform.js";
                    var e=document.getElementsByTagName(c)[0];e.parentNode.insertBefore(d,e)}
                }(document);
   </script> 
</p> 

