// @ts-check
//
// The line above enables type checking for this file. Various IDEs interpret
// the @ts-check directive. It will give you helpful autocompletion when
// implementing this exercise.

/**
 * Calculates the total bird count.
 *
 * @param {number[]} birdsPerDay
 * @returns {number} total bird count
 */
export function totalBirdCount(birdsPerDay) {
  let total = 0;
  for(let idx = 0;idx < birdsPerDay.length; idx++){
    total += birdsPerDay[idx];
  }
  return total;
}

/**
 * Calculates the total number of birds seen in a specific week.
 *
 * @param {number[]} birdsPerDay
 * @param {number} week
 * @returns {number} birds counted in the given week
 */
export function birdsInWeek(birdsPerDay, week) {
  let start = (week-1)*7
  let end = start + 7
  let total = 0;
  
  for(let idx = start;idx < end && idx < birdsPerDay.length; idx++){
    total += birdsPerDay[idx];
  }
  return total;
}

/**
 * Fixes the counting mistake by increasing the bird count
 * by one for every second day.
 *
 * @param {number[]} birdsPerDay
 * @returns {void} should not return anything
 */
export function fixBirdCountLog(birdsPerDay) {
  console.log(birdsPerDay)
  for(let idx = 0;idx < birdsPerDay.length; idx+=2){
    birdsPerDay[idx] +=1;
  }
  console.log(birdsPerDay)
  return birdsPerDay
}
