#Check Prime

checkPrime=int(input("Enter Value to check prime"))
count=0




for i in range(1,1+checkPrime):
    if (checkPrime == 1):
        print("not prime")
        checkPrime=0
        break
    elif(checkPrime%i==0):
        count=count+1

if count>2:
    if checkPrime==1:
        print(checkPrime,"is not Prime")
elif(count==1):

    print(checkPrime,"is prime")