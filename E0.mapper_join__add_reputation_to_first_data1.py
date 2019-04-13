#!/usr/bin/env python                                                                                                                                                   
                                                                                                                                                                        
import sys                                                                                                                                                              
import csv                                                                                                                                                              
reader = csv.reader(sys.stdin, delimiter = '\t', quotechar='"')                                                                                                         
                                                                                                                                                                        
for line in reader:                                                                                                                                                     
    if len(line)==19:                                                                                                                                                   
        try:                                                                                                                                                            
            author_id=int(line[3])                                                                                                                                      
            print("{x}A\t1".format(x=author_id))                                                                                                                        
        except:                                                                                                                                                         
            pass
    elif len(line)==5:                                                                                                                                                  
        try:                                                                                                                                                            
            rep=int(line[1])                                                                                                                                            
            print("{x}B\t{y}".format(x=line[0], y=rep))                                                                                                                 
        except:                                                                                                                                                         
            pass
