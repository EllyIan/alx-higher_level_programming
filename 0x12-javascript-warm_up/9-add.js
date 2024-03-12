#!/usr/bin/node

const process = require('module');

function add (a , b ) {

    return a + b;
}
if (typeof process !== 'undefined') {
	if (process.argv.length !== 3) {
	  console.log('Usage: add.js <number1> <number2>');
	  process.exit(1);
	}
}

console.log(add(Number(process.argv[2]) , Number(process.argv[3])));
