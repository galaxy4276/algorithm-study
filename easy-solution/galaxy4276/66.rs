impl Solution {
  pub fn plus_one(digits: Vec<i32>) -> Vec<i32> {
  let mut digits = digits;
  for v in digits.iter_mut().rev() {
    let sum = *v + 1;
    *v = sum % 10;
    if sum < 10 {
      return digits;
    }
  }

  [&vec![1], &digits[..]].concat()
  }
}