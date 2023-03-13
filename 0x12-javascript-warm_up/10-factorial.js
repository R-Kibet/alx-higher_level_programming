#!/usr/bin/node

function fact (a) {
  if (isNaN(a) || a === 1) {
    return (1);
  } else {
    const r = a * fact(a - 1);
    return (r);
  }
}
console.log(fact(parseInt(process.argv[2])));
