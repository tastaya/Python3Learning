# importing the required module
from cProfile import label
from turtle import color
import matplotlib.pyplot as plt

ax = plt.axes()

# Set color

ax.set_facecolor('pink')

# 1st Line values
x = [1, 2, 3]
y = [2, 4, 1]

# plotting the points
plt.plot(x, y, label="1st Line")

# 2nd Line values
x1 = [0, 1, 4]
y1 = [1, 3, 1]

# plotting the points
plt.plot(x1,
         y1,
         label="2nd Line",
         color='red',
         linestyle='dashed',
         marker='o',
         markerfacecolor='yellow',
         markersize=12)

# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')

# giving a title to my graph
plt.title('Graphy!')

plt.legend()

# function to show the plot
plt.show()
