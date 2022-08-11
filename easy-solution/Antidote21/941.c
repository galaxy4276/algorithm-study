
// retry 
bool validMountainArray(int* arr, int arrSize){
    int i = 0;
    while(i+1 < arrSize && arr[i] < arr[i+1]) // 올라가는 조건 
        i++;
    if(i==0 || i==arrSize-1) //ex) 0 1 2 3 4 5 / 5 4 3 2 1
        return false;
    while(i+1< arrSize && arr[i] > arr[i+1]) // 내려가는 조건 
        i++;
    return i == arrSize-1;
}
