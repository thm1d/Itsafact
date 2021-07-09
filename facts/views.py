from django.shortcuts import render
import requests

def factView(req):
    r = requests.get('https://uselessfacts.jsph.pl/random.json').json()
    #print(r['text'])
    context = {
        'text': r['text']
    }
    return render(req, 'facts/index.html', context)
