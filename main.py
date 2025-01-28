from modules import emailutils as email
from modules import latexutils as latex
import csv

your_email = input('Enter your email: ')
your_password = input('Enter your password: ')

with open('data.csv', 'r') as file:
    # Data preparation
    ## read from csv
    reader = csv.reader(file)
    
    ## read header
    header = next(reader)
    
    ## read score nickname (skip first 3 columns)
    score_nickname = next(reader)[3:]

    ## read score weight
    score_weight = next(reader)[3:]
    
    ## read data of each student
    for row in reader:
        name = row[0]
        nim = row[1]
        email_address = row[2]
        scores = row[3:]

        ### Generate PDF
        latex.add_identity(name, nim)
        latex.add_table(score_nickname, score_weight, scores)
        latex.compile_latex(nim)

        ### Send email
        subject = 'Rincian Nilai IF2123 Aljabar Linear dan Geometri' # Customize the email subject here
        body = f'Berikut adalah rincian nilai Anda untuk mata kuliah IF2123 Aljabar Linear dan Geometri.\n\nTerima kasih.' # Customize the email body here
        attachment_path = f'outputs/{nim}.pdf'
        attachment_filename = f'{nim}.pdf'
        email.send_email(your_email, your_password, email_address, subject, body, attachment_path, attachment_filename)