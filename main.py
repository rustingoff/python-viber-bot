from flask import Flask, request, Response
from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration
from viberbot.api.messages import VideoMessage
from viberbot.api.messages.text_message import TextMessage
import logging

from viberbot.api.viber_requests import ViberConversationStartedRequest
from viberbot.api.viber_requests import ViberFailedRequest
from viberbot.api.viber_requests import ViberMessageRequest
from viberbot.api.viber_requests import ViberSubscribedRequest
from viberbot.api.viber_requests import ViberUnsubscribedRequest

logger = logging.getLogger()

app = Flask(__name__)
viber = Api(BotConfiguration(
    name='Agrodata',
    avatar='https://dl-media.viber.com/1/share/2/long/vibes/icon/image/0x0/c0b3'+
           '/fe86971e158e03c9722d18f0f1bf1b8e9d8b7429fbc9204546734a5bf727c0b3.jpg',
    auth_token='4fde5475b5a7e0e5-a07b269d4a6405a7-a1023d748320bb57'
))

viber.set_webhook('https://python-viber-bot2.herokuapp.com:443')


@app.route('/incoming', methods=['POST'])
def incoming():
    logger.debug("received request. post data: {0}".format(request.get_data()))
    # handle the request here
    return Response(status=200)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=443, debug=True)
