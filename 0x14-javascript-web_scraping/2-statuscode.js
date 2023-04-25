#!/usr/bin/node

const req = require('request');

req(process.argv[2], function (err, response) {
  if (err) { console.error(err); }
  console.log('code:', response && response.statusCode);
});
