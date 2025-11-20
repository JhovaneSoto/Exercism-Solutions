//
// This is only a SKELETON file for the 'RNA Transcription' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const toRna = (dna) => {
  let output = "";
  for (let item of dna){
    switch (item){
      case "G":
        output += "C";
        break;
      case "C":
        output += "G";
        break;
      case "T":
        output += "A";
        break;
      case "A":
        output += "U";
        break;
      default:
        output += item;
        break;
    }
  }
  return output;
};
