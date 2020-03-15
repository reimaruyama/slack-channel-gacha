from os import environ as env
import random

import slack

from .channel import Channel, ChannelId, ChannelPurpose

class Gacha:
	default_slack_error_message = "不明なエラー"

	def __init__(self):
		self.__client = slack.WebClient(token=env['SLACK_BOT_USER_TOKEN'])


	def call(self):
		channels = self.fetch_channels()
		selected = self.select(channels)
		selected = self.convert_channel_object(selected)
		self.notify(selected)


	def fetch_channels(self):
		response = self.__client.conversations_list(
			exclude_archived="true",
			types="public_channel",
			limit=1000
		)

		self.response_check(response)

		channels = response["channels"]

		return channels

	def response_check(self, response):
		if not response["ok"] == True:
			message = response.get(
				"error",
				Gacha.default_slack_error_message
			)
			raise SlackClientError(message)

		pass


	def select(self, channels):
		"""
		引数で与えられたチャンネルから一つ選択します
		"""
		selected = random.sample(channels, 1)[0]
		return selected


	def convert_channel_object(self, channel):
		"""
		引数で与えられたslack APIの返り値のchannnelオブジェクト(dict)
		をChannelオブジェクトにして返します。
		"""
		return Channel(
			id = ChannelId(channel["id"]),
			purpose = ChannelPurpose(channel["purpose"]["value"])
		)


	def notify(self, channel):
		"""
		結果をSlackに投稿します
		"""
		response = self.__client.chat_postMessage(
			channel = env["SLACK_OUTPUT_CHANNEL"],
			text = channel.for_post_format()
		)
		self.response_check(response)

		return response



class SlackChannelGachaError(Exception):
	pass

class SlackClientError(SlackChannelGachaError):
    pass

def main():
	gacha = Gacha()
	gacha.call()


if __name__ == "__main__":
	main()