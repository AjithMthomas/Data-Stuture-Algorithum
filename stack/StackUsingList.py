stack=[]
def push():
    element = int(input('Enter the element to add:'))
    stack.append(element)
    print('added',element,'succesfully')
    print(stack)
def pop():
    
    element=int(input('enter and element to pop:'))
    stack.pop(element)
    print('removed',element,'succesfully')
    print(stack)

while True:
    choice =int(input('enter choice 1 for pop,2 for push,3 for quit:'))
    if choice >3:
        print('choose  valid option')
    if choice == 1:
        pop()
    elif choice ==2:
        push()
    else:
        break
