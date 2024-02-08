#import smtplib, ssl
#
#port = 587  # For starttls
#smtp_server = "smtp.gmail.com"
#sender_email = "abcanonymus42@gmail.com"
#receiver_email = "abcanonymus42@gmail.com"
#password = input("Type your password and press enter:")
#message = """\
#Subject: Hi there
#
#This message is sent from Python."""
#
#context = ssl.create_default_context()
#with smtplib.SMTP(smtp_server, port) as server:
#    server.ehlo()  # Can be omitted
#    server.starttls(context=context)
#    server.ehlo()  # Can be omitted
#    server.login(sender_email, password)
#    for i in range(20):
#        server.sendmail(sender_email, receiver_email, message)
import email, smtplib, ssl,csv

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd

subject = "Bilingual Children Book Live Reading For Your Latin American Students"
body = """Good Afternoon Ms/Mr {name}
My name is Raúl Jimenez. I am a writer from Tampico Tamaulipas, Mexico. I am reaching you today, because a few weeks ago, a school on Wisconsin contacted me because one of the teachers wanted me to do a live reading of my book to the children.
I really enjoyed the experience, so right now I am trying to reach more schools that may have Mexican American children.
What I would like, its reading to the students trough zoom or google meet, and that the teachers put information about me and my books on the wall of the classroom like they did in Wisconsin, to promote my work to the parents.
I work from 11 am to 11 pm, but I am free during the early hours of the day, and if by any way, you are not the one who can decide this, can you pass my message to the one who handle this kind of things in your school?
As I am not American, and know almost nothing about schools there, I had to search through the internet manually for elementary schools, and I do not know how you handle this kind of things on the US education system.
Anyway, I’ll let some photos of my happy costumers, one of them was the ex ambassador of the United States of America in Mexico, and if you want to reach me, you can just reply this email.
Amazon Author page: https://www.amazon.com/Ra%C3%BAl-Jim%C3%A9nez/e/B078V2PPLV/ref=dp_byline_cont_book_1
Facebook author page: https://www.facebook.com/Mexislang"""
sender_email = "blackmacuahuitl@gmail.com"
receiver_email = "abcanonymus42@gmail.com"
password = "Supernintendo64"

# Create a multipart message and set headers


# Log in to server using secure context and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    message = MIMEMultipart()
    message["Subject"] = subject
     # Recommended for mass emails
    
    # Add body to email
    filename = "1.jpg"
    with open(filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read()) 
    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )
    message.attach(part)
    filename1 = "2.jpg"
    with open(filename1, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read()) 
    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename1}",
    )
    message.attach(part)
    filename = "3.jpg"
    with open(filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read()) 
    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )
    message.attach(part)
    filename1 = "4.jpg"
    with open(filename1, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read()) 
    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename1}",
    )
    message.attach(part)
    filename = "5.jpg"
    with open(filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read()) 
    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )
    message.attach(part)
    filename1 = "6.jpg"
    with open(filename1, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read()) 
    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename1}",
    )
    message.attach(part)
    filename = "7.jpeg"
    with open(filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read()) 
    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )
    message.attach(part)
    filename1 = "8.jpeg"
    with open(filename1, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read()) 
    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename1}",
    )
    message.attach(part)
    filename = "9.jpeg"
    with open(filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read()) 
    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )
    message.attach(part)
    filename1 = "10.jpeg"
    with open(filename1, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read()) 
    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename1}",
    )
    message.attach(part)
    filename = "12.jpeg"
    with open(filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read()) 
    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )
    message.attach(part)
    server.login(sender_email, password)
    o=0
#    server.sendmail(sender_email, receiver_email, text)
    df = pd.read_excel (r'c1.xlsx') #place "r" before the path string to address special character, such as '\'. Don't forget to put the file name at the end of the path + '.xlsx'
    for index, row in df.iterrows():
#        message = MIMEMultipart()
        message.attach(MIMEText(body.format(name=row['Name']), "plain"))
        

      
       
        
        
        
        
        text = message.as_string()
#        print(text)
        
        
        
#    print(row['Name'], row['Email'])
        server.sendmail(
                sender_email,
                row['Email'],
                text,
            )
        print(row['Email'])
#        message.set_payload([message.get_payload()[0],message.get_payload()[1],message.get_payload()[2],
#                             message.get_payload()[3],message.get_payload()[4],message.get_payload()[5],
#                              message.get_payload()[6],message.get_payload()[7],message.get_payload()[8],
#                               message.get_payload()[9],message.get_payload()[10],])
        message.set_payload(message.get_payload()[0:-1])
        o=o+1
        print(o)
#        text=""
#        message.del_param('text/plain')
#        del message
    
#import csv, smtplib, ssl
#
#message = """Subject: Your grade
#
#Hi {name}, your grade is {grade}"""
#from_address = "my@gmail.com"
#password = input("Type your password and press enter: ")
#
#context = ssl.create_default_context()
#with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
#    server.login(from_address, password)
#    with open("contacts_file.csv") as file:
#        reader = csv.reader(file)
#        next(reader)  # Skip header row
#        for name, email, grade in reader:
#            server.sendmail(
#                from_address,
#                email,
#                message.format(name=name,grade=grade),
#            )