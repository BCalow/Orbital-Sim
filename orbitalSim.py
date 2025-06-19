import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.animation import FuncAnimation

#np.random.seed(19680801)

#Setting up window
#plt.style.use('dark_background')
mpl.rcParams['toolbar'] = 'None'
fig, axes = plt.subplots(nrows = 1, ncols = 1)
fig.tight_layout()
axes.axis('equal')
axes.set_ylim(-1500, 1500)
axes.axis('off')
#fig.set_edgecolor('k')

#Setting constants
G = 1 #Gravitational constant
dt = 0.1 #Delta time
nObjects = 10 #Number of objects

#Create object data array
object = np.zeros(nObjects, dtype = [
                                    ('position', float, (2,)),
                                    ('mass', float),
                                    ('speed', float, (2,)),
                                    ('momentum', float, (2,))
                                    ])

#Creating initial object data
object['position'] = np.random.uniform(-500, 500, (nObjects, 2)) #Random position x, y
object['mass'] = np.random.uniform(10, 100, nObjects) #Random mass
object['momentum'] = np.random.uniform(-250, 250, (nObjects, 2)) #Random momentum x, y

#Creating massive object
object['position'][0] = [0, 0]
object['mass'][0] = 100000
object['momentum'][0] = [0, 0]

#Calculate object speed
for idx, i in enumerate(object['speed']):
    i[0] = object['momentum'][idx, 0] / object['mass'][idx] #Calculated speed x
    i[1] = object['momentum'][idx, 1] / object['mass'][idx] #Calculated speed y

#Creating initial scatter plot
scatter = axes.scatter(
                       object['position'][0],
                       object['position'][1],
                       linewidths = 0.5,
                       edgecolors = ['k'],
                       facecolors = ['none']
                      )

#Math
def math():
    for idx1, i in enumerate(object):
        for idx2, j in enumerate(object):
           if idx1 != idx2:
               #Distance
               xdif = j['position'][0] - i['position'][0] #Distance between objects on x axis
               ydif = j['position'][1] - i['position'][1] #Distance between objects on y axis
               r = np.sqrt(np.square(xdif)+np.square(ydif)) #Distance between objects
               thetaF = np.arctan2(ydif, xdif) #Angle between x axis and r
               #Forces
               forcet = G * i['mass'] * j['mass'] / np.square(r) #Total force
               forcex = forcet * np.cos(thetaF) #Force on x axis
               forcey = forcet * np.sin(thetaF) #Force on y axis
               #Momentum
               momentumx = i['momentum'][0] + (forcex * dt) #Momentum on x axis
               momentumy = i['momentum'][1] + (forcey * dt) #Momentum on y axis
               #Position
               positionx = i['position'][0] + (momentumx / i['mass'] * dt) #Position on x axis
               positiony = i['position'][1] + (momentumy / i['mass'] * dt) #Position on y axis
               #Speed
               speedx = momentumx / i['mass'] #Speed on x axis
               speedy = momentumy / i['mass'] #Speed on y axis
               #Update position, speed, and momentum
               i['position'][0] = positionx #Update position on x axis
               i['position'][1] = positiony #Update position on y axis
               i['speed'][0] = speedx #Update speed on x axis
               i['speed'][1] = speedy #Update speed on y axis
               i['momentum'][0] = momentumx #Update momentum on x axis
               i['momentum'][1] = momentumy #Update momentum on y axis
    return object

def update(frame):
    math()
    scatter.set_offsets(object['position'])
    scatter.set_sizes(np.log(object['mass'])*4)
    return [scatter]

animation = FuncAnimation(
                        fig = fig,
                        func = update,
                        interval=10,
                        save_count=10,
                        blit = True
                        )

manager = plt.get_current_fig_manager()
manager.full_screen_toggle()
plt.show()