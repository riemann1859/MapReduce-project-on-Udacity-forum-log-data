#!/usr/bin/env python                                                                                                                                                   
# the above line must be in the first line, not second or below!, in hadoop streaming                                                                                                                                                                        
import sys                                                                                                                                                              
                                                                                                                                                                        
users=dict()                                                                                                                                                            
                                                                                                                                                                        
for line in sys.stdin:                                                                                                                                                  
    items=line.strip().split("\t")                                                                                                                                      
    if items[0] not in users.keys():                                                                                                                                    
        users[items[0]]=[0]*24                                                                                                                                          
        users[items[0]][int(items[1])]=1                                                                                                                                
    else:                                                                                                                                                               
        users[items[0]][int(items[1])]+=1                                                                                                                               
                                                                                                                                                                        
                                                                                                                                                                        
for user, activity_list in  users.items():                                                                                                                              
                                                                                                                                                                        
    print("{x}\t{y}".format(x=user,y=activity_list))                                                                                                                    
                                                         
