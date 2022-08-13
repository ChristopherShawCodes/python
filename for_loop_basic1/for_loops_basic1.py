from ast import Continue


for i in range(0,151):
    print(i)

for m in range(5,1000,5):
    print(m)


for i in range(0,101):
    if (i % 10 == 0):
        print('Coding Dojo')
    elif (i % 5 == 0):
        print('Coding')
    else:
        print(i)

start = 1
end = 500000

result=0

for x in range (start,end):
    if(x % 2 == 1):
        result=result+x
print(result)


for m in range(2018,0,-4):
    print(m)


lowNum = 1
highNum = 42
mult = 6

for i in range (lowNum,highNum,mult):
    print(i)




