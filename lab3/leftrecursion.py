from  typing import *


def printans(arr:List)->None:
    for ans in arr:
        print(ans)

def driver(directory:str)->None:

    with open(directory,'r') as file:
        s = file.readline()
        # E->E+T/T
    f = s[0]
    other = s[3:]
    a =  []
    beta =[]
    li = other.strip('\n').split('|')
    beta_count=0
    for st in li:
        
        if f == st[0]:
            a.append(st[1:])
        else:
            beta_count += 1 
            beta.append(st)

    part1 = ""
    part2 =" "

    final_answer = []

    if len(a)!=0:
        fd = f+"'"
        part1 = f + "->"
        part2 = fd+"->"
        for i in range(len(a)):
        
            if i==len(a)-1:
                part1 += beta[i] + fd  
            else:
                part1 += beta[i] + fd  + "|"

            part2 += a[i]+fd  + "|"
        

        part2+= "Epshila"
        final_answer.append(part1)
        final_answer.append(part2)
        
        printans(final_answer)
    else:
        print("Sorry no left recursion found")


if __name__ == "__main__":
    directory = input("Please provide location of text-file with grammar \n")
    driver(directory)
    
    


