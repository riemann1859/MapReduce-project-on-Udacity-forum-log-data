                                                                                                                                                                        
#!/usr/bin/env python                                                                                                                                                   
                                                                                                                                                                        
import sys                                                                                                                                                              
import csv                                                                                                                                                              
reader = csv.reader(sys.stdin, delimiter = '\t', quotechar='"')                                                                                                         
reader.next()                                                                                                                                                           
for line in reader:                                                                                                                                                     
    if len(line)!=19:                                                                                                                                                   
        continue                                                                                                                                                        
    else:                                                                                                                                                               
        if line[5]=='question':                                                                                                                                         
            tags=line[2].strip().split(' ')                                                                                                                             
            for tag in tags:                                                                                                                                            
                print("{x}\t1".format(x=tag))   
