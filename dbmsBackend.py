import sqlite3

class MovieDbBackend:

    # Connection Establishment
    def __init__(self):
        try:
            self.conn = sqlite3.connect("MulesoftMovieDb.db")
        except Exception as ex:
            print("Error initializing the db:  %s" % (ex))


    # Table creation method
    def tableCreation(self):
        cur = self.conn.cursor()

        cur.execute('''CREATE TABLE IF NOT EXISTS Movies
        (Movie_Name TEXT NOT NULL,
        Actor TEXT,
        Actress TEXT,
        Director TEXT NOT NULL,
        Year_Of_Release TEXT,
        PRIMARY KEY(Movie_Name))''')
    

    # Insert movie data into database method
    def insertToMovieDb(self, moviename, actor, actress,director, yor):
        if(len(yor)==4 and yor.isnumeric()): # checks whether the year of release is valid or not
            # converted actor name to lowercase, because we are gonna fetch info based on actor
            self.conn.execute("INSERT INTO Movies (Movie_Name, Actor, Actress, Director, Year_Of_Release) VALUES(?, ?, ?, ?, ?)", (moviename, actor.lower(),actress,director,yor))
            self.conn.commit()
            # self.close() # if you want close db after one insert
        else:
            print("please provide correct year of release")
    

    # Query from movies database using the actor name
    def queryFromMovies(self,actor):
        cur = self.conn.cursor()
        # converted actor name to lower, now if the user provides in any case the result will be displayed
        cur.execute("SELECT * FROM Movies where Actor=?",(actor.lower(),))
        movieInfo = cur.fetchall()
        return movieInfo


    # Query all the movies from movies table
    def queryAllMovies(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM Movies")
        allMovieInfo = cur.fetchall()
        return allMovieInfo



# The execution part is written here itself - for testing purpose

# creating the object of db
# movdb = MovieDbBackend()  

#Creating the table Movies
# movdb.tableCreation()   

# Inserting the values to Movies table
# movdb.insertToMovieDb("KGF 1", "Yash", "Srinidhi Shetty", "Prashanth Neel", "20188") #checking the exceptions
# movdb.insertToMovieDb("KGF 1", "Yash", "Srinidhi Shetty", "Prashanth Neel", "201x")
# movdb.insertToMovieDb("KGF 1", "Yash", "Srinidhi Shetty", "Prashanth Neel", "2018")

# Querying the Movies database using the actor name
# info = movdb.queryFromMovies('Yash')
# print(info)

# query all movies
# allInfo = movdb.queryAllMovies()
# print(allInfo)