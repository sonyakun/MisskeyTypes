from typing import Union

from pydantic import dataclasses, Field

from .user import User, UserLite
from .drive import DriveFile

@dataclasses.dataclass(config=dict(extra="allow"))
class Note:
    id: str
    createdAt: str
    userId: str
    user: UserLite
    replyId: Union[str, None]
    renoteId: Union[str, None]
    visibility: str
    localOnly: bool

    reactions: Union[dict, None] = None
    myReaction: Union[dict, None] = None
    uri: Union[str, None] = None
    url: Union[str, None] = None
    renoteCount: Union[int, None] = None
    replyesCount: Union[int, None] = None
    isHidden: Union[bool, None] = None
    deletedAt: Union[str, None] = None
    text: Union[str, None] = None
    cw: Union[str, None] = None
    reply: Union[dict, None] = None
    renote: Union[dict, None] = None
    mentions: list[str] = Field(default_factory=list)
    visibleUserIds: list[str] = Field(default_factory=list)
    fileIds: list[str] = Field(default_factory=list)
    files: list[DriveFile] = Field(default_factory=list)
    tags: list[str] = Field(default_factory=list)
    poll: Union[dict, None] = None
    channelId: Union[str, None] = None
    channel: Union[dict, None] = None
    reactionAcceptance: Union[str, None] = None
    reactionAndUserPairCache: list[str] = Field(default_factory=list)