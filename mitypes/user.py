from typing import Union

from pydantic import dataclasses

@dataclasses.dataclass(config=dict(extra="allow"))
class AvatarDecorations:
    id: str
    url: str
    angle: float = None
    flipH: bool = None

@dataclasses.dataclass(config=dict(extra="allow"))
class User:
    id: str
    createdAt: str
    username: str
    host: Union[str, None] = None 
    name: Union[str, None] = None 
    avatarUrl: Union[str, None] = None 
    avatarBlurhash: Union[str, None] = None 
    avatarDecorations: list[Union[AvatarDecorations, None]] = None
    isAdmin: bool = False
    isModerator: bool = False
    isBot: bool = False
    isCat: bool = False
    onlineStatus: Union[str, None] = None

@dataclasses.dataclass(config=dict(extra="allow"))
class UserLite:
    id: str
    username: str
    name: Union[str, None] = None
    
    host: Union[str, None] = None
    avatarUrl: Union[str, None] = None
    avatarBlurhash: Union[str, None] = None
    avatarDecorations: list[Union[AvatarDecorations, None]] = None
    isAdmin: bool = False
    isModerator: bool = False
    isBot: bool = False
    isCat: bool = False
    onlineStatus: Union[str, None] = None