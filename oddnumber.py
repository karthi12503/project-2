lastnumber=int(input("enter the last number of series ="))
print("The series is")
for number in range(1,lastnumber+1):
	print(number)
sum=0
for oddsum in range(1,lastnumber+1,2):
	sum+=oddsum
print("The sum of odd number of the series=",sum)