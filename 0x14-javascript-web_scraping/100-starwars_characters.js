#!/usr/bin/node

const request = require('request');
const url = 'https://swapi.co/api/films/' + process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
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
