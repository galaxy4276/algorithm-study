

void reverseString(char* s, int sSize){
    int i;
    char tmp;
    for(i=0;i<(sSize/2);i++){
        tmp = s[i];
        s[i] = s[sSize-i-1];
        s[sSize-1-i] = tmp;
    }
}
