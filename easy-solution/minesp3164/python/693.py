list = bin(5)
list = [char for char in list[2::]]
for i in range(len(list)-1):
    if(list[i] == list[i+1]):
        return False
return True

