# Verlet algorithm for
# 1) harmonic oscillator
# 2) Lennard-Jones potential
# advice: use jupyter notebook

import numpy as np;
import matplotlib.pyplot as plt;


#%%

# harmonic oscillator
def energy(x,*,k=1.0):
    return 0.5*k*x**2
def force(x,*,k=1.0):
    return -k*x

def run(dt=0.1,q=2,qold=2,maxt=10,k=1.0):
    time = []
    traj = []
    nsteps = int(maxt/dt)
    qold = 2*np.cos(-dt)
    for istep in range(nsteps):
        qn = 2*q-qold+force(q,k=k)*dt**2
        qold = q
        q = qn
        traj.append(q)      # add elements to the list
        time.append(dt*(istep+1))
    return np.array(time),np.array(traj) 


#%%
  
# comparison with the analytic solution  
time,traj = run() 
plt.plot(time,traj,label="verlet")  
plt.plot(time,2*np.cos(time),label="cos") 
plt.legend() 


#%%

# find dt s.t. the trajectory becomes unstable
time = np.linspace(0,400,1000)
plt.plot(time,2*np.cos(time),label="cos")
#for dt in (0.01,0.02,0.05,0.1,0.2,0.5,1.0,2.0):
for dt in (2,):
    time,traj = run(dt=dt,maxt = 400)
    plt.plot(time,traj,label="verlet dt=" +str(dt))
plt.legend()
plt.show()
# for dt = 2.0 the traj increases linearly


#%%

# relation between k and maximum dt
time = np.linspace(0,40,1000)
plt.plot(time,2*np.cos(time),label="cos")
dt = 2.0
for k in (0.1,0.2,0.5,1.0):
    time,traj = run(k=k,maxt=40,dt=dt)
    plt.plot(time,traj,label="verlet k=" +str(k))
plt.legend()
plt.show()
# it goes as 1/sqrt(k), because it is stable for dt=T/pi,
# with T the period of the oscillator


#%%

# Lennard-Jones potential
def energy(x):
    return 4.0*(1/x**12-1/x**6)
def force(x):
    return 24.0*(2/x**13-1/x**7)

def run(dt=0.01,q=2,qold=2,maxt=40,k=1.0):
    time = []
    traj = []
    nsteps = int(maxt/dt)
    for istep in range(nsteps):
        qn = 2*q-qold+force(q)*dt**2
        qold = q
        q = qn
        traj.append(q)      # add elements to the list
        time.append(dt*(istep+1))
    return np.array(time),np.array(traj) # list to array

time,traj = run() 
plt.plot(time,traj)

# explosion due to non conservation of energy
for dt in (0.01,0.02,0.04,0.05,0.06):
    time,traj = run(maxt=1000,dt=dt)
    plt.plot(time,traj,label="dt=" +str(dt))
plt.legend()

'''if we initialize the system close to the minimum x = 2**(1/6)
it behaves like an harmonic oscillator, and we can compare
the results we have obtained approximating the LJ potential 
as 1/2*d^2(energy(x0))/dt^2*(x-x0)
The correspondent k is 57.15 and dt has to be smaller than
T/pi because the potential is not exactly quadratic'''