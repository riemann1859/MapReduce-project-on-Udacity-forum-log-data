#!/usr/bin/python

                                                                                                                                                                        
import sys                                                                                                                                                              
                                                                                                                                                                        
                                                                                                                                                                        
id=''                                                                                                                                                                   
count=0                                                                                                                                                                 
sum=0.0                                                                                                                                                                 
length_question_post=0                                                                                                                                                  
                                                                                                                                                                        
for line  in sys.stdin:                                                                                                                                                 
    items=line.strip().split('\t')                                                                                                                                      
    if len(items)!=2:                                                                                                                                                   
        continue                                                                                                                                                        
    else:                                                                                                                                                               
                                                                                                                                                                        
        if items[0][-1]=='A':                                                                                                                                           
                                                                                                                                                                        
            if count!=0:                                                                                                                                                
                print("{0}\t{1}\t{2}".format(id,length_question_post,sum/count))                                                                                        
            else:                                                                                                                                                       
                if id!='':                                                                                                                                              
                                                                                                                                                                        
                    print("{0}\t{1}\t{2}".format(id,length_question_post,0))                                                                                            
                else:                                                                                                                                                   
                    print("question_id\tquestion length\taverage answer length" )                                                                                       
                                                                                                                                                                        
            sum=0.0                                                                                                                                                     
            count=0                                                                                                                                                     
            id=items[0][:-1]                                                                                                                                            
            length_question_post=int(items[1])                                                                                                                          
        elif items[0][-1]=='B':                                                                                                                                         
            count+=1                                                                                                                                                    
            sum+=int(items[1]) 
            
if count==0:                                                                                                                                                            

    print("{0}\t{1}\t{2}".format(id,length_question_post,0))                                                                                                            
else:                                                                                                                                                                   
    print("{0}\t{1}\t{2}".format(id,length_question_post,sum/count))  
