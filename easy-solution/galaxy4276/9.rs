impl Solution {
    pub fn is_palindrome(x: i32) -> bool {
        if x < 0 {
            return false;
        }
        let chars: Vec<char> = x.to_string().chars().collect();
        let reversed_chars: Vec<char> = x.to_string().chars().rev().collect();
        for idx in 0..chars.len() {
            if chars[idx] != reversed_chars[idx] {
                return false;
            }
        }
        true
    }
}
