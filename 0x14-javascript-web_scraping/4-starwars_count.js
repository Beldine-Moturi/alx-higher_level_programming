#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    let count = 0;
    const movies = JSON.parse(body).results;
    for (const movie of movies) {
      const movieChars = movie.characters;
      for (const movieChar of movieChars) {
        if (movieChar.includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  } else {
    console.log(`Error code: ${response.statusCode}`);
  }
});
