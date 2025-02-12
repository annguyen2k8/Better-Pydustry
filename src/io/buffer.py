from __future__ import annotations
import struct, io

class Buffer():
    _in:io.BufferedReader
    def __init__(self, data:bytes) -> None:
        self.buffer = io.BytesIO()
        self.buffer.write(data)
        self.buffer.seek(0)

    def getInt(self) -> int:
        var0 = self.buffer.read(4)
        return struct.unpack('!i', var0)[0]
    
    def getStr(self) -> int:
        var0 = self.getUnsignedByte()
        return self.buffer.read(var0).decode()
    
    def getUnsignedByte(self) -> int:
        var0 = self.buffer.read(1)
        return struct.unpack('!B', var0)[0]