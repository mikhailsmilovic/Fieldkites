from kite_functions import leap_year, day

#input is a cell and year

def growing_season(cell, year):
    #from growing_season import growing_season
    begin=(1,1,year)
    
    file = open("C:\\FAO\\Aquacrop\\DATA\\"+str(cell)+'\\'+str(cell)+'_'+str(year)+'.TMP', 'r')
    lines=file.readlines()[8:]
    file.close()
    
    lines_corrected=[[i.split()[0], i.split()[-1]] for i in lines]
    
    # The start of the growing season is determined as the day following 5 consecutive days of average temperature greater than or equal to 5 degrees celsius    
    
    # Start planting after March 15, so start searching on March 10
    if leap_year(year):
        days_before=31+29+9
    else:
        days_before=31+28+9
    
    averages=[min(int((float(i[0])+float(i[1]))//2), 5) for i in lines_corrected]
    GDD=[max((float(i[0])+float(i[1]))/2.-5, 0) for i in lines_corrected]
        
    consecutive=averages[days_before:days_before+5]

    warm=False
    while not warm:

        if consecutive == [5]*5:
            warm=True
        else:
            days_before+=1
            consecutive = averages[days_before:days_before+5]
            
    #count+5 is the sowing date
    sowing_0=days_before+5
    sowing=day(begin)+sowing_0
    
    harvest_0=sowing_0+1
    gdd=GDD[harvest_0]
    while gdd<1100:
        
        harvest_0+=1
        gdd+=GDD[harvest_0]
        
        
    harvest=day(begin)+harvest_0

    return [sowing, harvest]

    
    