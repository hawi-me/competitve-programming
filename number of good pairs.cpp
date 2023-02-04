class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
        int count = 0;
        unordered_map<int, int> ump;
        for(int i=0;i<nums.size();i++) {
            if(ump[nums[i]] > 0) {
                count += ump[nums[i]];
            }
            ump[nums[i]]++;
        }
        return count;
    }
};
