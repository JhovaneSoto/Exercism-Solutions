// @ts-check

/**
 * Generates a random starship registry number.
 *
 * @returns {string} the generated registry number.
 */
export function randomShipRegistryNumber() {
  let number = Math.floor(Math.random()*9000 + 1000);
  return `NCC-${number}`;
}

/**
 * Generates a random stardate.
 *
 * @returns {number} a stardate between 41000 (inclusive) and 42000 (exclusive).
 */
export function randomStardate() {
  let number = Math.random()*1000 + 41000;
  return number;
}

/**
 * Generates a random planet class.
 *
 * @returns {string} a one-letter planet class.
 */
export function randomPlanetClass() {
  let planets = ["D", "H", "J", "K", "L", "M", "N", "R", "T", "Y"];
  let idx = Math.floor(Math.random()*planets.length);
  console.log(idx)
  return planets[idx];
}
