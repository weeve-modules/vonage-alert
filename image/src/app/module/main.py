"""
This file receives data and passes a specific, to Vonage API, a specific alert triggered by the received data.
"""
import requests
from app.config import APPLICATION

# module settings
INPUT_LABEL = APPLICATION['INPUT_LABEL']
INPUT_UNIT = APPLICATION['INPUT_UNIT']
ALERT_SEVERITY = APPLICATION['ALERT_SEVERITY']
VONAGE_API = APPLICATION['VONAGE_API']

# Vonage API specifics
VONAGE_API_KEY = APPLICATION['VONAGE_API_KEY']
VONAGE_API_SECRET = APPLICATION['VONAGE_API_SECRET']
VONAGE_BRAND_NAME = APPLICATION['VONAGE_BRAND_NAME']
TO_SMS_NUMBER = '+' + APPLICATION['TO_NUMBER']
SMS_URL = APPLICATION['SMS_URL']
MESSAGES_API_URL = APPLICATION['MESSAGES_API_URL']
BASE_URL = APPLICATION['BASE_URL']
WHATSAPP_NUMBER = APPLICATION['WHATSAPP_NUMBER']
TO_WHATSAPP_NUMBER = APPLICATION['TO_NUMBER']
FB_SENDER_ID = APPLICATION['FB_SENDER_ID']
FB_RECIPIENT_ID = APPLICATION['FB_RECIPIENT_ID']

vonage_message = {
    "warning": f'WARNING! {INPUT_LABEL.capitalize()} reading shows %s {INPUT_UNIT.capitalize()} ',
    "alarming": f'ALARM! Detected an alarming reading of {INPUT_LABEL.capitalize()}: %s {INPUT_UNIT.capitalize()} ',
    "caution": f'CAUTION! {INPUT_LABEL.capitalize()} is %s {INPUT_UNIT.capitalize()} ',
    "broken": f'BROKEN Device! Detected {INPUT_LABEL.capitalize()} reading is %s {INPUT_UNIT.capitalize()} ',
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

    responseData = requests.post(MESSAGES_API_URL, json=request_body, headers=headers, auth=(
        VONAGE_API_KEY, VONAGE_API_SECRET))

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

    print(responseData.text)

    if responseData.status_code == 202:
        return True
    else:
        return False


vonage_api = {
    "SMS": sms,
    "WhatsApp": whatsapp,
    "Messenger": messenger
}


def module_main(parsed_data):
    """
    Implement module logic here. Although this function returns data, remember to implement
    egressing method to external database or another API.

    Args:
        parsed_data ([JSON Object]): [The output of data_validation function]

    Returns:
        [string, string]: [data, error]
    """
    try:
        message = (vonage_message[ALERT_SEVERITY]) % (parsed_data[INPUT_LABEL])
        if vonage_api[VONAGE_API](message):
            return None, None
        else:
            return None, "Failed to connect with Vonage API"
    except Exception:
        return None, "Unable to perform the module logic"
