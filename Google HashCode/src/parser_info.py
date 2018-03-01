#!/usr/bin/python
# -*- coding: utf-8 -*-

import classes as c

# first line

class Parser_info:

    def __init__(self):
        self.f = open("e_high_bonus.in", "r")
        self.firstLine = self.f.readline().split()
        self.R = int(self.firstLine[0])
        self.C = int(self.firstLine[1])
        self.F = int(self.firstLine[2])
        self.N = int(self.firstLine[3])
        self.B = int(self.firstLine[4])
        self.T = int(self.firstLine[5])

    #f.close()

    def rows(self):
        return self.R

    def columns(self):
        return self.C

    def vehicles(self):
        return self.F

    def rides(self):
        return self.N

    def bonus(self):
        return self.B

    def steps(self):
        return self.T

    def get_cars(self):
        cars = []
        for x in range(self.F):
            cars.append(c.Car(c.Loc(0,0)))
        return cars

    def get_rides(self):
        rides = []
        for line in self.f:
            l = line.split()
            start_loc = c.Loc (int(l[0]), int(l[1]))
            end_loc = c.Loc (int(l[2]), int(l[3]))
            start_time = int(l[4])
            end_time = int(l[5])
            rides.append(c.Ride(start_loc, end_loc, start_time, end_time))
        return rides
