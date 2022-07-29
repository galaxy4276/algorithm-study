fn main() {
  let result = add_binary("1010".to_string(), "1011".to_string());
  println!("result: {}", result);
}

fn add_binary(a: String, b: String) -> String {
  let rev_a = a.chars().into_iter().rev().collect::<String>();

  let mut result = String::new();
  let mut is_up: bool = false;
  for b in a.chars().into_iter().rev() {
    
    // for b in b.chars().into_iter().rev() {
    //   if is_up && (a == '1' || b == '1') {
    //     result.push('1');
    //   } else if a == '0' && b == '0' {
    //     result.push('1');
    //     is_up = false;
    //   } else if a == '1' && b == '1' {
    //     is_up = true;
    //     result.push('0');
    //   }
    }
  }

  if is_up {
    result.push('1');
  }

  return result.chars().into_iter().rev().collect::<String>();
}
