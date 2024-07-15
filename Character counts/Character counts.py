strings=[]
while True:
    string=input("Enter  a string(or'exit' to quit):")
    if string=='exit':
      break
    strings.append(string)
    counts={}
for string in strings:
        for char in string:
              counts[char]=counts.get(char,0)+1
        print("Character counts:")
        for char,count in counts.items():
                print(char,":",count)
