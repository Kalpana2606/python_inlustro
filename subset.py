num=[1,2,3,4]

subsets=[[]]

for num in num:
   
    new_subsets=[]
  
    for A in subsets:
   
        new_subsets.append(A+[num])
 
    subsets+=new_subsets

for A in subsets:
    
    if sum(A)%2==0:
       
        print(A)
