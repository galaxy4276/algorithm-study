

bool checkIfExist(int* arr, int arrSize){
    int i,j,k=0;
    
    for(i=0;i<arrSize;i++){
        if(arr[i]==0){
            ++k;
            if(k==2){
                return true;
            }
        }
    }
    
    for(i=0;i<arrSize;i++){
        for(j=0;j<arrSize;j++){ //j=1로 변경해야 함 
            if(arr[i] == 2*arr[j]&&arr[i]!=0){ //arr[i] == 2*arr[j] ||  arr[j] == 2 * arr[i] 0이 두 개 일때도 성립 가능 
                return true;
            }
        }
        
    }
    
    return false;
}

bool checkIfExist(int* arr, int arrSize){
        for (int i = 0; i < arrSize; i++){
            for (int j = i+1; j < arrSize; j++){
                if(arr[i] == 2*arr[j] ||  arr[j] == 2 * arr[i]) return true; 
            }
        }
        return false;
    }
