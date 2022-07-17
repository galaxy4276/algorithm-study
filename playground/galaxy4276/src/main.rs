fn main() {
    let strs = vec!["dog".to_string(), "racecar".to_string(), "car".to_string()];
    let strs2 = vec!["cir".to_string(), "car".to_string()];
    let res: String = longest_common_prefix(strs2);
    println!("res: {}", res);
}

fn longest_common_prefix(strs: Vec<String>) -> String {
    let mut first: String = strs[0].to_string();

    for i in 1..strs.len() {
        let mut calc_s = "".to_string();
        let mut switch = true;
        for (j, s) in strs[i].chars().enumerate() {
            let last_bytes = *&first.as_bytes();
            if switch && j < last_bytes.len() && last_bytes[j] as char == s {
                calc_s.push(s);
            } else {
                switch = false;
            }
        }
        if calc_s.len() == 0 { return "".to_string() }
        first = calc_s;
    }

    first
}
