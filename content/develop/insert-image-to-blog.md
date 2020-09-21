Title: 往 Pelican 中插入图片
Date: 2020-09-21 12:30
Category: 开发

为 Blog 插入图片有两种方法:

* 一种是使用云存储，设置为公开图片，直接链接过来，如Picasa来维护图片,推荐使用云图床；

```
![Test Cloud img](https://lh3.googleusercontent.com/-rBvjY3F2wEU/VvD3yZ9T-1I/AAAAAAAAAVc/LsPcb3CIxtomUcXq5aVKj27qSrI4OserwCCo/s400-Ic42/3d94dcb44aed2e730566c2068601a18b86d6fa7f.jpg)
```

![Test Cloud img](https://lh3.googleusercontent.com/-rBvjY3F2wEU/VvD3yZ9T-1I/AAAAAAAAAVc/LsPcb3CIxtomUcXq5aVKj27qSrI4OserwCCo/s400-Ic42/3d94dcb44aed2e730566c2068601a18b86d6fa7f.jpg)


* 另一种使用本地图片，参考,但Github有图片容量限制。content目录下建立一个 images目录 然后在 pelicanconf.py 中添加:
```
STATIC_PATHS = ["images"]
```

在文章中引用图片,路径要设置为本文件与图片文件中的相对路径，如果文件路径变更了，就需要修改图片的相对路径，格式可参考下例：

```
![Test img](../../../images/test.jpg)
```

以上设置参考[《Pelican札记》, Tue 22 March 2016, byjekyll](https://pelucky.github.io/pages/2016/03/22/gitpages-pelican/)
