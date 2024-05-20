#  build small application to query yaml file
import yaml


def Yaml(file):
    cnt = 0
    for client in file.keys():
        vals = file[client]
        print("Company no:", cnt)
        for key,val in vals.items():
            if key == 'companySize' :
                if val >= 500:
                    print("--------TAX implemented------")
                else:
                    print("------No Tax------")

            print(key,':',val)

        print('--------------------------')
        cnt += 1


def main():
   path = './yaml_dict.yaml'
   with open(path, 'r') as f:
      data =  yaml.safe_load(f)
      Yaml(data)



if __name__ == '__main__':
    main()