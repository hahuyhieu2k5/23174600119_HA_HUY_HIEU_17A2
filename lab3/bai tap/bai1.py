n=int(input("nhập số nguyên n: "))
S1=0
for i in range(1,n+1):
    if n<=0:
       print ("Vui lòng nhập lại")           
    else:
        S1+=i
print("Tổng của S1 là: ",S1)
#b.
S2=0
for i in range(1,n+1):
    if n<=0:
       print ("Vui lòng nhập lại")
    else:
       S2+=1/i
print("Tổng của S2 là: ",S2)            
#c.
import math
S3=0
for i in range(1,n+1):
    if n<=0:
        print("Vui lòng nhập lại")
    else:
        S3+=1/math.sqrt(i*2)
print("Tổng của S3 là: ",S3)
#d.
S4=0
for i in range(1,n+1):
    if n<=0:
        print("Vui lòng nhập lại") 
    else:
        S4+=((-1)**(i+1))/i
print("Tổng của S3 là: ",S4)                     
