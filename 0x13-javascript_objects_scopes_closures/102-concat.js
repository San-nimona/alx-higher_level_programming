#!/usr/bin/node
const fs = require('fs');
const myArgs = process.argv.slice(2);

const fileA = fs.readFileSync(myArgs[0]);
const fileB = fs.readFileSync(myArgs[1]);
const fileC = myArgs[2];
const newFile = fileA + fileB;
fs.writeFileSync(fileC, newFile);
