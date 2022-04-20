# RESTful Quran API

## Setup
Requires Python3 and the package installer for Python (pip) to run:

* Install requirements: `pip install -r requirements.txt`
* After cloning the repository, refer to the project folder and:
  1. Create new migrations based on the changes in models: `python3 manage.py makemigrations`
  2. Apply the migrations to the database: `python3 manage.py migrate`
  3. Create a superuser to be able to use Django Admin Interface: `python3 manage.py createsuperuser`
  4. Run the app locally: `python3 manage.py runserver`
  5. Visit the site: `http://localhost:8000`
  6. Enjoy!

## How to use
* [all_verses_api](https://ahr9n-quran-api.herokuapp.com/api/all-verses)
  - returns all verses of quran. 
* [search_word_api](https://ahr9n-quran-api.herokuapp.com/api/search-word/مدهامتان)
  - takes a string,
  - returns all verses in `json`, containing the given string. 
  - For example, given a string "مدهامتان", it returns:
  ```json
  {
    "resultsLength": 1,
    "data": [
      {
        "verse_pk": "S055V064",
        "page": 533,
        "hizbQuarter": 213,
        "juz": 27,
        "surah": "الرَّحمن",
        "verse": "مُدْهَامَّتَانِ",
        "verseWithoutTashkeel": "مدهامتان",
        "numberInSurah": 64,
        "numberInQuran": 4965,
        "audio": "https://cdn.alquran.cloud/media/audio/ayah/ar.alafasy/4965",
        "audio1": "https://cdn.islamic.network/quran/audio/128/ar.alafasy/4965.mp3",
        "audio2": "https://cdn.islamic.network/quran/audio/128/ar.alafasy/4965.mp3",
        "sajda": false
      }
    ]
  }
  ```
* [get_surah_api](https://ahr9n-quran-api.herokuapp.com/api/get-surah/1)
  - takes surah number,
  - returns all verses in this Surah in `json`. _Notice that Surah numbers are between 1 and 114._

* [get_verse_api](https://ahr9n-quran-api.herokuapp.com/api/get-verse/2/3)
  - takes surah number and verse number **in the specified surah**,
  - returns the specific verse in `json`. 
  - For example, given number of surah "2" and number of verse "3", it returns the third verse of the second surah:
  ```json
  {
    "data": 
      {
        "verse_pk": "S002V003",
        "page": 2,
        "hizbQuarter": 1, 
        "juz": 1, 
        "surah": "البَقَرَة",
        "verse": "الَّذِينَ يُؤْمِنُونَ بِالْغَيْبِ وَيُقِيمُونَ الصَّلَاةَ وَمِمَّا رَزَقْنَاهُمْ يُنفِقُونَ",
        "verseWithoutTashkeel": "الذين يؤمنون بالغيب ويقيمون الصلاة ومما رزقناهم ينفقون",
        "numberInSurah": 3,
        "numberInQuran": 10,
        "audio": "https://cdn.alquran.cloud/media/audio/ayah/ar.alafasy/10",
        "audio1":"https://cdn.islamic.network/quran/audio/128/ar.alafasy/10.mp3",
        "audio2":"https://cdn.islamic.network/quran/audio/128/ar.alafasy/10.mp3",
        "sajda":false
      }
  }
  ```

## JSON
You can return your needed data in `json` by adding `?format=json`:
```
https://ahr9n-quran-api.herokuapp.com/api/search-word/محمد?format=json
```
