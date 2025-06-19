# Orbital Simulation
Direct Gravitational N-Body Simulation  

## Table of Contents
- [Description](#description)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Common Issues](#common-issues)
- [References](#references)
- [Liscense](#liscense)

## Description  
This is a basic direct gravitational N-Body simulation made as my self directed study for Mr. Bachiu's Physics-30 class. Written in python with Numpy and MatPlotLib.  

## Prerequisites
Numpy:  
```pip install numpy```

MatPlotLib:  
```pip install numpy```

## Installation
Clone the repository:  
```git clone https://github.com/BCalow/Orbital-Sim```

## Usage
Run the file [orbitalSim.py](./orbitalSim.py)

## Code Explanation
▼Setting up MatPlotLib Window
```python
#Setting up window
#plt.style.use('dark_background')
mpl.rcParams['toolbar'] = 'None'
fig, axes = plt.subplots(nrows = 1, ncols = 1)
fig.tight_layout()
axes.axis('equal')
axes.set_ylim(-1500, 1500)
axes.axis('off')
#fig.set_edgecolor('k')
```
▼Setting gravitational constant, time in between frames, and the number of objects to simulate
```python
#Setting constants
G = 1 #Gravitational constant
dt = 0.1 #Delta time
nObjects = 10 #Number of objects
```
▼Creating numpy ndarray to store position (x,y), mass, speed (x,y), and momentum (x,y)
```python
#Create object data array
object = np.zeros(nObjects, dtype = [
                                    ('position', float, (2,)),
                                    ('mass', float),
                                    ('speed', float, (2,)),
                                    ('momentum', float, (2,))
                                    ])
```
▼Creating random initial position, mass, and momentum
```python
#Creating initial object data
object['position'] = np.random.uniform(-500, 500, (nObjects, 2)) #Random position x, y
object['mass'] = np.random.uniform(10, 100, nObjects) #Random mass
object['momentum'] = np.random.uniform(-250, 250, (nObjects, 2)) #Random momentum x, y
```

▼Setting one object to be at the center with zero momentum, but with significantly higher mass
```python
#Creating massive object
object['position'][0] = [0, 0]
object['mass'][0] = 100000
object['momentum'][0] = [0, 0]
```

▼Calculating speed for all objects  
```math
 v = \frac{p}{m}
```
```python
#Calculate object speed
for idx, i in enumerate(object['speed']):
    i[0] = object['momentum'][idx, 0] / object['mass'][idx] #Calculated speed x
    i[1] = object['momentum'][idx, 1] / object['mass'][idx] #Calculated speed y
```

▼Creating initial MatPlotLib scatter plot
```python
#Creating initial scatter plot
scatter = axes.scatter(
                       object['position'][0],
                       object['position'][1],
                       linewidths = 0.5,
                       edgecolors = ['k'],
                       facecolors = ['none']
                      )
```

▼Iterate through list, calculating the Force between each object with every other object
```python
    for idx1, i in enumerate(objects):
        for idx2, j in enumerate(objects):
           if idx1 != idx2:
```

▼Calculate distance x and y, then calculate distance along with angle θ
```math
d_x = x_j - x_i
```
```math
d_y = y_j - y_i
```
```math
r=\sqrt{d_x^2 + d_y^2}
```
```math
θ = tan^{-1}\left(\frac{d_y}{d_x}\right)
```
```python
               #Distance
               xdif = j['position'][0] - i['position'][0] #Distance between objects on x axis
               ydif = j['position'][1] - i['position'][1] #Distance between objects on y axis
               r = np.sqrt(np.square(xdif)+np.square(ydif)) #Distance between objects
               thetaF = np.arctan2(ydif, xdif) #Angle between x axis and r
```

▼Calculate total force, and force x and y
```math
F_t = G \cdot \frac{m_i \cdot m_j}{r^2}
```
```math
F_x = F_t \cdot cos\left(θ\right)
```
```math
F_y = F_t \cdot sin\left(θ\right)
```
```python
               #Forces
               forcet = G * i['mass'] * j['mass'] / np.square(r) #Total force
               forcex = forcet * np.cos(thetaF) #Force on x axis
               forcey = forcet * np.sin(thetaF) #Force on y axis
```

▼Calculate momentum x and y
```math
p_{xf} = p_{xi} + F_x \cdot \Delta t
```
```math
p_{yf} = p_{yi} + F_y \cdot \Delta t
```
```python
               #Momentum
               momentumx = i['momentum'][0] + (forcex * dt) #Momentum on x axis
               momentumy = i['momentum'][1] + (forcey * dt) #Momentum on y axis
```
▼Calculate position x and y
```math
x_f = x_i + \frac{p_x}{m} \cdot \Delta t
```
```math
y_f = y_i + \frac{p_y}{m} \cdot \Delta t
```
```python
               #Position
               positionx = i['position'][0] + (momentumx / i['mass'] * dt) #Position on x axis
               positiony = i['position'][1] + (momentumy / i['mass'] * dt) #Position on y axis
```

▼Calculate speed x and y
```math
v_x = \frac{p_x}{m}
```
```math
v_y = \frac{p_y}{m}
```
```python
               #Speed
               speedx = momentumx / i['mass'] #Speed on x axis
               speedy = momentumy / i['mass'] #Speed on y axis
```

▼Update position x and y, speed x and y, and momentum x and y
```python
               #Update position, speed, and momentum
               i['position'][0] = positionx #Update position on x axis
               i['position'][1] = positiony #Update position on y axis
               i['speed'][0] = speedx #Update speed on x axis
               i['speed'][1] = speedy #Update speed on y axis
               i['momentum'][0] = momentumx #Update momentum on x axis
               i['momentum'][1] = momentumy #Update momentum on y axis
```

▼Updating scatter plot every frame
```python
def update(frame):
    math()
    scatter.set_offsets(object['position'])
    scatter.set_sizes(np.log(object['mass'])*4)
    return [scatter]
```

▼Setting up the FuncAnimation function
```python
animation = FuncAnimation(
                        fig = fig,
                        func = update,
                        interval=10,
                        save_count=10,
                        blit = True
                        )
```

▼Running animation, and setting to fullscreen
```python
manager = plt.get_current_fig_manager()
manager.full_screen_toggle()
plt.show()
```

## Common Issues
If the graph is fullscreen and zoomed in, comment out manager.full_screen_toggle()
```python
manager = plt.get_current_fig_manager()
manager.full_screen_toggle()
plt.show()
```

## References
[matplotlib](https://matplotlib.org/)  
[Numpy](https://numpy.org/)  

## Liscense
Copyright © 2025 Ben Calow

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.