val1=int(input("Enter your frist value :"))
val2=int(input("Enter your second value :"))
operator=input('enter your operator')
if operator=='+':
    val=val1+val2
    print(val,'answer')
elif operator=='-':
    val=val1-val2
    print(val,'answer')

elif operator=='*':
    val=val1*val2
    print(val,'answer')
elif operator=='/':
    val=val1 / val2
    print(val,'answer')
elif operator=='*2':
    val=val**val2
    print(val,'answer')
else:
    print("your are not actual value opertaor")