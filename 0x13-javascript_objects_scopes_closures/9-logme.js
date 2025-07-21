#!/usr/bin/node
let index = 0;
exports.logMe = function (item) {
  const list = [];
  list.push(item);
  list.forEach(item => {
    console.log(index + ': ' + item);
    index++;
  });
};
