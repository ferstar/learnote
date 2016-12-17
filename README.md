
learnote
========

> 孤独不是终点, 是机会~

受知乎此答 [非计算机专业学生怎么走上计算机技术之路？](http://zhihu.com/question/21671705/answer/132534680) 启发, 决定把曾经 "折腾" 过且还能找到的脚本代码集中到 Github 上面来, 作为积累记录, 详细折腾记录及月经贴暂时放在 http://0ne.farbox.com. (http://ferstar.org不想维护了)

1. [使用七牛云存储创建自己的图床,用于写博客](https://github.com/ferstar/qiniu4blog)

   > 静态博客图片等多媒体资源需要有个窝，目前在用七牛，看到有人写了qiniu4blog，蛮好用的，拿来小改了下，以适应个人需求

2. [阿里大于短信 SDK for python3](https://github.com/ferstar/bigfish)

   > 最近一个项目刚好需要接入短信验证收发这一功能, 经过筛选以后敲定选择阿里大于的解决方案. 比较良心的是提供了 Python 的 SDK, 然而这是一份长了草的SDK, 为署名 lihao 的开发者在 2012 年更新的源码, 所以悲催的事情出现, 只支持 Python2.x, 经过一番爬坑修改后, 成功让短信验证功能跑通, 对应的接口是`AlibabaAliqinFcSmsNumSendRequest`, 别的接口没整:-)

3. [通过微信自动发送工资条(图片)](https://github.com/ferstar/auto_send_wage)

   > 认识一个人事妹子每次发工资时要给每个员工依次用微信发送对应的工资条, 本着程序猿济世救民的国际主义精神, 撸了这么个小脚本

4. [微wiki](https://github.com/ferstar/simiki)

   > Simiki 是一个简单的个人Wiki框架。使用[Markdown](https://daringfireball.net/projects/markdown/)书写Wiki, 生成静态HTML页面。Wiki源文件按目录分类存放, 方便管理维护。
   >
   > 提了点微小的pr, 混contribute

5. [树莓派 mjpg-streamer](https://github.com/ferstar/mjpg-streamer-diy)

   > 树莓派接摄像头后可以远程查看相机内容, 源码在树莓派部署有问题, 修改了下, 凑合可用

6. [rtl8192 USB无线网卡树莓派驱动](https://github.com/ferstar/rtl8192cu-fixes)

   > Linux上的东西总是不太能让人省心, 这次是网卡问题, 小改后树莓派可用

7. [NetSparkle / C#程序自动升级module hack](https://github.com/ferstar/NetSparkle/tree/master)

   > 实习公司用C#写一CS架构客户端, 我负责自动更新环节, 找了一堆轮子都不太靠谱, 只好随便挑个小改一番, 所幸能用, 交差后吃灰

8. [MongoKit](https://github.com/namlook/mongokit/tree/development)

   > 写一RESTful API后端用到了MongoDB, 顺便用这个, 自带structured schema and validation layer
   >
   > 挺方便, 后面发现一个小兼容问题, 顺路就混了个contribute

9. [Flask](https://github.com/pallets/flask)

   > 一个APP服务后端用这写的, 软件已经扑街, 不过貌似用的过程中发现了点BUG, 成功混contribute