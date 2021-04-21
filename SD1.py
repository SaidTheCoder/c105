import csv
import math

with open("data1.csv",newline='') as f:
    reader=csv.reader(f)
    file_data=list(reader)

data=file_data[0]

#step 1 Finding mean
def mean(data):
    n=len(data)
    total=0
    for x in data :
        total+=int(x)

    mean= total/n
    return mean

#step 2 squaring and getting the values
 
squared_list=[]
for number in data:
    a=int(number)-mean(data)
    a=a ** 2
    squared_list.append(a)

#step 3 get the sum of all of the squared data

sum=0
for i in squared_list:
    sum=sum+i

#step 4 dividing by the sum of the total values

result=sum/(len(data)-1)

#last step find the square root and get the SD

std_deviation=math.sqrt(result)

print("the standard deviation of the givin data is:  ",std_deviation)