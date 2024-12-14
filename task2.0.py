with open('E:/Arshad/Semester-7/input.txt') as file:
     numbers=[int(line.strip())for line in file]
total_sum=sum(numbers)
print("The sum of the integers is:",total_sum)
