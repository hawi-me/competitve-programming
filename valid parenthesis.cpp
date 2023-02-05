class Solution {
public:
    bool isValid(string s) {
        stack<char> stk ; 
        for (int i = 0 ;  i< s.length() ; i++)
        {
            char ch = s[i];

            // if opening bracket then push into the stack 
            if (ch == '(' || ch == '{' || ch == '[')
            {
                stk.push(ch) ; 
            }

            else {
                
                if (!stk.empty())
                {
                    char top = stk.top() ;
                    if ((ch == ')' && top == '(') || 
                        (ch == '}' && top == '{') ||
                        (ch == ']' && top == '[')) 
                        {
                            // if matches then pop 
                            stk.pop() ;
                        }
                        else 
                        {
                            return false ; 
                        }
                }
                else 
                {
                   
                    return false ;
                }
            }
        }

       
        if (stk.empty())
        {
            return true ; 
        }
        return false ;
    }
};
