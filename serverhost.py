import smtplib
server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login( 'kumabaskerice@gmail.com', #password )