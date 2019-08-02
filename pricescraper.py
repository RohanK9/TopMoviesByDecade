import sqlite3
from namescraper import decades
import requests
from bs4 import BeautifulSoup
from movie import Movie

connection = sqlite3.connect('movies.db')
cursor = connection.cursor()

movies1970s = []
movies1980s = []
movies1990s = []
movies2000s = []

USER_AGENT = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

# decides which table to use based on the decade
def selectTableNameByDecade(decade):
    if decade == "1970s":
        tableName = "movies1970s"
    if decade == "1980s":
        tableName = "movies1980s"
    if decade == "1990s":
        tableName = "movies1990s"
    if decade == "2000s":
        tableName = "movies2000s"

    return tableName

# alright this is an interesting one
# gets the name of the movie from the table and googles it
# scrapes the platform names (Amazon Prime Video, Netflix, Vude, etc.) and prices from results page
def scrape(decade):
    tableName = selectTableNameByDecade(decade)

    for movieName in cursor.execute("SELECT name FROM {}".format(tableName)):

        cleanedName = movieName[0].replace("&", "and").replace(" ", "+")
        linkToScrape = "https://www.google.com/search?q=" + cleanedName + "+movie+online"
        page = requests.get(linkToScrape, headers=USER_AGENT)

        soup = BeautifulSoup(page.text, "html.parser")

        platformSoup = soup.find_all("div", {"class": "i3LlFf"})
        priceSoup = soup.find_all("div", {"class": "V8xno"})

        movie = Movie()

        for platform, price in zip(platformSoup, priceSoup):
            platform = platform.text
            cost = price.text.replace("From", "")

            movie.name = cleanedName
            
            if platform == "YouTube":
                movie.ytcost = cost
            elif platform == "Amazon Prime Video":
                movie.amznprimecost = cost
            elif platform == "Vudu":
                movie.vuducost = cost
            elif platform == "iTunes":
                movie.itunescost = cost
            elif platform == "Google Play Movies & TV":
                movie.googleplaycost = cost
            elif platform == "Netflix":
                movie.netflix = 1
            else:
                pass

        if decade == "1970s":
            movies1970s.append(movie)
        if decade == "1980s":
            movies1980s.append(movie)
        if decade == "1990s":
            movies1990s.append(movie)
        if decade == "2000s":
            movies2000s.append(movie)

        print(decade, cleanedName, "Added a movie")     


# adds the prices to the corresponding tables
def addToDB():      
    for movie in movies2000s:
        cursor.execute("UPDATE movies2000s SET amznPrimeCost = ?, youtubeCost = ?, googlePlayCost = ?, vuduCost = ?, itunesCost = ?, netflixAvailability = ?", (movie.amznprimecost, movie.ytcost, movie.googleplaycost, movie.vuducost, movie.itunescost, movie.netflix))
    
    for movie in movies1990s:
        cursor.execute("UPDATE movies1990s SET amznPrimeCost = ?, youtubeCost = ?, googlePlayCost = ?, vuduCost = ?, itunesCost = ?, netflixAvailability = ?", (movie.amznprimecost, movie.ytcost, movie.googleplaycost, movie.vuducost, movie.itunescost, movie.netflix))
    
    for movie in movies1980s:
        cursor.execute("UPDATE movies1980s SET amznPrimeCost = ?, youtubeCost = ?, googlePlayCost = ?, vuduCost = ?, itunesCost = ?, netflixAvailability = ?", (movie.amznprimecost, movie.ytcost, movie.googleplaycost, movie.vuducost, movie.itunescost, movie.netflix))
    
    for movie in movies1970s:
        cursor.execute("UPDATE movies1970s SET amznPrimeCost = ?, youtubeCost = ?, googlePlayCost = ?, vuduCost = ?, itunesCost = ?, netflixAvailability = ?", (movie.amznprimecost, movie.ytcost, movie.googleplaycost, movie.vuducost, movie.itunescost, movie.netflix))
    
    connection.commit()

# if __name__ == "__main__":
#     for decade in decades:
#         scrape(decade)

#     addToDB()

if __name__ == "__main__":
    for name in cursor.execute("SELECT * FROM movies2000s"):
        print(name)