# read symbol_day_close file, store all close prices (only for one symbol) in a list and
# find troughs in the list

with open('./trident_stocks.csv') as f:

    lst = []
    next(f)
    for line in f:
        lst.append(float(line[44:49]))
    print(lst)

    peaks = []
    valley = []
    ascend = True
    for idx in range(len(lst)-1):
        if lst[idx]< lst[idx+1]:
            if not ascend:
                valley.append(lst[idx])
            ascend = True
        else:
            if ascend:
                peaks.append(lst[idx])
                ascend = False
    print("peaks",peaks)
    print("valleys",valley)
    


