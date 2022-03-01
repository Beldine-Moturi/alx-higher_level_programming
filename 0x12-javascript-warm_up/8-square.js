#!/usr/bin/node
const myVar = Number(process.argv[2]);
if (!(Number.isInteger(myVar))) {
  console.log('Missing size');
} else {
    for (let i = 0; i < myVar; i++) {
	let row = '';
	for (let n = 0; n < myVar; n++) row += 'X';
	console.log(row);
    }
}
