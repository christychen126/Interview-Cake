"""
Write a class TempTracker with these methods:

insert()—records a new temperature
get_max()—returns the highest temp we've seen so far
get_min()—returns the lowest temp we've seen so far
get_mean()—returns the mean ↴ of all temps we've seen so far
get_mode()—returns a mode ↴ of all temps we've seen so far
Optimize for space and time. Favor speeding up the getter functions (get_max(), get_min(), get_mean(), and get_mode()) over speeding up the insert() function.

get_mean() should return a float, but the rest of the getter functions can return integers. Temperatures will all be inserted as integers. We'll record our temperatures in Fahrenheit, so we can assume they'll all be in the range 0..1100..110.

If there is more than one mode, return any of the modes.

"""

# O(1) time and space

class TempTracker(Object):

    def __init__(self):

        self.min_temp = None
        self.max_temp = None

        self.sum_temp = 0.0
        self.number_temp = 0
        self.mean_temp = None

        self.mode_dict = {}

        self.temp_list = [0]*111
        self.most_frequent = 0
        self.mode_temp = None



    def insert(self,temp):
        
        if self.min_temp is None or temp < self.min_temp:
            self.min_temp = temp

        if self.max_temp is None or temp > self.max_temp:
            self.max_temp = temp

        self.sum_temp += temp
        self.number_temp += 1
        self.mean_temp = self.sum_temp / self.number_temp

        self.temp_list[temp] += 1
        if self.temp_list[temp] > self.most_frequent:
            self.most_frequent = self.temp_list[temp]
            self.mode_temp = temp

    def get_max(self):
        return self.max_temp

    def get_min(self):
        return self.min_temp
    
    def get_mean(self):

        return self.mean_temp

    def get_mode(self):
        return self.mode_temp


