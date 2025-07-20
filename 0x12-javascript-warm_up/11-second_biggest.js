#!/usr/bin/node

const x = process.argv.slice(2);
let num;
let i;
const array = [];
let temp;
let j;

for (i = 0; i < x.length; i++) {
  num = Number(x[i]);
  array.push(num);
}
function secBiggest () {
  if (!x[0] || !x[1]) {
    console.log(0);
  } else {
    function sort (myArray) {
      // let newArray = [];
      for (i = 0; i < (myArray.length - 1); i++) {
        for (j = 0; j < (myArray.length - 1 - i); j++) {
          if (myArray[j] > myArray[j + 1]) {
            temp = myArray[j];
            myArray[j] = myArray[j + 1];
            myArray[j + 1] = temp;
          }
        }
      }
      console.log(myArray[(myArray.length - 2)]);
    }
    sort(array);
  }
}
secBiggest();
