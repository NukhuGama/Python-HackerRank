if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    # Sorting Ascendent 
    ls = list(arr)
    ls.sort()
    # Find Max Number
    # print(ls)
    max_num = max(ls)
    # Remove Maximum number
    new_ls=[]
    for i in range (len(ls)-1):
        if (ls[i]!=max_num):
            new_ls.append(ls[i])       
    # Get the maximum number and consider as second maximum number(RunnerUp)
    runnerup = max(new_ls)
    print(runnerup)
    



    # 
