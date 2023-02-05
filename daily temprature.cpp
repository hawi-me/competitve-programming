



class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        
        int n = temperatures.size();
        vector<int> warm_index(n);
        stack<pair<int,int>> stak; // {temperature , index};

        for(int i=0;i<n;i++){
            while(!stak.empty() && stak.top().first<temperatures[i]){
                warm_index[stak.top().second] = i-stak.top().second;
                stak.pop();
            }
            stak.push({temperatures[i],i});
        }

        while(!stak.empty()){
            warm_index[stak.top().second]=0;
            stak.pop();
        }
        
        return warm_index;
    
    }
};
