def arithmetic_arranger(prob,chk = False):
    arranged_problems = list()
    l1 = list()
    l2 = list()
    l3 = list()
    l4 = list()
    line1 = str()
    line2 = str()
    line3 = str()
    line4 = str()

    #checking for no. of problems
    if len(prob)>5:
        err = "Error: Too many problems."
        return err
    
    for p in prob:
        p = p.split()
        try:
            num1 = int(p[0])
            num2 = int(p[2])
        except:
            err = "Error: Numbers must only contain digits."
            return  err

        if len(str(num1)) > 4 or len(str(num2)) > 4:
            err = "Error: Numbers cannot be more than four digits."
            return err

        op = p[1]

        if op=='+':
            ans = num1+num2
        elif op=='-':
            ans = num1-num2        
        else:
            err = "Error: Operator must be '+' or '-'."
            return err

        num1s = str(num1)
        num2s = str(num2)

        # .extend() method for appending multiple values
        if chk == False:
            arranged_problems.extend((num1s,op,num2s))
        elif chk == True:
            arranged_problems.extend((num1s,op,num2s,str(ans)))
        
    # Sorting different parts into different lists
    if chk == False:
        n = (len(prob)*3)
        for i in range(0,n,3):
            l1.append(arranged_problems[i])
            l2.append(arranged_problems[i+1])
            l3.append(arranged_problems[i+2])

        for j in range(len(prob)):
            len_max = max(len(l1[j]),len(l3[j]))

            if j==(len(prob)-1):
                line1 = line1 + l1[j].rjust(len_max+2)
                line2 = line2 + l2[j] + " " + l3[j].rjust(len_max)
                line3 = line3 + "-"*(len_max+2)
            else:
                line1 = line1 + l1[j].rjust(len_max+2) + "    "
                line2 = line2 + l2[j] + " " + l3[j].rjust(len_max) + "    "
                line3 = line3 + "-"*(len_max+2) + "    "              
        
        ly = line1 + "\n" + line2 + "\n" + line3
        return ly

    elif chk == True:
        n = len(prob)*4
        for i in range(0,n,4):
            l1.append(arranged_problems[i])
            l2.append(arranged_problems[i+1])
            l3.append(arranged_problems[i+2])
            l4.append(arranged_problems[i+3])

        for j in range(len(prob)):
            len_max = max(len(l1[j]),len(l3[j]))

            if j==(len(prob)-1):
                line1 = line1 + l1[j].rjust(len_max+2)
                line2 = line2 + l2[j] + " " + l3[j].rjust(len_max)
                line3 = line3 + "-"*(len_max+2)
                line4 = line4 + l4[j].rjust(len_max+2)
            else:
                line1 = line1 + l1[j].rjust(len_max+2) + "    "
                line2 = line2 + l2[j] + " " + l3[j].rjust(len_max) + "    "
                line3 = line3 + "-"*(len_max+2) + "    " 
                line4 = line4 + l4[j].rjust(len_max+2) + "    "    
                  
        ly = line1 + "\n" + line2 + "\n" + line3 + "\n" + line4
        return ly  


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"],True))