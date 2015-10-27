##RHEL7利用iso镜像做本地yum源
标签: 教程

----------
1. 创建iso存放目录和挂载目录
    `mkdir /root/iso
    mkdir /mnt/cdrom`
2. 将iso镜像文件上传到/root/iso文件夹下
3. 将/root/iso/下的iso文件(rhel-workstation-7.0-x86_64-dvd.iso)挂载到/mnt/cdrom目录
    `mount -o loop /root/iso/rhel-workstation-7.0-x86_64-dvd.iso /mnt/cdrom`
4. 在/etc/yum.repos.d目录下新建rhel-media.repo文件(可以自己指定名字,但后缀必须是repo,如果只需要本地yum源的话,可以把别的repo文件全删掉),内容如下
    `[rhel-media]
    name=Red Hat Enterprise Linux 7.0
    baseurl=file:///mnt/cdrom
    enabled=1
    gpgcheck=1
    gpgkey=file:///mnt/cdrom/RPM-GPG-KEY-redhat-release`
5. 清理yum源缓存
    `yum clean all`
6. 创建yum源缓存
    `yum makecache`
7. 测试
    `yum install emacs`
8. 开机自动挂载本地yum源
    编辑/etc/fstab,最后一行添加内容
    `/root/iso/rhel-workstation-7.0-x86_64-dvd.iso /mnt/cdrom iso9660 defaults,ro,loop 0 0`
    保存退出即可