import shutil
import os
from kite_functions import day


#This creates a PRM file where all simulations have the same date range
#This is for creating multiple runs with different irrigation inputs, but same climate and soil data 

#.CLI, .TMP, .ETo, .PLU, .CO2, .CRO, .IRR, and .SOL files are all in ../Data

def generate_PRM(date, SCHEDULES, title, counter, cell, FC):

	#date should take the form [{start sim}(m, d, y),{stop sim}(m,d,y),{start crop}(m,d,y,),{stop crop}(m,d,y)]

	file = open(str(cell)+'_'+str(date[0][2])+'_'+title+'_'+counter+'.PRM', "w")
	data_folder = 'C:\\FAO\\AquaCrop\\DATA'
	
	for schedule in SCHEDULES:
		
		if schedule==SCHEDULES[0]:
			file.write("text\n")
			file.write("5.0\t: AquaCrop Version (June 2012)\n")
			
		file.write(str(day(date[0]))+"\t: First day of simulation period - "+str(date[0])+"\n")
		file.write(str(day(date[1]))+"\t: Last day of simulation period - "+str(date[1])+"\n")
		file.write(str(day(date[2]))+"\t: First day of cropping period - "+str(date[2])+"\n")
		file.write(str(day(date[3]))+"\t: Last day of cropping period - "+str(date[3])+"\n")
	
		if schedule==SCHEDULES[0]:
			#These parameters apply to all runs in PRM
			file.write("4\t: Evaporation decline factor for state II\n")
			file.write("1.10\t: Ke(x) Soil evaporation coefficient (fully wet and non-shaded)\n")
			file.write("5\t: Threshold for CC below HI can no longer increase (% cover)\n")
			file.write("70\t: Starting depth of root zone expansion curve (% of Zmin)\n")
			file.write("5.00\t: Maximum allowable root zone expansion (fixed at 5 cm/day)\n")
			file.write("-6\t: Shape factor for effect water stress on root zone expansion\n")
			file.write("20\t: Required soil water content in soil for germination (% TAW)\n")
			file.write("1.0\t: Adjustment factor for soil water depletion )p) by ETo\n")
			file.write("3\t: Number of days after which deficient aeration is fully effective\n")
			file.write("1.00\t: Exponent of senescence adjusting photosynthetic activity\n")
			file.write("12\t: Evaporation decline factor for state II\n")
			file.write("1\t: Evaporation decline factor for state II\n")
			file.write("30\t: Evaporation decline factor for state II\n")
			file.write("0.30\t: Evaporation decline factor for state II\n")
			file.write("1\t: Evaporation decline factor for state II\n")
			file.write("20\t: Evaporation decline factor for state II\n")
			file.write("100\t: Evaporation decline factor for state II\n")
			file.write("16\t: Evaporation decline factor for state II\n")
			file.write("12.0\t: Evaporation decline factor for state II\n")
			file.write("28.0\t: Evaporation decline factor for state II\n")
			file.write("3\t: Evaporation decline factor for state II\n")
	
		file.write("\t1.\tClimate (CLI)\n")
		file.write("\t\t"+str(cell)+'_'+str(date[0][2])+".CLI\n")
		file.write("\t\t"+data_folder+"\\"+str(cell)+"\\\n")
	
		file.write("\t1.1\tTemperature (TMP)\n")
		file.write("\t\t"+str(cell)+'_'+str(date[0][2])+".TMP\n")
		file.write("\t\t"+data_folder+"\\"+str(cell)+"\\\n")

		file.write("\t1.2\tReference ETo (ETo)\n")
		file.write("\t\t"+str(cell)+'_'+str(date[0][2])+".ETo\n")
		file.write("\t\t"+data_folder+"\\"+str(cell)+"\\\n")

		file.write("\t1.3\tRain (PLU)\n")
		file.write("\t\t"+str(cell)+'_'+str(date[0][2])+".PLU\n")
		file.write("\t\t"+data_folder+"\\"+str(cell)+"\\\n")

		file.write("\t1.4\tAtmospheric CO2 (CO2)\n")
		file.write("\t\tRCP8-5.CO2\n")
		file.write("\t\t"+data_folder+"\\\n")
		
		file.write("\t2.\tCrop (CRO) file\n")
		file.write("\t\t"+str(cell)+".CRO\n")
		file.write("\t\t"+data_folder+"\\"+str(cell)+"\\\n")	
	
		file.write("\t3.\tIrrigation (IRR) file\n")
		file.write("\t\t"+schedule+"\n")
		file.write("\t\tC:\\FAO\\IRR\\"+str(cell)+'\\'+str(date[0][2])+'\\'+title+"\\"+title+"_"+counter+"\\\n")
	
		file.write("\t4.\tManagement (MAN) file\n")
		file.write("\t\t(None)\n")
		file.write("\t\t(None)\n")
	
		file.write("\t5.\tSoil Profile (SOL) file\n")
		file.write("\t\t"+str(cell)+".SOL\n")
		file.write("\t\t"+data_folder+"\\"+str(cell)+"\\\n")
	
		file.write("\t6.\tGroundwater (GWT) file\n")
		file.write("\t\t(None)\n")
		file.write("\t\t(None)\n")
		
		file.write("\t7.\tInitial conditions (SW0) file\n")
		if FC:
		    file.write("\t\t(None)\n")
		    file.write("\t\t(None)\n")
		else:
		    file.write("\t\t"+str(cell)+"_"+str(date[0][2])+".SW0\n")
		    file.write("\t\t"+data_folder+"\\"+str(cell)+"\\\n")
	
		file.write("\t8.\tOff-season conditions (OFF) file\n")
		file.write("\t\t(None)\n")
		file.write("\t\t(None)\n")
	
	file.close()
	
def generate_PRM_generate(date, SCHEDULES, cell):

	#date should take the form [{start sim}(m, d, y),{stop sim}(m,d,y),{start crop}(m,d,y,),{stop crop}(m,d,y)]

	file = open(str(cell)+'_'+str(date[0][2])+'.PRM', "w")
	data_folder = 'C:\\FAO\\AquaCrop\\DATA'
	
	for schedule in SCHEDULES:
		
		if schedule==SCHEDULES[0]:
			file.write("9186 2003\n")
			file.write("5.0\t: AquaCrop Version (June 2012)\n")
			
		file.write(str(day(date[0]))+"\t: First day of simulation period - "+str(date[0])+"\n")
		file.write(str(day(date[1]))+"\t: Last day of simulation period - "+str(date[1])+"\n")
		file.write(str(day(date[2]))+"\t: First day of cropping period - "+str(date[2])+"\n")
		file.write(str(day(date[3]))+"\t: Last day of cropping period - "+str(date[3])+"\n")
	
		if schedule==SCHEDULES[0]:
			#These parameters apply to all runs in PRM
			file.write("4\t: Evaporation decline factor for state II\n")
			file.write("1.10\t: Ke(x) Soil evaporation coefficient (fully wet and non-shaded)\n")
			file.write("5\t: Threshold for CC below HI can no longer increase (% cover)\n")
			file.write("70\t: Starting depth of root zone expansion curve (% of Zmin)\n")
			file.write("5.00\t: Maximum allowable root zone expansion (fixed at 5 cm/day)\n")
			file.write("-6\t: Shape factor for effect water stress on root zone expansion\n")
			file.write("20\t: Required soil water content in soil for germination (% TAW)\n")
			file.write("1.0\t: Adjustment factor for soil water depletion )p) by ETo\n")
			file.write("3\t: Number of days after which deficient aeration is fully effective\n")
			file.write("1.00\t: Exponent of senescence adjusting photosynthetic activity\n")
			file.write("12\t: Evaporation decline factor for state II\n")
			file.write("1\t: Evaporation decline factor for state II\n")
			file.write("30\t: Evaporation decline factor for state II\n")
			file.write("0.30\t: Evaporation decline factor for state II\n")
			file.write("1\t: Evaporation decline factor for state II\n")
			file.write("20\t: Evaporation decline factor for state II\n")
			file.write("100\t: Evaporation decline factor for state II\n")
			file.write("16\t: Evaporation decline factor for state II\n")
			file.write("12.0\t: Evaporation decline factor for state II\n")
			file.write("28.0\t: Evaporation decline factor for state II\n")
			file.write("3\t: Evaporation decline factor for state II\n")
	
		file.write("\t1.\tClimate (CLI)\n")
		file.write("\t\t"+str(cell)+'_'+str(date[0][2])+".CLI\n")
		file.write("\t\t"+data_folder+"\\"+str(cell)+"\\\n")
	
		file.write("\t1.1\tTemperature (TMP)\n")
		file.write("\t\t"+str(cell)+'_'+str(date[0][2])+".TMP\n")
		file.write("\t\t"+data_folder+"\\"+str(cell)+"\\\n")

		file.write("\t1.2\tReference ETo (ETo)\n")
		file.write("\t\t"+str(cell)+'_'+str(date[0][2])+".ETo\n")
		file.write("\t\t"+data_folder+"\\"+str(cell)+"\\\n")

		file.write("\t1.3\tRain (PLU)\n")
		file.write("\t\t"+str(cell)+'_'+str(date[0][2])+".PLU\n")
		file.write("\t\t"+data_folder+"\\"+str(cell)+"\\\n")

		file.write("\t1.4\tAtmospheric CO2 (CO2)\n")
		file.write("\t\tRCP8-5.CO2\n")
		file.write("\t\t"+data_folder+"\\\n")
		
		file.write("\t2.\tCrop (CRO) file\n")
		file.write("\t\t9186.CRO\n")
		file.write("\t\t"+data_folder+"\\\n")	
	
		file.write("\t3.\tIrrigation (IRR) file\n")
		file.write("\t\t"+schedule+"\n")
		file.write("\t\tC:\\FAO\\Programs\\IRR\\Generate\\\n")
	
		file.write("\t4.\tManagement (MAN) file\n")
		file.write("\t\t(None)\n")
		file.write("\t\t(None)\n")
	
		file.write("\t5.\tSoil Profile (SOL) file\n")
		file.write("\t\tS1.SOL\n")
		file.write("\t\t"+data_folder+"\\\n")	
	
		file.write("\t6.\tGroundwater (GWT) file\n")
		file.write("\t\t(None)\n")
		file.write("\t\t(None)\n")
	
		file.write("\t7.\tInitial conditions (SW0) file\n")
		file.write("\t\t"+str(cell)+"_"+str(date[0][2])+".SW0\n")
		file.write("\t\t"+data_folder+"\\"+str(cell)+"\\\n")
	
		file.write("\t8.\tOff-season conditions (OFF) file\n")
		file.write("\t\t(None)\n")
		file.write("\t\t(None)\n")
	
	file.close()
	

	
	
