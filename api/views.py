from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.
def index(request):
	return render(request, "api/index.html")

def get_json(request):
	data = {"User-Agent": request.headers.get('User-Agent'), "text": "test"}
	return HttpResponse(json.dumps(data), content_type="application/json") 