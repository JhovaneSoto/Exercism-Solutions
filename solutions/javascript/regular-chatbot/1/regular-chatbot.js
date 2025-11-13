// @ts-check

/**
 * Given a certain command, help the chatbot recognize whether the command is valid or not.
 *
 * @param {string} command
 * @returns {boolean} whether or not is the command valid
 */

export function isValidCommand(command) {
  const regex = /^Chatbot/i;
  return regex.test(command);
}

/**
 * Given a certain message, help the chatbot get rid of all the emoji's encryption through the message.
 *
 * @param {string} message
 * @returns {string} The message without the emojis encryption
 */
export function removeEmoji(message) {
  console.log(message);
  const regex = /[a-z]+[0-9]+/;
  while (regex.test(message)) {
    message = message.replace(regex,"");
  }
  return message;
}

/**
 * Given a certain phone number, help the chatbot recognize whether it is in the correct format.
 *
 * @param {string} number
 * @returns {string} the Chatbot response to the phone Validation
 */
export function checkPhoneNumber(number) {
  console.log(number);
  const regex = /^\(\+\d{2}\)\s\d{3}-\d{3}\-\d{3}$/;
  if (regex.test(number)){
    return "Thanks! You can now download me to your phone.";
  }
  return `Oops, it seems like I can't reach out to ${number}`;
}

/**
 * Given a certain response from the user, help the chatbot get only the URL.
 *
 * @param {string} userInput
 * @returns {string[] | null} all the possible URL's that the user may have answered
 */
export function getURL(userInput) {
  console.log(userInput);
  const regex = /[a-z]+\.[a-z]+/g;
  return userInput.match(regex);
}

/**
 * Greet the user using the full name data from the profile.
 *
 * @param {string} fullName
 * @returns {string} Greeting from the chatbot
 */
export function niceToMeetYou(fullName) {
  console.log(fullName);
  fullName = fullName.replace(/[a-zA-Z]+\,\s[a-zA-Z]+/,function (word) {
    const name = word.split(", ");
    console.log(name);
    return `${name[1]} ${name[0]}`
  });
  console.log(fullName);
  return `Nice to meet you, ${fullName}`;
}
