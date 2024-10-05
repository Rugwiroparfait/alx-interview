#!/usr/bin/node

const request = require('request');
const util = require('util');
const requestPromise = util.promisify(request);

const movieId = process.argv[2];

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

if (!movieId) {
  console.log('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

async function starWarsCharacters () {
  try {
    const resp = await requestPromise(apiUrl);
    const movies = JSON.parse(resp.body);
    const characters = movies.characters;
    for (const charUrl of characters) {
      const chars = await requestPromise(charUrl);
      const movieCharacters = JSON.parse(chars.body);
      console.log(movieCharacters.name);
    }
  } catch (error) {
    throw error;
  }
}

starWarsCharacters();
