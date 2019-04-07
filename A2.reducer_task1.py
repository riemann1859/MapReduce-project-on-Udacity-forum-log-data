#!/usr/bin/python                                                                                                                                                       
                                                                                                                                                                        
import sys                                                                                                                                                              
                                                                                                                                                                        
users={}                                                                                                                                                                
for line in sys.stdin:                                                                                                                                                  
    items=line.strip().split("\t")                                                                                                                                      
    if len(items)!=2:                                                                                                                                                   
        continue                                                                                                                                                        
    else:                                                                                                                                                               
        items[1]=[int(x) for x in items[1].strip('[').strip(']').split(',')]                                                                                            
        if items[0] not in users.keys():                                                                                                                                
            users[items[0]]=items[1]                                                                                                                                    
        else:                                                                                                                                                           
            users[items[0]]=[a+b for a,b in zip(users[items[0]],items[1])]                                                                                              
                                                                                                                                                                        
                                                                                                                                                                        
for user, activity_list in  users.items():                                                                                                                              
    max_=max(activity_list)                                                                                                                                             
    if activity_list.count(max_)==1:                                                                                                                                    
        print("{x}\t{y}".format(x=user,y=activity_list.index(max_)))                                                                                                    
    else:                                                                                                                                                               
        for ind,num in enumerate(activity_list):                                                                                                                        
            if  num==max_:                                                                                                                                              
                print("{x}\t{y}".format(x=user,y=ind))                                                                                                                  
                                                                                                                                                                        
                                                   
