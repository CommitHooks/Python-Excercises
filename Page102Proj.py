#! python3

def list_to_string(myList):
    length = len(myList)
    #print('length is ' + str(length))
    myStr = ''
    if length > 0:
        if length == 1:
            myStr = str(myList[0])
        elif length > 1:
            for i in range(length):
                if i < length - 1:
                    myStr += str(myList[i]) + ', '
                else:
                    myStr += 'and ' + str(myList[i])
        print(myStr)

myList = ['apples', 'bananas', 'tofu', 'cats', 'hats', 'Dane']
#myList = ['Dane']
list_to_string(myList)
