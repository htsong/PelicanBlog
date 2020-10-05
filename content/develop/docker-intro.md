Title: Docker入门之一：Docker是什么？
Date: 2020-10-05 10:10
Category: 开发
Slug: docker_slug
Tags: docker, container, virtual machine

# 源起

Docker 最初是 dotCloud 公司创始人 [Solomon Hykes](https://github.com/shykes) 在法国期间发起的一个公司
内部项目，它是基于 dotCloud 公司多年云服务技术的一次革新，并于 2013 年 3 月以 Apache 2.0 授权协议开源，
主要项目代码在 GitHub 上进行维护。[Docker](https://github.com/moby/moby) 项目后来还加入了 Linux 基金会，
并成立推动 开放容器联盟（OCI）。

## 发展

Docker 自开源后受到广泛的关注和讨论，至今其 GitHub 项目 已经超过 5 万 7 千个星标和一万多个 fork。甚至
由于 Docker 项目的火爆，在 2013 年底，dotCloud 公司决定改名为 [Docker](https://www.docker.com/)。Docker 
最初是在 Ubuntu 12.04 上开发实现的；Red Hat 则从 RHEL 6.5 开始对 Docker 进行支持；Google 也在其 PaaS 产品
中广泛应用 Docker。

## 商业化

Docker官网分为moby、docker-ce与docker-ee不同板块，ce和ee版本好理解，但自2017年开始又多出个Moby，有点令人凌乱。
简单地说，Docker公司直接把原Docker项目改名成了Moby，是为了将之前数年里构建出来的庞大的粉丝团体和Google搜索内容（Google search footprint）全部转移到Docker公司的商业产品上。

Moby会以一个开源组织（Github Org）的方式存在。Docker CE这个产品，会由Moby组织下的Moby项目以及其他项目构建和编译出来的。Moby组织下面的项目均由社区开发者共同维护。

这也就意味着对于Moby社区的参与者来说，你们今后的工作方式是：贡献Moby下的项目，然后使用Docker公司的Docker CE产品。

你也应该明白了，并不会存在一个开源项目叫Docker CE。因为Docker CE是一个产品，你一定得从Docker公司官网上来下载使用。

技术公司的话，一般会选择继续维护自己的开源项目，然后在自己公司里卖一个企业版以及企业服务。这种例子太多了，几乎每个开源项目都是这个套路。

但是唯独Docker公司，它直接把Docker开源项目改名了，或者说的更直白一点，给抹去了。从这天开始，你再也不可能找到一个叫Docker的开源项目。你从Google上搜到所有跟『Docker』相关的信息，都会指向Docker公司的那两个产品。原先Docker项目庞大的粉丝群，直接变成了Docker公司的客户。

这也是为什么所罗门一再解释『原先的Docker用户并不受影响』但是很多人并不买账的原因。问题不在于什么项目要改名啦，依赖库不能用啦这种小问题。

关键问题在于，原Docker开源项目的用户被实实在在地愚弄了一把。

这是前所未有的（不知道过去20年里大家有没有类似的例子）。



---------
参考文献

1. Docker————从入门到实践，[EB/OL] https://yeasy.gitbook.io/docker_practice/introduction/what，20201005
