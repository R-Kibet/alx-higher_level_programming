#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const getres = JSON.parse(body).characters;
    getres.forEach((results) => {
      request(results, (err, res, body) => {
        if (res) {
          console.log(JSON.parse(body).name);
        } else {
          console.log(err);
        }
      });
    });
  }
});
