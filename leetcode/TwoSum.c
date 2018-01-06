int* twoSum(int* nums, int numsSize, int target) {
    int largest_p = 0;
	int smallest_n = 0;
	
	for (int i = 0; i < numSize; ++i) {
		if (nums[i] > largest_p) largest_p = nums[i];
		if (nums[i] < smallest_n) smallest_n = nums[i];
	}
	
	//positive & negative number occurences
	int pnum_count[largest_p + 1] = {0};
	int nnum_count[(smallest_n * -1) + 1] = {0};
	
	//order of each number from input
	int pnum_order[] = pnum_count;
	int nnum_order[] = nnum_count;
	
	for (int i = 0; i < numSize; ++i) {
		if (nums[i] >= 0) {
			pnum_count[nums[i]]++;
			pnum_order[nums[i]] = i;
		}
		else if (nums[i] < 0) {
			pnum_count[nums[i] * -1]++;
			pnum_order[nums[i] * -1] = i;
		}
	}
	
	//p + p = target
	//p + n = target
	//n + n = target
	
}