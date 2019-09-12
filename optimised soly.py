length = input()
numbers = input()
numbers = numbers.split(" ")
onum = 0
if str(len(numbers)) != length:
    print("somethings fishy!")
    raise SystemExit
else:
    for i in range(len(numbers)):
        if str(numbers[0]) == "mumble":
            for x in range(len(numbers)-1):
                numbers[x] = numbers[x+1]
                length = int(length)-1
    for i in range(int(length)):
        if numbers[i] != onum:
            print("somethins fishy!")
            raise SystemError
print("Make sence")