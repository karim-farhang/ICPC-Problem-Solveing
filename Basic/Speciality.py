for _ in range(int(input())):
    Setter, Tester, Editorialist = map(int, input().split())
    if max(Setter, Tester, Editorialist) == Setter:
        print('Setter')
    elif max(Setter, Tester, Editorialist) == Tester:
        print('Tester')
    else:
        print('Editorialist')
