/**
 * Find timestamp when absence of packets
 * casues buffering.
 */

function cleanup(buffer, t) {
  return buffer.filter((p) => p >= t);
}

function lookup(buffer, t) {
  return buffer[0] == t;
}

/**
 *
 * @param {int} rate - arrival rate
 * @param {int} n - number of packets
 * @param {array} packets - packets
 */
function bufferTime(rate, n, packets) {
  let buffer = []; // Assuming infinite length buffer
  let rebufferTimestamp = -1;

  let t = 0;
  let i = 0;
  while (i < n && rebufferTimestamp < 0) {
    t++; // tick each instance
    buffer = cleanup(buffer, t); // remove expired packets

    let tempPackets = packets.slice(i, i + rate); // if rate = 2, check 2 packets at once

    if (tempPackets[0] !== t && !lookup(buffer, t)) {
      // t not receieved now or in buffer
      rebufferTimestamp = t;
      break;
    }

    buffer.push(...tempPackets.filter((p) => p > t && buffer.indexOf(p) < 0)); // future packet not in buffer
    i += rate;
  }

  return rebufferTimestamp;
}

console.log(bufferTime(2, 8, [1, 2, 4, 1, 2, 5, 5, 4]));
