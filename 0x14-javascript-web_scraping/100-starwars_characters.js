#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const starWarsApi = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(starWarsApi, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const getResults = JSON.parse(body);
    getResults.characters.forEach((results) => {
      //  console.log(results)
      request(results, function (err, res, body2) {
        if (res) {
          const charactersName = JSON.parse(body2);
          console.log(charactersName.name);
        } else {
          console.log(err);
        }
      });
    });
  }
});
