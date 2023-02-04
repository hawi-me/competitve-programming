class Solution {
public:
    int maxFrequency(vector<int>& num, int k) {
        sort(begin(num), end(num));
        long i = 0, N = num.size(), ans = 1, sum = 0;
        for (int j = 0; j < N; ++j) {
            sum += num[j];
            while ((j - i + 1) * num[j] - sum > k) 
            sum -= num[i++];
            ans = max(ans, j - i + 1);
        }
        return ans;
    }
};
