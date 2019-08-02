
# def addToList(name, year, image, movies2000s):
#     movie.name = name.a.string
#     movie.year = (year.text).strip('()')
#     movie.poster = image['src']
#     movies2000s.append(movie)
#     movie.reset()

# # print(name.a.string)
# names.append(name.a.string)
# # print((year.text).strip('()'))
# years.append((year.text).strip('()'))
# # print(image['src'])
# images.append(image['src'])

# num = 1
# for name, year, image in zip(names, years, images):
#     print(num, name, year, image)
#     num = num + 1

# for image in images:
#     print(num, image)
#     num = num +1

# for name, year, image in zip(names, years, images):
#     movie = Movie()
#     movie.name = name
#     movie.year = year
#     movie.image = image

#     movie2000s.append(movie)

# for movie in movie2000s:
#     print(movie.name, movie.year)

# cursor.execute("DELETE FROM movies1970s")
# cursor.execute("DELETE FROM movies1980s")
# cursor.execute("DELETE FROM movies1990s")
# cursor.execute("DELETE FROM movies2000s")
# connection.commit()
           
# for decade in decades:
#     scrape(decade)

# for movie in movies2000s:
#     cursor.execute("INSERT INTO movies2000s (name, year, poster) VALUES (?, ?, ?)", (movie.name, movie.year, movie.poster))

# for movie in movies1990s:
#     cursor.execute("INSERT INTO movies1990s (name, year, poster) VALUES (?, ?, ?)", (movie.name, movie.year, movie.poster))

# for movie in movies1980s:
#     cursor.execute("INSERT INTO movies1980s (name, year, poster) VALUES (?, ?, ?)", (movie.name, movie.year, movie.poster))

# for movie in movies1970s:
#     cursor.execute("INSERT INTO movies1970s (name, year, poster) VALUES (?, ?, ?)", (movie.name, movie.year, movie.poster))

# connection.commit()

# cursor.execute("INSERT INTO movies2000s (name, year, poster) VALUES (?, ?, ?)", ("The Dark Knight", 2008, "https://resizing.flixster.com/2cf9FQ6fOfRyQm-2KIcph7xHv1A=/180x270/v1.bTsxMTE2NTE2MDtqOzE4MjA0OzIwNDg7ODAwOzEyMDA"))
# connection.commit()

# has all the links but is an absolute mess
# linkSoup = soup.find_all("a", href=True)
    
#     for link in linkSoup:
#         print(link["href"])

# testDictionary = {"movie1": [{"yt": 3.99, "itunes": 3.99, "prime": 3.99, "netflix":1}], "movie2": [{"yt": 3.99, "itunes": 3.99, "prime": 3.99, "netflix":1}]}

# for movie in testDictionary:
#     print(testDictionary[movie])
    
# name can be found in the i3LlFf class
# price can be found in the V8xno class

# for movie in cursor.execute("SELECT name FROM movies1970s"):
#     print(movie[0].replace(" ", "+"))

# toSearch = https://www.google.com/search?q= + movie name
# getPrice = urllib.request.urlopen(toSearch)
# soup = BeautifulSoup(getPrice, "html.parser")
# parse
# store corresponding prices in table

################################ PARSE FUNCTION FOR PRICES ################################
# def parse(decade, name, platform, price):
#     if decade == "1970s":
#         movie1970 = Movie()
#         platform = platform.text
#         cost = price.text.replace("From", "")

#         movie1970.name = name
        
#         if platform == "YouTube":
#             movie1970.ytcost = cost
#         elif platform == "Amazon Prime Video":
#             movie1970.amznprimecost = cost
#         elif platform == "Vudu":
#             movie1970.vuducost = cost
#         elif platform == "iTunes":
#             movie1970.itunescost = cost
#         elif platform == "Google Play Movies & TV":
#             movie1970.googleplaycost = cost
#         elif platform == "Netflix":
#             movie1970.netflix = 1
#         else:
#             pass
#         movies1970s.append(movie1970)
        
#     if decade == "1980s":
#         movie1980 = Movie()
#         platform = platform.text
#         cost = price.text.replace("From", "")

#         movie1980.name = name
        
#         if platform == "YouTube":
#             movie1980.ytcost = cost
#         elif platform == "Amazon Prime Video":
#             movie1980.amznprimecost = cost
#         elif platform == "Vudu":
#             movie1980.vuducost = cost
#         elif platform == "iTunes":
#             movie1980.itunescost = cost
#         elif platform == "Google Play Movies & TV":
#             movie1980.googleplaycost = cost
#         elif platform == "Netflix":
#             movie1980.netflix = 1
#         else:
#             pass
#         movies1980s.append(movie1980)
        
#     if decade == "1990s":
#         movie1990 = Movie()
#         platform = platform.text
#         cost = price.text.replace("From", "")

#         movie1990.name = name
        
#         if platform == "YouTube":
#             movie1990.ytcost = cost
#         elif platform == "Amazon Prime Video":
#             movie1990.amznprimecost = cost
#         elif platform == "Vudu":
#             movie1990.vuducost = cost
#         elif platform == "iTunes":
#             movie1990.itunescost = cost
#         elif platform == "Google Play Movies & TV":
#             movie1990.googleplaycost = cost
#         elif platform == "Netflix":
#             movie1990.netflix = 1
#         else:
#             pass
#         movies1990s.append(movie1990)
        
#     if decade == "2000s":
#         movie2000 = Movie()
#         platform = platform.text
#         cost = price.text.replace("From", "")

#         movie2000.name = name
        
#         if platform == "YouTube":
#             movie2000.ytcost = cost
#         elif platform == "Amazon Prime Video":
#             movie2000.amznprimecost = cost
#         elif platform == "Vudu":
#             movie2000.vuducost = cost
#         elif platform == "iTunes":
#             movie2000.itunescost = cost
#         elif platform == "Google Play Movies & TV":
#             movie2000.googleplaycost = cost
#         elif platform == "Netflix":
#             movie2000.netflix = 1
#         else:
#             pass
#         movies2000s.append(movie2000)

# movie1970 = Movie()
# movie1980 = Movie()
# movie1990 = Movie()
# movie2000 = Movie()
# parse(decade, movieName, platform, price)

# for movie in movies2000s:
#     cursor.execute("INSERT INTO movies2000s (amznPrimeCost, youtubeCost, googlePlayCost, vuduCost, itunesCost, netflixAvailability) VALUES (?, ?, ?, ?, ?, ?)", (movie.amznprimecost, movie.ytcost, movie.googleplaycost, movie.vuducost, movie.itunescost, movie.netflix))