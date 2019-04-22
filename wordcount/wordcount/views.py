from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    freetext = fulltext.translate({ord(c): None for c in '!@#$.,-—:;<>«"»%?*'})
    wordlist = freetext.lower().split()

    worddict = {}
    for word in wordlist:
        if word in worddict:
            worddict[word] += 1
        else:
            worddict[word] = 1
    sortedwords = sorted(worddict.items(), key=operator.itemgetter(1), reverse=True)
    context = {
        'fulltext': fulltext,
        'count': len(wordlist),
        'sortedwords': sortedwords,
    }
    return render(request, 'count.html', context)