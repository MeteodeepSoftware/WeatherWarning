import smtplib
server = smtplib.SMTP(‘smtp.gmail.com’, 587)
server.starttls()
server.login(“FromUser@gmail.com“, “FromUserPassword“)
msg = “This is a simple email test!”
server.sendmail(“FromUser@gmail.com“, “ToUser@gmail.com“, msg)
server.quit()
