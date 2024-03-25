/**
 * Find shortest distance/quickest time for a given string in
 * a circular printer.
 */

const LETTER_ARR = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

/**
 *
 * @param {String} a - path from this letter
 * @param {String} b - to this letter
 */
function findShortestCircularPath(a, b) {
  let between = 0;
  let back = 0;
  let found = false;

  for (let i = 0; i < LETTER_ARR.length; i++) {
    let char = LETTER_ARR[i];

    if (char === a || char === b) {
      found = !found;
    }
    if (!found) {
      back++;
    } else {
      between++;
    }
  }

  return Math.min(back, between);
}

function adder(sum, a) {
  return sum + findShortestCircularPath(a[0], a[1]);
}

(function main(string) {
  let coupled = [];
  for (let i = 0; i < string.length - 1; i++) {
    coupled.push([string[i], string[i + 1]]);
  }

  console.log(coupled.reduce(adder, 0));
})("AZGB");
