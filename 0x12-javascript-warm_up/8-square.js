#!/usr/bin/node

const myArgs = process.argv.slice(2);

const x = Number(myArgs[0]);
let i;
let j;
let str = '';

if ((myArgs[0]) && x > 0) {
  for (j = 0; j < x; j++) {
    for (i = 0; i < x; i++) {
      str += 'X';
    }
    console.log(str);
    str = '';
  }
} else {
  console.log('Missing size');
}
