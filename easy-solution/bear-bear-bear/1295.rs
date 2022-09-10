impl Solution {
    pub fn find_numbers(nums: Vec<i32>) -> i32 {
        let mut count: i32 = 0;
        for num in &nums {
            if num.to_string().len() % 2 == 0 {
                count += 1;
            }
        }
        count
    }


    // https://leetcode.com/problems/find-numbers-with-even-number-of-digits/discuss/457571/Python3-C%2B%2B11-C%2B%2B20-Java-Haskell-Clojure-Rust-Scala-Elixir-and-APL-Solutions
    pub fn refactored_find_numbers(nums: Vec<i32>) -> i32 {
        return nums.iter()
            .map(|i| i.to_string().len())
            .filter(|i| i % 2 == 0)
            .count() as i32;
    }
}
