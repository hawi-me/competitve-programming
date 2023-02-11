class Solution {
public:
    int compress(vector<char>& chars) {
        int ansIndex=0;
        int i=0;
        while(i<chars.size())
        {
            int j=i+1;
            while(j<chars.size()&&chars[i]==chars[j])
            {
                j++;
            }
            chars[ansIndex++]=chars[i];
            int count=j-i;
            if(count>1)
            {
                string s=to_string(count);
                for(char ch: s)
                {
                    chars[ansIndex++]=ch;
                }
            }
            i=j;
        }
        return ansIndex;
    }
};
