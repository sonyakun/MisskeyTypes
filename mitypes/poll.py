from typing import List, Union

from pydantic import dataclasses


@dataclasses.dataclass(config=dict(extra="allow"))
class Poll:
    choices: List[str]
    multiple: bool = False
    expiresAt: Union[int, None] = None
    expiredAfter: Union[int, None] = None
