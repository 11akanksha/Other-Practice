import numpy as np
import matplotlib.pyplot as plt

languages = ['C','C++','JavaScript','Python']
liking = [15,25,18,19]
plt.pie(liking,labels = languages,explode = (0,0.1,0,0),autopct = '%1.1f%%',shadow = True)
plt.title('Languages')
plt.show()

#-----------------------------------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn')

x_coord = np.array([0,1,2])*2
plt.bar(x_coord - 0.25,[10,20,15],width = 0.5,label = 'Current Year',tick_label = ['IIT','KIIT','IIIT'],color = 'pink')
plt.bar(x_coord + 0.25,[5,15,10],width = 0.5,label = 'Last Year',color = 'yellow')
plt.title('College wise Placements')
plt.xlabel('College')
plt.ylabel('students in thousand')
plt.ylim(0,30)
plt.xlim(-1,6)
plt.legend()
plt.show()
