#  build small application to query json file
import json as js

def jSon(file):

    # opening a file from jason
    with open(file) as f:
        data = js.load(f)
        print(data.keys())
        print(data['quiz']['sport'])
        user = input("Enter thr correct team in nba: ")
        cnt = 0
        if user == data['quiz']['sport']['q1']['answer']:
            print('Correct')
            cnt+=1
        else:
            print("Wrong")

        user2 = input("Now enter what is 5+7 will be: ")
        if user2 == data['quiz']['maths']['q1']['answer'] == '12':
            print(True)
            cnt+=1
        else:
            print(False)

        if cnt == 2:
            print('You win')
        else:
            print("You lose or get only one correct ans")


    # Convert python to jason
    #
    # adic = {'name':'ron','age':55,'occupation':'fund_manager','country':'poland'}
    # print(adic)
    #
    # x =  js.dumps(adic)
    # print(x)
    #
    ####


def main():
    path = './json2.json'
    jSon(path)

if __name__ == '__main__':
    main()
