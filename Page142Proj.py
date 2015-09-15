#! python3

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carrol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

numOfLists = len(tableData)
numOfListItems = len(tableData[0])
colWidth = [0] * numOfLists

for i in range(numOfLists):
    for j in range(numOfListItems):
        if colWidth[i] < len(tableData[i][j]):
            colWidth[i] = len(tableData[i][j])

justStr = ''
for j in range(numOfListItems):
    for i in range(numOfLists):
        justStr += tableData[i][j].rjust(colWidth[i]) + ' '
    justStr += '\n'


print(justStr)
