class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> s;
        for (auto a : tokens) {
            if (a.size() == 1 && !isdigit(a[0])) {
                int num2 = s.top();
                s.pop();
                int num1 = s.top();
                s.pop();
                switch (a[0]) {  
                case '+':
                    s.push(num1 + num2);
                    break;
                case '-':
                    s.push(num1 - num2);
                    break;
                case '*':
                    s.push(num1 * num2);
                    break;
                case '/':
                    s.push(num1 / num2);
                    break;
                }
            }
            else { 
                s.push(atoi(a.c_str()));
            }
        }
        return s.top();
    }
};
