# If you are using it at the frontend please import the dbmsBackend module
import dbmsBackend

# creating the object of db
movdb = dbmsBackend.MovieDbBackend()  

# Creating the table Movies
movdb.tableCreation()   

# Inserting the values to Movies table
# movdb.insertToMovieDb("KGF 1", "Yash", "Srinidhi Shetty", "Prashanth Neel", "20188") #checking the exceptions
# movdb.insertToMovieDb("KGF 1", "Yash", "Srinidhi Shetty", "Prashanth Neel", "201x")

movdb.insertToMovieDb("KGF 1", "Yash", "Srinidhi Shetty", "Prashanth Neel", "2018") # correct insert values
movdb.insertToMovieDb("KGF 2", "Yash", "Srinidhi Shetty", "Prashanth Neel", "2022")
movdb.insertToMovieDb("Doctor", "ShivaKarthikeyan", "Priyanka Mohan", "Nataraj", "2021")
movdb.insertToMovieDb("Don", "ShivaKarthikeyan", "Priyanka Mohan", "Chakravarthy", "2022")

# Querying the Movies database using actor name (see the search is not case sensitive)
info = movdb.queryFromMovies('ShivaKarthikeyan')
print(info, end="\n\n")

# query all movies
allInfo = movdb.queryAllMovies()
print(allInfo,  end="\n\n")
