#!/usr/bin/env python                                                                                                                                                   
                                                                                                                                                                        
import sys                                                                                                                                                              
import csv                                                                                                                                                              
from datetime import datetime                                                                                                                                           
reader=csv.reader(sys.stdin, delimiter='\t',quotechar='"')                                                                                                              
next(reader)                                                                                                                                                            
                                                                                                                                                                        
for line in reader:                                                                                                                                                     
    if len(line)!=19:                                                                                                                                                   
                                                                                                                                                                        
        continue                                                                                                                                                        
    else:                                                                                                                                                               
                                                                                                                                                                        
        date_string=line[8].replace('+00','')                                                                                                                           
        user_id=line[3]                                                                                                                                                 
        date=datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S.%f')                                                                                                     
        print("{x}\t{y}".format(x=user_id,y=date.hour))                                                                                                                 
                                                         
