
t = 0
y = .5
n = 10
h = .2

def function(w, t, h):
    f = w - t**2 + 1
    return w + h*((w+(h/2)*(f))-((t+h/2)**2)+1)

for i in range(n):
    #y = function(y, t, h)
    y = float(f'{function(y, t, h):.4f}')
    print(y, t)
    t+=h


