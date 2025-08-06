#!/usr/bin/node
const request = require('request');
const fs = require('fs');
request('https://jquery-tutorial.net/dom-manipulation/getting-and-setting-content/').pipe(fs.createWriteStream('README.md'));
