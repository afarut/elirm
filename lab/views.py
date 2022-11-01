from django.shortcuts import render
from django.http import HttpResponse
from .models import LaboratoryWork

# Create your views here.
def index(request):
	labs = LaboratoryWork.objects.all()
	return render(request, "lab/index.html", {"labs": labs})