# views.py
# I have created this file - Harry
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

    # return HttpResponse("Home")

def analyze(request):
    djtext=request.GET.get("text", "default")
    remove = request.GET.get("removepunc", "off")
    print(remove)
    if remove=="on":
        punctuations="""!~`@#$%^&*()_\.,'"?<>-/{[}]|;:"""
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params={'purpose':'Remove Punctuations','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    else:
        analyzed=djtext
        params={"purpose":"Don't Make Change",'analyzed_text':analyzed}
        return render(request,'analyze.html',params)


def removepunc(request):
    print(request.GET.get("text","default"))
    return HttpResponse("remove punc")

def capfirst(request):
    return HttpResponse("capitalize first")

def newlineremove(request):
    return HttpResponse("newline remove first")


def spaceremove(request):
    return HttpResponse("space remover back")

def charcount(request):
    return HttpResponse("charcount ")