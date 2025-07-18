#!/usr/bin/node

const x = process.argv.slice(2);
const Num1 = Number(x[0]);
const Num2 = Number(x[1]);

function add (a, b) {
  return (a + b);
}
const sum = add(Num1, Num2);
console.log(sum);
