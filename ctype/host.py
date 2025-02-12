from dataclasses import dataclass

@dataclass
class Host:
    ping:int
    name:str
    address:str
    port:int
    mapName:str
    wave:int
    players:int
    version:int
    versionType:str
    mode:str
    playerLimit:int
    description:str
    modeName:str