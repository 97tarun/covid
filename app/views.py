from django.shortcuts import render
import requests
import urllib,json
# Create your views here.

def covid(request):
    url='https://api.covid19india.org/data.json'
    res=urllib.request.urlopen(url)
    data=json.loads(res.read())

    labels=[]
    chartdata=[]
    for state in data['statewise']:
        labels.append(state['state'])
        chartdata.append(state['confirmed'])
    
    return render(request, 'covid.html',{'data':data, 'labels':labels, 'chartdata':chartdata})


