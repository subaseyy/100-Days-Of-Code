from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def counter(request):
    words = request.POST['text']
    text_count = len(words.split())
    return render(request, 'counter.html', {"text": text_count})