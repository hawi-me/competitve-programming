

class Solution {
public:
    int maxArea(vector<int>& height) {
        int maxArea = 0;
        int start = 0, end= height.size()-1;

        while(start < end){
            if(height[start] <= height[end]){
                maxArea = max(maxArea,(end-start) * height[start]);
                start++;
            }else{
                maxArea = max(maxArea,(end-start) * height[end]);
                end--;
            }
        }
        return maxArea;
    }
};
