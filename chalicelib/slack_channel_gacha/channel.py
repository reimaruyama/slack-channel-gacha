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


@dataclasses.dataclass(frozen=True)
class Channel:
    id: ChannelId
    purpose: ChannelPurpose

    blank_purpose_text = "未設定"

    def for_post_format(self):
        """
        Slackに投稿する形式の文字列を返します。
        チャンネルの説明が空文字列だった場合は`未設定`と表示します。
        """
        result = f"本日のチャンネルガチャ\nチャンネル: <#{self.__id_for_post()}>\n説明: {self.__purpose_for_post()}"
        return result

    def __id_for_post(self):
        id = self.id
        return id.value

    def __purpose_for_post(self):
        purpose = self.purpose

        if len(purpose.value) == 0: return Channel.blank_purpose_text

        return purpose.value