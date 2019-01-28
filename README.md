How to extract your word list from google translate:

A fast way to create a vocabulary list while watching a TV show or a movie is to use the google translate app. You can use the voice recognition to enter the word faster. Make sure to enter the word exactly like it is spelled in the subtitles, otherwise this script won't work. Save the words by clicking on the star. Here is how you can export this list:
1. Open the google translate website on your computer: https://translate.google.com/
2. Click on "Saved" at the bottom of the page. 
3. On the right, click on the language pair that you want to filter. For example "French -> English"
4. Click on the weird square button that says "Export to Google Sheets".
5. In Google Sheets, keep only the column with the words that you want to study. Delete all the other columns.
6. Export the file. Go to file -> Download as -> Comma-separated values. This will download a .csv file that you will need later.
Alternatively, if you don't like using Google translate, you can also simply create a vocabulary list in Google Sheets and export it. Just make sure that the words match exactly the words from the subtitles.

How to download the subtitles from Netflix:

1. Install https://chrome.google.com/webstore/detail/tampermonkey/dhdgffkkebhmkfjojejmpbldmpobfkfo
2. Install https://greasyfork.org/en/scripts/26654-netflix-subtitle-downloader
3. To download the subtitles file from Netflix, open the episode in Netflix and download them by clicking on "Download subs from this episode". See: https://greasyfork.org/system/screenshots/screenshots/000/013/616/original/menu.png?1546605608

How to add examples sentences the the list of words:

1. Create an empty folder in your computer. There should be 3 files in it:
            - the .csv files of the words from google translate
            - the .vtt files 
            - the file called "vtt_to_csv.py"
5. In the terminal, navigate to the folder you created, type this command and then hit enter: python vtt_to_csv.py
6. This will create a file called words_with_sentences.csv
7. Import this file in google sheets and voilà, you now have your list of words with a matching sentence extracted from that episode.
8. Important: delete all the files in the folder except for the file called "vtt_to_csv.py" before you run the script again.
