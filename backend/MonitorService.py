from TwilioWhatsapp import send_whatsapp_message
from URLChecker import  find_text_from_URL, extract_text_from_URL
import json
import time
import os

def monitor_service():
    while True:
        # every one hour check the service itself is working.
        send_whatsapp_message(os.environ['ADMIN_PHONE_NUMBER'], "From Downotifier: the monitoring service is fully functioning")

        for i in range(60):
            with open("site_to_monitor.json") as site_info:
                site_info = json.load(site_info)

            for site in site_info:
                if not find_text_from_URL(site['URL'], site['text_to_find']):
                    send_whatsapp_message(site['phone_number'], "Your site {} is down, please check it".format(site['URL']))
                    print(site['URL'] + " is down.")

            time.sleep(60)

if __name__ == "__main__":
    monitor_service()