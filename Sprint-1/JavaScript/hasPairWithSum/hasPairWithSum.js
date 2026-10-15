/**
 * Find if there is a pair of numbers that sum to a given target value.
 *
 * Time Complexity: O(n²) — nested loops check pairs of numbers.
 * Space Complexity: O(1) — uses only a fixed number of variables.
 * Optimal Time Complexity:O(n) — a Set can find a matching pair in one pass, on average.
 *
 * @param {Array<number>} numbers - Array of numbers to search through
 * @param {number} target - Target sum to find
 * @returns {boolean} True if pair exists, false otherwise
 */
export function hasPairWithSum(numbers, target) {
  const seen = new Set();
  for (const number of numbers) {
    const needed = target - number;

    if (seen.has(needed)) {
      return true;
    }

    seen.add(number);
  }

  return false;
}

/*
After Refactoring
 * Time Complexity: O(n) — checks each number once on average.
 * Space Complexity: O(n) — stores numbers in a Set.
 * Optimal Time Complexity: O(n) — one pass using a Set, on average.
 */
