#!/usr/bin/node
const rect = require('./4-rectangle');
module.exports = class Square extends rect {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    const sym = c == null ? 'X' : c;
    for (let i = 0; i < this.height; i++) {
      let line = '';
      for (let j = 0; j < this.width; j++) {
        line += sym;
      }
      console.log(line);
    }
  }
};
