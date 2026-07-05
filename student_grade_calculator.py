print("===== Student Grade Calculator =====")

name = input("Enter Student Name: ")

tamil = int(input("Enter Tamil Mark: "))
english = int(input("Enter English Mark: "))
maths = int(input("Enter Maths Mark: "))
science = int(input("Enter Science Mark: "))
social = int(input("Enter Social Mark: "))

total = tamil + english + maths + science + social
average = total / 5

print("\nStudent Name:", name)
print("Total Marks:", total)
print("Average:", average)

if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "Fail"

print("Grade:", grade)
