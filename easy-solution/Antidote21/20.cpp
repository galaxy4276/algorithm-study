class Solution {
public:
    bool isValid(string s) {
        stack<char> t; 
        //int i; 
        
        for(auto i:s) 
        {
            if(i == '(' || i =='{' || i == '[')
            {
                t.push(i);
            }
            else
            {
                // check condition for false
                if(t.empty() || (t.top() == '(' && i != ')') || (t.top() == '{' && i != '}') || (t.top() == '[' && i != ']'))
                {
                    return false;
                }
                
                t.pop(); // else pop from stack
            }
        }
        
        return t.empty(); // if stack is empty then it is valid, otherwise no
    }
};
