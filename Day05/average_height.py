# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
# Can't use len()
# Can't use sum()
# Must use for loops

agg_height = 0
count_height = 0

for value in student_heights:
    agg_height += value
    count_height += 1

#print(agg_height)      #DEBUG
#print(count_height)    #DEBUG

print(round(agg_height / count_height))


