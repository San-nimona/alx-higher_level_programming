#!/usr/bin/node

const Rectangle = require('./4-rectangle.js');

class Square extends Rectangle {
  size;

  constructor (size) {
    super(size);
    this.width = size;
    this.height = size;
  }
}
module.exports = Square;
