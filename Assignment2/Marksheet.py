sub1=int(input("Enter your English Marks :"))
sub2=int(input("Enter your Math Marks :"))
sub3=int(input("Enter your computer Marks :"))
sub4=int(input("Enter your chemistry Marks : "))
sub5=int(input("Enter your physics Marks :"))
obtained=sub1+sub2+sub3+sub4+sub5
print(obtained)

percent=obtained/500*100
print(percent)
if percent>=90:
    print("A1 grade")    
elif percent<90>=80:
    print("A grade")
elif percent<80>=60:
    print("B grade")
elif percent<60>=40:
    print("C grade")
else:
    print("Your fail")










# if percent>=90:
#     print("A1 grade")
# # elif percent<90>=80:
# #     print("A Grade")
# elif percent<80>=60:
#     print("B Grde")
# elif percent<60>=40:
#     print("C Grade")
# else percent<40>=30:

 