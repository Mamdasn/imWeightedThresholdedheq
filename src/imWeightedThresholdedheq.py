import numpy as np 
import numba

@numba.njit()
def imhist(image):
    hist, _ = np.histogram(image.reshape(1, -1), bins=256, range=(0, 255))
    return hist

@numba.njit()
def imWTHeq(image, Wout_list=np.zeros((10)), r=0.5, v=0.5):
    [h, w] = image.shape
    PMF = imhist(image) / (h*w)
    Pl = 1e-4
    Pu = v*np.max(PMF)
    Pwt = np.zeros_like(PMF)
    for indx, pmf in enumerate(PMF):
        if pmf < Pl:
            Pwt[indx] = 0
        elif pmf > Pu:
            Pwt[indx] = Pu
        else:
            Pwt[indx] = ( ((pmf - Pl) / (Pu - Pl))**r ) * Pu
    
    Cwt = np.cumsum(Pwt)
    Cwtn = Cwt / Cwt[-1]
    Win = len(np.where(PMF>0)[0])
    Gmax = 1.5 # 1.5 .. 2


    Wout = min(255, Gmax*Win)
    if np.where(Wout_list>0)[0].size==Wout_list.size:
        Wout = (np.sum(Wout_list)+Wout) / (1+Wout_list.size)

    F = image.copy().reshape(-1)
    Ftilde = Wout * Cwtn[F]
    
    Madj = np.mean(image) - np.mean(Ftilde)
    Ftilde = Ftilde + Madj

    Ftilde = np.where(Ftilde>=0, Ftilde, np.zeros_like(Ftilde))
    Ftilde = np.where(Ftilde<=255, Ftilde, 255*np.ones_like(Ftilde))
    Ftilde = Ftilde.astype(np.uint8)

    image_heq = Ftilde.reshape(h, w)
    return image_heq, Wout

