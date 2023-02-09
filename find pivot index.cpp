
class Solution {
    public:
    int pivotIndex(vector<int>& nums) {
      if(nums.size() == 0) return - 1;
      int leftSum = 0, rightSum = 0;
      for(int num : nums) 
          rightSum += num;

      for(int i = 0; i < nums.size(); i ++) {
        rightSum -= nums[i];
        if(rightSum == leftSum) return i;
        leftSum += nums[i];
      }
      return - 1;
    }
};
