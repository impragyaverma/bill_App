import smtplib
import config_bill_var

Email_Address = config_bill_var.Email_Address_sender
Password = config_bill_var.Password_sender

def send_email():
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()

            smtp.login(Email_Address, Password)

            subject = "Thank you for visiting test retail shop"
            body = config_bill_var.mail_body

            msg = f'Subject: {subject} \n\n {body}'

            smtp.sendmail(Email_Address, config_bill_var.reciever_email_address, msg)

    except Exception as e:
        print(f"An exception occurred: {e}")

send_email()
