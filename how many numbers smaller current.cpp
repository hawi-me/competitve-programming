class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
       vector<int>num1;
       int n=nums.size();
       int count=0,i=0,j=1;
       
       //sort(nums.begin(),nums.end(),greater<int>());
       while(i<n){
            while(j!=i)
            {
                if(nums[j]<nums[i])
                count++;
                j=(j+1)%n;
            }
            num1.push_back(count);
            count=0;
            i++;
            if(i<n-1)
            j=i+1;
            else
            j=(i+1)%n;

        }
        return num1;

    }
};
