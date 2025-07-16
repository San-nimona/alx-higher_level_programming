#!/usr/bin/node
// A script that prints arguments passed
//

const myArgs = process.argv;
const i = myArgs.length;
if (i <= 2) {
  console.log('No argument found');
} else if (i === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
