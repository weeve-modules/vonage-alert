from os import getenv

PARAMS = {
    "INPUT_LABEL": getenv("INPUT_LABEL", "temperature"),
    "ALERT_SEVERITY": getenv("ALERT_SEVERITY", "warning"),
    "VONAGE_API": getenv("VONAGE_API", "SMS"),
    "VONAGE_API_KEY": getenv("VONAGE_API_KEY", ""),
    "VONAGE_API_SECRET": getenv("VONAGE_API_SECRET", ""),
    "VONAGE_BRAND_NAME": getenv("VONAGE_BRAND_NAME", "weeve module"),
    "TO_NUMBER": getenv("TO_NUMBER", ""),
    "WHATSAPP_NUMBER": getenv("WHATSAPP_NUMBER", ""),
    "SMS_URL": getenv("SMS_URL", "https://rest.nexmo.com/sms/json"),
    "MESSAGES_API_URL": getenv("MESSAGES_API_URL", "https://api.nexmo.com/v0.1/messages"),
    "BASE_URL": getenv("BASE_URL", "https://api.nexmo.com/"),
    "FB_SENDER_ID": getenv("FB_SENDER_ID", ""),
    "FB_RECIPIENT_ID": getenv("FB_RECIPIENT_ID", "")
}
