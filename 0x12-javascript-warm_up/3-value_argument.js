#!/usr/bin/node

const x = process.argv[2];
if (x) {
  console.log(`${x}`);
} else {
  console.log('No argument');
}
