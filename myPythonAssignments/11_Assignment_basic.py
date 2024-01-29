#Program to concatinate name and surname and print name and surnamee in lower case if name starts with b or print it in title 

a = input("Enter a name=");
b = input("Enter a surname=");

if (a[0] == "b"):
    print(a.lower() + " " + b.lower());
else:
    print(a.title() + " " + b.lower());

"""
c = input("Enter name and surname=").strip().replace(" ","").lower();
if(c[0]=='b'):
    print(c);
else:
    print(c.title());
"""



