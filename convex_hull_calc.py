import math

"""
Calculate distance between two given points
"""
def calculate_distance(p1, p2):
  distance = math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
  return distance

"""
Find the greatest distance, diatmeter between any two points given an array of points
"""
def find_diameter(point_arr):
  diameter = 0
  for p1 in point_arr:
    for p2 in point_arr:
      distance = calculate_distance(p1, p2)
      if distance > diameter:
        diameter = distance
  return diameter

"""
Find area of circle given diameter
"""
def find_area(diameter):
  area = math.pi*(diameter/2)**2
  return area

"""
Calculate reock score from district area input and given circle area
"""
def reock(circle_area):
  dis_area = float(input("District area: "))
  reock_score = dis_area/circle_area
  return reock_score

"""
Get inputs for array of points
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
diameter = find_diameter(point_arr)
circle_area = find_area(diameter)
reock_score = reock(circle_area)
print(point_arr)
print("Area of minimum enclosing circle:",round(circle_area,7))
print("Reock score:", round(reock_score,7))
