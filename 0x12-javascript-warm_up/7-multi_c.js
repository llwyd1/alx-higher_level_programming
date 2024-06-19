#!/usr/bin/node
let i = parseInt(process.argv[2]);
if (i) {
  for (; i > 0; i--) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurences');
}
