import os
from pprint import pprint

from dotenv import load_dotenv
from imap_tools.mailbox import MailBox


load_dotenv()

MAIL_SERVER = os.getenv("IMAP_SERVER_SSL")
USER_ID= os.getenv("USER_ID")
USER_PWD = os.getenv("USER_PWD")
print(MAIL_SERVER,USER_ID,USER_PWD)

with MailBox(MAIL_SERVER).login(USER_ID,USER_PWD,"INBOX") as mailbox:
    for msg in mailbox.fetch():
        pprint(msg.subject)
