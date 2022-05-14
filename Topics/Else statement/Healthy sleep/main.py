A = int(input())
B = int(input())
hours_of_sleep = int(input())
if hours_of_sleep < A or hours_of_sleep > B:
    if hours_of_sleep < A:
        print('Deficiency')
    else:
        print('Excess')
else:
    print('Normal')
