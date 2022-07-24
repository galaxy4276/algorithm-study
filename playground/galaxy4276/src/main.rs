fn main() {
  let nums = vec![1, 3, 5, 6];
  search_insert(nums, 5);
}

fn search_insert(nums: Vec<i32>, target: i32) -> i32 {
  for i in 0..nums.len() {
    if nums[i] == target {
      return i as i32;
    }
  }

  for i in 0..nums.len() {
    if nums[i] > target {
      return i as i32;
    }
  }

  return nums.len() as i32;
}

// fn main() {
//   let mut input = vec![3, 2, 2, 3];
//   let result = remove_element(&mut input, 3);
//   println!("result: {:?}", result);
// }


// fn remove_element(nums: &mut Vec<i32>, val: i32) -> i32 {
//   for i in 0..nums.len() {
//     if nums[i] == val {
//       nums.remove(nums[i] as usize);
//     }
//   }
//   return 2;
// }