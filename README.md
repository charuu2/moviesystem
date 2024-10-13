# Movie Recommendation System

## Problem Statement :

In today’s digital entertainment landscape, users are bombarded with a wide variety of movies, making it challenging to discover films that match their preferences. A movie recommendation system can help users navigate this vast collection by predicting and suggesting movies they are likely to enjoy based on their historical behavior, preferences, and the behavior of other users with similar tastes.

## Objective:
To develop a movie recommendation system using machine learning algorithms that accurately predicts and recommends movies to users based on their preferences, viewing history, and ratings. The system should be capable of handling large datasets and providing personalized suggestions for each user.

## Features

- **Data Analysis**: Explore and preprocess movie data from TMDb.
- **Recommendation Algorithms**: Implement various algorithms to generate movie recommendations.
- **Content-Based Filtering**: Recommends movies similar to those a user has liked based on movie attributes.
- **Collaborative Filtering**: Suggests movies based on the preferences of similar users.
- **Hybrid Approach**: Combines multiple recommendation techniques for improved accuracy.

## Dataset

The dataset used in this project is sourced from TMDb and includes the following features:
- `movie_id`: Unique identifier for each movie.
- `title`: Title of the movie.
- `overview`: Brief description of the movie.
- `release_date`: Release date of the movie.
- `genres`: Genres associated with the movie.
- `vote_average`: Average rating of the movie.
- `vote_count`: Number of votes the movie has received.
- `popularity`: Popularity score of the movie.
- `cast`: Main cast members of the movie.
- `crew`: Key crew members of the movie.


<img width="1470" alt="Screenshot 2024-10-13 at 11 27 39 PM" src="https://github.com/user-attachments/assets/4a4f664d-4fa3-4379-96a9-f6d116345efb">

<img width="1470" alt="Screenshot 2024-10-13 at 11 28 09 PM" src="https://github.com/user-attachments/assets/34d52ea2-98e1-4ec9-afd4-71b1db049974">


## Key Requirements:
**User Preferences :** The system should take into account user-specific data, such as movie ratings, genres of interest, and watch history, to provide tailored recommendations.

**Collaborative Filtering :** Implement collaborative filtering techniques to leverage user interaction data, finding patterns in user behavior to suggest movies that similar users have enjoyed.

**Content-Based Filtering :** Use movie metadata (e.g., genre, director, cast) to recommend movies with similar characteristics to those a user has liked in the past.

**Hybrid Approach :** Combine collaborative and content-based filtering for a more robust and accurate recommendation model.

**Scalability :** The system should be able to handle large-scale datasets with thousands of users and movies while maintaining efficiency and accuracy.

**Cold Start Problem :** Develop strategies to handle new users or movies with little to no prior data.

Sure! Here’s the revised explanation of the steps you took in your project, without the objective section:

---

##  Steps for Data Preparation and Analysis

1. **Data Cleaning**
   - **Removed Missing Values**: Identified and removed missing values in key columns, such as movie titles, genres, and other critical attributes. This step was essential to ensure that the analysis and models would not be negatively impacted by incomplete data.
   - **Handled Incomplete Entries**: Addressed any incomplete entries by either filling in gaps with appropriate default values or removing those records, ensuring a consistent and reliable dataset.

    <img width="1470" alt="Screenshot 2024-10-13 at 11 34 49 PM" src="https://github.com/user-attachments/assets/a68123f7-73ae-454c-a593-c35aba80bbc7">

2. **Data Transformation**
   - **Feature Engineering**: 
     - Created new features by combining multiple columns. This included extracting relevant information such as genres, keywords, cast, and crew to form more informative features that could enhance the recommendation process.
   - **Lowercasing**: Converted all text data to lowercase to maintain consistency and avoid issues related to case sensitivity. This transformation helps ensure that text comparisons are accurate and reliable.

3. **Feature Extraction**
   - **Genres, Keywords, Cast, and Crew**: Relevant information was extracted from the original dataset to create structured data. This involved isolating key features that would later be used in the recommendation algorithm. 
   - **Tag Creation**: Combined the movie overview, cast, crew, genres, and keywords into a single text string called ‘tags’. This single string format simplifies the process of similarity calculations and model training by providing a comprehensive representation of each movie.

4. **Data Structuring**

    - **Merging Data**: Merged the movies and credits datasets into one cohesive dataset. This step involved combining information about the movies (e.g., titles, release dates, genres) with information about the cast and crew (e.g., actors, directors). The merged dataset provides a unified view that is easier to analyze and work with.

5. **Cosine Similarity Calculation**
   
   - **Measuring Similarity**: Calculated cosine similarity to measure the similarity between movies based on their tags. This mathematical metric helps determine how alike two movies are based on their combined features, which is crucial for making personalized recommendations.


6. **Data Visualization :**
 
**Histograms and Bar Charts:** Plotted various visualizations, including histograms and bar charts, to showcase the distribution of movie ratings and other relevant metrics. This included visualizing the distribution of ratings to understand user preferences better and identifying trends.

**For example -Top 10 Movie Keywords:** Created bar charts to display the top 10 movie keywords, allowing for a quick overview of the most common themes and subjects present in the dataset. 

<img width="1470" alt="Screenshot 2024-10-13 at 11 35 16 PM" src="https://github.com/user-attachments/assets/e46e61be-5865-4f64-94a2-6f63c6d08c96">


## Expected Outcome:
A machine learning-based movie recommendation system that continuously learns and improves based on user interactions, delivering personalized movie suggestions and enhancing the overall user experience.

**Example**-If you watch a movie like Spider-Man, it will suggest related movies such as Spider-Man 2, Spider-Man 3, and others with similar features.

<img width="1470" alt="Screenshot 2024-10-13 at 11 45 28 PM" src="https://github.com/user-attachments/assets/552eb361-adb7-41c8-9b15-2a2704030081">

