class MyQueue {
    stack<int> stak1;
    stack<int> stak2;
public:
    MyQueue() {
       
    }
   
    void push(int x) {
        if(this->stak1.empty())
        {
            this->stak1.push(x);
        }
        else{
            while(!this->stak1.empty())
            {
               
                this->stak2.push(this->stak1.top());
                this->stak1.pop();
            }
            this->stak2.push(x);
            while(!this->stak2.empty())
            {
               
                this->stak1.push(this->stak2.top());
                this->stak2.pop();
            }
           
        }
    }
   
    int pop() {
        int temp=this->stak1.top();
        this->stak1.pop();
        return temp;
    }
   
    int peek() {
        return this->stak1.top();
    }
   
    bool empty() {
        if(this->stak1.empty())
        return true;
        else
        return false;
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */
