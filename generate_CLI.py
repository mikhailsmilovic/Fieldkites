import shutil
import os
from kite_functions import leap_year

def generate_CLI(cell):
    
    file_r = open("C:\\FAO\\AquaCrop\\DATA\\"+str(cell)+"\\"+str(cell)+".TMP", 'r')
    lines=file_r.readlines()
    file_r.close()
    year_0=int(lines[4].split()[0])
    LINES=lines[9:]
    years=len(LINES)/365
    DAYS=0

    for year in range(year_0, year_0+years):

        file = open(str(cell)+'_'+str(year)+'.CLI', "w")
        file.write("\n")
        file.write(" 5.0   : AquaCrop Version (June 2012) -Program by Mikhail \n")
        file.write(str(cell)+'_'+str(year)+".TMP\n")
        file.write(str(cell)+'_'+str(year)+".ETo\n")
        file.write(str(cell)+'_'+str(year)+".PLU\n")
        file.write("RCP8-5.CO2\n")
        
        file.close()
        shutil.move(os.getcwd()+'/'+str(cell)+'_'+str(year)+'.CLI', 'C:\\FAO\\AquaCrop\\DATA\\'+str(cell)+'\\')

    
    for ending in ['ETo', 'TMP', 'PLU']:
        file_r = open('C:\\FAO\\AquaCrop\\DATA\\'+str(cell)+'\\'+str(cell)+"."+ending, 'r')
        lines=file_r.readlines()
        file_r.close()
        year_0=int(lines[4].split()[0])
        LINES=lines[9:]
        years=len(LINES)/365
        DAYS=0
        for year in range(year_0, year_0+years):
            
            file = open(str(cell)+'_'+str(year)+'.'+ending, "w")

            file.write("Canada - daily data: 1 January 1950 - 31 December 2010 \n")
            file.write("\t1\t:\tDaily records (1=daily, 2=10-daily and 3=monthly data) \n")
            file.write("\t1\t:\tFirst day of record (1, 11 or 21 for 10-day or 1 for months) \n")
            file.write("\t1\t:\tFirst month of record \n")
            file.write(str(year)+"\t:\tFirst year of record (1901 if not linked to a specific year) \n")
            file.write(ending+" \n")
            file.write("======================= \n\n")
            
            if leap_year(year):
                days=366
            else:
                days=365
                
            counter=0
            for i in LINES[DAYS: DAYS+days]:
                file.write(i)
                counter+=1
                
            DAYS+=days
            file.close()
            shutil.move(os.getcwd()+'/'+str(cell)+'_'+str(year)+'.'+ending, 'C:\\FAO\\AquaCrop\\DATA\\'+str(cell)+'\\')
            
            #from generate_CLI import generate_CLI
    
   