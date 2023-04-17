# Movie-Recommendation-System


## Objectives:
Recommend movies based on properties of the movie selected.

## Description
This is a content-based movie recommendation system which recommends similar movies based on the properties of the selected movie.
Content-based methods are based on the similarity of movie attributes. Using this type of recommender system, if a user watches one movie, similar movies are recommended. For example, if a user watches a comedy movie starring Adam Sandler, the system will recommend them movies in the same genre or starring the same actor, or both. With this in mind, the input for building a content-based recommender system is movie attributes.

The data was extracted by scraping www.imdb.com using BeautifulSoup and Selenium. This movie data includes the title of the movie, movie id, overview, average ratings, 
number of votes, movie certificate, year of release, runtime, genre and image url. The data was loaded cleaned to remove data inconsistencies, empty rows and general data wrangling to prepare the data for recommendation.

Finally, cosine similarity was used to compute the similarity textual data. Consider an example where we have to find similar movies. The textual data is converted in the form of vectors and checked the cosine angle between those two vectors if the angle between them is 0. After this, I reset the index with the movie name that is the original title and defined a function for the recommendation that will search for similar movies by checking cosine similarities and will return the top 4 values to check the most similar movies. The poster images were fetched using OMDB API by referencing the movie ids from the data passed for recommendation.
The demonstration can be found here: (https://rho-movie-recommender.herokuapp.com/)
