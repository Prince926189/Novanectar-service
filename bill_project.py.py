print("Bill generator")
print(" ")
num = int(input("No. of item : "))
print(" ")

sam = 0
for i in range(1 , num+1):
    a = input("Item : ")
    b = int(input("Quantity : "))
    c = int(input("Price : "))
    
    if i != num:
        print(" ")
        print("Next")
        print(" ")
    m = b * c 
    sam = sam + m 

print(" ")
print("Total Amount : " ,sam)
