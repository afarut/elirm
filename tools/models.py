from django.db import models


class Image(models.Model):    
	file = models.ImageField(upload_to='media/image_text')

	def __str__(self):
		return "Изображение"


class Audio(models.Model):    
	file = models.FileField(upload_to='media/audio_text')

	def __str__(self):
		return "Аудио"