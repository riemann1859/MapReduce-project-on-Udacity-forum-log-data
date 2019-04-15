                                                                                                                                                                        
#!/usr/bin/env python                                                                                                                                                   
                                                                                                                                                                        
                                                                                                                                                                        
from datetime import datetime                                                                                                                                           
                                                                                                                                                                        
                                                                                                                                                                        
@outputSchema("date:tuple(weekday:int,hour:int)")                                                                                                                       
def finding_weekday_and_hour(datestring):                                                                                                                               
    date_string=datestring.replace('+00','')                                                                                                                            
    date=datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S.%f')                                                                                                         
    return date.weekday(), date.hour                                                                                                                                    
                                             
