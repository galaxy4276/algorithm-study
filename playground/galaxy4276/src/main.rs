fn main() {
    let s = String::from("MCMXCIV");
    let mut result_number = 0;
    let mut last = 0;
    for c in s.chars() {
        let romanic_to_int = get_value(c);

        if last != 0 && last >= romanic_to_int {
            // println!("number: {}", romanic_to_int);
            result_number += romanic_to_int;
        } else {
            let calculated = romanic_to_int - last - last;
            // println!("calculated: {}", calculated);
            result_number += calculated;
        }
        last = romanic_to_int;
    }
    println!("result is {}", result_number);
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
