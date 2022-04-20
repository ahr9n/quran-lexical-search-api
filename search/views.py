from django.shortcuts import render
from django.db.models import Q
from .models import Verses


# Create your views here.

def index(request):
    """ Home Page """
    return render(request, "search/index.html")


def search_by_word(request):
    words = request.POST.get('ayah')
    if words:
        verses = Verses.objects.filter(
            Q(verse__icontains=words) | Q(verseWithoutTashkeel__icontains=words)
        )
        print(verses)
        verses = {'verses': verses}
        print(verses)
        return render(request, 'search/search.html', verses)
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
