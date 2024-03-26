/**
 * Sort ancestry names by first name and roman num.
 */

const ROMAN_NUMERAL = {
  I: 1,
  V: 5,
  X: 10,
  L: 50,
  C: 100,
};

const ROMAN_REGEX = /(I|V|X|L|C)+/g;

function toRomanValue(string) {
  let value = 0;

  let i = 0;
  while (i < string.length) {
    let char = string[i];
    let nextChar = string[1 + i];

    if (ROMAN_NUMERAL[nextChar] > ROMAN_NUMERAL[char]) {
      value += ROMAN_NUMERAL[nextChar] - ROMAN_NUMERAL[char];
      i++;
    } else {
      value += ROMAN_NUMERAL[char];
    }
    i++;
  }

  return value;
}

function regexToValue(string) {
  const found = string.match(ROMAN_REGEX);

  if (found) {
    const longest = found.sort((a, b) => b.length - a.length)[0]; // Longest string of Roman numerals will be replaced.
    return string.replace(longest, toRomanValue(longest));
  }
  return string;
}

(function main(names) {
  let collator = new Intl.Collator("en", {
    numeric: true,
    sensitivity: "base",
  });
  console.log(names.map((n) => regexToValue(n)).sort(collator.compare));
})(["Henry VIII", "Henry IV", "Will I AM XII", "Will V"]);
