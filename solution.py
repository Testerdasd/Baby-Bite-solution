input1 = input()
input2 = input()
number = 0
input2 = input2.split(" ")
for i in range(int(input1)):
    i=i+1
    if str(i) != input2[i-1]:
        if input2[i-1] == "mumble":
            input2[i-1] = i
        else:
            print("something is fishy")
            raise SystemExit
if len(input2) != int(input1):
    print("Something is fishy!")
else:
    print("Make sence")