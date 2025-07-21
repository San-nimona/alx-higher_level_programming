#!/usr/bin/node

const Rect = require('./5-square.js');

class Square extends Rect {
  constructor (size) {
    super(size);
    if (!size || size <= 0) {
      return;
    }
    this.width = size;
    this.height = size;
  }

  charPrint (c) {
    for (let i = 0; i < this.height; i++) {
      if (c !== undefined) {
        console.log(c.repeat(this.width));
      } else {
        console.log(this.str.repeat(this.width));
      }
    }
  }
}
module.exports = Square;
