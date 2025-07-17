#!/usr/bin/node

const myArgs = process.argv.slice(2);

let x = Number(myArgs[0]);
let i;
let j;

if ((myArgs[0]) & x != 'NaN'){
	for( i = 0; i < x; i++){
		console.log('X');
		for( j = 0; j < x; j++){
			console.log('X');
		}
	}
} else {
	console.log('Missing size');
}
