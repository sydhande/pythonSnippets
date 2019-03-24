Books= []
Borrower=[]
Checkout=[]
input_str = input()
if input_str == "Books":
    while True:
        input_str = input()
        if input_str == "Borrowers":
            break
        else:
            Books.append(input_str)
while True:
    input_str = input()
    if input_str == "Checkouts":
        break
    else:
        Borrower.append(input_str)
while True:
    input_str = input()
    if input_str == "EndOfInput":
        break
    else:
        Checkout.append(input_str)
book_list=[]
borrower_list=[]
checkout_list=[]
for item in Books:
    x = item.split("~")
    book_list.append(x)
for item in Borrower:
    x = item.split("~")
    borrower_list.append(x)
for item in Checkout:
    x = item.split("~")
    checkout_list.append(x)
ans=[]
y=[]
for item in checkout_list:
    for x in borrower_list:
        if item[0] in x[0]:
            y.append([item[2],"~",x[1]])


i=0
for item in checkout_list:
    for x in book_list:
        if item[1] in x[0]:
            y[i].append('~'+item[1]+"~"+x[1])
            i += 1
ans = sorted(y, key=lambda x: x) 


for item in ans:
    z = ''.join(item)               
    print(z)

