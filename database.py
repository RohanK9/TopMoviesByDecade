import sqlite3

connection = sqlite3.connect('movies.db')
cursor = connection.cursor()

# creates tables for the top movies from the 1970s, 1980s, 1990s, and 2000s
cursor.execute("CREATE TABLE IF NOT EXISTS movies1970s (name text, year integer, poster blob, amznPrimeCost real, youtubeCost real, googlePlayCost real, vuduCost real, itunesCost real, netflixAvailability integer)")
cursor.execute("CREATE TABLE IF NOT EXISTS movies1980s (name text, year integer, poster blob, amznPrimeCost real, youtubeCost real, googlePlayCost real, vuduCost real, itunesCost real, netflixAvailability integer)")
cursor.execute("CREATE TABLE IF NOT EXISTS movies1990s (name text, year integer, poster blob, amznPrimeCost real, youtubeCost real, googlePlayCost real, vuduCost real, itunesCost real, netflixAvailability integer)")
cursor.execute("CREATE TABLE IF NOT EXISTS movies2000s (name text, year integer, poster blob, amznPrimeCost real, youtubeCost real, googlePlayCost real, vuduCost real, itunesCost real, netflixAvailability integer)")

connection.commit()
connection.close()