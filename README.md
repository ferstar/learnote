
learnote
========

> 孤独不是终点, 是机会~

　　受知乎此答 [非计算机专业学生怎么走上计算机技术之路？](http://zhihu.com/question/21671705/answer/132534680) 启发, 决定把曾经 "折腾" 过且还能找到的脚本代码集中到 Github 上面来, 作为积累记录, 详细折腾记录及月经贴放在
  
  <https://ferstar.org>

　　[segmentfault](https://segmentfault.com/u/ferstar/answers?sort=vote)回答合集 / [CSDN博客](http://blog.csdn.net/ferstar)



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

10. [记一次好玩的微信刷票](https://ferstar.org/post/python/ji-ci-hao-wan-de-wei-xin-shua-piao)

 > 公司参加一个创新项目的比赛,活动主办方为了活跃气氛, 或者是扩大知名度, 发起了一个微信投票活动, 得票数前三位还是多少位就可以免机票去参加总决赛
 >
 > PS: 这明显是可以被检测到是开挂的行为, 自然也没有啥好的结果

11. 生成随机字符串

   > 早先是这样

   ```
   import random
   import string
   def GenString(length):
       # return ''.join(random.sample(chars, 15))    # 得出的结果中字符不会有重复的
       return ''.join([random.choice(string.ascii_letters) for i in range(length)])
   ```

   > 后面发现了更好的

   ```
   import random
   import string

   def id_generator(size=8, chars=string.ascii_letters + string.digits):
       return ''.join(random.choice(chars) for _ in range(size))

   print(id_generator())
   ```

12. [Python struct](https://ferstar.org/post/python/pythonchu-li-er-jin-zhi-shu-ju)

   > 原地址的sample太老旧2.7x, 已经不适用于3.x, 我修正了下, 3.x测试通过

13. [优化sqlite3数据插入性能](https://ferstar.org/post/python/you-hua-sqlite3xing-neng)

   > 需要序列化个略大的文本文件到数据库, 源代码效率略低, 小改一点, 效率提升明显

14. [加速下载NCBI数据库](https://ferstar.org/post/ngs/jia-su-xia-zai-ncbishu-ju-ku)

   > 利用两个工具 ascp 和 axel 来加速NCBI数据的下载速度

15. [awk的一次具体应用](https://ferstar.org/post/ngs/awkde-ci-ju-ti-ying-yong)

   > classification.txt数据是对LJ.fasta样本数据的分析结果, 其中Classification列表示所标记序列对应的菌种, 但是有可能并没有识别到种, 只识别到属或者更粗放的结果. 所以问题来了: 把样本数据中只定到属未定到具体种的序列提取出来

16. [批量转换bam到fastq](https://ferstar.org/post/ngs/pi-liang-zhuan-huan-bamdao-fastq)

   > 批量转换指定目录下面所有bam格式到fastq格式, 如果有的话

17. [比较两台centos已安装程序的异同](https://ferstar.org/post/python/bi-jiao-liang-tai-centosyi-an-zhuang-cheng-xu-de-yi-tong)

   > 一台计算节点硬件故障终于修好, 是时候把这货加入集群了, 然而比较悲催的是集群已经运行很久, 上面新安装了啥软件包我自己也记不清, 所以就需要挑一个正常运行的节点把上面已安装的程序找出来, 然后把新加入的节点默认安装的软件也列出来, 最后两者取差集即可得到需要在新节点上额外安装的程序列表

18. [segmentfault答题之-字典生成的一个问题](https://segmentfault.com/q/1010000006624056/a-1020000006628560))

19. [pandas 两文本取交集](https://ferstar.org/post/python/liang-wen-ben-qu-jiao-ji)

   > aa.txt 和 bb.txt 中间有一列内容有交集, 需要把这个交集和差集提出来

20. [Python控制windows10自动关机](https://segmentfault.com/q/1010000006782616)

   > 看到`segmentfault`的这个问题, 就花了点时间解决了下, 感叹`python`的轮子真多, 真好用

21. [译 - 一个生物信息工作者的UNIX工具箱](https://ferstar.org/post/fan-yi/a-bioinformatician-s-unix-toolbox)

22. [对任意深度任意形式的list嵌套求平均](https://ferstar.org/post/python/dui-ren-yi-shen-du-ren-yi-xing-shi-de-listqian-tao-qiu-ping-jun)

23. [更改rocks cluster自带wordpress管理密码](https://ferstar.org/post/ngs/geng-gai-rocks-clusterzi-dai-wpguan-li-mi-ma)

24. [数字尾巴淘机记 - 简单爬虫](https://ferstar.org/post/za-ji/shu-zi-wei-ba-tao-ji-ji)

   > 前段时间手机又摔了个角, 实在惨不忍睹, 急需换机, 放眼望去安卓一片巨屏手机实非我所愿, 只能选`5se`, 秉承坚决不浪费的原则, 还是准备去数字尾巴淘个好成色的二手, 然而好成色又好价的机子总是被别人秒, 略蛋疼, 所以就整了这么个脚本, 刷到`se`字样的卖机贴就给我发邮件提醒

25. [Windows路由表配置_双网卡同时上公司内外网](https://ferstar.org/post/za-ji/windowslu-you-biao-pei-zhi-_shuang-wang-qia-tong-shi-shang-gong-si-nei-wai-wang)

26. [利用python-docx更新word中的表格内容](https://ferstar.org/post/python/li-yong-python-docxgeng-xin-wordzhong-de-biao-ge-nei-rong)

...Zz
