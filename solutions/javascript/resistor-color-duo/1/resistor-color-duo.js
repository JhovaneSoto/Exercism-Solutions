//
// This is only a SKELETON file for the 'Resistor Color Duo' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const decodedValue = (resistor) => Number(`${COLORS.indexOf(resistor[0])}${COLORS.indexOf(resistor[1])}`);


const COLORS = ["black","brown","red","orange","yellow","green","blue","violet","grey","white"]