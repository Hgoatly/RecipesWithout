import smtplib, ssl

smtp_server = "smtp.gmail.com"
port = 587
sender = "recipetest17@gmail.com"
password = input("Enter your password here:")
context = ssl.create_default_context()

try:
    server = smtp.SMTP(smtp_server, port)
    server.ehlo()
    server.starttls(context=context)
    
    server.login(sender, password)

    print("It worked")

except Exception as e:
    print(e)

finally:
    server.quit()