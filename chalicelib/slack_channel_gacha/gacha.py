from os import environ as env
import random

from .channel import GachaedChannel, ChannelId, ChannelPurpose
from .client import Client

class Gacha:
	def __init__(self):
		self.__client = Client(token=env['SLACK_BOT_USER_TOKEN'], channel=env["SLACK_OUTPUT_CHANNEL"])

	def play(self):
		channels = self.__client.fetch_channels()
		selected = self.select(channels)
		selected_channel = self.convert_channel_object(selected)
		self.__client.notify(str(selected_channel))

	def select(self, channels):
		"""
		引数で与えられたチャンネルから一つ選択します
		"""
		selected = random.sample(channels, 1)[0]
		return selected


	def convert_channel_object(self, channel):
		"""
		引数で与えられたslack APIの返り値のchannnelオブジェクト(dict)
		をGachaedChannelオブジェクトにして返します。
		"""
		return GachaedChannel(
			id = ChannelId(channel["id"]),
			purpose = ChannelPurpose(channel["purpose"]["value"])
		)


def main():
	gacha = Gacha()
	gacha.play()


if __name__ == "__main__":
	main()