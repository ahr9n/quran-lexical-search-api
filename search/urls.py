from django.urls import path
from .views import *
from .api_views import *

app_name = 'search'

urlpatterns = [
    # views
    path('', index, name='index'),
    path('search-word', search_by_word, name='search_by_word'),
    path('surah/<int:surah_id>', get_surah, name='get_surah'),
    path('api', api_docs, name='api_docs'),

    # API views
    path('api/all-verses', all_verses_api, name='all_verses_api'),
    path('api/search-word/<str:words>', search_word_api, name='search_word_api'),
    path('api/get-surah/<int:surah_id>', get_surah_api, name='get_surah_api'),
    path('api/get-verse/<int:surah_id>/<int:verse_id>', get_verse_api, name='get_verse_api'),
]
