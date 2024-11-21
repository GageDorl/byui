num = 1
num_list = []
print('Enter a list of numbera, type 0 when finished.')
while num !=0:
    num = int(input("Enter number: "))
    if num != 0:
        num_list.append(num)
sum=0
count=0
largest = 0
smallest = 1000000000
sorted_list=num_list
sorted_list.sort()
for i,num in enumerate(num_list):
    sum+=num
    count+=1
    if num>largest:
        largest = num
    if num>0 and num<smallest:
        smallest = num


average = sum/count
print(f'The sum is: {sum}\nThe average is: {average}\nThe largest number is: {largest}\nThe smallest positive number is: {smallest}')
print('The sorted list is: ')
for num in sorted_list:
    print(num)