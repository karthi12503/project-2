
def number():
     number=str(input("enter the number:"))
     reverse=number[::-1]
     if number == reverse:
           print("The number",number,"is a PALINDROME")
     else:
  	     print("It is not a PALINDROME")
number()
while True:
	choise = int(input("If you want to use it again press '1' or press anyother number"))
	if choise == 1:
		number()
	else:
		print("THANK YOU (^_^)")
		break

