//
// This is only a SKELETON file for the 'Gigasecond' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const gigasecond = (dateInicio) => {
  return new Date(dateInicio.getTime() + 1_000_000_000 * 1000);
};
