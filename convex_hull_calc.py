#https://stackoverflow.com/questions/19873596/convex-hull-area-in-python + my stuff
import numpy as np

def conv_hull_area(point_arr):
    lines = np.hstack([point_arr,np.roll(point_arr,-1,axis=0)])
    area = 0.5*abs(sum(x1*y2-x2*y1 for x1,y1,x2,y2 in lines))
    return area

def conv_hull(area):
  dis_area = float(input("District area: "))
  conv_hull = dis_area/area
  return conv_hull

num_point = int(input("Num points: "))
point_arr = []
for point in range(num_point):
  print("Point " + str(point + 1))
  x = float(input("X: "))
  y = float(input("Y: "))
  point_arr.append([x, y])
area = conv_hull_area(point_arr)
conv_hull = conv_hull(area)
print(point_arr)
print("Area of convex hull:",round(area,7))
print("Convex hull:",round(conv_hull,7))
