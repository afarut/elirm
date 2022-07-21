from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import vk_api
import json
import traceback
from elirm.utils import send_to_telegram
from elirm.settings import VK

@csrf_exempt
def vk_bot(request):
	vk_session = vk_api.VkApi(token=VK["API_KEY"])
	vk = vk_session.get_api()
	if request.method == "POST":
		data = json.loads(request.body)
		send_to_telegram(str(data))
		if data['type'] == 'confirmation':
			return HttpResponse('73558d42')
	return HttpResponse('ok')