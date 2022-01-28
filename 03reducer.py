#Mackenzie Bishop
#03 Reducer

f = open("s.txt","r")
o = open("r.txt", "w")

thisKey = ""
thisValue = 0.0

for line in f:
  data = line.strip().split('\t')
  store, amount = data
  if store != thisKey:
    if thisKey:

      # output the last key value pair result
      o.write(thisKey + '\t' + str(thisValue)+'\n')

    # start over when changing keys
    thisKey = store
    thisValue = 0.0

  # apply the aggregation function
  thisValue += float(amount)

# output the final entry when done
o.write(thisKey + '\t' + str(thisValue)+'\n')

f.close()
o.close()