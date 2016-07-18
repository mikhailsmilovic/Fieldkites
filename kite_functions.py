#True if year is a leap year, False otherwise
def leap_year(year):
	
	if not (year % 400): #400 is a divisor of j
		return True
	elif not (year % 100): #100 is a divisor of j
		return False
	elif not (year % 4): #4 is a divisor of j
		return True
	else:
		return False

# Determines the days passed + 1 since January 1, 1901	
def day(date):

	day=0
	Month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
	
	for j in range(1901, date[2]):
		if leap_year(j):
			day+=366
		else:
			day+=365
	
	for j in range(0, date[1]-1):
		day+=Month_days[j]
		if j==1 and leap_year(date[2]):
			day+=1
	
	day += date[0]
	
	return day
	
def date(DAY):
    year=1901
    month=0
    day=0
    
    while DAY>366:
        if leap_year(year):
            DAY-=366
            Month_days = [31,29,31,30,31,30,31,31,30,31,30,31]
        else:
            DAY-=365
            Month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
        year+=1
    if DAY==366 and not leap_year(year):
        year+=1
        DAY-=365
    
    
    
    while DAY>Month_days[month]:
        DAY-=Month_days[month]
        month+=1
        
    day=DAY
    print(year)
    print(month+1)
    print(day)
    
    return (day,month+1,year)

# Constructs the list of partitions of n
# Source: http://jeromekelleher.net/partitions.php
# Use as a list, i.e. list(accelAsc(n))	
def generate_partitions(n):
    a = [0 for i in range(n + 1)]
    k = 1
    y = n - 1
    while k != 0:
        x = a[k - 1] + 1
        k -= 1
        while 2*x <= y:
            a[k] = x
            y -= x
            k += 1
        l = k + 1
        while x <= y:
            a[k] = x
            a[l] = y
            yield a[:k + 2]
            x += 1
            y -= 1
        a[k] = x + y
        y = x + y - 1
        yield a[:k + 1]