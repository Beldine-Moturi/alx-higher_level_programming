#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${id}`;

request.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const characters = JSON.parse(body).characters;
    for (const actor of characters) {
      request.get(actor, (err, response, body) => {
        if (err) {
          console.log(err);
        } else if (response.statusCode === 200) {
          const name = JSON.parse(body).name;
          console.log(name);
        } else {
          console.log(`Error code: ${response.statusCode}`);
        }
      });
    }
  } else {
    console.log(`Error code 1: ${response.statusCode}`);
  }
});
