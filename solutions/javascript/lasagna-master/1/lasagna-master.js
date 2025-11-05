/// <reference path="./global.d.ts" />
// @ts-check

/**
 * Implement the functions needed to solve the exercise here.
 * Do not forget to export them so they are available for the
 * tests. Here an example of the syntax as reminder:
 *
 * export function yourFunction(...) {
 *   ...
 * }
 */

export function cookingStatus(timeCook) {
  if (timeCook === undefined){
    return 'You forgot to set the timer.';
  }else if (timeCook === 0){
    return 'Lasagna is done.';
  }
  return 'Not done, please wait.';
}

export function preparationTime(layers, time = 2) {
  return layers.length * time;
}

export function quantities(layers) {
  let sauce = 0;
  let noodles = 0;

  for (let layer of layers){
    console.log(layer)
    if (layer === "noodles"){
      noodles += 50;
    }
    if (layer === "sauce"){
      sauce += 0.2;
    }
  }
  return {
    noodles: noodles,
    sauce: sauce
  }
}

export function addSecretIngredient(friendsList, myList) {
  myList.push(friendsList.at(-1));
}

export function scaleRecipe(recipe, num) {
  let out = {};
  for(let ingredient in recipe){
    out[ingredient] = recipe[ingredient] / 2 * num;
  }
  return out
}