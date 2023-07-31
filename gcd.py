""" computing GCD of 2 numbers """


def str_to_num(numStr):
    wordLength3 = {'one':1, 'two':2, 'six':6}
    wordLength4 = {'zero':0, 'four':4, 'five':5, 'nine':9}
    wordLength5 = {'three':3, 'seven':7, 'eight':8}
    
    if len(numStr) <= 5:
        if numStr in wordLength3:
            num1 = wordLength3[numStr]
        elif numStr in wordLength4:
            num1 = wordLength4[numStr]
        elif numStr in wordLength5:
            num1 = wordLength5[numStr]

        return num1        
        
    else:
        word3, remain3 = numStr[:3], numStr[3:]
        word4, remain4 = numStr[:4], numStr[4:]
        word5, remain5 = numStr[:5], numStr[5:] 
        
        if word3 in wordLength3:
            num1 = wordLength3[word3]
            if remain3 in wordLength3:
                num2 = wordLength3[remain3]
            elif remain3 in wordLength4:
                num2 = wordLength4[remain3]
            elif remain3 in wordLength5:
                num2 = wordLength5[remain3]

        elif word4 in wordLength4:
            num1 = wordLength4[word4]
            if remain4 in wordLength4:
                num2 = wordLength4[remain4]
            elif remain4 in wordLength3:
                num2 = wordLength3[remain4]
            elif remain4 in wordLength5:
                num2 = wordLength5[remain4]
            
        elif word5 in wordLength5:
            num1 = wordLength5[word5]
            if remain5 in wordLength5:
                num2 = wordLength5[remain5]
            elif remain5 in wordLength4:
                num2 = wordLength4[remain5]
            elif remain5 in wordLength3:
                num2 = wordLength3[remain5]

        num = int(str(num1)+str(num2))
        
        return num


def find_gcd():
    n1 = input("Enter 1st number in words : ")
    x = str_to_num(n1)

    n2 = input("Enter 2nd number in words : ")
    y = str_to_num(n2)

    def calculate(x,y):
        if x == 0:
            return y
        if y == 0:
            return x
        if x == y:
            return x
        if x > y:
            return calculate(x-y,y)

        return calculate(x,y-x)
            
    ans = calculate(x,y)
    print(f"GCD of {x} and {y} is", ans)
    

if __name__ == '__main__':
    find_gcd()