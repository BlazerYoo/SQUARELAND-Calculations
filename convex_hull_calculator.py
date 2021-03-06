"""
Library for finding ConvexHull
"""
from scipy.spatial import ConvexHull

"""
Calculate convex hull score from district area input and given convex hull area
"""
def conv_hull(conv_hull_area):
  dis_area = float(input("District area: "))
  conv_hull_score = dis_area/conv_hull_area
  return conv_hull_score

"""
Get input for array of points
"""
num_point = int(input("Num points: "))
point_arr = []
for point in range(num_point):
  print("Point " + str(point + 1))
  x = float(input("X: "))
  y = float(input("Y: "))
  point_arr.append([x, y])

"""
Do all calculations and display results
"""
hull = ConvexHull(point_arr)
conv_hull_score = conv_hull(hull.area)
print(point_arr)
print("Area of convex hull: ",hull.area)
print("Convex hull scores:",conv_hull_score)
