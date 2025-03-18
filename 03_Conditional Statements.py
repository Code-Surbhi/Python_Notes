'''
    if elif else

    if condition:
        if statement block
        _______________
        _______________
    elif condition:
        elif statement block
        _______________
        _______________        
    else:
        else statement block
        _______________
        _______________
'''

num = int(input("Enter a number: "))
if num<0:
    print("Number is negative")
else:
    print("Number is positive")

'''
    Compound Conditions -> and or not

    and -> AND -> only if both true then true
    or -> OR -> if either true it becomes true
    not -> NOT -> opposite 
'''

'''
    Nested if and elif 

    if j>s and j>a:
        print("j is the eldest")
    else:
        if s>a:
            print("s is the eldest")
        else:
            print("a is the eldest")

    OR

    if j>s and j>a:
        print("j is the eldest")
    elif s>a:
        print("s is the eldest")
    else:
            print("a is the eldest")
'''

age=int(input("Enter age: "))
if age>=18 and age<=30:
    print("You are young")
elif age<18:
    print("You are a child")
else:
    print("You are old")

gender=input("Enter m for male and f for female")
if gender=='m' or gender=='M':
    print("You are a male")
elif gender=='f'or gender=='F':
    print("You are a female")
else:
    print("Invalid gender")

'''
    Relational operator < , <= , > , >= , == , !=

    int, float , bool ,str => all are allowed
    complex only -> == and != are allowed 
'''
'''
    s1="America" -> first in dictionary
    s2="Brazil" -> second in dictionary
    s1<s2 -> True

    Strings mai hum dictionary order check krte hai 

    s1="brazil" -> 2nd
    s2="Brazil" -> 1st
    Uppercase comes first
    s1<s2 -> False
    s1>s2 -> True
'''
'''
    0 is false
    rest all is true
'''
'''
    1. Non bool type
        if 0 and 6 : -> false ayega hamesha
        if 5 and 6 : -> true ayega hamesa

        0 , 0.0 , 0+0j , "" -> FALSE values

    2. Short Circuit
        a<b and a<c -> if a<b hi false agya then it wont even check a<c
'''
'''
    Bitwise operator

    a=10
    format(a,'b') -> output = 1010

    formal(variable , 'b') => function to find out the binary form of the number

    bin(a) -> output = 0b1010

    a.bit_length() -> know how many bits there are for storing the value
'''
'''
    1*1 = 1
    1*0 = 0
    0*1 = 0
    0*0 = 0

    1+1 = 1
    1+0 = 1
    0+1 = 1
    0+0 = 0

    1^1 = 0
    1^0 = 1
    0^1 = 1
    0^0 = 0
'''
'''
    a=10 -> a = 1010
    b=13 -> b = 1101

    a&b = 1000 -> 8
    a|b = 1111 -> 15
    a^b = 0111 -> 7

    a<<1 ->  1010 -> value 10
            10100 -> value 20 -> extra space will have 0 there
    
    when we left shift by 1 -> number doubles
    similarly when we right shift by 1 -> number becomes half and so on

    40<<5 -> means left shift 50 by 5 places

    a>>n => a/2^n
    a<<n => a*2^n

    bitwise shift operators have a higher precedence than bitwise & operator
'''
'''
    Is or Is not

    Is -> compares the identity of 2 variables and returns true if they referance the same object

    a=10
    b=10
    happens with literals 

    a and b ka variable box with refer to a same box with value 10 hence
    a is b -> True 
    because a and b are reffering to the same data 

    x = 10
    y = 20
    x is y -> False
    x is not y - True

    num = 10
    id(num) -> shows the address of num

    a and b dono ki value 10 hai but on doing a is b we get false -> why?
    a=input("enter number: ")
    b=input("enter number2: ")
        if we typecast both the strings -> means ke same memory is used
        but if not then input function assumes that every entry is a unique/different entity
'''
'''
    if a>b>c:
        print("yes")
    else:
        print("no")

    prints yes if value of a>b and b>c -> not the case of greatest / smallest
'''


