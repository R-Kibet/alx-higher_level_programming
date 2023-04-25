#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = `https://swapi.co/api/films/${id}`;

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const getres = JSON.parse(body).characters;
    getres.forEach((results) => {
      request(results, (err, res, body1) => {
        if (res) {
          console.log(JSON.parse(body1).name);
        } else {
          console.log(err);
        }
      });
    });
  }
});
