#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
from threading import Thread

N = 2**16 - 1

host = str(input('Введите имя хоста или IP-адрес\n'))

try:
    sock = socket.socket()
    sock.connect((host, 9999))
    sock.close()
except (socket.gaierror):
    print(host, ' - unknown host')
else:
    for port in range(1, N):
        sock = socket.socket()
        try:
            sock.connect((host, port))
            print("Порт ", port, " открыт")
        except:
            continue
        finally:
		sock.close()
