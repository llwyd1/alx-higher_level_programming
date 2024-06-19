#!/usr/bin/node
const myArg = parseInt(process.argv[2]);
const myArr = [];
let i = 0;
if (myArg) {
  for (i; i < myArg; i++) {
    myArr[i] = 'X';
  }
  for (i = 0; i < myArg; i++) {
    console.log(myArr.join(''));
  }
} else {
  console.log('Missing size');
}
