// @ts-check
//
// The line above enables type checking for this file. Various IDEs interpret
// the @ts-check directive. It will give you helpful autocompletion when
// implementing this exercise.

/**
 * Removes duplicate tracks from a playlist.
 *
 * @param {string[]} playlist
 * @returns {string[]} new playlist with unique entries
 */
export function removeDuplicates(playlist) {
  const out = new Set(playlist);
  return Array.from(out);
}

/**
 * Checks whether a playlist includes a track.
 *
 * @param {string[]} playlist
 * @param {string} track
 * @returns {boolean} whether the track is in the playlist
 */
export function hasTrack(playlist, track) {
  const out = new Set(playlist);
  return out.has(track);
}

/**
 * Adds a track to a playlist.
 *
 * @param {string[]} playlist
 * @param {string} track
 * @returns {string[]} new playlist
 */
export function addTrack(playlist, track) {
  let out = new Set(playlist);
  if (!out.has(track)){
    out.add(track);
  }
  return Array.from(out);
}

/**
 * Deletes a track from a playlist.
 *
 * @param {string[]} playlist
 * @param {string} track
 * @returns {string[]} new playlist
 */
export function deleteTrack(playlist, track) {
  let out = new Set(playlist);
  if (out.has(track)){
    out.delete(track);
  }
  return Array.from(out);
}

/**
 * Lists the unique artists in a playlist.
 *
 * @param {string[]} playlist
 * @returns {string[]} list of artists
 */
export function listArtists(playlist) {
  let names = new Set()
  for (let name of playlist) {
    names.add(string_name(name));
  }
  
  return Array.from(names);
}

function string_name(cadena) {
  let idx = 0;
  let artista = "";
  if (cadena.includes("-")){
    artista = cadena.split("-")[1].trim();
  }
  return artista;
}

