#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

if (!movieId) {
  console.log('Please provide a Movie ID');
  process.exit(1);
}

// Fetch the movie details from the API
request(apiUrl, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode === 200) {
    const filmData = JSON.parse(body);
    const characters = filmData.characters;

    // Fetch and print each character's name
    characters.forEach((characterUrl) => {
      request(characterUrl, function (error, response, body) {
        if (!error && response.statusCode === 200) {
          const characterData = JSON.parse(body);
          console.log(characterData.name);
        } else {
          console.error('Error fetching character:', error);
        }
      });
    });
  } else {
    console.log(`Failed to retrieve movie: ${response.statusCode}`);
  }
});

