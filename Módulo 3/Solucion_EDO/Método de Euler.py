import matplotlib.pyplot as plt
def f(x, y):
    return 0.5*x*y

a = 0
b = 1
h = 0.01
x = a
y = 1
k = 0
print('{4}{0:^4}{4}{1:^8}{4}{2:^8}{4}{3:^8}{4}'.format('k', 'x', 'y', 'f(x,y)', '|'))
while x <= b:
    plt.scatter(x, y, color=(0.19, 0.55, 0.91))
    print('{4}{0:^4}{4}{1:>8.6f}{4}{2:>8.6f}{4}{3:>8.6f}{4}'.format(k, x, y, f(x,y), '|'))
    y = y + f(x, y) * h
    x = x + h
    k += 1
plt.show()