from os import environ as env

import slack

class Client:
	def __init__(self, token=env['SLACK_BOT_USER_TOKEN'], channel=env["SLACK_OUTPUT_CHANNEL"]):
		self.__client = slack.WebClient(token=token)
		self.__output_channel = channel

	def fetch_channels(self):
		response = self.__client.conversations_list(
			exclude_archived="true",
			types="public_channel",
			limit=1000
		)

		channels = response["channels"]

		return channels

	def notify(self, text):
		"""
		引数に渡されたtextをSlackに投稿します
		"""
		response = self.__client.chat_postMessage(
			channel = self.__output_channel,
			text = text
		)

		return response
