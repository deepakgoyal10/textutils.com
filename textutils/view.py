# I have created this file - Deepak
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request, 'index.html')


def analyze(request):
    # get the text
    djtext = (request.POST.get('text','default'))

    # Check the checkbox value
    removepunc = (request.POST.get('removepunc','off'))
    allcaps = (request.POST.get('allcaps','off'))
    spaceremover = (request.POST.get('spaceremover','off'))
    charcount = (request.POST.get('charcount', 'off'))

    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    param= {}
    # check which checkbox is on
    if removepunc == "on":
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed+char
        param = {'purpose': 'Remove Punctuations', 'analyzed_text' : analyzed}
        djtext = analyzed

    if allcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        param = {'purpose': 'ALL UPPERCASE', 'analyzed_text': analyzed}
        djtext = analyzed

    if spaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index] == djtext[index+1]): # agar aisa nhi hota hai to ye is condition me ghusega
                analyzed = analyzed+char
        param = {'purpose': 'remove extra space', 'analyzed_text': analyzed}
        djtext = analyzed

    if charcount == "on":
        analyzed = len(djtext)
        param = {'purpose': 'Count the character', 'analyzed_text': analyzed}


    if removepunc != "on" and allcaps != "on" and spaceremover != "on" and charcount != "on":
        return HttpResponse("Error")

    return render(request, 'analyze.html', param)

def about(request):
    return render(request, 'about.html')
