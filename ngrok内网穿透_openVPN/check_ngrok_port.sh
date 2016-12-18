#!/bin/bash
export PATH=/bin:/usr/bin

# 从最新日志中抓取natapp最新端口
new_port=$(grep "Tunnel established at" /var/log/supervisor/natapp_stdout.log | tail -1 | awk -F: '{print $5}')
# 从历史日志中抓取natapp服务端口
if [ ! new_port ]; then
    new_port=$(grep "Tunnel established at" /var/log/supervisor/natapp_stdout.log* | tail -1 | awk -F: '{print $6}') 
fi

if [ ! -f /tmp/ngrok_port ]; then
    echo $new_port > /tmp/ngrok_port
fi

old_port=$(cat /tmp/ngrok_port)

if [ $old_port != $new_port ]; then
    # 检测到端口变更, 给零信发送incoming message
    curl -s https://hooks.pubu.im/services/xxx -F text=$new_port > /dev/null
    # 向目标邮箱发送变更后的端口(要求本机正确配置了mail服务)
    echo $new_port | mail -s "VPN port has been changed" fer_star@qq.com
    # 暂存新端口
    echo $new_port > /tmp/ngrok_port
fi
