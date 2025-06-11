# --- rabin karip algorithm ---
s = input()
s1 = input()
for i in range(len(s)):
    if s1 == s[i:len(s1)+i]:
        print(i)