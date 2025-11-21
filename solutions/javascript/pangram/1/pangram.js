//
// This is only a SKELETON file for the 'Pangram' exercise. It's been provided as a
// convenience to get you started writing code faster.
//
const abc = "abcdefghijklmnopqrstuvwxyz".split("")
export const isPangram = (sentence) => {
  const arreglo = sentence.toLowerCase().split("");
  return abc.every((letter) => arreglo.includes(letter));
};
