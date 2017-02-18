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
                message = slack_message.get("text")
                user = slack_message.get("user")
                channel = slack_message.get("channel")
                ts = slack_message.get("ts")
                message_string = str(message).strip(' \t\n\r')
                if (message_string.startswith("<http://") or message_string.startswith("<https://")) and message_string.endswith(">"):
                    # TODO Get this to work. Why not authorized to delete a message?
                    delete_response = slack_client.api_call("chat.delete", as_user="true", channel=channel, ts=ts)
                    user_info = slack_client.api_call("users.info", user=user)
                    user_name = user_info.get("user").get("name")
                    slack_client.api_call("chat.postMessage", as_user="true", channel=channel, link_names="true", text=RANDOM_LINK_DETECTED_MESSAGE % user_name)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection error! Invalid Slack token (%s) or bot ID (%s)?" % (TOKEN, BOT_ID))
