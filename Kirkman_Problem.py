print ("Program ")

l_girls = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
l_days = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']



for i in l_days:
    if (i == "Mon"):
        for girls in l_girls[1:3]:
            print (girls)
