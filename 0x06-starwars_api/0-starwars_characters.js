#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

if (!movieId) {
	console.log('Please provide a Movie ID');
	process.exit(1);
}

request(apiUrl, function (error, response, body) {
	if (error) {
		console.error('Error:', error);
	} else if (response.statusCode === 200) {
		const filmData = JSON.parse(body);
		const characters = filmData.characters;

		characters.forEach((characterUrl) => {
			request(characterUrl, function (error, response, body) {
				if (!error && response.statusCode === 200) {
					const characterData = JSON.parse(body);
					console.log(characterData.name);
				}
			});
		});
	} else {
		console.log(`Failed to retrieve movie: ${response.statusCode}`);
	}
});
