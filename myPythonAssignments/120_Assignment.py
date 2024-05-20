# read yaml file and print all lines, search specific tags
import yaml


def funYaml(sport,country):
    idx = 0
    user = str(input("Enter a sport name: "))
    for idx in range(0,len(sport)):
        if user == sport[idx]:
            print(country[idx])


def main():
    with open('./categories.yaml', 'r') as f:
        data = (yaml.safe_load(f))
        # print(data)
        # print(data.items())
        # print(data.keys())
        # print(data.values())

    sports = data['sports']
    country = data['countries']
    funYaml(sports,country)


if __name__ == '__main__':
    main()



