class Place:
 def __init__(self, place_id, host_id, city):
     self.place_id = place_id
     self.host_id = host_id
     self.city = city
 def setup(self):
    n = self.city.size
    x = self.place_id % n
    y = self.place_id // n
    neighbours = [(x-1,y-1), (x,y-1), (x+1,y-1),
                  (x-1,y ),           (x+1,y ),
                  (x-1,y+1), (x,y+1), (x+1,y+1)]
    neighbours = [i + j*n for i, j in neighbours
                  if 0<=i<n and 0<=j<n]
    self.neighbours = neighbours
    self.area = (x >= n/2) + 2 * (y >= n/2)