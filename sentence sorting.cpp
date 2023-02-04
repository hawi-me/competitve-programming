class Solution {
public:
  static bool comp(string a,string b)
    {
        return a.back()<b.back();
    }
    string sortSentence(string s) {
        vector<string>v;
       string x="";
       for(int i=0;i<s.length();i++)
       {
           if(s[i]==' ')
           {
               v.push_back(x);
               x="";
           }
           else
           {
               x+=s[i];
           }
       }
       v.push_back(x);
       x="";
       sort(v.begin(),v.end(),comp);
        for(int i=0;i<v.size();i++)
        {
            x+=v[i];
        }
        s="";
        for(int i=0;i<x.length();i++)
        {
            if(x[i]>='1' && x[i]<='9')
            {
                s+=' ';
            }
            else
            {
                s+=x[i];
            }
        }
        s.pop_back();
        return s;

    }
};
