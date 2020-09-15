Title: 用 html 扩展 Pelican 的 Markdown
Date: 2020-09-15 16:01
Category: 开发

测试字体和特殊格式，参考了 [markdown种嵌入html标签，实现自定义样式](https://my.oschina.net/u/4404259/blog/3330517)。
<span style='color:red'>This is red</span> //字体颜色 <ruby> 漢 <rt> ㄏㄢˋ </rt> </ruby> // 特殊字 <kbd>Ctrl</kbd>+<kbd>F9</kbd> // 按键标识 <span style="font-size:2rem; background:yellow;">**Bigger**</span> //字体大小和背景 <font face="微软雅黑" color="red" size="6">字体及字体颜色和大小</font> <font color="#0000ff">字体颜色</font> <p align="left">居左文本</p> <p align="center">居中文本</p> <p align="right">居右文本</p>

测试一下嵌入 YOUTUBE 视频， 参考了 [Pelican YouTube](https://github.com/kura/pelican_youtube/tree/407b97b49112345ea3dfe76f1a5ae41586c4ffb1)。
<div class="youtube youtube-16x9">
<iframe src="https://www.youtube.com/embed/VIDEO_ID" allowfullscreen seamless frameBorder="0"></iframe>
</div>

测试表格插入：
<table> 
  <tr> <td>1</td> <td>2</td> </tr> 
  <tr> <td>3</td> <td>4</td> </tr>
</table>

按照 Embdely_Cards 插件的方法嵌入Youtube视频：
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
<h3>Embedding a YouTube video <em>with</em> card border.</h3>

