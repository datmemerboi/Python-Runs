/**
 * Count stars between bars of a given index.
 */

function countStars(string) {
  let count = 0;
  let startIndex = -1;

  let i = 0;
  while (i < string.length) {
    const char = string[i];

    if (char === "|") {
      if (startIndex === -1) {
        // First |
        startIndex = i;
      } else {
        // Followed |. End enclosed
        count += i - startIndex - 1;
        startIndex = i;
      }
    }
    i++
  }

  return count;
}

(function main(string, start, end) {
  let substring = string.substring(start - 1, end);
  console.log(
    countStars(substring)
  )
})("||**|", 1, 5);
