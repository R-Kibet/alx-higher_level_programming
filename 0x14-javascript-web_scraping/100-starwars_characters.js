#!/usr/bin/node

const request = require('request');
const url = 'https://swapi.co/api/films/' + process.argv[2];

request(url, (err, response, body) => {
  if (!err) {
    const result = JSON.parse(body).characters;
    result.forEach((character) => {
      request(character, (err, response, body) => {
        if (response) {
          console.log(JSON.parse(body).name);
        } else {
          console.log(err);
        }
      });
    });
  }
});
