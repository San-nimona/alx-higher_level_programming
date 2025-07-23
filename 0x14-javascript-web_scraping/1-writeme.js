#!/usr/bin/node

const fs = require('fs');
const args = process.argv.slice(2);

try {
	const myFile = args[0];
	const text = args[1];
	fs.writeFileSync(myFile, text, 'utf-8');
} catch (error){
	console.error(error);
}
