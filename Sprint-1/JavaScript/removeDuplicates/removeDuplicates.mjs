/**
 * Remove duplicate values from a sequence, preserving the order of the first occurrence of each value.
 *
 * Time Complexity: O(n²),the nested loops may compare many items against one another.
 * Space Complexity:O(n) — stores the unique items in a new array.
 * Optimal Time Complexity: O(n) — a Set can check for duplicates in one pass, on average.
 *
 * @param {Array} inputSequence - Sequence to remove duplicates from
 * @returns {Array} New sequence with duplicates removed
 */
export function removeDuplicates(inputSequence) {
  return [...new Set(inputSequence)];
}

/*
After Refactoring
 *Time Complexity: O(n) — uses a Set, on average.
 * Space Complexity: O(n) — stores unique items in a new collection.
 * Optimal Time Complexity: O(n) — each input item must be checked.
*/