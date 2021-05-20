# Day10-0518.py

import sys
import calendar
from datetime import datetime

if len(sys.argv) > 1:
    
    sFile = 'Resource/Memo.txt'
    sOption = sys.argv[1].replace('-','')
    sValue = sys.argv[2]
       
    f = open(sFile, "w", encoding='utf-8')
    
    if "a" in sOption:
        f.write(sValue.replace(' ','\n'))
        f.write('\n')
        
    elif "c" in sOption:
        today = datetime.today()
        f.write(calendar.TextCalendar(firstweekday=6).formatmonth(today.year, today.month))

    f.close()
    
    f = open(sFile, 'r', encoding='utf-8')
    print("Memo=", f.read())
    f.close()

