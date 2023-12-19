class Car:
    def __init__(self):
        self.__petrol = 0
        self.__odometer_reading = 0

    def fill_up(self):
        self.__petrol = 60

    def drive(self, km: int):
        if self.__petrol >= km:
            self.__petrol -= km
            self.__odometer_reading += km
        else:
            self.__odometer_reading += self.__petrol
            self.__petrol = 0

    def __str__(self):
        return f"Car: odometer reading {self.__odometer_reading} km, petrol remaining {self.__petrol} litres"

class Recording:
    def __init__(self, length: int):
        if length >0:
            self.__length = length
        else:
            raise ValueError()
    @property
    def length(self):
        return self.__length
    @length.setter
    def length(self, length: int):
        if length >0:
            self.__length = length
        else:
            raise ValueError()


class WeatherStation:
    def __init__(self, name: str):
        self.__name = name
        self._observations = []

    def add_observation(self, observation: str):
        self._observations.append(observation)

    def latest_observation(self):
        if len(self._observations) == 0:
            return ''
        else:
            return self._observations[-1]

    def number_of_observations(self):
        return len(self._observations)

    def __str__(self):
        return f"{self.__name}, {self.number_of_observations()} observations"



