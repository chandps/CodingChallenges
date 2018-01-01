public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        
        int array_size = (nums.Max() > target) ?  nums.Max() + 1 : target + 1;
        int[] nums_count = new int[array_size];
        int[] nums_count_index = new int[array_size];
        int[] result = new int[2];
        
        
        for(int i = 0; i < nums.Length; i++){
            nums_count[nums[i]]++;
            nums_count_index[nums[i]] = i;
        }
        
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