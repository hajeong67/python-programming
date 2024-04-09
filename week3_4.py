a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cnt = [0, 2, 4, 6]
with open("homework4.txt", 'w') as file:
    file.writelines(str(a[i]*a[i]) + "\n" for i in cnt)
