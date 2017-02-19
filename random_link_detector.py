#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import time
from slackclient import SlackClient


BOT_ID = os.environ.get("BOT_ID")
TOKEN = os.environ.get('SLACK_BOT_TOKEN')
slack_client = SlackClient(TOKEN)
RANDOM_LINK_DETECTED_MESSAGE = "Dear @%s, it looks like you have posted a random link. This is considered spam. " \
                               "Please provide a description of your link and explain why anyone should bother clicking on it."


if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 1
    if slack_client.rtm_connect():
        print("Random Link Detector bot connected and listening for random links!")
        while True:
            for slack_message in slack_client.rtm_read():
                message = unicode(slack_message.get("text")).strip(' \t\n\r')
                user = slack_message.get("user")
                channel = slack_message.get("channel")
                if (message.startswith("<http://") or message.startswith("<https://")) and message.endswith(">"):
                    user_info = slack_client.api_call("users.info", user=user)
                    user_name = user_info.get("user").get("name")
                    slack_client.api_call("chat.postMessage", as_user="true", channel=channel, link_names="true", text=RANDOM_LINK_DETECTED_MESSAGE % user_name)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection error! Invalid Slack token (%s) or bot ID (%s)?" % (TOKEN, BOT_ID))
