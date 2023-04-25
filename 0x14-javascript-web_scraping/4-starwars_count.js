#!/usr/bin/node

const request = require('request');
const argv = process.argv[2];
let counter = 0;

request(argv, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const obj = JSON.parse(body).results;
    for (const k of obj) {
      for (const i of k.characters) {
        if (i.search('/18/') > 0) {
          counter++;
        }
      }
    }
    console.log(counter);
  }
});
