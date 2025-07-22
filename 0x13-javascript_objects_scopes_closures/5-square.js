#!/usr/bin/node

const Rectangle = require('./4-rectangle.js');

class Square extends Rectangle {
  size;

  constructor (size) {
    if (arguments.length !== 1){
      return;
    }
    super(size);
    this.width = size;
    this.height = size;
  }
}
module.exports = Square;
