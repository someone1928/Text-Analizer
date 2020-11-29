from django.http import HttpResponse
from django.shortcuts import render
import webbrowser
def index(request):
    return render(request,'index2.html')

def result(request):
    text=request.POST.get('djtex','nothing')
    fcaps=request.POST.get('capital','off')
    rmspace=request.POST.get('spacerm','off')
    upcs=request.POST.get('uppec','off')
    scr=request.POST.get('src',"")
    print(text)
    print(fcaps)
    print(rmspace)
    print(upcs)

    params={
        'text':text,
        'scr':f'https://www.google.com/search?q={scr}'
    }
    if text:
        if fcaps=='on':
            params.update({'text':params['text'].capitalize()})
        else:
            pass
        
        if rmspace=='on':
            params.update({'text':params['text'].replace(' ','')})
        else:
            pass

        if upcs=='on':
            params.update({'text':params['text'].upper()})
        else:
            pass
        return render(request,'result2.html',params)
    else:
        return HttpResponse('We can\'t find the text')
    