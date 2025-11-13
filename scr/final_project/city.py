from scr.final_project.host import Host
from final_project.place import Place

class City:
    def __init__(self, size, area_rates):
        self.size = size
        self.area_rates = area_rates
        self.step = 0

    def initialize(self):
        n = self.size
        places = [Place(place_id = x, host_id = x, city = self)
                  for x in range(n*n)]
        _= [place.setup() for place in places]

        self.places = places
        hosts = [Host(host_id = x, place=places[x], city = self)
                 for x in range(n*n)]
        self.hosts = hosts