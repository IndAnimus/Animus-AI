####################################################################
#    Animus AI Developed by Kuldeep Paul Dated 13th March 2018     #
####################################################################

import smtplib
import time
import imaplib
import email
from EchoSkill import echo

ORG_EMAIL   = "@gmail.com"
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT   = 993

def MailSkill(username, password):
    try:
        echo("Sir, I activated the Mail Skill.")
        mail_id = username + ORG_EMAIL

        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(mail_id, password)
        mail.select('inbox')
        echo("Sir, I logged in into your gmail Account")
        type, data = mail.search(None, 'ALL')
        mail_ids = data[0]

        id_list = mail_ids.split()   
        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])


        for i in range(latest_email_id,first_email_id, -1):
            typ, data = mail.fetch(i, '(RFC822)' )
            echo("Sir, I am trying to fetch your mails.") 
            for response_part in data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_string(response_part[1])
                    email_subject = msg['subject']
                    email_from = msg['from']
                    print 'From : ' + email_from + '\n'
                    print 'Subject : ' + email_subject + '\n'
                    echo("Sir, you received a mail from" + email_from + "having the subject" + email_subject)
        echo("Sir, there are no more mails in your account.")

    except Exception, e:
        echo(str(e))

    return 0

######################################################################
#Mail Reading Skill in Animus AI                                     #
#Copyright Kuldeep Paul                                              #
######################################################################

