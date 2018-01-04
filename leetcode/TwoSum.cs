public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        
		int max_positive_number = nums.Max();
		int max_negative_number = nums.Min();
		
        int array_size_positive = (max_positive_number > target) ?  max_positive_number + 1 : target + 1;
		int array_size_negative = (max_negative_number < target) ? (max_negative_number * -1) + 1 : (target * -1) + 1;
        int[] nums_count = new int[array_size_positive];
		int[] nums_count_negative = new int[array_size_negative];
        int[] nums_count_index = new int[array_size_positive];
		int[] nums_count_index_negative = new int[array_size_negative];
        int[] result = new int[2];
        
		
        //count occurences for positive and negative numbers
        for(int i = 0; i < nums.Length; i++){
			
			if(nums[i] >= 0){
				nums_count[nums[i]]++;
				nums_count_index[nums[i]] = i;
			}
			else {
				nums_count_negative[nums[i]]++;
				nums_count_index_negative[nums[i]] = i;
			}
			
        }
		
		// iterate to target, check the complement, if nothing exist, iterate again to max positive number
		bool outOfBounds = false;
		int i = 0;
		
		while(!outOfBounds) {
			//check out of bonds
			if (i <= target) {
				if (i > max_positive_number) {
					outOfBounds = true;
					continue;
				}				
			}
			else if(i > target) {
				if (i-target < max_negative_number) {
					outOfBounds = true;
					continue;
				}
			}
		
			if (i < target) {
				if (nums_count[i] + nums_count[target - i] >= 2) {
					result[0] = nums_count_index[i];
					result[1] = nums_count_index[target - i];
					
					outOfBounds = true;
				}
			}
			else { //i > target
				
			}
			
			
			outOfBounds = true;
		}
		
		
		
		
		
		
		
		
		
		
		
		// check which index is larger (- or +)
		
		// case 1: target is + number
		// + plus + = target
		for (int i = 0; i < target; i++) {
			if (nums_count[i] + nums_count[target - i] >= 2) {
				result[0] = nums_count_index[i];
				result[1] = nums_count_index[target - i];
				
				i == target;
			}
		}
		
		
		// + plus - = target
		for (int i = 0; i < target; i++) {
			if (nums_count[i] + nums_count[target - i] >= 2) {
				result[0] = nums_count_index[i];
				result[1] = nums_count_index[target - i];
				
				i == target;
			}
		}
		
		// case 2: target is - number
		
		// - plus - = target
		
		// special case if target/2 + target/2 = target exist
		
		
        bool isFound = false;
        int left = 0;
        int right = target;
        
        while(!isFound && left < right){
            if(nums_count[left] + nums_count[right] >= 2){
                isFound = true;
                result[0] = nums_count_index[left];
                result[1] = nums_count_index[right];
            }
            
            left++;
            right--;
        }
        return result;
    }
}