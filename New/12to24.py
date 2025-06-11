
ts = int(input())
for _ in range(ts):
    st = input().split(':')
    h = int(st[0])
    org = h
    m = 0
    hours = ['12', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11']
    ampm = ''
    h = hours[h % 12]
    if st[1].count('am') == 1:
        ampm = 'am'
        m = int(st[1].replace('am', ''))
    if st[1].count('pm') == 1:
        m = int(st[1].replace('pm', ''))
        ampm = 'pm'
    if ampm == '':
        m = int(st[1])
        if org > 12 and org != 24:
            ampm = 'pm'
        else:
            ampm = 'am'
    if m < 9:
        m = '0' + str(m)
    result = h + ":" + str(m) + ampm
    print(result)
