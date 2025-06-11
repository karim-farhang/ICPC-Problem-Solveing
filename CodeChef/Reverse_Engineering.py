tc = int(input().strip())
rtc = []
while tc > 0:
    inp = ' '
    shap = []
    count = 0
    while inp != '':
        inp = input()
        if inp == '':
            break
        else:
            shap.append(list(inp))
            count += 1
    shapType = ''
    shapStyle = shap[-1][-1]
    siz = 0
    if shap[0][0] == ' ':
        shapType = 'Triangle'
        siz = int((len(shap) * len(shap[0])) * 0.5)

    elif count == 1:
        shapType = 'Line'
        siz = int(len(shap[0]))
    else:
        shapType = 'Rectangle'
        siz = int((len(shap) * len(shap[0])))

    if shapStyle == 'C':
        shapStyle = 'Clay'
    elif shapStyle == 'W':
        shapStyle = 'Wood'
    else:
        shapStyle = 'Metal'
    rtc.append(str(shapType) + '; ' + str(siz) + '; ' + str(shapStyle))
    tc -= 1
for i in rtc:
    print(i)
