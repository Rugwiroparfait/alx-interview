#!/usr/bin/node

const request = require('request');

// Get the movie ID from the command line argument
const movieId = process.argv[2];

// Construct the API URL for the movie
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

if (!movieId) {
  console.log('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

// Make the HTTP request to the API
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  // Parse the JSON response
  const film = JSON.parse(body);
  const characters = film.characters;

  // For each character URL, make another HTTP request
  characters.forEach(characterUrl => {
    request(characterUrl, (charError, charResponse, charBody) => {
      if (!charError) {
        const character = JSON.parse(charBody);
        console.log(character.name); // Print character name
      }
    });
  });
});

