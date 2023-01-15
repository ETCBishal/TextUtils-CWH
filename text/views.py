from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def analyze(request):
    djText = request.POST.get('text', 'default')
    puncresp = request.POST.get('removepunc', 'off')
    capsfirst = request.POST.get('capsfirst', 'off')
    camalcase = request.POST.get('camalcase', 'off')
    extraspaceremover = request.POST.get('rmvspace', 'off')
    newlineresp = request.POST.get('newlinermvr', 'off')

    if puncresp == "on":
        punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djText:
            if char not in punc:
                analyzed += char
        param = {"purpose": "RemovePunctuation", "work": analyzed}
        djText = analyzed

    if capsfirst == "on":
        text = djText.capitalize()
        param = {"purpose": "CapitalizeFirst", "work": text}

        djText = text

    if camalcase == "on":
        text = djText.title()
        param = {"purpose": "CapitalizeFirst", "work": text}

        djText = text

    if extraspaceremover == "on":
        analyzed = ""
        for i, char in enumerate(djText):
            if not(djText[i] == " " and djText[i+1] == " "):
                analyzed += char
        param = {"purpose": "RemoveExtraSpaces", "work": analyzed}

        djText = analyzed

    if newlineresp == 'on':
        ftext = ""
        for character in djText:
            if character != '\n' and character != '\r':
                ftext += character

        param = {'purpose': 'Remove New Line', 'work': ftext}

        djText = ftext

    if not(puncresp == 'on' or capsfirst == 'on' or camalcase == 'on' or extraspaceremover == 'on' or newlineresp == 'on'):
        return render(request,'Error.html')
    return render(request, 'analyze.html', param)
