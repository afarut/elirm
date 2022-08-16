from django.http import HttpResponse
from django.shortcuts import render
from .forms import AudioForm, ImageForm
import speech_recognition as sr
from pydub import AudioSegment
from PIL import Image
import pytesseract

# Create your views here.
def index(request):
    return render(request, "tools/index.html")


def audio_convertor(request):
    lang = "ru"
    if request.method == "POST":
        form = AudioForm(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            print(dir(cd['file']))
            name, _ = str(cd['file']).split(".")

        if "ogg" in cd['file'].content_type:
            audio = form.save()
            song = AudioSegment.from_ogg(audio.file)
            song.export(f"media/audio_text/{name}.wav", format="wav")
        elif "mp3" in cd['file'].content_type:
            audio = form.save()
            song = AudioSegment.from_mp3(audio.file)
            song.export(f"media/audio_text/{name}.wav", format="wav")
        elif "wav" in cd['file'].content_type:
        	pass
        else:
        	return render(request, "tools/audio_convertor.html", {"form": AudioForm()})

        r = sr.Recognizer()
        file = sr.AudioFile(f'media/audio_text/{name}.wav')
        with file as source:
            r.adjust_for_ambient_noise(source)
            audio = r.record(source)
            text = r.recognize_google(audio, language=lang)
            return HttpResponse(text)
    return render(request, "tools/audio_convertor.html", {"form": AudioForm()})


def image_convertor(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            image = form.save()
            image = Image.open(image.file)
            text = pytesseract.image_to_string(image, lang = "rus")
            return HttpResponse(text)
    return render(request, "tools/image_convertor.html", {"form": ImageForm()})