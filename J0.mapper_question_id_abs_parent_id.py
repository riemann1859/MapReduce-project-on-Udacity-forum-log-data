#!/usr/bin/env python                                                                                                                                                       
                                                                                                                                                                        
import sys, csv                                                                                                                                            
                                                                                                                                                                        
reader = csv.reader(sys.stdin, delimiter = '\t', quotechar='"')                                                                                                         
reader.next()                                                                                                                                                           
                                                                                                                                                                        
for line in reader:                                                                                                                                                     
                                                                                                                                                                        
    if len(line)!=19:                                                                                                                                                   
        continue                                                                                                                                                        
    else:                                                                                                                                                               
        node_type = line[5]                                                                                                                                             
        node_id = line[0]                                                                                                                                               
        abs_parent_id = line[7]                                                                                                                                         
                                                                                                                                                                        
        if node_type == 'question':                                                                                                                                     
            print '{0}\tA'.format(node_id)                                                                                                                              
        else:                                                                                                                                                           
            print '{0}\tB'.format(abs_parent_id)                                                                                                                        
                                                   
