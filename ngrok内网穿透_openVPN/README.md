# ngrok 内网穿透

~~最早在知乎看到这个问题, 不想自己也碰到了同样的尴尬~~

~~[如何给不能做端口映射的内网架设VPN](https://www.zhihu.com/question/31220460/answer/103939079)~~

~~这里不会再重复我在知乎的回答, 只讲一种后来我在用的新方法, 效果很棒~~

用到的软件有三

1. ~~类ngrok的软件[natapp~~](https://natapp.cn/)
2. [openVPN](https://openvpn.net/)
3. [supervisor](http://supervisord.org/)


具体思路: 用natapp做内网穿透, 在内网机器上部署openVPN server, 用supervisor监控natapp进程状态, 这样即实现在外网轻松访问内网资源的需求, 简单描述为 VPN over ngrok under supervisor control.

~~教程: [natapp(ngrok) Linux 下使用 supervisor 后台运行&开机启动](https://natapp.cn/article/supervisor)~~

~~由于我用的是免费版本, 端口会不定期变动, 所以写了脚本, 检测到端口发生变化时, 给我发邮件/零信消息~~

~~目前使用良好~~

天杀的知乎, 以不宜讨论政治话题为由把我的回答删掉了, 另外`natpp.cn`这家网站前几日已免费通道被滥用为由关闭了免费配额, 所以只好再挪个别的窝, 比如`ngrok.cc`

方法还是一样的, 通过内网穿透连接内网服务器, 达到远程访问的目的