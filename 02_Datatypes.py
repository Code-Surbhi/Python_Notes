'''
    age = 15
    age -> variable 
    = -> assignment 
    15 -> data

    unlike , c c++ -> just leaving a variable like (int c) is not allowed in python 
    a value must be assigned to it

    EVERYTHING IN PYTHON IS OBJECT

    name = 'soap'
    price = 15
    weight = 10

    Declaring multiple variables -> 
    name, price, weight = 'soap' , 15 , 10
    a, b, c = 10, 15, 20

    Python is a DYNAMICALLY TYPED LANGUAGE ->
    variables datatype depends on the value assigned to them , and we can reassign a value of different datatype to the same variable

    type(variable_name) -> gives the datatype of the object

    x=25 -> datatype int -> type(x) => <class 'int'>
    x=17.25 -> dataype float -> type(x) => <class 'float'>
    x='a' -> datatype string -> type(x) => <class 'str'>

    Variable rules ->
    1. variable name should start with a letter or underscore
    2. Name can contain alpha-numeric character and underscore
    3. No keywords
    4. They are Case sensitive

'''
'''
    Python Datatypes 
    1. Numeric -> support single values 
        int , float , bool , complex
    2.Sequence -> collection of values -> every value has an index
        list(mutable), tuple (immutable), string , byte , bytearrray
    3.Set -> collection of values -> values dont have index 
        set , frozenset
    4.Dictionary -> dict -> key value pairs


    No size limit for any dataype in python -> use print(variable_Name.__sizeof__()) to know the memory consumed by the variable

    a= 125
    a= 200
    here now 125 is the garbage collected by PVM and deleted from the memory

    also we cant change the value of an already assigned variable -> assign it again somewhere to another variable -> because most datatypes are immutable
'''
'''
    Numeric Datatypes 
        1. int -> whole number -> 1, 2, 3, 4 -> positive and negative both 
        2. float -> decimal number -> 1.2, 3.4
            12.59 = 0.1259*10^2 => 0.1259E2 -> here 0.1259 is mantisa and 2 is the exponent
            12.59 = 1259/10^2 => 1259*10^-2 => 1259E.2
        3.Boolean -> True = 1, False = 0 -> both T and F should be capital 
        4. Complex -> a+ib -> a is real part and ib is imaginary part -> i=root of -1
            25+root-9 => 25+root-1*9 => 25+3root-1 => 25+i3
            x=complex(25,3)

            in python j is used instead of i => a+jb

            x=complex(3,5) => real 3 and imaginary 5 => 3+5j
            a.real => 3.0
            a.imag => 5.0

            x=complex(12) -> 12+0j
'''
'''
    Literals -> if the value of the variable is already written in the program it is called as literal 
    price = 250

        b=125092456 -> ok
        b=125_092_456 -> underscore is used to seperate values only for readable purposes -> ok
        comma is not allowed
        b = _234 -> NO

    Float literals
        a=123_459.45 -> OK
        e = 123_.45 -> NO -< underscore is just used to seperate values not to be used like this 

    Bool literals
        a=True
        b=False
    
    Complex literals
        a=5+6j 
        b+5_1+4_3j -> ok
    
    String literals -> single and double quotes both are allowed 
        a='John'
        name="Surbhi"
'''
'''
    price=input("Enter price")
    >> price
    jo bhi value input krega user hume usko convert krna hoga because string mai ayega and hume convert krna hoga

    int(price)
'''
'''
    Decimal(10)     Binary(2)      Octal(8)       Hexadecimal(16)
    0               0              0              0
    1               1              1              1
    2               10             2              2
    3               11             3              3
    4               100            4              4
    5               101            5              5
    6               110            6              6
    7               111            7              7
    8               1000           10             8
    9               1001           11             9
    10              1010           12             A
    11              1011           13             B
    12              1100           14             C
    13              1101           15             D
    14              1110           16             E
    15              1111           17             F
'''
'''
    a=10
    a=0b1010 -> binary mai written but 10 store hoga
        0b represents binary and 1010 represents the number
    a=0O12 -> octal mai written but 10 store hoga
        0O represents octal and 12 represents the number
    a=0XA -> hexadecimal mai written but 10 store hoga
        0X represents hexadecimal and A represents the number

    f=0b111.0b11 -> NO
    f=0b111.11 -> NO
    this method is only for integer literal not for float BUT 

    c=5+6j
    c=0b101+6j
    this method can be used for the real part in the complex number 
    print karwayenge toh c=10 value hi show hoga because it stores the value 10 in c , only the way of utility has changed
'''
'''
    price = input("Enter price: ")
    >> Enter price: 0b101
    >> price -> output will be '0b101' and not 5 because it takes input as a string

    BUT

    price = int(input("Enter price: "))
    if we typecast it to integer
    and we input the same value -> it will show the output as 5
'''
'''
    Base conversions

    bin() -> binary
    oct() -> octal
    hex() -> hexadecimal

    a=10
    x=bin(a) => gives binary form of a
    y=oct(a)
    z=hex(a)

    hex(255) -> works on numbers
    hex(True) -> works on bool => 0X1
    bin(12.5) -> ERROR -> float cant be interpreted as an integer , also complex number
'''
'''
    Type conversion
        1. Implicit -> done by python itself (automatically)
        2. Explicit -> done by the programmer 
            int(), float() , complex(), bool(), str()
        
    x = '0b1111'
    y=int(x , 2) -> this will convert into integer from binary

    a= '0XA2'
    b=int(a,16) -> Base has to be specified in these cases 

    Bool -> for anything -> true
            except empty string -> just quotes -> false


    Type casting        int     float   complex     bool    str

    int()               yes     yes     NO          yes     yes
    float()             yes     yes     NO          yes     yes
    complex()           yes     yes     yes         yes     yes
    bool()              yes     yes     yes         yes     yes
    str()               yes     yes     yes         yes     yes
'''
'''
    Operators 

    Type            Operator
    
    Arithmatic      + - * / ** // %
    Assignment      = += -= /= %= //= **=
    Unary minus     -10 -num
    Relational      == != > < >= <=
    Logical         and or not
    Boolean         T F
    Membership      in not in
    Bitwise         & | ~ ^ >> <<
    Identity        is isnot
    Special         + * []-slice []-range r/R %
    Mathematical    sqrt factorial sin cos...
'''
'''
    c = a+b 
    c-> operator
    a+b -> operands

    Precedence -> ke according operations perform hote hai
        If precendence of operator is same then assosiavity is seen
    Assosiavity -> L to R (mostly all) -> R to L (power/exponential)
'''

length = int(input("Enter length of rectangle: "))
#input function always gives string type of answer -> we need to typecast the value to the desried datatype if not string
breadth = int(input("Enter breadth of rectangle: "))
area = length*breadth
print("Area is",area)
#comma lagane se print statement mai bydefault aek space aa jaati hai
'''
    import math (first line of program)
            math.sqrt(9) -> square root of 9
                math sqrt cant get the value of negative numbers -> unless typecasted in to complex
            math.factorial(5) -> factorial of 5
            math.pi -> 3.14159
'''
'''
    Arithmatic operators on all dataypes

    Dataype         +       -       *       /       //      %       **   
    
    int             yes     yes     yes     yes     yes     yes     yes
    float           yes     yes     yes     yes     yes     yes     yes
    bool            yes     yes     yes     yes     yes     yes     yes
    complex         yes     yes     yes     yes     no     no       yes
    string          yes     no      yes     no      no     no       no
'''
'''
    int vs int and int vs float -> all ok
    integer vs bool -> 10+true => 11 and 10-False => 10 -> 10/False -> ERRROR
    integer vs complex -> all except // and %
    integer vs string -> * only => 2*'Hi' => HiHi
'''
'''
    float vs int , float , bool -> all ok
    float vs complex -> excpet // and % -> rest are ok
    float vs string -> NO
'''
'''
    bool vs int , float , bool -> all ok
    T+T = 2 , T-F = 1
    bool vs complex -> excpet // and % -> rest are ok -> False*(5+2j) = 0
    bool vs string -> only * => True*'Hi' gives -> HiHi
'''
'''
    complex vs int, float , bool , complex -> except // and % all ok
    complex vs string -> NO
'''
'''
    str vs int , bool -> * only
    str vs float , complex -> NO
    str vs str -> + only => 'Hello'+'Hello' = HelloHello
'''