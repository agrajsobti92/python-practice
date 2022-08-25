def main():
    s = input("Enter a string of brackets: ")
    print(func(s))


def func(s):
    d = {'(': ')', '{': '}', '[': ']'}

    stack = []

    for i in s:

        if i in d:
            stack.append(i)

        elif len(stack) == 0 or d[stack.pop()] != i:
            return False

    return len(stack) == 0


main()

# s = 'ahsjdbvnvc'

# l = []
# for i in s:
#     l.append(i)

# print("Initial list={}".format(l))

# for i in range(len(l)):
#     print("popping " + l.pop())
#     print("updated list = {}".format(l))
