import dataclasses
from os import environ as env
import re

from .i18n import I18n

@dataclasses.dataclass(frozen=True)
class ChannelId:
    """
    チャンネルIDを表現するValueオブジェクト
    """
    value: str
    REGEX = r"^C[0-9, A-Z]{8}$"

    def __post_init__(self):
        matched = re.match(ChannelId.REGEX, self.value)
        assert self.value == matched.group()

    def __str__(self):
        return str(self.value)


@dataclasses.dataclass(frozen=True)
class ChannelPurpose:
    """
    チャンネルの説明を表現するValueオブジェクト
    * channnelのpurposeはSlack上でdescription(説明)と表示されている
    """
    value: str
    max_length = 250

    def __post_init__(self):
        assert len(self.value) <= ChannelPurpose.max_length

    def __len__(self):
        return len(self.value)

    def __str__(self):
        return I18n.channel_purpose(self)


@dataclasses.dataclass(frozen=True)
class Channel:
    id: ChannelId
    purpose: ChannelPurpose

    def message_format(self):
        message = I18n.message_format(self, language=env["OUTPUT_LANGUAGE"])
        return message

