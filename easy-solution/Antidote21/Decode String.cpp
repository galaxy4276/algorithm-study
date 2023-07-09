class Solution {
public:
    string decodeString(string s) {
        stack<char> st;
        for(int i = 0; i < s.size(); i++){
            if(s[i] != ']'){
                st.push(s[i]);
            }
            else{
                string curr = "";
                while(st.top() != '['){
                    curr = st.top() + curr;
                    st.pop();
                }
                st.pop();
                string number;

                while(!st.empty() && isdigit(st.top())){
                    number = st.top() + number;
                    st.pop();
                }
                int k_time = stoi(number);

                while(k_time--){
                    for(int p=0; p < curr.size(); p++){
                        st.push(curr[p]);
                    }
                }
                
            }
            
        }
        string str = "";
        while(!st.empty()){
            str = st.top() + str;
            st.pop();
        }
        return str;      
    }
};
