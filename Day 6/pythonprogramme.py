#programm takes value n from the user:
value = int(input("Enter the number of iterations you would like"))
results = 1
for i in range (1,value+1):

    results =results*i
    i=i+1
print(results)




