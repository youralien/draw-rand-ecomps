import numpy as np
from draw import Capacitor, Resistor

batch = (10000, 10500)

for i in range(*batch):
    # Error is the error for where the points deviate from calculated
    cap = Capacitor(
        error = 4,
        id=i
    )
    cap.draw()
    cap.save()
    
    #Theta math.pi/5 is the angle on the resistors
    res = Resistor(
        25,
        np.pi/5,
        error = 5,
        id=i
    )
    res.draw()
    res.save()