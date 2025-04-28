import numpy as np
import math as m

    #BASIC GATES
def X():
    return np.array([[0,1],
                [1,0]])
def Y():
    return np.array([[0,-1j],
                [1j,0]])
                
def Z():
    return np.array([[1,0],
                [0,-1]])
def H():      
    s=2**0.5
    return np.array([[1/s,1/s], 
                [1/s,-1/s]])
    #ROTATIONAL GATES

def Rx(d):
    p=m.radians(d)
    return np.array([[m.cos(p/2),-1j*(m.sin(p/2))],
                [-1j*(m.sin(p/2)),m.cos(p/2)]])  
def Ry(d):
    p=m.radians(d)
    return np.array([[m.cos(p/2),m.sin(-p/2)],
                [m.sin(p/2),m.cos(+p/2)]])   
def Rz(d):
    p=m.radians(d)
    return np.array([[(m.cos(p/2)-m.sin(p/2)*1j),0],
                [0,(m.cos(p/2)-m.sin(p/2)*1j)]]) 
    #P GATE
def P(d):
    p=m.radians(d)
    return np.array([[1,0],
                [0,(m.cos(p/2)+m.sin(p/2)*1j)]])
    #SQUARE ROOT GATE
def Sr():
    return np.array([[(1-1j)/2,(1+1j)/2],
                [(1+1j)/2,(1-1j)/2]])  
    
def S():
    return np.array([[1,0],[0,1j]]) 

def T():
    return np.array([[1,0],
                [0,(m.cos(m.pi/4)+m.sin(m.pi/4)*1j)]])
    #HERMITIAN CONJUGATES
def St():
    return np.array([[1,0],
                [0, -1j]])
def Tt():
    return np.array([[1,0],
                [0,(m.cos(m.pi/4)-m.sin(m.pi/4)*1j)]])
def Srt():
    return np.array([[(1+1j)/2,(1-1j)/2],
              [(1-1j)/2,(1+1j)/2]])   
def I():
    return np.array([[1,0],
                     [0,1]])  
def Ketzero():
    return  np.array([[1],[0]])
def Ketone():
    return np.array([[0],[1]])
