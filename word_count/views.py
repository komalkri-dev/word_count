from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')

def count(request):
    FullText = request.GET['FullText']
    wordlist = FullText.split()

    WordDict = {}

    for word in wordlist:
        if word in WordDict:
            WordDict[word] += 1
        else:
            WordDict[word] = 1

    sorted_words = sorted(WordDict.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'FullText':FullText, 'count':len(wordlist), 'sorted_words':sorted_words})

def about(reuest):
    return render(reuest, 'about.html')