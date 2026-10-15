/**
 * Finds common items between two arrays.
 *
 * Time Complexity: O(n * m), where as well as m  referes to a size — checks each item in the first array against items in the second array.
 * Space Complexity: O(n) — creates a filtered array and a Set.
 * Optimal Time Complexity: O(n + m) — each array can be checked in linear time using a Set.
 *
 * @param {Array} firstArray - First array to compare
 * @param {Array} secondArray - Second array to compare
 * @returns {Array} Array containing unique common items
 */
export const findCommonItems = (firstArray, secondArray) => {
  const secondSet = new Set(secondArray);
  const commonItems = new Set();

  for (const item of firstArray) {
    if (secondSet.has(item)) {
      commonItems.add(item);
    }
  }

  return [...commonItems];
}

/**
 After Refactoring
 * Time Complexity: O(n + m) — uses a Set to check for common items efficiently.
 * Space Complexity: O(m + q) — stores items from the second array and the common items, where q is the number of unique matches.
 * Optimal Time Complexity: O(n + m) — each array is processed in linear time.
 */
