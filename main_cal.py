#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       main_cal.py
#       
#       Copyright 2012 Cameron Steer <cameronsteer@ubuntu>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.
#       
#
       
from array import *
import math

def sizeofwall(length, height):
	size = length * height
	return size

def question(mes, wall):
	print "what is the %s of wall %s in meters:" % (mes, wall)
	num = 	float(raw_input(">"))
	return num

def roomarea(wall1, wall2, wall3, wall4):
	area = (wall1 + wall2 + wall3 + wall4)
	return area
	
def paint(area):
	x = area * 16.26
	amountpaint = x * 0.003785 
	return amountpaint
	
def potsneeded(ampaint):
	pots_needed = ampaint / 0.005
	return potsneeded
	
print "Hello, the following program works out the size of your room and then gives\nan estimate of the amount of paint needed to paint the room.\nFrist it will ask for the dimentions of each wall:"
	
length = question("length", "one")
height = question("height", "one")
wall1 = sizeofwall(length, height)
length = question("length", "two")
height = question("height", "two")
wall2 = sizeofwall(length, height)
length = question("length", "three")
height = question("height", "three")
wall3 = sizeofwall(length, height)
length = question("length", "four")
height = question("height", "four")
wall4 = sizeofwall(length, height)

roomarea = roomarea(wall1, wall2, wall3, wall4)

print "The area of the room is %rm^2, press RETURN to see the amount of paint needed:" % roomarea
raw_input(">")
amount = paint(roomarea)

print "Total amount of paint needed: %fm^3" % amount
potsneeded = (amount)
potsroundup = math.ceil(potsneeded)
cost = potsroundup * 32.00
cost = ("%.2f" % cost)
print "Total pots needed to buy from B&Q %d \nThis will cost £%s" % (potsroundup, cost)
