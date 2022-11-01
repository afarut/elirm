from django.db import models


class LaboratoryWork(models.Model):
    upload = models.FileField(upload_to ='static/uploads/')
    title = models.CharField('Название лабы', max_length = 200)


    def __str__(self):
    	return self.title