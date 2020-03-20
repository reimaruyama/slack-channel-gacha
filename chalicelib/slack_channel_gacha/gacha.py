from os import environ as env
import random

from .channel import Channel, ChannelId, ChannelPurpose
from .client import Client

class Gacha:
    def __init__(self):
        self.__client = Client(token=env['SLACK_BOT_USER_TOKEN'], channel=env["SLACK_OUTPUT_CHANNEL"])

    def play(self):
        channels = self.__client.fetch_channels()
        selected_channel = self.select(channels)
        message = self.build_message(selected_channel)
        self.__client.notify(message)

    def select(self, channels):
        """
        引数で与えられたチャンネルから一つ選択します
        """
        selected = random.sample(channels, 1)[0]
        return self.convert_channel_object(selected)


    def convert_channel_object(self, channel):
        """
        引数で与えられたslack APIの返り値のchannnelオブジェクト(dict)
        をGachaedChannelオブジェクトにして返します。
        """
        return Channel(
            id = ChannelId(channel["id"]),
            purpose = ChannelPurpose(channel["purpose"]["value"])
        )


    def build_message(self, channel):
        """
        Slackに投稿する形式の文字列を返します。
        チャンネルの説明が空文字列だった場合は`未設定`と表示します。
        """
        message = f"本日のチャンネルガチャ\nチャンネル: <#{str(channel.id)}>\n説明: {str(channel.purpose)}"
        return message


def main():
    gacha = Gacha()
    gacha.play()


if __name__ == "__main__":
    main()