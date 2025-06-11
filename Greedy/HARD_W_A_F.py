t = int(input())
while t > 0:
    boold, armor = map(int, input().split(' '))
    count = 0
    water = (armor / boold)
    fire = (boold / armor)
    while boold >= 0 or armor >= 0:
        print(water)
        print(fire)
        if water > fire:
            boold -= 5
            armor -= 10
        if fire > water:
            boold -= 20
            armor -= 5
        else:
            boold += 3
            armor += 2
        count += 1
    print(count)
    t -= 1
