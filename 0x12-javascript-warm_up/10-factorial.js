#!/usr/bin/node

const x = process.argv.slice(2);
const num = Number(x[0]);

function factorial (n) {
  if (n === 0 || n === 1 || isNaN(n)) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
const fac = factorial(num);
console.log(fac);
