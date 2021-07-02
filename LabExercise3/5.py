'''Q.No.5 Write a function calledshow_stars(rows).Ifrowsis 5, it should print thefollowing:
***************'''

def show_stars():
    lst='soft'
    sum = 0
    for i in range(1,6):
        if i==5:
            sum = sum+i
            print(lst)
show_stars()
