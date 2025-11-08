/// <reference path="./global.d.ts" />
//
// @ts-check

/**
 * Determine the price of the pizza given the pizza and optional extras
 *
 * @param {Pizza} pizza name of the pizza to be made
 * @param {Extra[]} extras list of extras
 *
 * @returns {number} the price of the pizza
 */
export function pizzaPrice(...extras) {
  if (extras.length === 0){
    return 0;
  }
  let price = 0;
  
  switch(extras[0]){
    case "Margherita":
      price += 7;
      break;
    case "Caprese":
      price += 9;
      break;
    case "Formaggio":
      price += 10;
      break;
    case "ExtraSauce":
      price += 1;
      break;
    case "ExtraToppings":
      price += 2;
      break;
  }
  return price + pizzaPrice(...extras.slice(1));
}

/**
 * Calculate the price of the total order, given individual orders
 *
 * (HINT: For this exercise, you can take a look at the supplied "global.d.ts" file
 * for a more info about the type definitions used)
 *
 * @param {PizzaOrder[]} pizzaOrders a list of pizza orders
 * @returns {number} the price of the total order
 */
export function orderPrice(pizzaOrders) {
  let price = 0;
  for (let item of pizzaOrders) {
    price += pizzaPrice(item.pizza,...item.extras);
  }
  return price;
}
