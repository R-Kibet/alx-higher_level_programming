#!/usr/bin/node

function a (x, fun) {
  for (let i = 0; i < x; i++) {
    fun();
  }
}

module.exports = { callMeMoby: a };
