import pytest

import random, string
import textwrap
import os

import slack

from chalicelib.slack_channel_gacha.channel import ChannelPurpose, ChannelId, Channel
from chalicelib.slack_channel_gacha.gacha import Gacha

def test_channel_id_is_started_with_big_c():
	"""
	チャンネルIDは大文字のCで開始していないとエラーになる
	"""
	with pytest.raises(AttributeError):
		ChannelId("AAAAA")


def test_channel_id_raise_error_if_len_is_ten():
	"""
	チャンネルIDは10文字の場合エラーになる
	"""
	with pytest.raises(AttributeError):
		ChannelId("C123456789")


def test_channel_id_raise_error_if_len_is_eight():
	"""
	チャンネルIDは8文字の場合エラーになる
	"""
	with pytest.raises(AttributeError):
		ChannelId("C1234567")


def test_channel_id_is_alphabet_or_num_character():
	"""
	チャンネルIDに英数字以外が含まれる場合、エラーになる
	"""
	with pytest.raises(AttributeError):
		ChannelId("C12345Aあ亜")

def test_channel_id_is_valid():
	"""
	妥当なチャンネルIDを格納できる
	"""
	channel_id = ChannelId("C2740KJ1K")
	assert channel_id.value == "C2740KJ1K"


def channel_purpose_length_is_shorter_than_251():
	"""
	チャンネル説明が251字以上の場合エラーになる
	"""
	purpose = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(251)])
	with pytest.raises(AssertionError):
		ChannelPurpose(purpose)


def channel_purpose_length_is_valid_in_250_char():
	"""
	チャンネル説明が250字以内の場合エラーにならない
	"""
	purpose = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(250)])
	channel_purpose = ChannelPurpose(purpose)
	assert channel_purpose.value == purpose


def test_channel_object():
	channel = Channel(
		id=ChannelId("C2740KJ1K"),
		purpose=ChannelPurpose("チャンネル説明")
	)
	assert channel.id.value == "C2740KJ1K"
	assert channel.purpose.value == "チャンネル説明"

def test_channel_object_for_post_string():
	channel = Channel(
		id=ChannelId("C2740KJ1K"),
		purpose=ChannelPurpose("チャンネル説明")
	)
	gacha = Gacha()
	post_text = gacha.build_message(channel)

	assert post_text == "本日のチャンネルガチャ\nチャンネル: <#C2740KJ1K>\n説明: チャンネル説明"

def test_channel_object_purpose_blank():
	"""
	チャンネルの説明が空文字列のみの場合は未設定と表示される
	"""
	channel = Channel(
		id=ChannelId("C2740KJ1K"),
		purpose=ChannelPurpose("")
	)
	gacha = Gacha()
	post_text = gacha.build_message(channel)

	assert post_text == "本日のチャンネルガチャ\nチャンネル: <#C2740KJ1K>\n説明: 未設定"


# TODO: mockを使ってslack APIのテストをかく

