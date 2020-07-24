#create a nested for loop
#sequence [0,5]

numbers = range(0,5)

for i in range(6):
  print("outer loop | i = " + str(i))

  for j in range(6):
    print("inner loop | i = " + str(i) + " | j = " + str(j))


numbers = range(0,10)

for i in range(10):
  print("outer loop | i = " + str(i))

  for j in range(10):
    print("inner loop | i = " + str(i) + " | j = " + str(j))


numbers = range(0,8)

for i in range(8):
  print("outer loop | i = " + str(i))

  for j in range(8):
    print("inner loop | i = " + str(i) + " | j = " + str(j))
