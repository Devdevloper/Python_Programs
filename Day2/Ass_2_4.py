max = int(input(" Enter any number : "))
no = 1
print("Prime numbers between ",1, "to", max," are : ")

while(no <= max):
    count=0
    i=2

    while(i<=no//2):
        if(no % i==0):
            count=count+1
            break
        i=i+1

    if(count == 0 and no!=1):
        print("%d" %no, end=' ')
    no = no+1