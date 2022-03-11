# Vonage Alert

|                |                                 |
| -------------- | ------------------------------- |
| Name           | Vonage Alert                    |
| Version        | v0.0.2                          |
| Dockerhub Link | [weevenetwork/weeve-vonage-alert](https://hub.docker.com/r/weevenetwork/vonage-alert) |
| Authors        | Jakub Grzelak                   |



- [Vonage Alert](#vonage-alert)
  - [Description](#description)
  - [Features](#features)
  - [Supported Vonage Channels](#supported-vonage-channels)
  - [Sample Notifications](#sample-notifications)
  - [Environment Variables](#environment-variables)
    - [Module Specific](#module-specific)
    - [Set by the weeve Agent on the edge-node](#set-by-the-weeve-agent-on-the-edge-node)
  - [Dependencies](#dependencies)
  - [Input](#input)
  - [Output](#output)
  - [Docker Compose Example](#docker-compose-example)
  - [Additional Vonage Documentation and Resources](#additional-vonage-documentation-and-resources)


## Description

Vonage Alert is an alerting module responsible for sending notifications to Vonage API channels when triggered.
Currently supported channels are SMS, WhatsApp and Facebook Messenger.
Vonage Alert receives data and compares them to constraints set by a developer, if data are breaking the constraints then the module is sending a notification to a chosen Vonage channel.
This module is containerized using Docker.


## Features

* Egress data from data service
* Send notification to Vonage Channel: SMS, WhatsApp or Facebook Messenger

## Supported Vonage Channels

* SMS
* WhatsApp
* Facebook Messenger


## Sample Notifications

| Type     | Text                                                                                               |
| -------- | -------------------------------------------------------------------------------------------------- |
| warning  | _WARNING for MachineName! Temperature reading shows 41.19 Celsius (< 49.0 Celsius)._               |
| alarming | _ALARM from MachineName! Detected an alarming reading of Temperature: 100 Celsius (> 20 Celsius)._ |
| caution  | _CAUTION for MachineName! Temperature is 100 Celsius (>= 20 Celsius)._                             |
| broken   | _BROKEN device MachineName! Detected Temperature reading is -1.1 Celsius (<= -1 Celsius)._         |


## Environment Variables

### Module Specific

The following module configurations can be provided in a data service designer section on weeve platform:


| Name                  | Environment Variables | Type    | Description                                                                                                                                                                                                                    |
| --------------------- | --------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Input Label           | INPUT_LABEL           | string  | The field to apply alert on, i.e: "temperature"                                                                                                                                                                                |
| Input Unit            | INPUT_UNIT            | string  | I.e: "Celsius"                                                                                                                                                                                                                 |
| Alert Severity        | ALERT_SEVERITY        | string  | Alert type: warning, alarming, caution, broken                                                                                                                                                                                 |
| Vonage API            | VONAGE_API            | string  | Supported Vonage API channel: SMS, WhatsApp, Facebook Messenger                                                                                                                                                                |
| Vonage API Key        | VONAGE_API_KEY        | string  | Your Vonage API key (see it on your Vonage dashboard).                                                                                                                                                                         |
| Vonage API Secret     | VONAGE_API_SECRET     | string  | Your Vonage API secret (also available on your Vonage dashboard).                                                                                                                                                              |
| Vonage Brand Name     | VONAGE_BRAND_NAME     | string  | The alphanumeric string that represents the name or number of the organization sending the message.                                                                                                                            |
| To Number             | TO_NUMBER             | string  | The phone number you are sending the message to. Don't use a leading + or 00 when entering a phone number, start with the country code, for example, 447700900000.                                                             |
| SMS URL               | SMS_URL               | string  | Vonage SMS API endpoint: https://rest.nexmo.com/sms/json                                                                                                                                                                       |
| Messages API URL      | MESSAGES_API_URL      | string  | Vonage WhatsApp Messages API endpoint. For production use the Messages API endpoint is https://api.nexmo.com/v0.1/messages. For sandbox testing the Messages API endpoint is https://messages-sandbox.nexmo.com/v0.1/messages. |
| Base URL              | BASE_URL              | string  | For production use the base URL is https://api.nexmo.com/. For sandbox testing the base URL is https://messages-sandbox.nexmo.com/                                                                                             |
| WhatsApp Number       | WHATSAPP_NUMBER       | string  | The WhatsApp number that has been allocated to you by Vonage. For sandbox testing the number is 14157386170.                                                                                                                   |
| Facebook Sender ID    | FB_SENDER_ID          | string  | Facebook Messenger own form of ID for a business. Facebook Page (business) - Page ID                                                                                                                                           |
| Facebook Recipient ID | FB_RECIPIENT_ID       | string  | Facebook Messenger own form of ID for a user. acebook User (profile) - Page-Scoped ID (PSID)                                                                                                                                   |


Weeve agent will set SMS_URL, MESSAGES_API_URL and BASE_URL.
Moreover, other features required for establishing the inter-container communication between modules in a data service are set by weeve agent.


### Set by the weeve Agent on the edge-node

| Environment Variables | type   | Description                            |
| --------------------- | ------ | -------------------------------------- |
| EGRESS_API_HOST       | string | HTTP ReST endpoint for the next module |
| MODULE_NAME           | string | Name of the module                     |


## Dependencies

```txt
Flask==1.1.1
requests
python-decouple==3.4
```

## Input

Input to this module is JSON body single object:

Example:
```node
{
  temperature: 15,
}
```

## Output

This module does not produce any output except Slack notifications.

## Docker Compose Example

```yml
version: "3"
services:
  vonage-alert:
    image: weevenetwork/weeve-slack-alert
    environment:
      MODULE_NAME: vonage-alert
      INPUT_LABEL: 'temperature'
      INPUT_UNIT: 'Celsius'
      ALERT_SEVERITY: 'broken'
      VONAGE_API: 'WhatsApp'
      VONAGE_API_KEY: 'abc123'
      VONAGE_API_SECRET: 'abc123'
      VONAGE_BRAND_NAME: 'Weeve Vonage Testing'
      TO_NUMBER: '1234567890'
      SMS_URL: 'https://rest.nexmo.com/sms/json'
      MESSAGES_API_URL: 'https://messages-sandbox.nexmo.com/v0.1/messages'
      BASE_URL: 'https://messages-sandbox.nexmo.com/'
      WHATSAPP_NUMBER: '1234567890'
      FB_SENDER_ID: '1234567890'
      FB_RECIPIENT_ID: '1234567890'
    ports:
      - 5000:80
```

## Additional Vonage Documentation and Resources

* SMS: [Vonage SMS API](https://developer.nexmo.com/messaging/sms/code-snippets/send-an-sms)
* WhatsApp: [Vonage WhatsApp API](https://developer.nexmo.com/messages/code-snippets/whatsapp/send-text)
* Facebook Messenger: [Vonage Facebook API](https://developer.nexmo.com/messages/concepts/facebook)
* Sandbox Testing: [Vonage Sandbox](https://developer.nexmo.com/messages/concepts/messages-api-sandbox)