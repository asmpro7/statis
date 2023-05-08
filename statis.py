# Statis script
# made by asmpro
# date: 7/5/2023
# TG:@asmprotk

import statistics

input = input("enter value: ").split(",")
value = []
index = []

for num in input:
    value.append(int(num))

for num in sorted(value):
    index.append(str(num))

print("Sorted numbers: " + ",".join(index))
print("n: ", str(len(value)))
print("Mean: ", statistics.mean(value))

median = statistics.median(value)

print(f"Median(Q2): {median}")
print("Mode: ", statistics.mode(value))
print("Minimum: ", index[0])
print("Maximum: ", index[-1])
print("Range: ", str(int(index[-1])-int(index[0])))

Q1_list = []
Q3_list = []
for number in value:
    if number < median:
        Q1_list.append(number)
    elif number > median:
        Q3_list.append(number)

q1 = statistics.median(Q1_list)
print("Q1: ", q1)

q3 = statistics.median(Q3_list)
print("Q3: ", q3)

print("IQR: ", str(float(q3)-float(q1)))

print("Variance: ", statistics.pvariance(value))
print("Standard deviation: ", statistics.pstdev(value))
