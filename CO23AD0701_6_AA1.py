gender = input("Enter your gender")
age = int(input("Enter your age"))
if age > 22:
	if gender == "Male":
		print("Male Employee")
	else:
		print("Female Employee")
else:
	if gender == "Male":
		print("Male Intern")
	else:
		print("Female Intern")
