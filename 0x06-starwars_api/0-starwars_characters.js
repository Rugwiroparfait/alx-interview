#!/usr/bin/node

const axios = require('axios');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

if (!movieId) {
  console.log('Please provide a Movie ID');
  process.exit(1);
}

// Fetch the movie details from the API
axios.get(apiUrl)
  .then(response => {
    const characters = response.data.characters;

    // Fetch and print each character's name
    characters.forEach((characterUrl) => {
      axios.get(characterUrl)
        .then(response => {
          console.log(response.data.name);
        })
        .catch(error => {
          console.error('Error fetching character:', error);
        });
    });
  })
  .catch(error => {
    console.error('Error fetching movie:', error);
  });

