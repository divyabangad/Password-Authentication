
while True:
    print("\t1. Your password must contain a capital alphabet.")
    print("\t2. Your password must contain a small alphabet.")
    print("\t3. Your password must contain a digit.")
    print("\t4. Your password must contain a special character such as .,_,@,#,%,&,(,) and %.")

    print("\nEnter your Password:")
    pw=input()

    flag1=0
    flag2=0
    flag3=0
    flag4=0

    for ch in pw:
        if(ch>'A' and ch<'Z'):
            flag1=1
        elif(ch>'a' and ch<'z'):
            flag2=1
        elif(ch>'0' and ch<'9'):
            flag3=1
        elif(ch=='.' or ch=='_' or ch=='@' or ch=='#' or ch=='%' or ch=='&' or ch=='(' or ch==')' or ch=='%'):
            flag4=1

    if(flag1==0 or flag2==0 or flag3==0 or flag4==0):
        print("\nInvalid Password..!!\nPlease make sure all the requirements are met.\n")
    else:
        print("Entered password is Valid.")
        break





