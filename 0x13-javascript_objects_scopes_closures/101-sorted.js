#!/usr/bin/node

const dict = require('./101-data').dict;

const dic = {};

for (const i in dict) {
  if (dic[dict[i]] === undefined) {
    dic[dict[i]] = [];
  }
  dic[dict[i]].push(i);
}
console.log(dic);
