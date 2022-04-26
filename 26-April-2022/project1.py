import time


spaces = []
avail_spaces = 0
total_spaces = 0
rows = 0                        # display function variables
space_count = 0
border = ""   



# vehicle class, has a type and a plate number
class Vehicle:
    def __init__(self, vehicle_type, plate):
        """

        @param vehicle_type: Here the type of vehicle
        @param plate:plate number
        """
        self.type = vehicle_type
        self.plate = plate
        self.entry_time = time.time()

    # return type value (int)
    def get_type(self):
        return self.type

    # return type value (string)
    def get_type_string(self):
        """
        @return: returning the string type
        """
        return "Car" if self.type == 1 else "Truck" if self.type == 2 else "Motorcycle"

    def get_plate(self):
        return self.plate

    def get_entry_time(self):
        return self.entry_time

    # set epoch time manually - used for demo mode
    def set_entry_time(self, new_time):
        self.entry_time = new_time

    def get_vehicle(self):
        return self.type, self.plate, self.entry_time


# space class, stores a vehicle object and current occupied status,
class Space:
    def __init__(self):
        self.vehicle = None
        self.occupied = False

    def add_vehicle(self, vehicle):
        self.vehicle = vehicle
        self.occupied = True

    # remove a vehicle from a space and return object for final fare calculation
    def remove_vehicle(self):
        v_exit = self.vehicle
        self.vehicle = None
        self.occupied = False
        return v_exit

    def vehicle_info(self):
        return self.vehicle

    def is_available(self):
        return self.occupied
