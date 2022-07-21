fn main() {
    let test_case1 = "()[]{}".to_string();
    let test_case2 = "{[]}".to_string();
    let res = is_valid(test_case2);
    println!("res: {}", res);
}

pub fn is_valid(s: String) -> bool {
    let mut stack  = vec![];
    for c in s.chars() {
        match c {
            ')' => match stack.pop() {
                Some(c) => {
                    if c != '(' {
                        return false;
                    }
                }
                None => return false,
            },
            ']' => match stack.pop() {
                Some(c) => {
                    if c != '[' {
                        return false;
                    }
                },
                None => return false,
            },
            '}' => match stack.pop() {
                Some(c) => {
                    if c != '{' {
                        return false;
                    }
                },
                None => return false,
            },
            _ => {
                stack.push(c);
            },
        }
    }
    return stack.is_empty();
}
