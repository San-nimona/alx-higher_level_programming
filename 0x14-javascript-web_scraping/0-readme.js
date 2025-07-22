#!/usr/bin/node
const fs = require('fs');
const args = process.argv.slice(2);

const myFile = args[0];
if (myFile){
	try {
		const content = fs.readFileSync(myFile, 'utf-8');
		console.log(content);
	} catch (error){
		console.error(error);
	}
} else {
	console.log('Please enter a file to be read');
}
