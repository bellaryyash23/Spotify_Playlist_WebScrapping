# 🎶Spotify Playlist Musical Time Machine🎶 using BeautifulSoup WebScreaping of Python.

🌟A program which uses BeautifulSoup Package for WebScraping and the Spotify Developer options to automatically create a playlist of the Top 100 songs from a given 
date for the user to enjoy and share with others.

🌟A program which truely gives you a nostalgic feeling and takes you back in time when these songs from created the playlist were the Top hits and maybe even your 
favourites of the time.

👉In the 'main.py' file, first the user is asked for the input of the date to which they want to time travel musically.

![Input Format](https://github.com/bellaryyash23/Spotify_Playlist_WebScrapping/blob/master/samples/input.JPG?raw=true)

👆Input field Date Format👆

👉This input is used to phrase the url of the webpage from where the data or list of songs are to be acquired for web scraping. Now using requests module the html data from
the website is acquired as response and now the BeautifulSoup Object is uesd to parse through the received data.

👉Next, to get the list of the titles of Top 100 songs from the given date, the method of '.find_all()' is used which takes HTML element tag name and class as parameter
and returns a list of all the song titles which is formated using string operations.

👉Now, to get the urls of the songs to create a playlist on Spotify, we need to use the Developer options and first create a Spotify App to access in Python file. Add all
the Client IDs and Client Secrets in the python file. Once done, we can see our developer dashboard has a new app created.

![Spotify Developer Dashboard](https://github.com/bellaryyash23/Spotify_Playlist_WebScrapping/blob/master/samples/developer.jpg?raw=true)

👆Spotify Developer Dashboard👆

👉Python provides simple Authentication management of Spotify Apps from the 'spotify' package. Using this package and Spotify Developer options, the urls for songs from 
the titles of songs list is searched on spotify and stored in a separate list.

👉A new Private playlist is created where the songs will be later added.

👉Using spotify python package methods and the Spotify Developer tools the songs are appended to the previously created Playlist. Thus, the playlist of the Top 100 hits
from given date gets generated and the user can share and enjoy this musical time travel playlist.

![Created Spotify Playlist](https://github.com/bellaryyash23/Spotify_Playlist_WebScrapping/blob/master/samples/playlist.jpg?raw=true)

👆Gist of the created Automatic Spotify Playlist👆
