"""
This file implements module's main logic.
Data outputting should happen here.

Edit this file to implement your module.
"""

from logging import getLogger
import requests
from .params import PARAMS

log = getLogger("module")

# module settings
INPUT_LABEL = PARAMS['INPUT_LABEL']
ALERT_SEVERITY = PARAMS['ALERT_SEVERITY']
VONAGE_API = PARAMS['VONAGE_API']

# Vonage API specifics
VONAGE_API_KEY = PARAMS['VONAGE_API_KEY']
VONAGE_API_SECRET = PARAMS['VONAGE_API_SECRET']
VONAGE_BRAND_NAME = PARAMS['VONAGE_BRAND_NAME']
TO_SMS_NUMBER = '+' + PARAMS['TO_NUMBER']
SMS_URL = PARAMS['SMS_URL']
MESSAGES_API_URL = PARAMS['MESSAGES_API_URL']
BASE_URL = PARAMS['BASE_URL']
WHATSAPP_NUMBER = PARAMS['WHATSAPP_NUMBER']
TO_WHATSAPP_NUMBER = PARAMS['TO_NUMBER']
FB_SENDER_ID = PARAMS['FB_SENDER_ID']
FB_RECIPIENT_ID = PARAMS['FB_RECIPIENT_ID']


vonage_message = {
    "warning": f'WARNING! {INPUT_LABEL.capitalize()} reading shows %s ',
    "alarming": f'ALARM! Detected an alarming reading of {INPUT_LABEL.capitalize()}: %s ',
    "caution": f'CAUTION! {INPUT_LABEL.capitalize()} is %s ',
    "broken": f'BROKEN Device! Detected {INPUT_LABEL.capitalize()} reading is %s ',
}


def sms(alert_message):
    request_body = {
        'from': VONAGE_BRAND_NAME,
        'text': alert_message,
        'to': TO_SMS_NUMBER,
        'api_key': VONAGE_API_KEY,
        'api_secret': VONAGE_API_SECRET
    }

    responseData = requests.post(SMS_URL, data=request_body)

    if responseData.json()["messages"][0]["status"] == "0":
        return True
    else:
        return False


def whatsapp(alert_message):
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }

    request_body = {
        "from": {
            "type": "whatsapp",
            "number": WHATSAPP_NUMBER
        },
        "to": {
            "type": "whatsapp",
            "number": TO_WHATSAPP_NUMBER
        },
        "message": {
            "content": {
                "type": "text",
                "text": alert_message
            }
        }
    }

    responseData = requests.post(MESSAGES_API_URL, json=request_body, headers=headers, auth=(VONAGE_API_KEY, VONAGE_API_SECRET))

    if responseData.status_code == 202:
        return True
    else:
        return False


def messenger(alert_message):
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }

    request_body = {
        "from": {
            "type": "messenger",
            "id": FB_SENDER_ID
        },
        "to": {
            "type": "messenger",
            "id": FB_RECIPIENT_ID
        },
        "message": {
            "content": {
                "type": "text",
                "text": alert_message
            }
        }
    }

    responseData = requests.post(MESSAGES_API_URL, json=request_body, headers=headers, auth=(
        VONAGE_API_KEY, VONAGE_API_SECRET))

    if responseData.status_code == 202:
        return True
    else:
        return False


vonage_api = {
    "SMS": sms,
    "WhatsApp": whatsapp,
    "Messenger": messenger
}


def module_main(received_data: any) -> str:
    """
    Send received data to the next module by implementing module's main logic.
    Function description should not be modified.

    Args:
        received_data (any): Data received by module and validated.

    Returns:
        str: Error message if error occurred, otherwise None.

    """

    log.debug("Outputting ...")

    try:
        # YOUR CODE HERE

        message = (vonage_message[ALERT_SEVERITY]) % (received_data[INPUT_LABEL])
        if vonage_api[VONAGE_API](message):
            return None
        else:
            return "Failed to connect with Vonage API."

    except Exception as e:
        return f"Exception in the module business logic: {e}"
