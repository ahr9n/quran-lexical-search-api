from pyarabic.araby import strip_diacritics
import sqlite3

db = sqlite3.connect('quran.db')
cr = db.cursor()

for i in range(1, 6237):
    cr.execute(f'SELECT verse FROM verses WHERE id == {i}')
    verse = cr.fetchall()[0][0]
    verse = verse.replace('۞', '')
    verse = verse.replace('۩', '')
    cr.execute(f'UPDATE verses SET verseWithoutTaskeel = "{strip_diacritics(verse)}" WHERE id = {i}')

db.commit()
db.close()
