#!/usr/bin/node

const myArgs = process.argv.slice(2);
const Str = 'C is fun';
let x = Number(myArgs[0]);

if ((myArgs[0]) & x != 'NaN') {
	while (x > 0){
		console.log(Str);
		x--;
	}
} else {
	console.log('Missing number of occurrences');
}
