#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let i = 0;
  list.forEach(elem => {
    if (elem === searchElement) {
      i++;
    }
  });
  return i;
};
