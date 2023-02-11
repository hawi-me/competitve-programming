
class Solution {
public:
    int maxScore(vector<int>& nums, int k) {
        int front=k-1,back=nums.size()-1;
        int sum=0,maximscore=0;
        for(int i=0;i<k;i++){
            sum+=nums[i];
        }
        maximscore=sum;
        while(front>=0 && front<back){
            sum+=nums[back]-nums[front];
            maximscore=max(maximscore,sum);
            back--;
             front--;
        }
        return maximscore;
    }
};

