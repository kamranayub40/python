def fu_up_lo(str):
    up_count=0
    lo_count=0
    for i in  str:
        if i.isupper():
            up_count+=1
        else:
            lo_count+=1
    print(f"the upper case latter is : {up_count} ")
    print(f"The lower case latter is : {lo_count}")
fu_up_lo("KamRan AyoUb")