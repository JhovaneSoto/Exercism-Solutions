//
// This is only a SKELETON file for the 'Bob' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const hey = (message) => {
  message = message.trim();
  if (message === ""){
    return "Fine. Be that way!";
  }

  if (message.toUpperCase() == message && (/[A-Za-z]/.test(message))){
    if(message.endsWith("?")){
      return "Calm down, I know what I'm doing!";
    }
    return "Whoa, chill out!";
  }

  if(message.endsWith("?")){
    return "Sure.";
  }
  return "Whatever.";
};
