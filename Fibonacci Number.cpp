
class Solution {
public:
    int fib(int n) {
        if(n == 0 || n == 1)
            return n;
        int num1 = 0;
        int num2 = 1;
        int result= 0;
        for(int i = 1; i < n; i++){
            result = num1 + num2;
            num1= num2;
            num2= result;
        }
        return result;
    }
};
