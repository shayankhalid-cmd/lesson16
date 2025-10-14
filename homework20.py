test_dict = {'condingal': 6, 'is' : 6, ' best': 6, ' for' : 6,'coding' : 1}
print("the original dictonairy:" + str(test_dict))
k = 6
res = 0
for key in test_dict:
    if test_dict[key] == k:
        res = res+1
print("frequency of k is" + str(res))