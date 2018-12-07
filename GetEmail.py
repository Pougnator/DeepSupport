import email
import imaplib
import smtplib
import time
import quopri
import logging


ORG_EMAIL   = "@gmail.com"
FROM_EMAIL  = "arodiono" + ORG_EMAIL
FROM_PWD    = "12AZqswx"
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT   = 993


def readmail():
    try:
        # mail reading logic will come here !!
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(FROM_EMAIL,FROM_PWD)
        logging.info("Gmail connection success")
        logging.debug(mail.list())
        logging.debug(type(mail))
        mail.select('INBOX')
        #mail.select("[Gmail]/Sent Mail")
        email_type, data = mail.search(None, 'ALL')
        mail_ids = data[0]
        id_list = mail_ids.split()
        logging.debug(id_list)

        first_email_id = id_list[0]
        latest_email_id = id_list[-1]
    except: 
        logging.info("Failed getting emails from gmail") 

    if int(latest_email_id) > 0:
        print('Success: Inbox is not empty and contains ' + str(int(latest_email_id)) + " emails")
        try:
            typ, my_data = mail.fetch(id_list[-1], '(RFC822)' )
            logging.info("raw_email fetched")
            email_body = my_data[0][1].decode("utf-8")
            email_message = email.message_from_string(email_body)
        
            if email_message.is_multipart():
                logging.debug("the message is multipart")
                for part in email_message.walk():
                    logging.info("%s, %s" % (part.get_content_type(), part.get_content_charset()))
                    if part.get_content_type() == "text/plain": # ignore attachments/html
                        logging.info("getting text from a multipart message")
                        body = part.get_payload(decode = True)
                        text_body = body.decode(part.get_content_charset())
                        logging.info(text_body)
                            
                        
                    else:
                        continue
            elif email_message.get_content_type() == 'text':
                logging.debug("the message is single part")
                body=email_message.get_payload(decode=False)
                #text_body = body.decode(part.get_content_charset())
            
            else:
                logging.info("The message is not multipart, nor is it a single text message")
                return "nothing"
            
            logging.debug("The type of the email body is: %s", type(body))
            return text_body
        except: 
            logging.info("Failed fetching and decoding the email")
        
    else: 
        return "nothing"
    
  



#print(readmail())
if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    print(readmail())
    