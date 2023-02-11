
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> product(n, 1);
        for (int i = 1; i < n; i++) {
            product[i] = product[i - 1] * nums[i - 1];
        }
        for (int j = n - 1, k= 1; j >= 0; j--) {
            product[j] *= k;
            k*= nums[j];
        }
        return product;
    }
};
