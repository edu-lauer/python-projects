import smtplib
from get_contatos import *
from get_template import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


s = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
s.starttls()
s.login('email@hotmail.com', 'senha')

nomes, emails = get_contatos('_contatos.txt')
mensagem_template = get_template('_template.txt')

for nome, email in zip(nomes, emails):
    msg = MIMEMultipart()
    mensagem = mensagem_template.substitute(NOME_PESSOA=nome.title())

    msg['From'] = 'email@hotmail.com'
    msg['To'] = email
    msg['Subject'] = "Email test Python"

    msg.attach(MIMEText(mensagem, 'plain'))

    filename = "arquivos.zip"
    attachment = open('arquivos.zip', 'rb')
    p = MIMEBase('application', 'octet-stram')
    p.set_payload(attachment.read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    msg.attach(p)

    s.send_message(msg)

    del msg

