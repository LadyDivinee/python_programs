#ranger 1-100
for i in range (0, 101):
#check what number ends in 0 or 5
    if i % 10 ==0 or i % 10 == 5:
        continue
    print(i)