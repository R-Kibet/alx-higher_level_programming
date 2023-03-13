#!/usr/bin/node

function a (number, theFunction) {
  number++;
  theFunction(number);
}

module.exports = { addMeMaybe: a };
