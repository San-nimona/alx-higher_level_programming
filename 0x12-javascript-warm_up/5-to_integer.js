#!/usr/bin/node

const myArgs = process.argv.slice(2);

if ((myArgs[0]) & Number(myArgs[0]) != 'NaN'){
	console.log('My number: ' + Number(myArgs[0]));
} else {
	console.log('Not a number');
}
