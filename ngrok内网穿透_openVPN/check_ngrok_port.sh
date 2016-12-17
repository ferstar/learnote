#!/bin/bash
export PATH=/bin:/usr/bin

new_port=$(grep "Tunnel established at" /var/log/supervisor/natapp_stdout.log | tail -1 | awk -F: '{print $5}')
if [ ! new_port ]; then
    new_port=$(grep "Tunnel established at" /var/log/supervisor/natapp_stdout.log* | tail -1 | awk -F: '{print $6}') 
fi

if [ ! -f /tmp/ngrok_port ]; then
    # echo -e "create ngrok_port file"
    echo $new_port > /tmp/ngrok_port
fi

old_port=$(cat /tmp/ngrok_port)

if [ $old_port != $new_port ]; then
    #curl -s -X "POST" "https://hooks.pubu.im/services/pz98n941ngymfww" -H "Content-Type: application/json" -d "{\"snippet\":{\"type\":\"shell\",\"code\":\"$new_port\",\"name\":\"端口变更\"}}" > /dev/null
    curl -s https://hooks.pubu.im/services/xxx -F text=$new_port > /dev/null
    echo $new_port | mail -s "VPN port has been changed" fer_star@qq.com
    echo $new_port > /tmp/ngrok_port
fi
