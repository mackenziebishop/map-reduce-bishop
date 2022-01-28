# Mackenzie Bishop
# Example mapper

f = open("purchases.txt","r")  # open file, read-only
o = open("01.txt", "w") # open file, write
for line in f:  
    dataList = line.strip().split("    ") 
    if len(dataList) == 6:
        date, time, location, dept, amount, payType = dataList  #assign names
        o.write("{0}\t{1}\n".format(location, amount))
f.close()
o.close()