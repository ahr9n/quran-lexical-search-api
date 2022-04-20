# Quran SQLite Database

## Columns

```sql
- id (int)                     
- verse_pk (text): like(S1V1) 
    'S' for surah number        
    'V' for verse number       
- page (int)                  
- hizbQuarter (int)            
- juz (int)                    
- surah (int<surah number>)   
- verse (text)                 
- verseWithoutTaskeel (text)   
- numberInSurah (int)          
- numberInQuran (int)        
- audio (text <link>)      
- audio1 (text<link>)         
- audio2 (text<link>)        
- sajda (bool)
```

## Source

[Simple Quran API with Indonesia Tafsir and media audio (murrotal) Syekh. Mishary Rashid Alafasy](https://github.com/gadingnst/quran-api)
