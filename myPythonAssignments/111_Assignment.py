# 111 build employee hierarchy tree (using file employeeManager.txt) and write a program to traverse the
# tree in breadth first search
class EmpHierarchy:

    def __init__(self,e_id,name,age,ht,sal,p_id):
        self.e_id = e_id
        self.name = name
        self.age = age
        self.ht = ht
        self.sal = sal
        self.p_id = p_id

    def child(self,e1,parentDict,childDict):
        #print(parentDict)

        # if e1.p_id == -1000:
        #     print("Root")

        if e1.p_id not in childDict:
            c_list = []
            c_list.append(e1)
            childDict[e1.p_id] = c_list
            #print(e1.p_id, e1.e_id)
            #print(c_list)
        else:
            childDict[e1.p_id].append(e1)

        return childDict


def addNodeToLevelDict(nd, levelDict, l):
    if (l in levelDict):
        nodeList = levelDict[l]
        nodeList.append(nd)
        levelDict[l] = nodeList
    else:
        nodeList = []
        nodeList.append(nd)
        levelDict[l] = nodeList


def browseTreeAddConfLevelDict(node, memberDict, childDict, levelDict, lvl):
    addNodeToLevelDict(node, levelDict, lvl)
    if (node.e_id in childDict):
        childList = childDict[node.e_id]
        for child in childList:
            browseTreeAddConfLevelDict(child, memberDict, childDict, levelDict, lvl + 1)

def main():

    file = './empManager_csv.csv'
    parantTree = {}
    childTree = {}
    lvlDict = {}
    root_node = ''
    with (open(file) as f):
        next(f)
        for line in f:
            #print(line,end="")
            e_id,name,age,ht,sal,p_id = line.strip().split(',')
            e1 = EmpHierarchy(int(e_id),name,age,ht,sal,int(p_id))
            parantTree[int(e_id)]=e1

            childDict = e1.child(e1,parantTree,childTree)
            childTree = childDict
            if e1.p_id == -1000:
                root_node = e1

        node = -1000
        startNode = childDict[node]
        #print(startNode[0])
        browseTreeAddConfLevelDict(root_node,parantTree,childTree,lvlDict,0)

    for lvl,lst in lvlDict.items():
        print(lvl,':',lst)

    #print (parantTree)


if __name__ == '__main__':
    main()


