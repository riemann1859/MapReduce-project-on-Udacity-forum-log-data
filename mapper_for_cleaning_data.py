                                                                                                                                                                        
#!/usr/bin/env python                                                                                                                                                   
                                                                                                                                                                        
import sys                                                                                                                                                              
import csv                                                                                                                                                              
                                                                                                                                                                        
reader=csv.reader(sys.stdin, delimiter='\t',quotechar='"')                                                                                                              
writer=csv.writer(sys.stdout, delimiter='\t',quotechar='"')                                                                                                             
                                                                                                                                                                        
for line in reader:                                                                                                                                                     
    if len(line)!=19:                                                                                                                                                   
                                                                                                                                                                        
        continue                                                                                                                                                        
    else:                                                                                                                                                               
         
         # delete any newline characters 
                                                                                                                                                                        
        line=[str(item).replace('\n','').replace('\r','').replace('\r\n','').replace('<br>','') for item in line]    
        
        
        
        writer.writerow(line)                                                                                                                                           
                                
