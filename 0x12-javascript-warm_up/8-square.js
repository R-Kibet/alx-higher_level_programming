#!/usr/bin/node

const y = process.argv[2];
const x = parseInt(y);

if (isNaN(x)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < y; i++) {
    let r = '';
    for (let j = 0; j < y; j++) {
      r += 'X';
    }
    console.log(r);
  }
}
