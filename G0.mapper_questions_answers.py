                                                                                                                                                                        
#!/usr/bin/python                                                                                                                                                       
                                                                                                                                                                        
import sys, csv, string                                                                                                                                                 
                                                                                                                                                                        
reader = csv.reader(sys.stdin, delimiter = '\t', quotechar='"')                                                                                                         
reader.next()                                                                                                                                                           
                                                                                                                                                                        
for line in reader:                                                                                                                                                     
                                                                                                                                                                        
    if len(line)!=19:                                                                                                                                                   
        continue                                                                                                                                                        
    else:                                                                                                                                                               
                                                                                                                                                                        
        if line[5] == 'question':                                                                                                                                       
            print '{0}\tQ'.format(line[0])                                                                                                                              
        elif line[5] == 'answer':                                                                                                                                       
            print '{0}\tA'.format(line[7])  
