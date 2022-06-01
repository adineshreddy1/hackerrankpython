# import matplotlib.pyplot as plt
# import numpy as np

# y = np.array([35, 25, 25, 15])

# plt.pie(y)
# plt.savefig('books_read.png')

# plt.show() 

  
# # creating plotting data
# xaxis =[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# yaxis =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  
# # plotting 
# plt.plot(xaxis, yaxis)
# plt.xlabel("X")
# plt.ylabel("Y")
  
# # saving the file.Make sure you 
# # use savefig() before show().
# plt.savefig("squares.png")
  
# plt.show()
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery-nogrid')


# make data
x = [1, 2, 3, 4]
colors = plt.get_cmap('Blues')(np.linspace(0.2, 0.7, len(x)))

# plot
fig, ax = plt.subplots()
ax.pie(x, colors=colors, radius=3, center=(4, 4),
       wedgeprops={"linewidth": 1, "edgecolor": "white"}, frame=True)

ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))

plt.show()