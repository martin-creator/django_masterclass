# MOVIEMATE REST API

Welcome to MOVIEMATE REST API! This API provides access to a wide range of movie-related information, including details about movies, actors, directors, and more. With MOVIEMATE, you can easily integrate movie data into your applications, websites, or services.

## Features:

- **Search Movies**: Retrieve information about movies by title, genre, release year, and more.
- **Get Movie Details**: Access detailed information about a specific movie, including cast, crew, ratings, and reviews.
- **Explore Actors and Directors**: Get information about actors and directors, including their filmography and biographical details.
- **Discover Trending Movies**: Stay up-to-date with trending movies and popular releases.
- **User Authentication**: Secure access to certain features with user authentication.

## Usage:

To use the MOVIEMATE REST API, you'll need to sign up for an API key. Once you have your API key, you can start making requests to the endpoints listed in the documentation.

### Authentication:

To authenticate your requests, include your API key in the request headers:

```
Authorization: Bearer YOUR_API_KEY
```

### Endpoints:

- **GET /movies**: Retrieve a list of movies based on search criteria.
- **GET /movies/{id}**: Get detailed information about a specific movie.
- **GET /actors**: Retrieve a list of actors based on search criteria.
- **GET /actors/{id}**: Get detailed information about a specific actor.
- **GET /directors**: Retrieve a list of directors based on search criteria.
- **GET /directors/{id}**: Get detailed information about a specific director.
- **GET /trending**: Get a list of trending movies.
- **POST /auth/login**: Log in and obtain an authentication token.

For detailed information about request parameters and response formats, please refer to the full API documentation.

## Getting Started:

1. Sign up for a MOVIEMATE API key.
2. Review the API documentation to understand how to make requests.
3. Start integrating movie data into your application!

## Support:

If you have any questions, issues, or feedback regarding the MOVIEMATE REST API, please don't hesitate to contact our support team at martinlubowa@outlook.com

Happy coding! 🎬