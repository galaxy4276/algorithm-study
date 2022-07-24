fn main() {
  let haystack = "hello".to_string();
  let needle = "ll".to_string();

  let result = str_str(haystack, needle);
  println!("result: {}", result);
}

fn str_str(haystack: String, needle: String) -> i32 {
  match haystack.find(&needle) {
    Some(n) => n as i32,
    None => -1,
  }
}
