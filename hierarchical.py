#Lab
def hierarchical_num(n:int)->int:
    for i in range(n,0,-1):
        for j in range(i,0,-1):
            print(j, end=" ")
        
        print("")


hierarchical_num(5)
print()



#bouns
def hierarchical_num(n:int)->str:

    result=""

    
    for i in range(n,0,-1):
        for j in range(i,0,-1):
            result+=str(j)+ " "
        
        result+="\n"
    return result




x=hierarchical_num(5)
print(type(x))
print(x)
