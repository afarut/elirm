from django import forms
from .models import *


class AudioForm(forms.ModelForm):
	class Meta:
		model = Audio
		fields = ['file']


class ImageForm(forms.ModelForm):
	class Meta:
		model = Image
		fields = ['file']