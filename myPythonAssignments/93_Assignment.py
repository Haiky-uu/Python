# numbers and alphabets: assign 3 alphabets for each digit between 0 and 9.
# Write a program to write all possible
# codes that can be generated for any user entered number.
# For example: 1 - a,b,c and 2 - d,e,f then number 12 can
# be made as any of the codes: ad,ae,af,bd,be,bf,cd,ce,cf.

def letter(words: dict, ip):
       wordLst = []
       if ip>=10:
              newLst = words[ip%10]
              print(newLst)
              recLst = letter(words,ip//10)
              for w1 in recLst:
                     print(w1)
                     for w2 in newLst:
                            wordLst.append(w1+w2)
              return wordLst

       else:
              return words[ip]


dic = {0:['a','b','c'],1:['d','e','f'],2:['g','h','i'],3:['j','k','l'],4:['m','n','o'],
       5:['p','q','r'],6:['s','t','u'],7:['v','w','x'],8:['y','z','A'],9:['B','C','D']}
#ip = str(input("Enter a number: "))
print(letter(dic,132))



