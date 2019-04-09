#!/usr/bin/python
import sys, csv, string                                                                                                                                                 
                                                                                                                                                                        
reader = csv.reader(sys.stdin, delimiter = '\t', quotechar='"')                                                                                                         
reader.next()                                                                                                                                                           
                                                                                                                                                                        
for line in reader:                                                                                                                                                     
                                                                                                                                                                        
    if len(line)!=19:                                                                                                                                                   
        continue                                                                                                                                                        
    else:                                                                                                                                                               
        node_type = line[5]                                                                                                                                             
        body = line[4]                                                                                                                                                  
        body_len = len(body)                                                                                                                                            
        node_id = line[0]                                                                                                                                               
        question_id = str(line[7])                                                                                                                                      
                                                                                                                                                                        
        if node_type == 'question':                                                                                                                                     
            print '{0}A\t{1}'.format(node_id, body_len)                                                                                                                 
        elif node_type == 'answer':                                                                                                                                     
            print '{0}B\t{1}'.format(question_id,body_len)  
