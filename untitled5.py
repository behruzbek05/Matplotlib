# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1u9lWteskhmf6bH3YVpPkzDvCZJ2E6LZk
"""

import matplotlib.pyplot as plt
import numpy as np
x=np.array([1,2,6,8])
y=np.array([3,8,1,10])
plt.plot(x,y)
plt.show()

import matplotlib.pyplot as plt
import numpy as np
y=np.array([3,8,1,10])
plt.plot(y, marker='o',ms=20)
plt.show()

import matplotlib.pyplot as plt
import numpy as np

x1=np.array([0,1,2,3])
y1=np.array([3,8,1,10])
x2=np.array([0,1,2,3])
y2=np.array([6,2,7,11])

plt.plot(x1,y1,x2,y2)
plt.show()

import matplotlib.pyplot as plt
import numpy as np

y=np.array([3,8,1,10])


plt.plot(y, 'o:r')
plt.show()

import matplotlib.pyplot as plt
import numpy as np

x=np.array([1,2,4,6,8,10])
y=np.array([3,8,1,10,2,12,])


plt.plot(x,y)
plt.show()

import matplotlib.pyplot as plt
import numpy as np
x=np.array([0,1,2,3,4,5])
y=np.array([0,8,12,20,26,38])
plt.scatter(x,y)
plt.show()

import matplotlib.pyplot as plt
import numpy as np
x=np.array([0,1,2,3,4,5])
y=np.array([0,2,8,1,14,7])
plt.scatter(x,y,color='red')
x=np.array([12,6,8,11,8,3])
y=np.array([5,6,3,7,17,19])
plt.scatter(x,y,color='green')
plt.show()

import matplotlib.pyplot as plt
import numpy as np
x=np.array([0,1,2,3,4,5])
y=np.array([0,2,8,1,14,7])
mycolor=['red','green','purple','lime','aqua','yellow']
plt.scatter(x,y,color=mycolor)
plt.show()

import matplotlib.pyplot as plt
import numpy as np
x=np.array([0,1,2,3,4,5])
y=np.array([0,2,8,1,14,7])
mycolor=['red','green','purple','lime','aqua','yellow']
size=[10,60,120,80,20,190]
plt.scatter(x,y,color=mycolor,s=size)
plt.show()

import matplotlib.pyplot as plt
import numpy as np
x=np.array(['A','B','C','D'])
y=np.array([3,8,1,10])
plt.bar(x,y)
plt.show()

import matplotlib.pyplot as plt
import numpy as np
x=np.array(['A','B','C','D'])
y=np.array([3,8,1,10])
plt.barh(x,y)
plt.show()

import matplotlib.pyplot as plt
import numpy as np
x=np.array([35,25,25,15])
plt.pie(y)
plt.show()

