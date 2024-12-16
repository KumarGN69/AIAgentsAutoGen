from imap_tools import MailBox, AND
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()

MAIL_SERVER = os.getenv("IMAP_SERVER_SSL")
USER_ID= os.getenv("USER_ID")
USER_PWD = os.getenv("USER_PWD")
print(MAIL_SERVER,USER_ID,USER_PWD)

with MailBox(MAIL_SERVER).login(USER_ID,USER_PWD) as mailbox:
    for msg in mailbox.fetch():
        pprint(msg.subject)
