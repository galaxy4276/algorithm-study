impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        for (i_idx, i_num) in nums.iter().enumerate() {
            for (j_idx, j_num) in nums.iter().enumerate() {
                if i_num + j_num == target {
                    return vec![i_idx as i32, j_idx as i32];
                }
            }
        }

        unreachable!();
    }
}
