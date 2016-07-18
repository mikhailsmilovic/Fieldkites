# This constructs the irrigation schedules for all total irrigation depths

# Inputs: 
#	Growing days (day, month, year) with no leading zeroes ex. 17 May 2015 = (17,5,2015)
#		Optional: First day of simulation period,
#		Optional: Last day of simulation period, 
#		First day of cropping period (Date of the day after sowing/transplanting),
#		Last day of cropping period (Date of crop maturity),
# 	Irrigation frequency, 
# 	Irrigation depth interval, 
# 	Irrigation max

# Output: 
#	Irr_DEPTHS, 
#	Irr_SCHEDULES 

import math
import numpy
import itertools
import shutil
import os
from kite_functions import generate_partitions, day 

#list(itertools.permutations([...]))

#-------------------------------------------------------------#
#
# inputs
#
#-------------------------------------------------------------#
"""
Date_crop=[(18,5,2003),(8,8,2003)]
Irr_frequency = 14 #maximum is at least as often as every n days. Irrigation may occur if Irr_frequency is a divisor of the day.

# one can set Irr_frequency or Irr_days
# if Irr_frequency is set, Irr_days will be computed
# if Irr_days is set, Irr_frequency is not necessary

Date_crop_day=[day(i) for i in Date_crop]
Irrigatable_days = Date_crop_day[1]-Date_crop_day[0] #doesn't include day of sowing nor the day of maturity
Irr_days = 7 #math.floor(Irrigatable_days/Irr_frequency) #the number of days with irrigation

Irr_MAX = 314.5
Irr_depth_interval = 5

"""
#-------------------------------------------------------------#
#
# main
#
#-------------------------------------------------------------#

def generate_SCHEDULES(Date_crop, Irr_MAX, Irr_days, Irr_depth_interval, FC):

	Date_crop_day=[day(i) for i in Date_crop]
	Irrigatable_days = Date_crop_day[1]-Date_crop_day[0] #doesn't include day of sowing nor the day of maturity

	title=str(Irr_MAX)+"_"+str(Irr_days)+"_"+str(Irr_depth_interval)
	if title in os.listdir(os.getcwd()+"/depth_days_int"):
	    print('Help, I\'m in here!')
	    return()
	    
	file = open(title, "w")

	# Scenarios

	if Irr_MAX%Irr_depth_interval<1:
		Irr_MAX+=1

	# List of total irrigation depths from 0 to Irr_MAX
	Irr_DEPTHS = range(0,int(math.floor(Irr_MAX)),Irr_depth_interval)
	
	# For each irrigation depth in Irr_DEPTHS, there is an associated list of all possible distributions of this irrigation depth in Irr_Schedules
	# i.e. IF Irr_DEPTHS[i]=x THEN SUM_k(Irr_SCHEDULES[i][j][k])=x for all j
	Irr_SCHEDULES = []

	for i in Irr_DEPTHS:

		Irr_depth = i//Irr_depth_interval   #Irrigation depth interval is 5mm

		##### partitions, partitions_0, combinations

		partitions=list(generate_partitions(Irr_depth))
	
		#remove those with more than Irr_days
		partitions_days=[]
		for j in partitions:	
			if len(j)<=Irr_days:
				partitions_days.append(j)
	
		#Each element has length Irr_days
	
		partitions_0=[i+[0]*(Irr_days-len(i)) for i in partitions_days]
		combinations_beta=[]
		for j in partitions_0:
			combinations_beta.extend(list(set(list(itertools.permutations(j)))))	
		combinations=[]	
		
		
		for j in combinations_beta:
			x=[Irr_depth_interval*k for k in j]
			if min([c<=100 for c in x]):
			    if not FC:
			        MORE=[[0,0,0],[0,30,0],[0,0,30],[0,30,30],[30,0,0],[30,30,0],[30,0,30],[30,30,30]]
			        for i in MORE:
			            MORE_0=[i+[0] for i in MORE]
			            MORE_1=[i+[30] for i in MORE]
			        for more in MORE_0+MORE_1:
			            combinations.append(more+x)
			            file.write(str(more+x)+"\n")
			    else:
			        combinations.append(x)
			        file.write(str(x)+"\n")
			        
		Irr_SCHEDULES.append(combinations)

	file.close()

	shutil.move(os.getcwd()+"/"+title, os.getcwd()+"/depth_days_int")


