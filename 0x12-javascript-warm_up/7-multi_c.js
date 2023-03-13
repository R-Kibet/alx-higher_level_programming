#!/usr/bin/node

const x = parseInt(process.argv[2]);

if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  const j = process.argv[2];

  for (let i = 0; i < j; i++) {
    console.log('C is fun');
  }
}
