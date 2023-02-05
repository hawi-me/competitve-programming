class MyCircularDeque {
public:
    vector<int> q;
    int size, currSize = 0;
    int front, rear;
    MyCircularDeque(int k) {
        size = k;
        rear = -1;
        front = -1;
        q.resize(k, -1);
    }
    
    bool insertFront(int value) {
        if(isFull()) return false;
        if(currSize == 0) {
            rear = 0;
            front = 0;
        }else front = front == 0 ? size - 1: front - 1;

        currSize++;
        q[front] = value;
        return true;
    }
    
    bool insertLast(int value) {
        if(isFull()) return false;
        if(currSize == 0) {
            rear = 0;
            front = 0;
        }else rear = (rear + 1) % size;
        currSize++;
        q[rear] = value;
        return true;
    }
    
    bool deleteFront() {
        if(isEmpty()) return false;

        currSize--;
        q[front] = -1;
        if(currSize == 0) {
            front = -1;
            rear = -1;
        } else front = (front + 1) % size;
        return true;
    }
    
    bool deleteLast() {
        if(isEmpty()) return false;

        currSize--;
        q[rear] = -1;
        if(currSize == 0) {
            front = -1;
            rear = -1;
        } else rear = rear == 0 ? size - 1 : rear - 1;
        return true;
    }
    
    int getFront() {
         return isEmpty() ? -1 : q[front];
    }
    
    int getRear() {
        return isEmpty() ? -1 : q[rear];
    }
    
    bool isEmpty() {
        return currSize == 0;
    }
    
    bool isFull() {
        return currSize == size;
    }
};
