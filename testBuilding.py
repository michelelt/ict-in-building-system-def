#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import math
height = 4.05
Lwall = (3+4.4+12.2+0.8+2.6)*2
Awall = Lwall * height

Aceil = 236
Afloor = 236

d1={} #wall, floor, ceil
d2={}
d3={}
d1['max'] = 0.65 #wall (cosidered unique) light gray 
d1['min'] = 0.45
d2['max'] = 0.25 #floor, dark brown
d2['min'] = 0.10
d3['max'] = 0.88 #ceil. white piant
d3['min'] = 0.87
rho_list = [d1,d2,d3]

internal_surface = [Awall, Aceil, Afloor]

a_tot = sum(internal_surface)


epsilon = 0.5 #no obstruction

a_triangle = 1.65*1.65/2
a_frame = 0.36 #frame of the wnd to remove

glass_wnd=[16.5, 14, 9.4] #dimension of windos
a_wnd = []

#compute a_wnd
for length in glass_wnd:
    a_wnd_gross = height*length
    number_of_triangles = a_wnd_gross / a_triangle
    a_wnd_net = a_wnd_gross - (number_of_triangles * a_frame)
    a_wnd.append(a_wnd_net)
    
psi = 1 #approximation
tau = 0.47 #fino a 0.5 double glass low E

term = 0
for i,rho in zip(internal_surface, rho_list): #####glass should be considered here
    term = term + (i*(rho['min']))
    
rho_m = float(term/a_tot) #non considerato  vetro, più basso rho

num = 0
for i in range (0,3) : #####glass should be considered here?
    num = num + tau*a_wnd[i]* epsilon*psi
nu = num/((1-rho_m)*a_tot)
print "nu = " +str(nu)

'''
compute the number of light
'''
Em = 750
A = 8


A = 15.2
#b = 7
B = 14
h_first = height - 0.8


k = A*B / ((4.05-0.8)*(A+B)) #considerare rettangolo
print "k = " + str(k)
u = (0.63+0.71)/2
print "u = " + str(u)

flux = (Em*A)/(0.67*0.65)
print "Phi_tot = " + str(flux)
n_light_per_table = math.ceil(flux/4100)
print n_light_per_table