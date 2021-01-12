#--- pos time functions ---

# After generating the data from write_grav_calc.py, we can determine the position
# of the earth at any point in the time interval.


import ast
fyle = open(input('Enter file name : '), 'r')
print('Reading x')
x = ast.literal_eval(fyle.readline())
print('Done reading x')
print('Reading y')
y = ast.literal_eval(fyle.readline())
print('Done reading y')
print('Reading dx_dt')
dx_dt = ast.literal_eval(fyle.readline())
print('Done reading dx_dt')
print('Reading dy_dt')
dy_dt = ast.literal_eval(fyle.readline())
print('Done reading dy_dt')
print('Reading d2x_dt2')
d2x_dt2 = ast.literal_eval(fyle.readline())
print('Done reading d2x_dt2')
print('Reading d2y_dt2')
d2y_dt2 = ast.literal_eval(fyle.readline())
print('Done reading d2y_dt2')
print('Reading time stamps')
time_stamps = ast.literal_eval(fyle.readline())
print('Done reading time stamps')



def binary_search(arr, lower, high, x):
    mid = (high + lower) // 2
    if lower <= high:   
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, lower, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return mid

def func_r(t):
    p = binary_search(time_stamps, 0, len(time_stamps) - 1, t)
    if time_stamps[p] == t:
        return (x[p], y[p])
    else:
        def func_x(t_var):
            return (x[p + 1] - x[p])/(time_stamps[p + 1] - time_stamps[p]) * (t_var - time_stamps[p]) + x[p]

        def func_y(t_var):
            return (y[p + 1] - y[p])/(time_stamps[p + 1] - time_stamps[p]) * (t_var - time_stamps[p]) + y[p]
        return (func_x(t), func_y(t))

while True:
    t_val = float(input('Enter time : '))
    print(func_r(t_val))