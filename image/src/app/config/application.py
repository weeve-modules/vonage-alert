"""
All constants specific to the application
"""
from app.utils.env import env
from app.utils.floatenv import floatenv


APPLICATION = {
    "INPUT_LABEL": env("INPUT_LABEL", "temperature"),
    "INPUT_UNIT": env("INPUT_UNIT", "Celsius"),
    "ALERT_SEVERITY": env("ALERT_SEVERITY", "warning"),
    "VONAGE_API": env("VONAGE_API", "SMS"),
    "VONAGE_API_KEY": env("VONAGE_API_KEY", ""),
    "VONAGE_API_SECRET": env("VONAGE_API_SECRET", ""),
    "VONAGE_BRAND_NAME": env("VONAGE_BRAND_NAME", "weeve module"),
    "TO_NUMBER": env("TO_NUMBER", ""),
    "WHATSAPP_NUMBER": env("WHATSAPP_NUMBER", ""),
    "SMS_URL": env("SMS_URL", "https://rest.nexmo.com/sms/json"),
    "MESSAGES_API_URL": env("MESSAGES_API_URL", "https://api.nexmo.com/v0.1/messages"),
    "BASE_URL": env("BASE_URL", "https://api.nexmo.com/"),
    "FB_SENDER_ID": env("FB_SENDER_ID", ""),
    "FB_RECIPIENT_ID": env("FB_RECIPIENT_ID", "")
}
