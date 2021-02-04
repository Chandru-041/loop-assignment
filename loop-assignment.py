number = 0
count = 0
while True:
    val = input("Enter a number: ")
    if val == 'done':
        break
    try:
        new_val = float(val)
    except:
        print("Invalid Number")
        continue
    count = count + 1
    number = number + new_val
    
sum = number
avg = sum/count
print(sum)
print(count)
print(avg)
            
        
            
    
