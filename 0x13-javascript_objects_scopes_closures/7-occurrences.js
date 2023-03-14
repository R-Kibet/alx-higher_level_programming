#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  return list.reduce((acc, value) => {
    return (searchElement === value ? acc + 1 : acc);
  }, 0);
};
