                                                                                                                                                                        
#!/usr/bin/env python                                                                                                                                                   
                                                                                                                                                                        
import sys                                                                                                                                                              
                                                                                                                                                                        
number_of_answers=0                                                                                                                                                     
id=''                                                                                                                                                                   
for line in sys.stdin:                                                                                                                                                  
    data=line.strip().split("\t")                                                                                                                                       
    if len(data)!=2 and data[0]!='':                                                                                                                                    
        continue                                                                                                                                                        
    else:                                                                                                                                                               
        if id=='':                                                                                                                                                      
            id=data[0]                                                                                                                                                  
            if data[1]=='A':                                                                                                                                            
                number_of_answers+=1                                                                                                                                    
        else:                                                                                                                                                           
            if id==data[0]:                                                                                                                                             
                if data[1]=='A':                                                                                                                                        
                    number_of_answers+=1                                                                                                                                
            else:                                                                                                                                                       
                print "{x}\t{y}".format(x=id,y=number_of_answers)                                                                                                       
                id=data[0]                                                                                                                                              
                number_of_answers=0                                                                                                                                     
                if data[1]=='A':                                                                                                                                        
                    number_of_answers+=1                                                                                                                                
                                                                                                                                                                        
                                                                                                                                                                        
print "{x}\t{y}".format(x=id,y=number_of_answers)                                                                                                                       
                                                     
