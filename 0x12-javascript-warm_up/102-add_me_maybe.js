#!/usr/bin/node

function addMeMaybe (number, theFunction) {
  num = Number(number);
  num += 1;
  theFunction(num);
}
module.exports = {
  addMeMaybe
};
