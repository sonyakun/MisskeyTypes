from typing import Union

from pydantic import dataclasses, Field

from .user import User

@dataclasses.dataclass(config=dict(extra="allow"))
class DriveFolder:
    id: str
    createdAt: str
    name: str
    foldersCount: int
    filesCount: int
    parentId: Union[str, None] = None
    parent: Union[dict, None] = Field(default_factory=dict)

@dataclasses.dataclass(config=dict(extra="allow"))
class df_property:
    width: Union[int, None] = None
    height: Union[int, None] = None
    orientation: Union[int, None] = None
    avgColor: Union[str, None] = None

@dataclasses.dataclass(config=dict(extra="allow"))
class DriveFile:
    id: str
    createdAt: str
    name: str
    type: str
    md5: str
    size: int
    properties: df_property
    isSensitive: bool = False
    blurhash: Union[str, None] = None
    url: Union[str, None] = None
    thumbnailUrl: Union[str, None] = None
    comment: Union[str, None] = None
    folderId: Union[str, None] = None
    folder: Union[DriveFolder, None] = None
    userId: Union[str, None] = None
    user: Union[User, None] = None