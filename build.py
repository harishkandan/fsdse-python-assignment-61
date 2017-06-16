def solution(list_of_nums):
    o,e=0,0
    for i in range(0,len(list_of_nums)):
        if(list_of_nums[i]%2==0):
            e=e+1
        else:
            o=o+1
    return {'ODD': o, 'EVEN': e}
