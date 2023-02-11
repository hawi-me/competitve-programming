

class Solution {

public:

    int numberOfSubarrays(vector<int>& nums, int k) {

        int n = nums.size();

        int result = 0,odd = 0,count = 0;

        int l = 0,r = 0;

        while(r<n)

        {

            if(nums[r]%2 != 0)

            {

                odd++;

                count= 0;

            }

            while(odd == k)

            {

                ++count;

                odd -= nums[l++]&1; 

            }

            result += count;

            r++;

        }

        return result;

    }

};
