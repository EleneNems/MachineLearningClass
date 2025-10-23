import matplotlib.pyplot as plt
import numpy as np

# first
# xpoints = np.array([0, 1, 4, 6])
# ypoints = np.array([0, 7, 100, 250])
#
# plt.plot(xpoints, ypoints, 'o')
# plt.show()

# second
# ypoints = np.array([3, 8, 1, 10])

# plt.plot(ypoints, '*')
# plt.show()

# third
# ypoints = np.array([3, 8, 1, 10])
#
# plt.plot(ypoints, 'o:r')
# plt.show()

#forth
# ypoints = np.array([3, 8, 1, 10])
#
# plt.plot(ypoints, marker='o', ms=20, mec='hotpink')
# plt.show()

#fifth
# y1 = np.array([3, 8, 1, 10])
# y2 = np.array([6, 2, 7, 11])
#
# plt.plot(y1)
# plt.plot(y2)
#
# plt.show()

#sixth
# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
#
# font1 = {'family':'serif','color':'blue','size':20}
# font2 = {'family':'serif','color':'darkred','size':15}
#
# plt.title("Sports Watch Data", fontdict=font1)
# plt.xlabel("Average Pulse", fontdict=font2)
# plt.ylabel("Calorie Burnage", fontdict=font2)
#
# plt.plot(x, y)
# plt.show()

# x = np.array(["A", "B", "C", "D"])
# y = np.array([3, 8, 1, 10])
#
# plt.bar(x, y, color="hotpink")
# plt.show()

# x = np.random.normal(170, 10, 250)
#
# plt.hist(x)
# plt.show()

# y = np.array([35, 25, 25, 15])
# mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
#
# plt.pie(y, labels=mylabels)
# plt.show()

# y = np.array([35, 25, 25, 15])
# mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
# myexplode = [0.2, 0, 0, 0]
#
# plt.pie(y, labels = mylabels, explode=myexplode, shadow=True)
# plt.show()

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
mycolors = ["yellow", "hotpink", "r", "#4CAF50"]

plt.pie(y, labels=mylabels, colors=mycolors)
plt.legend()
plt.show()






