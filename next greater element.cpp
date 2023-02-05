class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        map<int,int>m;
        for(int i=0;i<nums2.size()-1;i++){
            if(nums2[i+1]>nums2[i])m[nums2[i]]=nums2[i+1];
            else{
                int j=i+1;
                while(j<nums2.size()){
                    if(nums2[j]>nums2[i]){
                        m[nums2[i]]=nums2[j];
                        break;
                    }else j++;
                }
                if(j>=nums2.size())m[nums2[i]]=-1;
            }
        }
        int n=nums2.size();
        m[nums2[n-1]]=-1;

        vector<int>ans;
        for(auto i:nums1){
            ans.push_back(m[i]);
        }

        return ans;
    }
};
