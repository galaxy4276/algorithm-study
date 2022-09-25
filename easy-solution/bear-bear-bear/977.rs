// TODO: O(n) 으로 처리해보기
impl Solution {
    pub fn sorted_squares(mut nums: Vec<i32>) -> Vec<i32> {
        nums.sort_unstable_by_key(|x| x.abs());
        nums.iter_mut().for_each(|x| *x = x.pow(2));
        nums
    }
}
