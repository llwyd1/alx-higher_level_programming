#!/usr/bin/node
const myArg = parseInt(process.argv[2]);
console.log(fact(myArg));

function fact (n) {
  if (!n) {
    return 1;
  }
  if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * fact(n - 1);
  }
}
