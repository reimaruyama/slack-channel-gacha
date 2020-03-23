from os import environ as env

class I18n:
    BLANK_PURPOSE_TEXT_JA = "未設定"
    BLANK_PURPOSE_TEXT_EN = "No Description."

    @classmethod
    def channel_purpose(klass, channel_purpose):
        if len(channel_purpose) > 0: return channel_purpose.value

        if env["OUTPUT_LANGUAGE"] == "ja":
            return I18n.BLANK_PURPOSE_TEXT_JA

        return I18n.BLANK_PURPOSE_TEXT_EN

    @classmethod
    def message_format(klass, channel, language=env["OUTPUT_LANGUAGE"]):
        i18n = I18n(channel, language)
        return i18n.message()


    def __init__(self, channel, language):
        self._channel = channel
        self.__language = language


    def __japanese(self):
        return f"本日のチャンネルガチャ\nチャンネル: <#{self._channel.id}>\n説明: {self._channel.purpose}"

    def __english(self):
        return f"Today's Channel Gacha!\nChannel: <#{self._channel.id}>\nDescription: {self._channel.purpose}"

    def message(self):
        if self.__language == "ja":
            return self.__japanese()

        return self.__english()
