import dataclasses
import re

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
    BLANK_PURPOSE_TEXT= "未設定"

    def __post_init__(self):
        assert len(self.value) <= ChannelPurpose.max_length

    def __str__(self):
        if len(self.value) == 0: return ChannelPurpose.BLANK_PURPOSE_TEXT

        return self.value


@dataclasses.dataclass(frozen=True)
class Channel:
    id: ChannelId
    purpose: ChannelPurpose

