from unittest import result
from django.shortcuts import render
from django.db.models import Q
from .models import Verses
import requests  
import json
from urllib import parse

# Create your views here.

def index(request):
    """ Home Page """
    return render(request, "search/index.html")


def search_by_word(request):
    words = request.POST.get('ayah')
    if words:
        if 'lexical' in request.POST:
            verses = Verses.objects.filter(
                Q(verse__icontains=words) | Q(verseWithoutTashkeel__icontains=words)
            )
            search_result = 'lexical'
            print(verses)
        else: # 'semantic' is in request.POST
            words = parse.quote(words)
            
            # I launched the lexical search on a different port
            url = f"http://localhost:5000/similar-verse/{words}"
            headers = {'content-type': 'application/json'}
            results = requests.get(url, headers=headers)
            search_result = 'semantic'
            
            # convert json to map to iterate over verses
            results = json.loads(results)
            results = results['results']

            # get verses from database
            verses = []
            for score, verse_id, verse in results:
                verse = Verses.objects.get(id=verse_id)
                verses.append(verse)
            
        out = {'verses': verses, 'search_result': search_result}
        # print(verses)
        return render(request, 'search/search.html', out)
    else:
        return index(request)


def get_surah(request, surah_id):
    surah_pk = f"S{str(surah_id).zfill(3)}"
    surah = Verses.objects.filter(
        Q(verse_pk__icontains=surah_pk)
    )
    verses = {'verses': surah}
    return render(request, 'search/search.html', verses)


def api_docs(request):
    return render(request, 'search/api.html')
