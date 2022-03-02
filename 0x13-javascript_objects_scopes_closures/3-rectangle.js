#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.width; i++) {
      let char = '';
      for (let n = 0; n < this.height; n++) char += 'X';
      console.log(char);
    }
  }
};
