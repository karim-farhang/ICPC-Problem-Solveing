t = int(input().strip())
rt = []
while t > 0:
    time_of_one_Swing, total_swing, clean_up_time, total_tree = [int(x) for x in input().strip().split(' ')]
    time = (time_of_one_Swing * total_swing + clean_up_time) * total_tree
    rt.append(time)
    t -= 1
for i in rt:
    print(i)
