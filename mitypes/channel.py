from typing import Union, List

from pydantic import dataclasses, Field


@dataclasses.dataclass(config=dict(extra="allow"))
class channel:
    id: str
    createdAt: str
    lastNotedAt: str
    name: str
    description: str
    bannerUrl: str
    isArchived: bool
    notedCount: int
    usersCount: int
    isFollowing: bool
    isFavorite: bool
    userId: str
    pinnedNoteIds: List[str]
    color: str
    isSensitive: bool
    allowRenoteToExternal: bool