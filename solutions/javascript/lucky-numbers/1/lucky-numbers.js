// @ts-check

/**
 * Calculates the sum of the two input arrays.
 *
 * @param {number[]} array1
 * @param {number[]} array2
 * @returns {number} sum of the two arrays
 */
export function twoSum(array1, array2) {
  let cont_1 = array1.join("");
  let cont_2 = array2.join("");
  return Number(cont_1) + Number(cont_2);
}

/**
 * Checks whether a number is a palindrome.
 *
 * @param {number} value
 * @returns {boolean} whether the number is a palindrome or not
 */
export function luckyNumber(value) {
  return String(value) === String(value).split("").reverse().join("");
}

/**
 * Determines the error message that should be shown to the user
 * for the given input value.
 *
 * @param {string|null|undefined} input
 * @returns {string} error message
 */
export function errorMessage(input) {

  
  if(input === "" || input === null || input === undefined){
    return "Required field";
  }
  
  let dat = Number(input);

  if (isNaN(dat) || dat === 0) {
    return "Must be a number besides 0";
  }

  return "";
}
