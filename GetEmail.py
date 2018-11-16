import email
import imaplib
import smtplib
import time
import quopri

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
        print("Gmail connection success")
        print(mail.list())
        print(type(mail))
        mail.select('INBOX')
        #mail.select("[Gmail]/Sent Mail")
        email_type, data = mail.search(None, 'ALL')
        mail_ids = data[0]
        id_list = mail_ids.split()
        #print(id_list)

        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])
        
        if latest_email_id > 0:
            print('Success: Inbox is not empty and contains ' + str(latest_email_id) + " emails")

        typ, my_data = mail.fetch(id_list[-1], '(RFC822)' )
        email_body = my_data[0][1].decode("utf-8")
        email_message = email.message_from_string(email_body)
        
        if email_message.is_multipart():
            for part in email_message.walk():
                if part.get_content_type() == "text/plain": # ignore attachments/html
                    body = part.get_payload(decode=False)
                   
                else:
                    continue
        else:
            body=email_message.get_payload(decode=False)
        print("The type of the email body is: ")
        print(type(body))
        print(body)
        #print(quopri.decodestring(body).decode("utf_8"))
        #return quopri.decodestring(body).decode("utf_8")
        return body
    except: 
        print("Failed")



#print(readmail())
if __name__ == '__main__':
    print(readmail())
    