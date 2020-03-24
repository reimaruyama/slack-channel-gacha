from os import environ as env
import logging
from logging import getLogger, INFO
import json

import requests
from chalice import Chalice
from chalicelib.slack_channel_gacha.gacha import Gacha

logger = getLogger()
logger.setLevel(logging.INFO)

app = Chalice(app_name='channel-gacha')

if not "OUTPUT_LANGUAGE" in env:
    env["OUTPUT_LANGUAGE"] = "en"

if not "SCHEDULE" in env:
    env["SCHEDULE"] = "0 9 ? * * *"


def notify_to_slack(text):
    if (not "ERROR_NOTICE_USER_MENTION" in env) or (not "ERROR_NOTICE_WEBHOOK" in env):
        return None

    payload = {"channel": env["ERROR_NOTICE_USER_MENTION"], "username": "webhookbot", "text": str(text), "icon_emoji": ":ghost:"}
    response = requests.post(env["ERROR_NOTICE_WEBHOOK"], data=json.dumps(payload))
    logger.info(response.text)
    return None


@app.schedule(f'cron({env["SCHEDULE"]})')
def index(event):
    try:
        logger.info(event)
        channel_gacha = Gacha()
        channel_gacha.play()
    except Exception as error:
        notify_to_slack(error)
        logger.info(error)
    return None

# ローカル実行時のエンドポイント
def main():
    try:
        channel_gacha = Gacha()
        channel_gacha.play()
    except Exception as error:
        notify_to_slack(error)
        logger.info(error)
    return None

if __name__ == "__main__":
	main()

