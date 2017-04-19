# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText
'''
# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.
fp = open('textfile.txt', 'rb')
# Create a text/plain message
#msg = MIMEText(fp.read())
fp.close()

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = 'The contents of %s' %('textfile')
msg['From'] = 'aghilan@abyres.net'
msg['To'] = 'aghilannara@gmail.com'
'''
# Send the message via our own SMTP server, but don't include the
# envelope header.
msg ="Done!"
s = smtplib.SMTP('smtp.gmail.com:587')
s.starttls()
s.login('aghilan@abyres.net','aghilan123')
s.sendmail('aghilan@abyres.net', 'aghilannara@gmail.com', msg)
s.quit()
