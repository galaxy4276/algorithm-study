impl Solution {
    pub fn roman_to_int(s: String) -> i32 {
        let mut result_number = 0;
        let mut last = 0;
        for c in s.chars() {
            let romanic_to_int = get_value(c);
            if last != 0 && last >= romanic_to_int {
                result_number += romanic_to_int;
            } else {
                let calculated = romanic_to_int - last - last;
                result_number += calculated;
            }
            last = romanic_to_int;
        }
        return result_number;
    }
}

fn get_value(c: char) -> i32 {
    match c {
        'I' => 1,
        'V' => 5,
        'X' => 10,
        'L' => 50,
        'C' => 100,
        'D' => 500,
        'M' => 1000,
        _ => 0,
    }
}
