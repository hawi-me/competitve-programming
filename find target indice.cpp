class Solution {
public:
    vector<int> targetIndices(vector<int>& nums, int target) {
         
        vector<int> ans;
        
        int index = 0;
        int f= 0;
        int n=nums.size();
        
        for(int i = 0; i < n; i++){
            if(nums[i] < target)
                index++;
            else if(nums[i] == target)
                f++;
        }
        
        while(f> 0){
            ans.push_back(index);
            f--;
            index++;
        }
        return ans;
    }
    
};
