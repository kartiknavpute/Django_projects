# i have create a this file kartik
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
     return render(request,'index2.html')


def analyze(request):
     djtext = request.POST.get('text','default')
     removepunc = request.POST.get('removepunc','off')
     fullcaps = request.POST.get('fullcaps','off')
     newlineremover = request.POST.get('newlineremover','off')
     extraspaceremover = request.POST.get('extraspaceremover','off')
     # analyze = djtext
     if removepunc == "on" and fullcaps=="on":
          punctuations='''<>,'*\():`{}-""''...!.~?;/[]'''
          analyze =""
          for char in djtext:
               if char not in punctuations:
                    analyze = analyze + char.upper()
          params={'purpose':'Removed Punctuations and upper case letter','anylyzed_text':analyze}
          return render(request,'analyze.html',params)
     if fullcaps=="on":
          analyze=""
          for char in djtext:
               analyze = analyze + char.upper()
          params={'purpose':'upper case letter','anylyzed_text':analyze}
          analyze = djtext

          return render(request,'analyze.html',params)
     if removepunc=="on":
          punctuations='''<>,'*\():`{}-""''...!.~?;/[]'''
          analyze =""
          for char in djtext:
               if char not in punctuations:
                    analyze = analyze + char
          params = {'purpose': 'Remove Punctuations', 'anylyzed_text': analyze}
          analyze = djtext
          return render(request, 'analyze.html', params)
     if newlineremover =="on":
          analyze =""
          for char in djtext:
               if char != "\n" and char!="\r":
                    analyze = analyze +char.upper()
          params = {'purpose': 'newlineremover', 'anylyzed_text': analyze}
          analyze = djtext

          return render(request,'analyze.html', params)
     if extraspaceremover == "on":
          analyze = ""
          for char in (djtext):
               if char != "\n":
                    analyze = analyze + char.upper()
          params = {'purpose': 'Extra spaceremover', 'anylyzed_text': analyze}
          analyze = djtext
          return render(request, 'analyze.html', params)

     else:
          return HttpResponse("Error")
