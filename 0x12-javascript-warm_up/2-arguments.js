#!/usr/bin/node
let count =  process.argv.lenghth;
console.log(count === 2 ? 'No argument':count === 3 ? 'Argument found':'Arguments found');