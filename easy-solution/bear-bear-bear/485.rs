impl Solution {
    pub fn find_max_consecutive_ones(nums: Vec<i32>) -> i32 {
        let mut max_count: i32 = 0;
        let mut curr_count: i32 = 0;

        for num in &nums {
            match num {
                0 => {
                    curr_count = 0;
                }
                1 => {
                    curr_count += 1;
                }
                _ => ()
            }

            max_count = if curr_count > max_count {
                curr_count
            } else {
                max_count
            };
        }

        max_count
    }

    pub fn find_max_consecutive(nums: Vec<i32>) -> i32 {
        let mut max_count: i32 = 0;
        let mut curr_count: i32 = 0;
        let mut last_value: i32 = nums[0];

        for num in &nums {
            match num {
                v if *v == last_value => {
                    curr_count += 1;
                }
                _ => {
                    last_value = *num;
                    curr_count = 1;
                }
            }

            max_count = if curr_count > max_count {
                curr_count
            } else {
                max_count
            };
        }

        max_count
    }
}
