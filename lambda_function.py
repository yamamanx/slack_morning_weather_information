# coding:utf-8

import logging
import traceback
import requests
import get_message
import util
import json
import os

error_slack_url = os.environ.get('ERROR_SLACK_URL', None)
error_slack_channel = os.environ.get('ERROR_SLACK_CHANNEL', None)
logger = logging.getLogger()
logger.setLevel(util.logger_level())


def slack_message(url, channel, message):
    requests.post(
        url,
        json.dumps(
            {
                'channel': channel,
                'text': message
            }
        )
    )


def lambda_handler(event, context):
    try:
        slack_url = os.environ.get('SLACK_URL', None)
        slack_channel = os.environ.get('SLACK_CHANNEL', None)

        city_array = ['130010','270000']
        for city_id in city_array:
            message = u':earth_asia:おはようございます！\n'
            message += get_message.weather_info(city_id)
            slack_message(slack_url, slack_channel, message)

    except:
        slack_message(
            error_slack_url,
            error_slack_channel,
            'slack_morning_weather_information error\n{message}'.format(
                        message=traceback.format_exc()
            )
        )
        raise Exception(traceback.format_exc())
