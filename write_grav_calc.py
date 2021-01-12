# --- My program ---
import time

end_time = 3600 * 24 * 365 * 2
time_inc = 3600 * 24 * 30

def generate_time(start, finish, increment):
    time_stamps = []
    curr = start
    s_0 = time.time()
    while curr <= finish:

        # This little snippet enables users to view the progrees
        # * Useful for larger time scales and smaller increments
        if time.time() - s_0 >= 1:
            s_0 = time.time()
            print('time stamp progress : {} %'.format(time_stamps[-1] / finish * 100)) # For when start is 0



        time_stamps.append(curr)
        curr += increment
    return time_stamps
print('Generating time stamps')
time_stamps = generate_time(0, end_time, time_inc)
print('Time stamps generated!')


def L(x, y):
    # This is the acceleration function
    G = 6.67430 * 10 ** (-11)
    m_2 = 1.989 * 10 ** (30)
    return -G * m_2 / ((x ** 2 + y ** 2) ** (3/2))

x = [151.97 * 10 ** (9)] # This is the initial x - position
y = [0] # This is the initial y - position
dx_dt = [0] # This is the initial velocity in the x - direction
dy_dt = [29318.75] # This is the initial velocity in the y - direction
d2x_dt2 = [L(x[0], y[0]) * x[0]] # This is the initial acceleration in the x
d2y_dt2 = [L(x[0], y[0]) * y[0]] # This is the initial acceleration in the y



from math import atan, pi

print('Generating position vectors')
s_0 = time.time()
path_len = 0
velocity_sum = 0
acceleration_sum = 0
for i in range(1, len(time_stamps)):

    if time.time() - s_0 >= 1:
        s_0 = time.time()
        print('position vectors progress : {} %'.format((i - 1) / len(time_stamps) * 100))


    x.append(dx_dt[i - 1] * (time_stamps[i] - time_stamps[i - 1]) + x[i - 1])
    y.append(dy_dt[i - 1] * (time_stamps[i] - time_stamps[i - 1]) + y[i - 1])
    dx_dt.append(d2x_dt2[i - 1] * (time_stamps[i] - time_stamps[i - 1]) + dx_dt[i - 1])
    dy_dt.append(d2y_dt2[i - 1] * (time_stamps[i] - time_stamps[i - 1]) + dy_dt[i - 1])
    d2x_dt2.append(L(x[i], y[i]) * x[i])
    d2y_dt2.append(L(x[i], y[i]) * y[i])
    
    # Path length calculation
    path_len += (((x[i] - x[i - 1]) ** 2 + (y[i] - y[i - 1]) ** 2) ** 0.5)  / ((x[i] ** 2 + y[i] ** 2) ** 0.5) * 180 / pi
    velocity_sum += (dx_dt[i] ** 2 + dy_dt[i] ** 2) ** 0.5
    acceleration_sum += (d2x_dt2[i] ** 2 + d2y_dt2[i] ** 2) ** 0.5
print('Generated position vectors!')

# path_len = sum([((x[i] - x[i - 1]) ** 2 + (y[i] - y[i - 1]) ** 2) ** 0.5 for i in range(1, len(x))])


# --- Write data into text file plan ---
# File naming format (time interval)_(time inc)_sun_earth_(init x, init y)_(init vx, init vy)
# In text file :
# first line is x, second line is y
# third line is dx_dt, fourth line is dy_dt
# fifth line is d2x_dt2, sixth line is d2y_dt2
# seventh line is time stamps

print('Writing to output file')
fiyl = open('{}_{}_sun_earth_{}_{}.txt'.format(end_time, time_inc, (x[0], y[0]), (dx_dt[0], dy_dt[0])), 'w')
print('Writing x')
fiyl.write(str(x).strip('[]') + '\n')
print('Done writing x')
print('Writing y')
fiyl.write(str(y).strip('[]') + '\n')
print('Done writing y')
print('Writing dx_dt')
fiyl.write(str(dx_dt).strip('[]') + '\n')
print('Done writing dx_dt')
print('Writing dy_dt')
fiyl.write(str(dy_dt).strip('[]') + '\n')
print('Done writing dy_dt')
print('Writing d2x_dt2')
fiyl.write(str(d2x_dt2).strip('[]') + '\n')
print('Done writing d2x_dt2')
print('Writing d2y_dt2')
fiyl.write(str(d2y_dt2).strip('[]') + '\n')
print('Done writing d2y_dt2')
print('Writing time stamps')
fiyl.write(str(time_stamps).strip('[]') + '\n')
print(time_stamps)
print('Done writing time stamps')
print('Done!')
E = input()





# print(x[-1], y[-1], atan(y[-1] / x[-1]) * 180 / pi)
# print('rev : {} degrees'.format(path_len))
# print('average velocity : {}'.format(velocity_sum / len(dx_dt)))
# print('average acceleration : {}'.format(acceleration_sum / len(d2x_dt2)))
        
