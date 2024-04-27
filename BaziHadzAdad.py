import random
print("adad bein 0 ta 10 hast")
adad=random.randint(0,100)
# print(adad)
t=0
for i in range(6):
    adadKarbar=int(input("adad bede :"))
    t+=1
    if adadKarbar==adad:
        print("dorost hadz zadi")
    elif adadKarbar>adad and adadKarbar<=11:
        print("ghalat hadz zadi adadi ke entekhsb kardi bozorg tar az adad hast")
    elif adadKarbar<adad and adadKarbar>=0:
        print("ghalat hadz zadi adadi ke entekhsb kardi kochek tar az adad hast")
    else:
        print("az range kharej hast")
    print(i)
