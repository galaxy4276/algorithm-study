#include <stdio.h>
#include <string.h>

int findNumbers(int* nums, int numsSize) {
	int i, cnt , len = 0;
	for (int i = 0; i < numsSize; i++) {
		cnt = 0;
		while(nums[i]!=0) {
			nums[i] = nums[i] / 10;
			++cnt;
		}
		if (cnt % 2 == 0) {
			len++;
		}
	}
	return len;
}

int main(void) {
	int k;
	int str[7] = { 437,315,322,431,686,264,442 };
	k = findNumbers(&str, 7);
	printf("%d", k);

}