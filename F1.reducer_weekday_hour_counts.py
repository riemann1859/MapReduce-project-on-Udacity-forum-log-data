#!/usr/bin/env python                                                                                                                                                   
import sys                                                                                                                                                              
                                                                                                                                                                        
key=''                                                                                                                                                                  
count_weekday=0                                                                                                                                                         
count_hour=0                                                                                                                                                            
for line  in sys.stdin:                                                                                                                                                 
    items=line.strip().split('\t')                                                                                                                                      
    if len(items)!=2 or items[0][:-1]=='':                                                                                                                              
        continue                                                                                                                                                        
    else:                                                                                                                                                               
        if key=='':                                                                                                                                                     
            key=items[0][:-1]                                                                                                                                           
            if items[0][-1]=='h':                                                                                                                                       
                count_hour+=1                                                                                                                                           
            else:                                                                                                                                                       
                count_weekday+=1                                                                                                                                        
        else:                                                                                                                                                           
            if items[0][:-1]==key:                                                                                                                                      
                if items[0][-1]=='h':                                                                                                                                   
                    count_hour+=1                                                                                                                                       
                else:                                                                                                                                                   
                    count_weekday+=1                                                                                                                                    
            else:                                                                                                                                                       
                print("hour\t{x}\t{y}".format(x=key,y=count_hour))                                                                                                      
                print("weekday\t{x}\t{y}".format(x=key,y=count_weekday))                                                                                                
                key=items[0][:-1]                                                                                                                                       
                count_hour=0                                                                                                                                            
                count_weekday=0                                                                                                                                         
                if items[0][-1]=='h':                                                                                                                                   
                    count_hour+=1                                                                                                                                       
                else:                                                                                                                                                   
                    count_weekday+=1                                                                                                                                    
                                                                                                                                                                        
print("hour\t{x}\t{y}".format(x=key,y=count_hour))                                                                                                                      
print("weekday\t{x}\t{y}".format(x=key,y=count_weekday))  
