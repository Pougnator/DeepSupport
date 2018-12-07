import logging
from GetEmail import readmail

def isFromApp(message):
    startflag = "Detailed description of your issue:" 
    endflag= "Phone brand and model:" 
    intstart = message.find(startflag)
    intend = message.find(endflag)
    logging.debug(intstart)
    logging.debug(intend)
    
    if intstart==-1 or intend ==-1 :
        logging.info("This is not a message from app")
        return False, message
        
    else:
        logging.info("This is a message from app")
        body = message[intstart:intend]
        logging.debug("The body is: %s", body)
        return True, body

    



if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    #print(readmail())
    isFromApp(readmail())
