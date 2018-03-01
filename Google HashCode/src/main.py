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

    def run_simulation(self):
        rides_per_car = len(self.rides)/len(self.cars)
        #print(rides_per_car)
        for car in self.cars:
            current_step = 0

            while current_step < self.steps and len(car.rides) < rides_per_car:
                best_ride = None
                maximum_points = 0
                ride_index = -1
                #print("mata")
                for i in range(0,len(self.rides)):
                    ride = self.rides[i]
                    if ride.is_done == False:
                        points_now = pyculator.calculate_points(car,ride,current_step,self.bonus)
                        if points_now > maximum_points:
                            maximum_points = points_now
                            best_ride = ride
                            ride_index = i

                #print(ride_index)
                if ride_index != -1:
                    current_step = current_step + pyculator.ride_time(car,best_ride,current_step)
                    car.set_loc(best_ride.get_end_loc())
                    car.add_ride(ride_index)
                    car.increment_rides()
                    best_ride.set_done()
                    #print("mata")
                else:
                    break

    def print_info(self):
        f = open("output_e.txt","w")
        for car in self.cars:
            output = str(len(car.rides))
            for index in car.rides:
                output = output + " " + str(index)
            #print(output)
            f.write(output + "\n")
        f.close()



#___________________M_A_I_N_______________________________________________________________________

p = parser_info.Parser_info()
simulator = Simulator(p.R,p.C,p.get_cars(),p.get_rides(),p.B,p.T)
simulator.run_simulation()

simulator.print_info()
