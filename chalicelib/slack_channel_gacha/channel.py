import dataclasses
import re

@dataclasses.dataclass(frozen=True)
class ChannelId:
    """
    チャンネルIDを表現するValueオブジェクト
    """
    value: str
    regex = r"^C[0-9, A-Z]{8}$"

    def __post_init__(self):
        matched = re.match(ChannelId.regex, self.value)
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
    blank_purpose_text = "未設定"

    def __post_init__(self):
        assert len(self.value) <= ChannelPurpose.max_length

    def __str__(self):
        if len(self.value) == 0: return ChannelPurpose.blank_purpose_text

        return self.value


@dataclasses.dataclass(frozen=True)
class GachaedChannel:
    id: ChannelId
    purpose: ChannelPurpose


    def __str__(self):
        """
        Slackに投稿する形式の文字列を返します。
        チャンネルの説明が空文字列だった場合は`未設定`と表示します。
        """
        result = f"本日のチャンネルガチャ\nチャンネル: <#{str(self.id)}>\n説明: {str(self.purpose)}"
        return result


