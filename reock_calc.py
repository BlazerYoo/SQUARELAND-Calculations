#https://www.geeksforgeeks.org/minimum-enclosing-circle-set-1/ + my stuff
from math import sqrt, pi

INF = 10**18

def dist(a, b): 
	return sqrt(pow(a[0] - b[0], 2) + pow(a[1] - b[1], 2)) 

def is_inside(c, p): 
	return dist(c[0], p) <= c[1] 

def get_circle_center(bx, by, cx, cy): 
	B = bx * bx + by * by 
	C = cx * cx + cy * cy 
	D = bx * cy - by * cx 
	return [(cy * B - by * C) // (2 * D), 
			(bx * C - cx * B) // (2 * D) ] 

def circle_frOm(A, B,C): 
	I = get_circle_center(B[0] - A[0], B[1] - A[1], 
								C[0] - A[0], C[1] - A[1]) 
	I[0] += A[0] 
	I[1] += A[1] 
	return [I, dist(I, A)] 

def circle_from(A, B): 
	C = [ (A[0] + B[0]) / 2.0, (A[1] + B[1]) / 2.0] 
	return [C, dist(A, B) / 2.0] 

def is_valid_circle(c, P): 
	for p in P: 
		if (is_inside(c, p) == False): 
			return False
	return True

def minimum_enclosing_circle(P): 
	n = len(P) 
	if (n == 0): 
		return [[0, 0], 0] 
	if (n == 1): 
		return [P[0], 0] 
	mec = [[0, 0], INF] 
	for i in range(n): 
		for j in range(i + 1, n): 
			tmp = circle_from(P[i], P[j]) 
			if (tmp[1] < mec[1] and is_valid_circle(tmp, P)): 
				mec = tmp 
	for i in range(n): 
		for j in range(i + 1, n): 
			for k in range(j + 1, n): 
				tmp = circle_frOm(P[i], P[j], P[k]) 
				if (tmp[1] < mec[1] and is_valid_circle(tmp, P)): 
					mec = tmp 
	return mec 

def area(mec):
  circle_area = pi*mec[1]**2
  return circle_area

def reock(circle_area):
  dis_area = float(input("District area: "))
  reock_score = dis_area/circle_area
  return reock_score

num_point = int(input("Num points: "))
point_arr = []
for point in range(num_point):
  print("Point " + str(point + 1))
  x = float(input("X: "))
  y = float(input("Y: "))
  point_arr.append([x, y])
mec = minimum_enclosing_circle(point_arr)
circle_area = area(mec)
reock_score = reock(circle_area)
print("Center = (",mec[0][0],",",mec[0][1],") Radius = ",round(mec[1],7)) 
print("Area of minimum enclosing circle:",round(circle_area,7))
print("Reok score:", round(reock_score,7))
