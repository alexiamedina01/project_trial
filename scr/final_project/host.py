class Host():
   def __init__(self, host_id, place, city, profits = 0):
       self.host_id = host_id
       self.city = city
       self.profits = profits
       
       self.area = place.area
       self.assets = set([place.place_id])