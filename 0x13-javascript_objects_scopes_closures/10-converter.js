#!/usr/bin/node

exports.converter = function (base) {
  function myConvert (number) {
    return number.toString(base);
  }
  return myConvert;
};
