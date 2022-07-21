from django.shortcuts import render
from django.http import HttpResponse
from elirm.utils import send_to_telegram
import json
import requests


def index(request):
	return render(request, "core/index.html")


def get_json(request):
	data = {"User-Agent": request.headers.get('User-Agent'), "text": "test"}
	return HttpResponse(json.dumps(data), content_type="application/json") 