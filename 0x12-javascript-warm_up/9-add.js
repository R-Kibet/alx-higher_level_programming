#!/usr/bin/node

function add (a, b) {
  a = process.argv[2];
  b = process.argv[3];

  const y = parseInt(a);
  const z = parseInt(b);

  if (isNaN(y) || isNaN(z)) {
    console.log(NaN);
  } else {
    const r = y + z;
    console.log(r);
  }
}
add();
