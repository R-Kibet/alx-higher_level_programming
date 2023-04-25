#!/usr/bin/node

const request = require('request');
const url = 'https://swapi.co/api/films/' + process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const getres = JSON.parse(body).characters;
    getres.forEach((results) => {

      request(results, (err, res, data) => {
        if (res) {
          console.log(JSON.parse(data).name);
        } else {
          console.log(err);
        }
      });
    });
  }
});
