#!/usr/bin/node

const req = require('request');

const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

req(url, (err, response, body) => {
  console.log(err || JSON.parse(body).title);
});
