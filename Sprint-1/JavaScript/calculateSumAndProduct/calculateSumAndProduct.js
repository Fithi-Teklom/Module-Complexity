/**
 * Calculate the sum and product of integers in a list
 *
 * Note: the "sum" is every number added together
 * and the "product" is every number multiplied together
 * so for example: [2, 3, 5] would return
 * {
 *   "sum": 10, // 2 + 3 + 5
 *   "product": 30 // 2 * 3 * 5
 * }
 *
 * Time Complexity:O(n) — two loops each visit every number.
 * Space Complexity: O(1) — uses a fixed number of variables.
 * Optimal Time Complexity: O(n) — every number must be checked.
 *
 * @param {Array<number>} numbers - Numbers to process
 * @returns {Object} Object containing running total and product
 */

export function calculateSumAndProduct(numbers) {
  let sum = 0;
  let product = 1;
  for (const num of numbers) {
    sum += num;
    product *= num;
  }
  return {
    sum: sum,
    product: product,
  };
}

/** 
 After Refactor 
 * Time Complexity: O(n) — one loop calculates both results.
 * Space Complexity: O(1) — uses a fixed number of variables.
 * Optimal Time Complexity: O(n) — every number must be checked.
 */
