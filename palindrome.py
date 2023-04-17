num = input("Enter a number: ")
n = len(num)
is_palindrome = True
for i in range(n // 2):
    if num[i] != num[n - i - 1]:
        is_palindrome = False
        break
if is_palindrome:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")