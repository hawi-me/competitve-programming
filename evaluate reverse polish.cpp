class Solution {
public:

    int evalRPN(vector<string>& tokens) {
        stack<int>stak;
        for(int i=0;i<tokens.size();i++)
        {
            if((tokens[i]=="/")||(tokens[i]=="*")||(tokens[i]=="+")||(tokens[i])=="-")
            {
                 int val1=stak.top();
                 stak.pop();
                 int val2=stak.top();
                 stak.pop();
                 if(tokens[i]=="/")
                 val1=val2/val1;
                 else if(tokens[i]=="*")
                 val1=val2*1LL*val1;//prevent stack over flow
                 else if(tokens[i]=="+")
                 val1=val1+val2;
                 else
                 val1=val2-val1;
                 stak.push(val1);
            }
            else
            {
                stak.push(stoi(tokens[i]));
            }
        }
        return stak.top();
    }
};
