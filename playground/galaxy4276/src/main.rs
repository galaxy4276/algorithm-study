fn main() {
    let mut s: String = String::from("World is Beautiful.");
    let result: usize = first_word(&s);
    println!("{}", result);
}

fn first_word(s: &String) -> usize {
    let bytes = s.as_byte();

    for (i, &item) in bytes.iter().enumerate() {
        if item == b' ' {
            return i;
        }
    }

    s.len()
}
