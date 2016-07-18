from generate_SCHEDULES import generate_SCHEDULES
from generate_IRR import generate_IRR
from generate_PRM import generate_PRM, generate_PRM_generate
from kite_functions import day, date
from growing_season import growing_season
from generate_SW0 import generate_SW0
import math
import os, shutil
import time
start_time = time.time()

#---- Setup ----
FC=True #True=Initial soil moisture is at field capacity, False=Soil moisture determined otherwise, such as according to simulated soil moisture

#Either Irr_days or Irr_frequency is set

Irr_days = 9 #with soil moisture, make it 7-8, with FC make it 9+
choice='days'

"""
Irr_frequency = #This is a maximum, namely, irrigation is at least as often as every n days.
choice='frequency'
# Irrigation will occur if Irr_frequency is a divisor of the day.
"""


Irr_depth_interval = 30
Irr_MAX = 180 #with soil moisture, make it 320, with FC make it <300

for cell in [435]: #[167,208,227,255,266,349,435,451,478]:
    for year in range(2003, 2003+1):

        #Generate yearly TMP files if not already done
        
        #Establish the beginning of the growing season
        DAYS=growing_season(cell, year)
        Date_crop=[date(DAYS[0]),date(DAYS[1])]
        Date_crop_day=[day(i) for i in Date_crop]

        #Establish the soil moisture for the day of sowing
        if str(cell)+'_'+str(year)+'.SW0' not in os.listdir('C:\\FAO\\AquaCrop\\DATA\\'+str(cell)+'\\'):
            generate_SW0(Date_crop[0], cell)

        #Determines Irr_days anf Irr_frequency
        Irrigatable_days = Date_crop_day[1]-Date_crop_day[0] #doesn't include day of sowing nor the day of harvest

        if choice=='frequency':
            Irr_days = int(math.floor(Irrigatable_days/Irr_frequency)) #the number of days with irrigation
        elif choice=='days':
            Irr_frequency = math.ceil(Irrigatable_days/(Irr_days+1))

        print("Irr_days: "+str(Irr_days)+'\n')
        print("Irr_frequency: "+str(Irr_frequency))
    
        generate_SCHEDULES(Date_crop, Irr_MAX, Irr_days, Irr_depth_interval, FC)
        title_end=str(Irr_MAX)+"_"+str(Irr_days)+"_"+str(Irr_depth_interval)
    
    
        title='C:\\FAO\\Programs\\depth_days_int\\'+title_end
        file = open(title, 'r')
        
        if str(cell) not in os.listdir('C:\\FAO\\Programs\\IRR\\'):
            os.mkdir('C:\\FAO\\Programs\\IRR\\'+str(cell))
        if str(cell) not in os.listdir('C:\\FAO\\Programs\\PRM\\'):
            os.mkdir('C:\\FAO\\Programs\\PRM\\'+str(cell))
        
    
        #Make folder for years if it doesn't yet exist
        if str(year) not in os.listdir('C:\\FAO\\Programs\\IRR\\'+str(cell)):
            os.mkdir('C:\\FAO\\Programs\\IRR\\'+str(cell)+'\\'+str(year))
        if str(year) not in os.listdir('C:\\FAO\\Programs\\PRM\\'+str(cell)):
            os.mkdir('C:\\FAO\\Programs\\PRM\\'+str(cell)+'\\'+str(year))
        
        if title_end not in os.listdir('C:\\FAO\\Programs\\IRR\\'+str(cell)+'\\'+str(year)+'\\'):
            os.mkdir('C:\\FAO\\Programs\\IRR\\'+str(cell)+'\\'+str(year)+'\\'+title_end)
    
            num_lines = sum(1 for line in file)
            num_programs = int(math.ceil(num_lines/125.))
    
            digits = int(math.log10(num_programs))+1
            digits_string="%0"+str(digits)+"d"
    
            for i in range(num_programs):    
                os.mkdir('C:\\FAO\\Programs\\IRR\\'+str(cell)+'\\'+str(year)+'\\'+title_end+'\\'+title_end+'_'+digits_string%i)
        
            file = open(title, 'r')
            counter=0 
            for line in file:
    
                schedule=eval(line)
                filename=generate_IRR(schedule, Irr_frequency, Irrigatable_days, FC)
                shutil.move(os.getcwd()+'\\'+filename, 'C:\\FAO\\Programs\\IRR\\'+str(cell)+'\\'+str(year)+'\\'+title_end+'\\'+title_end+'_'+ digits_string%(int(math.floor(counter/125.))))
                counter+=1
    
        SCHEDULES_125=[os.listdir('C:\\FAO\\Programs\\IRR\\'+str(cell)+'\\'+str(year)+'\\'+title_end+'\\'+i) for i in os.listdir('C:\\FAO\\Programs\\IRR\\'+str(cell)+'\\'+str(year)+'\\'+title_end)]
        os.mkdir('C:\\FAO\\Programs\\PRM\\'+str(cell)+'\\'+str(year)+'\\'+title_end+'\\')
    
        for i in range(len(SCHEDULES_125)):
            generate_PRM(Date_crop*2, SCHEDULES_125[i], title_end, digits_string%i, cell, FC)
            shutil.move(os.getcwd()+'/'+str(cell)+'_'+str(Date_crop[0][2])+'_'+title_end+'_'+str(digits_string%i)+'.PRM', 'C:\\FAO\\Programs\\PRM\\'+str(cell)+'\\'+str(year)+'\\'+title_end+'\\')

print("--- %s seconds ---" % (time.time() - start_time))



	



	


