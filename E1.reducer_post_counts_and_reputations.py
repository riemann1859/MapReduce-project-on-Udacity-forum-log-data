                                                                                                                                                                        
#!/usr/bin/env python                                                                                                                                                   
import sys                                                                                                                                                              
id=''                                                                                                                                                                   
count=0                                                                                                                                                                 
reputation="no score"                                                                                                                                                   
for line  in sys.stdin:                                                                                                                                                 
    items=line.strip().split('\t')                                                                                                                                      
    if len(items)!=2 or items[0][:-1]=='':                                                                                                                              
        continue                                                                                                                                                        
    else:                                                                                                                                                               
        if id=='':                                                                                                                                                      
            print("id\ttotal number of posts\treputation")                                                                                                              
            id=items[0][:-1]                                                                                                                                            
            if items[0][-1]=='A':                                                                                                                                       
                count+=1                                                                                                                                                
            else:                                                                                                                                                       
                reputation=items[1]                                                                                                                                     
        else:                                                                                                                                                           
            if items[0][:-1]==id:                                                                                                                                       
                if items[0][-1]=='A':                                                                                                                                   
                    count+=1                                                                                                                                            
                else:                                                                                                                                                   
                    reputation=items[1]                                                                                                                                 
            else:                                                                                                                                                       
                print("{0}\t{1}\t{2}".format(id,count,reputation))                                                                                                      
                id=items[0][:-1]                                                                                                                                        
                reputation='no score'                                                                                                                                   
                count=0                                                                                                                                                 
                if items[0][-1]=='A':                                                                                                                                   
                    count+=1                                                                                                                                            
                else:                                                                                                                                                   
                    reputation=items[1]                                                                                                                                 
                                                                                                                                                                        
print("{0}\t{1}\t{2}".format(id,count,reputation)) 
