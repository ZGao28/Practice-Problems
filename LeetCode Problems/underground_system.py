from statistics import mean

class UndergroundSystem:

    def __init__(self):
        self.stations = {}
        self.customers = {}
        
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customers[id] = (t, stationName)
                

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_t, start_station = self.customers[id]
        if stationName not in self.stations:
            self.stations[stationName] = {}
        if start_station not in self.stations[stationName]:
            self.stations[stationName][start_station] = []
        self.stations[stationName][start_station].append(t-start_t)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return mean(self.stations[endStation][startStation])
