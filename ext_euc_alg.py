import subprocess
subprocess.call('clear', shell=True)

print("\n\n\n\n\nEnter 2 integers for the Extended Euclidian Algorithm.\n")

num1 = 0
num2 = 0
while ((num1 == 0) or (num2 == 0)):
    try:
        num1 = int(input("Please enter number 1:\t"))
        num2 = int(input("Please enter number 2:\t"))
    except TypeError:
        print("Enter integers.")

if (num1 < num2):
    num1, num2 = num2, num1

print("\ni\t", "q\t", "r\t", "s\t", "t\t")
i = [0,1]
q = [0,0]
r = [num1, num2]
s = [1,0]
t = [0,1]
c = 1

while ((rtmp := (r[c-1] - ((qtmp := (r[c-1] // r[c]))*r[c]))) > 0):
    i.append(c+1)
    q.append(qtmp)
    r.append(rtmp)
    s.append(s[c-1] - (q[c+1]*s[c]))
    t.append(t[c-1] - (q[c+1]*t[c]))
    c += 1

for n in i:
    print(i[n], "\t", q[n], "\t", r[n], "\t", s[n], "\t", t[n])

print("\nYour GCD is: ", (s[i[-1]]*num1)+(t[i[-1]]*num2), "\n\n")
