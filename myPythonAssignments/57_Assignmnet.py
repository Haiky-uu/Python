# read symbol_day_close file, store all close prices (only for one symbol) in a list and
# find peaks in the list

with open('./trident_stocks.csv') as f:

    lst = []
    next(f)
    for line in f:
        lst.append(float(line[44:49]))
    print(lst)
    peak = []
    valley = []
    peaks = ()
    acend = 0
    for ele in range(len(lst)-1):
        if (lst[ele]<lst[ele+1]):
            if not acend:
                valley.append(lst[ele])
            acend = 1
        else:
            if acend == 1:
                peak.append(lst[ele])
                acend =0

    peaks =[]
    for idx in range(len(lst)-1):
        if lst[idx] > lst[idx-1]:
            if lst[idx] > lst[idx+1]:
                peaks.append(lst[idx])
    print(peaks)

    print("peaks",peak)
    print("Valleys",valley)







