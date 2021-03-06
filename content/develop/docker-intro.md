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
简单地说，Docker公司直接把原Docker项目改名成了Moby，是为了将之前数年里构建出来的庞大的粉丝团体和Google搜索内容
（Google search footprint）全部转移到Docker公司的商业产品上：包括docker-ce和docker-ee。

重点是，原先的开源项目Docker不再存在了。现在，Moby是以一个开源组织（Github Org）的方式存在的。Docker CE这个
产品，由Moby组织下的Moby项目以及其他项目构建和编译出来的。Moby组织下面的项目均由社区开发者共同维护。这也就意味
着对于Moby社区的参与者来说，你们今后的工作方式是：贡献Moby下的项目，然后使用 **Docker公司** 的Docker CE产品。
因为Docker CE是一个商业产品（虽然免费），但你一定得从Docker公司官网上来下载使用。

开源技术公司的一般做法是，选择继续维护自己的开源项目，然后在自己公司里卖一个企业版以及企业服务。这种例子太多了，
几乎每个开源项目都是这个套路。但Docker公司直接把Docker开源项目改名了，或者说的更直白一点，给抹去了。从Docker
改名Moby这天开始，你再也不可能找到一个叫Docker的开源项目。你从Google上搜到所有跟『Docker』相关的信息，都会指
向Docker公司的那两个产品。原先Docker项目庞大的粉丝群，直接变成了Docker公司的客户。

这也是为什么所罗门(Solomon)一再解释『原先的Docker用户并不受影响』但是很多人并不买账的原因。问题不在于什么项目
要改名啦，依赖库不能用啦这种小问题。关键问题在于，**原Docker开源项目的用户被实实在在地愚弄了一把**，这是开源
世界前所未有的“狸猫换太子”的做法。

# VMWare2.0？

是什么让所罗门敢冒天下之大不韪？除了来自投资人的业绩压力外，巨大的商业利益使之然也。Docker脱胎于[LXC](https://linuxcontainers.org/lxc/introduction/)，[RUNC](https://github.com/opencontainers/runc)，
对进程进行封装隔离，属于操作系统层面的虚拟化技术。由于隔离的进程独立于宿主和其它的隔离的进程，因此也称其为容器。
Docker在容器中进一步封装了文件系统、网络互联等等，极大的简化了容器的创建和维护。

提到虚拟化，就会联想起另一个明星产品VMWare，VMWare是虚拟机层面的虚拟化。下图比较了 Docker 和传统虚拟机虚拟化方式
的不同之处。传统虚拟机技术是虚拟出一套硬件后，在其上运行一个完整操作系统，在该系统上再运行所需应用进程；而容器内的
应用进程直接运行于宿主的内核，容器内没有自己的内核，而且也没有进行硬件虚拟。因此容器要比传统虚拟机更为轻便。


![VM](https://gblobscdn.gitbook.com/assets%2F-M5xTVjmK7ax94c8ZQcm%2F-M5xT_hHX2g5ldlyp9nm%2F-M5xTdXNYDmRWNH-Lqez%2Fvirtualization.png?alt=media)

![Docker](https://gblobscdn.gitbook.com/assets%2F-M5xTVjmK7ax94c8ZQcm%2F-M5xT_hHX2g5ldlyp9nm%2F-M5xTdXP2scg0hxytUHA%2Fdocker.png?alt=media)

对比传统虚拟机总结

| 特性   |   容器  |     虚拟机| 
|  ----  | ----  |  ----  | 
| 启动   | 秒级    | 分钟级| 
| 硬盘使用| 一般为 MB| 一般为 GB| 
| 性能| 接近原生| 弱于原生| 
| 系统支持量| 单机支持上千个容器| 一般几十个| 


# 为何要用Docker？

## 更加快捷高效
**更高效的利用系统资源**
由于容器不需要进行硬件虚拟以及运行完整操作系统等额外开销，Docker 对系统资源的利用率更高。无论是应用执行速度、内存损耗或者文件存储速度，都要比传统虚拟机技术更高效。因此，相比虚拟机技术，一个相同配置的主机，往往可以运行更多数量的应用。

**更快速的启动时间**
传统的虚拟机技术启动应用服务往往需要数分钟，而 Docker 容器应用，由于直接运行于宿主内核，无需启动完整的操作系统，因此可以做到秒级、甚至毫秒级的启动时间。大大的节约了开发、测试、部署的时间。

## 更轻松的维护和扩展
Docker 使得应用的维护更新更加简单，基于基础镜像进一步扩展镜像也变得非常简单。

**持续交付和部署**
对开发和运维（DevOps）人员来说，最希望的就是一次创建或配置，可以在任意地方正常运行。开发过程中一个常见的问题是环境一致性问题。由于开发环境、测试环境、生产环境不一致，导致有些 bug 并未在开发过程中被发现。而 Docker 的镜像提供了除内核外完整的运行时环境，确保了应用运行环境一致性，从而不会再出现 「这段代码在我机器上没问题啊」 这类问题。

**更轻松的迁移**
由于 Docker 确保了执行环境的一致性，使得应用的迁移更加容易。Docker 可以在很多平台上运行，无论是物理机、虚拟机、公有云、私有云，甚至是笔记本，其运行结果是一致的。因此用户可以很轻易的将在一个平台上运行的应用，迁移到另一个平台上，而不用担心运行环境的变化导致应用无法正常运行的情况。

Docker 基于分层存储的镜像构建技术，使得应用的维护更新更加简单，也使得应用重复部分的复用更为容易。

# Docker入门之二：Win10 平台 Docker 安装使用


---------
【参考文献】

1. Docker————从入门到实践，[EB/OL] https://yeasy.gitbook.io/docker_practice/introduction/what，20201005

2. moby、docker-ce与docker-ee的区别，[EB/OL] https://my.oschina.net/u/4375221/blog/3389946，20201005

3. “对于 Docker 改名 Moby ，大家怎么看？”，[EB/OL] https://www.zhihu.com/question/58805021， 20170526
