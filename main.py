#create a nested for loop
#sequence [0,5]

numbers = range(0,5)

for i in range(6):
  print("outer loop | i = " + str(i))

  for j in range(6):
    print("inner loop | i = " + str(i) + " | j = " + str(j))