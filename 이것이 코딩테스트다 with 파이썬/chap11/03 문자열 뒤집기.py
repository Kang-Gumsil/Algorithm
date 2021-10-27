s = input()

now = s[0]
index = 0
count = [1, 0]

for i in range(1, len(s)):
    if now != s[i]:
        now = s[i]
        index = (index + 1) % 2
        count[index] += 1

print(min(count))
