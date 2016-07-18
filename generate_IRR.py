import shutil
import os
import math
import itertools

def generate_IRR(schedule, frequency, Irrigatable_days, FC):
        
	total_irrigation_depth = str(sum(schedule))
	irrigation_days = str(len(schedule))
	
	title=total_irrigation_depth+"_"+irrigation_days+"_"
	for i in schedule:
		title+=str(i)+"."
	title+="IRR"
	
	file = open(title, "w")
	
	Irr_days =int(math.floor(Irrigatable_days/frequency)) #the number of days with irrigation

        if not FC:
            frequency = math.ceil((Irrigatable_days-(16))/(Irr_days+1))
        
        file.write("Total irrigation depth: "+total_irrigation_depth+"mm, Irrigation frequency: every "+str(frequency)+" days, and Distribution schedule: "+str(schedule)+"\n")
	file.write("\t4.0\t: AquaCrop Version (June 2012)\n")
	file.write("\t1\t: Sprinkler irrigation\n")
	file.write("\t100\t: Percentage of soil surface wetted by irrigation\n")
	file.write("\t1\t: Irrigation schedule\n\n")
	file.write("\tDay\tDepth (mm)\tECw (dS/m)\n")
	file.write("=============================================\n")
	
	if not FC:
	    days_irrigated=['1','6','11','16']+[str(frequency*(i)+16) for i in range(1,len(schedule)+1)]
	else:
	    days_irrigated=[str(frequency*(i)) for i in range(1,len(schedule)+1)]
	
	for i in range(0,len(schedule)):
	    file.write("\t"+days_irrigated[i]+"\t"+str(schedule[i])+"\t\t0.0\n")
	file.close()
	
	return title
	
	shutil.move(os.getcwd()+'/'+title, os.getcwd()+'/IRR')

"""
def generate_IRR_RAWFC():
	
	RAW=[80,90,95,100,105,110,120,125,130]
	#FC=[ 0,-10, -20, -30, -35, -40, -45, -50]
	FC=[10,20,25,30,35,40,45]
	
	MAIN=list(itertools.product(RAW, FC))
        for main in MAIN:
            
            title='RAW'+str(main[0])+'_FCm'+str(main[1])+'.IRR'
            file = open(title, "w")
            file.write(title+"\n")
            file.write("\t5.0\t: AquaCrop Version (October 2015)\n")
            file.write("\t1\t: Sprinkler irrigation\n")
            file.write("\t100\t: Percentage of soil surface wetted by irrigation\n")
            file.write("\t2\t: Generate irrigation schedule\n")
            file.write("\t3\t: Time criterion = allowable fraction of RAW\n")
            file.write("\t2\t: Depth criterion = back to FC\n\n") #2 Fixed aplication depth
            
            file.write("\tFrom day\tDepleted RAW (%)\tBack to FC(+/- mm)\tECw (dS/m)\n")
            file.write("=================================================================================\n")
            file.write("\t1\t\t"+str(main[0])+"\t\t\t"+str(main[1])+"\t\t\t0.0\n")
            
            file.close()
            shutil.move(os.getcwd()+'/'+title, os.getcwd()+'/IRR/Generate')
"""