#!/usr/bin/node

const square = require('./5-square');

class Square extends square {
  charPrint (c) {
    if (c) {
      console.log((c.repeat(this.width) + '\n').repeat(this.height - 1) + c.repeat(this.width));
    } else {
      this.print();
    }
  }
}

module.exports = Square;
