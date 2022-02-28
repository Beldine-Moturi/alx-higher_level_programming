#!/usr/bin/node
const myVar = Number(process.argv[2]);
if (Number.isInteger(myVar) === false) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < myVar; i++) {
    console.log('C is fun');
  }
}
