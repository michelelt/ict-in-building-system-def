#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import math
height = 4.05
Lwall = (3+4.4+12.2+0.8+2.6)*2
surface_wall = Lwall * height

Aceil  = 236
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

internal_surfaces = [surface_wall, Aceil, Afloor]
total_internal_surface = sum(internal_surfaces)

epsilon = 0.5 #no obstruction

triangle_area = 1.65*1.65/2 #from plates
frame_area = 0.36           #frame of the wnd to remove, approximation

glass_wnd_length=[16.5, 14, 9.4] #length of each glass facade
net_wnd_surfaces = []

#compute the net area
for length in glass_wnd_length:
    gross_wnd_area = height*length #compute the gross surface  
    #compute how many triangle shading system are contained in the gross area
    number_of_triangles = int(gross_wnd_area / triangle_area) 
    #eliminate the frame area: is the same for all the triangles belongeng at the considered glass facade
    net_wnd_area = gross_wnd_area - (number_of_triangles * frame_area) 
    net_wnd_surfaces.append(net_wnd_area)
    
psi = 1 #approximation
tau = 0.47 #fino a 0.5 double glass low E

term = 0
for surface,rho in zip(internal_surfaces, rho_list): #####glass should be considered here
    term = term + (surface*(rho['min']))
rho_m = float(term/total_internal_surface) #non considerato  vetro, più basso rho

num = 0
for i in range (0,3) : #####glass should be considered here?
    num = num + tau*net_wnd_surfaces[i]* epsilon*psi
nu = num/((1-rho_m)*total_internal_surface)


print "Wall surface = " + str(surface_wall)
print "Floor Surface = " + str(Afloor)
print "Ceil Surface = " + str(Aceil)
print "Glass surface = " + str(sum(glass_wnd_length)*height)
print "Internal surface = " +  str(sum(internal_surfaces))
for surface,rho in zip(internal_surfaces, rho_list): 
    print "rho = " + str(rho["min"]) 
print "epsilon = " + str(epsilon)
print "Psi = " + str(psi)
print "Tau = " + str(tau)
print "nu = " +str(nu)

print


'''
compute the number of light
'''
Em = 750
desk_area = 8
A = 15.2
B = 14
desk_height = 0.8
h_first = height - desk_height
lamp_flux = 7000
U = (0.57+0.63)/2
M = 0.72 #low dust level

k = A*B / (h_first*(A+B)) #considerare rettangolo
flux = (Em*desk_area)/(M*U)
n_light_per_table = math.ceil(flux/lamp_flux)

print "Space index (k) = " + str(k) 
print "Utilization Factor (U) = " + str(U)
print "Maintenance Factor (M) = " + str(M)
print "Phi_tot = " + str(flux)
print "Light per table = " + str(n_light_per_table)