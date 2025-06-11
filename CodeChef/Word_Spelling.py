t = int(input().strip())
re = []
while t > 0:
    words = input().strip().split(' ')
    main_word = words[0]
    words.remove(main_word)
    can = 'Yes'
    for i in main_word:
        if i in words:
            words.remove(i)
        else:
            can = 'No'
            break
    re.append(can)
    t -= 1

for i in re:
    print(i)
