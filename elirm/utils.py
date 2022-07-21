import requests
from .settings import TELEGRAM
import logging
import datetime


logger = logging.getLogger(__name__)

def send_to_telegram(text):
	s = requests.Session()
	url = f"https://api.telegram.org/bot{TELEGRAM['API_KEY']}/sendMessage"
	for user_id in TELEGRAM['admins']:
		data = {"chat_id": user_id, "text": text}
		req = s.post(url, data=data)

		if req.status_code != 200:
			logger.error(f"ERROR|{str(datetime.datetime.now())}|Telegram: {req.json()['description']}")