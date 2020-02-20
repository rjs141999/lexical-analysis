keywords=["auto","break","case","char","const","continue","default","do","double","else",
          "enum","extern","float","for","goto","if","int","long","register","return","short",
          "signed","sizeof","static","struct","switch","typedef","union","unsigned","void","volatile","while"]
f = open("demo.txt", "r")
file=f.read()
oper="+-=!%^&*"
file=file.split()
for i in file:
    if i in oper:
        print(i,'is operator')
    elif i in keywords:
        print(i,"is keyword")
    elif i.isalpha():
        print(i,"is indentifier")
    elif i.isnumeric():
        print(i,"is numeric value")
