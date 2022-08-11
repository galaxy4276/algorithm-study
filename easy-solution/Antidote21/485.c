int findMaxConsecutiveOnes(int* nums, int numsSize) {
	int i, max = 0, cnt = 0;
	for (i = 0; i < numsSize; i++) {
		if (nums[i] == 1) {
			cnt++;
			if (max < cnt) max = cnt;
		}
		else cnt = 0;
	}
	return max; 
}
