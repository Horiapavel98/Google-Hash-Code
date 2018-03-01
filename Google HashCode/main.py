import classes
import pyculator
import parser_info

class Simulator:

    def __init__(self,rows,columns,cars,rides,bonus,steps):
        self.rows = rows
        self.columns = columns
        self.cars = cars
        self.rides = rides
        self.bonus = bonus
        self.steps = steps
        self.no_pending_rides = len(rides)

    def run_simulation(self):
        rides_per_car = len(rides)/len(cars)
        for car in cars:
            current_step = 0
            while current_step < steps and len(car.rides) < rides_per_car:
                best_ride = None
                maximum_points = 0
                ride_index = -1
                for i in range(0,len(rides)):
                    ride = rides[i]
                    if ride.is_done == False:
                        points_now = calculate_points(car,ride,current_step,self.bonus)
                        if points_now > maximum_points:
                            maximum_points = points_now
                            best_ride = ride
                            ride_index = i

                if ride_index != -1:
                    current_step = current_step + ride_time(car,best_ride,current_step)
                    car.set_loc(best_ride.get_end_loc())
                    car.add_ride(ride_index)
                    car.increment_rides()
                    best_ride.set_done()
                else:
                    break

    def print_info():
        for car in cars:
            output = str(len(car.rides))
            for index in car.rides:
                output = output + " " + str(index)
            print(output)


#___________________M_A_I_N_______________________________________________________________________

p = Parser_info()

simulator = Simulator(p.R,p.C,p.get_cars,p.get_rides,p.B,p.T)
simulator.run_simulation()
