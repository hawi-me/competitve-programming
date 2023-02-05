class Solution {
public:
    string reverseParentheses(string s) {
        stack<int> stak;
        string res;
        for (int i = 0; i < s.size(); i ++) {
            if (s[i] == '(') {
                stak.push(i);    
            } else if (s[i] == ')') {
                int top = stak.top();
                stak.pop();
                reverse(s.begin() + top + 1, s.begin() + i);
            }
        }
        for (auto it: s) {
            if (it != '(' && it != ')') {
                res.push_back(it);
            }
        }
        return res;
    }
};
