class MinStack {
public:
    MinStack() {
        
    }
    stack<pair<int, int>> stak;

    
    void push(int val) {
        if(stak.empty()){
            stak.push({val, val});
        }
        else{
            if(stak.top().second<val){
                stak.push({val, stak.top().second});
            }
            else{
                stak.push({val, val});
            }
        }
        
    }
    
    void pop() {
        if(stak.empty()){
            return;
        }
        stak.pop();
    }
    
    int top() {
        if(stak.empty()){
            return -1;
        }
        return stak.top().first;
    }
    
    int getMin() {
         if(stak.empty()){
            return -1;
        }
        return stak.top().second;
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */
