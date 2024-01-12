
number = input("Enter a number: ")

def reverse(n, partial=0):
    if n == 0:
        return partial
    return reverse(n // 10, partial * 10 + n % 10)

trial = int(number)
if reverse(trial) == trial:
    print("It's a Palindrome!")
else:
    print("It's not a Palindrome!")