# Slack Channel Gacha

The more channels there are, the less chance members have of knowing that a channel exists.
The app regularly selects and introduces channels at random, providing a chance for new members to become aware of the channel's existence.

## About Architecture

This is a serverless app that consists only of AWS Lambda and Amazon CloudWatchEvents to deploy using AWS Chalice.

## Getting Started

1. `pip install chalice`
2. `pip install awscli`
3. `aws configure`
4. `git clone git@github.com:reimaruyama/slack-channel-gacha.git`
5. `cd slack-channel-gacha`
6. Setting `.chalice/config.json`

```json5
{
  "version": "2.0",
  "app_name": "slack-channel-gacha",
  "stages": {
    "dev": {
      "api_gateway_stage": "api",
      "environment_variables": {
        // [Required]
        // Your Slack Bot user Token
        // This app needs 2 permissions below.
        // - `chat:write`
        // - `channels:read`
        "SLACK_BOT_USER_TOKEN": "xoxb-0000000000-00000000000-XXXXXXXXXXXXXXXXXXX",
        // [Required]
        // A channel to post channel gacha result.
        // Ensure this bot is invited in the channel.
        "SLACK_OUTPUT_CHANNEL": "random",
        // [Optional]
        // A string of CRON expressions representing the schedule on which this app runs.
        "SCHEDULE": "0 9 ? * * *",
        // [Optional]
        // The language that the gacha post is written in.
        "OUTPUT_LANGUAGE": "en",
        // [Optional]
        // webhook URL to post the notification about error encountered in this app.
        "ERROR_NOTICE_WEBHOOK": "https://hooks.slack.com/services/TOUR_WEB_HOOK",
        // [Optional]
        // User mension to notify the error.
        "ERROR_NOTICE_USER_MENTION": "@john.doe"
      }
    }
  }
}

```

7. deploy! `chalice deploy`

