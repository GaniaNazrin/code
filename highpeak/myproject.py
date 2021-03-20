input_file =open("sample_input.txt","r")
output_file = open("output.txt","w+")
goodies={}
output_list=[]
for f in input_file:
    toRead_index_price=f.index(":")
    print(f[toRead_index_price+1:].strip())
    print(f[:toRead_index_price])
    goodies[f[:toRead_index_price]]=f[toRead_index_price+1:].strip()
print(goodies) 
list_prices=list(goodies.values())
list_prices=[int(i)for i in list_prices]
list_prices.sort(reverse=True)#sort price in reverse
print(list_prices)
n=int(input("Enter the number of employees="))
l=(len(list_prices)-n)

for i in range(l):
    max_price=list_prices[i]
    min_price=list_prices[n+i]
    if i == 0:
        diff=max_price-min_price
        idx_choosen=i
    elif (max_price-min_price)<diff:
        diff=max_price-min_price
        idx_choosen=i

choosen_prices=list_prices[idx_choosen:n+idx_choosen]
diff=max(choosen_prices)-min(choosen_prices)
print("difference between highest and lowest price=",diff)
count=0
for key,value in goodies.items():
    list_prices[count]
    print(value)
    if int(value)in choosen_prices and count<n:
        str1=key+": "+value
        output_list.append(str1)
        count=count+1
        print(str1)
output_file.write("The goodies selected for distribution are: ")
output_file.write("\n")
output_file.write("\n")
for i in output_list:
    output_file.write(i)
    output_file.write("\n")
    output_file.write("\n")
output_file.write("And the difference between the choosen goodies with highest price and the lowest price is "+str(diff))
input_file.close()
output_file.close()
