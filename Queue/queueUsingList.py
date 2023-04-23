queue = []

def addElement():
    element = int(input('Enter an element to add:'))
    queue.append(element)
    print(element,'Added to Queue')
    print(queue)
def removeElement():
    if not queue:
        print('The Queue id empty')
    else:
        element = queue.pop(0)
        print(element,'Removed from Queue')
while True:
    choice =int(input("Enter the choice 1-add ,2-remove ,3-Quit:"))
    if choice == 1:
        addElement()
    elif choice == 2:
        removeElement()
    elif choice == 3:
        break
    else:
        print('Enter a valid option')
    