#!/bin/bash

ports=(1021 8081 8444 8881 33961 2201 63791 3391 50601 1162 1124 1070 8002 2301 14331 5901)

for port in "${ports[@]}"; do
   iptables -A INPUT -p tcp --dport $port -J DROP
   iptables -A INPUT -p udp --dport $port -J DROP
done
