str1= input("Enter a string:")
char=str1[0]
str2=char
count=0
for i in range(1,len(str1)):
    if(char==str1[i]):
        count+=1
    else:
        str2=str2+str1[i]
        char=str1[i]
print( str2 + str(count))
    
