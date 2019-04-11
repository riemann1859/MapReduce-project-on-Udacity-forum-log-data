#!/usr/bin/env python                                                                                                                                                   
                                                                                                                                                                        
import sys                                                                                                                                                              
                                                                                                                                                                        
                                                                                                                                                                        
tag=''                                                                                                                                                                  
count=0                                                                                                                                                                 
                                                                                                                                                                        
for line  in sys.stdin:                                                                                                                                                 
    items=line.strip().split('\t')                                                                                                                                      
    if len(items)!=2 or items[0]=='':                                                                                                                                   
        continue                                                                                                                                                        
    else:                                                                                                                                                               
        if items[0]!=tag:                                                                                                                                               
            if count==0:                                                                                                                                                
                print "Tag counts:"                                                                                                                                     
            else:                                                                                                                                                       
                print("{0}\t{1}".format(tag,count))                                                                                                                     
            tag=items[0]                                                                                                                                                
            count=1                                                                                                                                                     
        else:                                                                                                                                                           
            count+=1                                                                                                                                                    
                                                                                                                                                                        
                                                                                                                                                                        
print("{0}\t{1}".format(tag,count))    
