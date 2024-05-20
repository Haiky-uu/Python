# 119 read json file and print all lines, search specific tags

import json

def jsonr(path):
    with open(path) as f:
        data = json.load(f)
        print(data)
        print(data.keys())
        print(data.values())
        for vals in data.values():
            print(vals)
def main():
    path = './json2.json'
    jsonr(path)

if __name__ == '__main__':
    main()
