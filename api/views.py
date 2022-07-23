from django.shortcuts import render
from django.http import HttpResponse
import json
import pytesseract
from PIL import Image
from django.views.decorators.csrf import csrf_exempt
from django.utils.datastructures import MultiValueDictKeyError
from elirm.settings import TESSERACT_LANGS
from pydub import AudioSegment
import speech_recognition as sr
import random

# Create your views here.
def index(request):
    return render(request, "api/index.html")

def get_json(request):
    data = {"User-Agent": request.headers.get('User-Agent'), "text": "test"}
    return HttpResponse(json.dumps(data), content_type="application/json") 


@csrf_exempt
def image_text(request):
    try:
        lang = request.POST["lang"]
    except MultiValueDictKeyError:
        response = {"text": "Отсутствует язык"}
        return HttpResponse(json.dumps(response), content_type="application/json", status=204)
    try:
        ext = request.POST["extension"]
    except MultiValueDictKeyError:
        response = {"text": "Отсутствует определение расширения"}
        return HttpResponse(json.dumps(response), content_type="application/json", status=204)
    try:
        lang = request.POST["lang"]
    except MultiValueDictKeyError:
        response = {"text": "Отсутствует язык"}
        return HttpResponse(json.dumps(response), content_type="application/json", status=204)
    try:
        last_name = request.FILES["file"].name.split(".")
        name = last_name[0] + "".join(random.sample("qwertyuiopasdfghjklzxcvbnm", 6)) + "." + ext
    except MultiValueDictKeyError:
        response = {"text": "Отсутствует файл", "example": "png jpg jpeg"}
        return HttpResponse(json.dumps(response), content_type="application/json", status=204)
    
    if lang not in TESSERACT_LANGS:
        response = {"text": "Выберите другой язык", "example": " ".join(TESSERACT_LANGS)}
        return HttpResponse(json.dumps(response), content_type="application/json", status=406)

    with open(f'media/image_text/{name}', 'wb+') as destination:
        for chunk in request.FILES["file"].chunks():
            destination.write(chunk)

    image = Image.open(f'media/image_text/{name}')
    text = pytesseract.image_to_string(image ,lang = lang)
    response = {"text": text, "lang": lang}
    return HttpResponse(json.dumps(response), content_type="application/json")


@csrf_exempt
def audio_text(request):
    try:
        lang = request.POST["lang"]
    except MultiValueDictKeyError:
        response = {"text": "Отсутствует язык"}
        return HttpResponse(json.dumps(response), content_type="application/json", status=204)
    try:
        ext = request.POST["extension"]
    except MultiValueDictKeyError:
        response = {"text": "Отсутствует определение расширения"}
        return HttpResponse(json.dumps(response), content_type="application/json", status=204)
    try:
        lang = request.POST["lang"]
    except MultiValueDictKeyError:
        response = {"text": "Отсутствует язык"}
        return HttpResponse(json.dumps(response), content_type="application/json", status=204)
    try:
        last_name = request.FILES["file"].name.split(".")
        name = last_name[0] + "".join(random.sample("qwertyuiopasdfghjklzxcvbnm", 6))
    except MultiValueDictKeyError:
        response = {"text": "Отсутствует файл", "example": "png jpg jpeg"}
        return HttpResponse(json.dumps(response), content_type="application/json", status=204)
    
    if len(lang) != 3:
        response = {"text": "Язык введён некорректно", "example": " ".join(TESSERACT_LANGS)}
        return HttpResponse(json.dumps(response), content_type="application/json", status=400)
    else:
    	lang = lang[0:2]

    with open(f'media/audio_text/{name+"."+ext}', 'wb+') as destination:
        for chunk in request.FILES["file"].chunks():
            destination.write(chunk)
    if ext == "ogg":
    	song = AudioSegment.from_ogg(f"media/audio_text/{name}.ogg")
    	song.export(f"media/audio_text/{name}.wav", format="wav")
    elif ext == "mp3":
    	song = AudioSegment.from_mp3(f"media/audio_text/{name}.mp3")
    	song.export(f"media/audio_text/{name}.wav", format="wav")

    r = sr.Recognizer()
    file = sr.AudioFile(f'media/audio_text/{name}.wav')
    with file as source:
        r.adjust_for_ambient_noise(source)
        audio = r.record(source)
        text = r.recognize_google(audio, language=lang)
    response = {"text": text, "lang": lang}
    return HttpResponse(json.dumps(response), content_type="application/json")