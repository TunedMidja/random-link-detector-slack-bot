# Random Link Detector (Slack bot)

Detects the annoying behaviour some people have of posting a link without any description whatsoever and  gives them a slap on the wrist!


## Install

Install Python 2.x (developed with Python 2.7.13).

Add Slack's official Python library:

`
pip install SlackClient
`

Create a new bot in the Slack admin console and export the token:

`
export SLACK_BOT_TOKEN=[my-token]
`

Find the bot id and export it as well:

`
export BOT_ID=[my-bot-id]
`

How to perform the above steps is nicely described here:

https://www.fullstackpython.com/blog/build-first-slack-bot-python.html


## Run

`
python random_link_detector.py
`

Invite the bot to a Slack channel and watch it work its magic!
