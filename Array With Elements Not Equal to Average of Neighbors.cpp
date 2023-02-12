
class Solution {
public:

    vector<int> rearrangeArray(vector<int>& nums) {
          for(int i=1;i+1<nums.size();i++){
                    int x=nums[i-1],y=nums[i],z=nums[i+1];
                    if( x<y&& y<z|| x>y &&y>z  ) swap(nums[i],nums[i+1]);
          }
        return nums;
    }
    };
