// @ts-check

/**
 * Create an appointment
 *
 * @param {number} days
 * @param {number} [now] (ms since the epoch, or undefined)
 *
 * @returns {Date} the appointment
 */
export function createAppointment(days, now = undefined) {
  if (now === undefined){
    now = new Date();
  }else{
    now = new Date(now);
  }
  now.setDate(now.getDate()+days);
  return now;
}

/**
 * Generate the appointment timestamp
 *
 * @param {Date} appointmentDate
 *
 * @returns {string} timestamp
 */
export function getAppointmentTimestamp(appointmentDate) {
  return appointmentDate.toISOString();
}

/**
 * Get details of an appointment
 *
 * @param {string} timestamp (ISO 8601)
 *
 * @returns {Record<'year' | 'month' | 'date' | 'hour' | 'minute', number>} the appointment details
 */
export function getAppointmentDetails(timestamp) {
  const tiempo = new Date(timestamp);
  const out ={
    year: tiempo.getFullYear(),
    month: tiempo.getMonth(),
    date: tiempo.getDate(),
    hour: tiempo.getHours(),
    minute: tiempo.getMinutes()
  }
  return out;
}

/**
 * Update an appointment with given options
 *
 * @param {string} timestamp (ISO 8601)
 * @param {Partial<Record<'year' | 'month' | 'date' | 'hour' | 'minute', number>>} options
 *
 * @returns {Record<'year' | 'month' | 'date' | 'hour' | 'minute', number>} the appointment details
 */
export function updateAppointment(timestamp, options) {
  let date = new Date(timestamp);
  console.log(timestamp, options);
  for (let item in options) {
    switch(item){
      case "year":
        date.setFullYear(options[item]);
        break;
      case "month":
        date.setMonth(options[item]);
        break;
      case "date":
        date.setDate(options[item]);
        break;
      case "hour":
        date.setHours(options[item]);
        break;
      case "minute":
        date.setMinutes(options[item]);
        break;
    }
  }
  return getAppointmentDetails(date);
}

/**
 * Get available time in seconds (rounded) between two appointments
 *
 * @param {string} timestampA (ISO 8601)
 * @param {string} timestampB (ISO 8601)
 *
 * @returns {number} amount of seconds (rounded)
 */
export function timeBetween(timestampA, timestampB) {
  let difference = new Date(timestampB) - new Date(timestampA);
  return Math.ceil(difference/1000);
}

/**
 * Get available times between two appointment
 *
 * @param {string} appointmentTimestamp (ISO 8601)
 * @param {string} currentTimestamp (ISO 8601)
 */
export function isValid(appointmentTimestamp, currentTimestamp) {
  return new Date(appointmentTimestamp) > new Date(currentTimestamp);
}
