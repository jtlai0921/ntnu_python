employees = {
    'Tom':[70000, 1, {'m':2.5}],
    'Mary':[80000, 2, {'m':1.5}],
    'John':[55000, 2, {'m':3}],
}
for key in employees:
    print('%s 的資料 %s' % (key, employees[key]))
print('---------------------------------------------')
for key in employees:
    if(employees[key][1] == 2) :
        print('%s 的資料 %s' % (key, employees[key]))
print('---------------------------------------------')