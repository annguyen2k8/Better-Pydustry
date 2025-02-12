from __future__ import annotations
from typing import *

import time

import socket
from socket import AF_INET, SOCK_DGRAM

from .io import *
from .ctype import *
from .content import *

class Network:
    @staticmethod
    def getServer(hostAddress:str, hostPort:int=6567) -> Host:
        with socket.socket(AF_INET, SOCK_DGRAM) as s:
            s.connect((hostAddress, hostPort))
            s.settimeout(10)
            s_time = time.time()
            s.send(b"\xfe\x01")
            data = s.recv(1024)
            e_time = time.time()
        ping = round((e_time - s_time) * 1000)
        data = Buffer(data)
        return Network.readServerData(ping, hostAddress, data)
    
    @staticmethod
    def readServerData(ping:int, hostAddress:str, buffer:Buffer, kwargs:Dict={}) -> Host:
        kwargs['ping'] = ping
        kwargs['name'] = buffer.getStr()
        kwargs['address'] = hostAddress
        kwargs['mapName'] = buffer.getStr()
        kwargs['players'] = buffer.getInt()
        kwargs['wave'] = buffer.getInt()
        kwargs['version'] = buffer.getInt()
        kwargs['versionType'] = buffer.getStr()
        kwargs['mode'] = list(Gamemode)[buffer.getUnsignedByte()].value
        kwargs['playerLimit'] = buffer.getInt()
        kwargs['description'] = buffer.getStr()
        kwargs['modeName'] = buffer.getStr()
        port =  buffer.getInt()
        kwargs['port'] = port if port != 0 else 6567
        return Host(**kwargs)