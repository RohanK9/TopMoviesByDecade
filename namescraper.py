import urllib.request
from bs4 import BeautifulSoup
from movie import Movie
import sqlite3

decades = ["1970s", "1980s", "1990s", "2000s"]

# lists for movie objects
movies1970s = []
movies1980s = []
movies1990s = []
movies2000s = []

connection = sqlite3.connect('movies.db')
cursor = connection.cursor()

# decides which rotten tomatoes link to use based on the decade
def selectLinkByDecade(decade):
    if decade == "1970s":
        linkToScrape = "https://editorial.rottentomatoes.com/guide/essential-1970s-movies/"
        numPages = 3

    if decade == "1980s":
        linkToScrape = "https://editorial.rottentomatoes.com/guide/140-essential-80s-movies/"
        numPages = 4

    if decade == "1990s":
        linkToScrape = "https://editorial.rottentomatoes.com/guide/140-essential-90s-movies/"
        numPages = 4

    if decade == "2000s":
        linkToScrape = "https://editorial.rottentomatoes.com/guide/essential-2000s-movies/"
        numPages = 4

    return numPages, linkToScrape

# goes through the soup and finds the name, year, and poster of a movie
# saves that data into an object
# object is added to a list corresponding to the decade it belongs to
def parse(decade, name, year, image):
    if decade == "1970s":
        movie1970 = Movie()
        movie1970.name = name.a.string
        movie1970.year = (year.text).strip('()')
        movie1970.poster = image['src']
        movies1970s.append(movie1970)
        
    if decade == "1980s":
        movie1980 = Movie()
        movie1980.name = name.a.string
        movie1980.year = (year.text).strip('()')
        movie1980.poster = image['src']
        movies1980s.append(movie1980)
        
    if decade == "1990s":
        movie1990 = Movie()
        movie1990.name = name.a.string
        movie1990.year = (year.text).strip('()')
        movie1990.poster = image['src']
        movies1990s.append(movie1990)
        
    if decade == "2000s":
        movie2000 = Movie()
        movie2000.name = name.a.string
        movie2000.year = (year.text).strip('()')
        movie2000.poster = image['src']
        movies2000s.append(movie2000)

# scrapes data from each page of the 4 different rotten tomatoes links
def scrape(decade):
    numPages, linkToScrape = selectLinkByDecade(decade)

    for pageNum in range(1, numPages+1):
        rottenTomatoesLink = linkToScrape + str(pageNum) + "/"
        page = urllib.request.urlopen(rottenTomatoesLink)

        soup = BeautifulSoup(page, "html.parser")

        nameSoup = soup.findAll("div", {"class": "article_movie_title"})
        dateSoup = soup.findAll("span",{"class": "subtle start-year"})
        imageSoup = soup.findAll("img",{"class": "article_poster"})

        movie2000 = Movie()

        for name, year, image in zip(nameSoup, dateSoup, imageSoup):
            parse(decade, name, year, image)

# adds the names, years, and posters to the corresponding tables
def addToDB():      
    for movie in movies2000s:
        cursor.execute("INSERT INTO movies2000s (name, year, poster) VALUES (?, ?, ?)", (movie.name, movie.year, movie.poster))
    
    for movie in movies1990s:
        cursor.execute("INSERT INTO movies1990s (name, year, poster) VALUES (?, ?, ?)", (movie.name, movie.year, movie.poster))
    
    for movie in movies1980s:
        cursor.execute("INSERT INTO movies1980s (name, year, poster) VALUES (?, ?, ?)", (movie.name, movie.year, movie.poster))
    
    for movie in movies1970s:
        cursor.execute("INSERT INTO movies1970s (name, year, poster) VALUES (?, ?, ?)", (movie.name, movie.year, movie.poster))
    
    connection.commit()

if __name__ == "__main__":
    for decade in decades:
        scrape(decade)

    addToDB()