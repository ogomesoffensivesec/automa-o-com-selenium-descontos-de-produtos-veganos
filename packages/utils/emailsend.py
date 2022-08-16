import smtplib
from email.message import EmailMessage
from packages.utils.secret import secretpasswd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
from email.mime.base import MIMEBase


def sendEmail(emailcliente):
    EMAIL_ADDRESS = 'gomes.rootkit@gmail.com'
    EMAIL_PASSWORD = secretpasswd
    corpo = 'Envio de planilha com os melhores descontos do site www.vegin.com.br'
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = emailcliente
    msg['Subject'] = 'MELHORES DESCONTOS VEGIN'
    msg.attach(MIMEText(corpo,))

    path_planilha = 'C:\\Develop\\python\\Projetos\\Automação_ Melhores Descontos do Site Vegin.com.br\\dados.xlsx'
    attachment = open(path_planilha, 'rb')
    att = MIMEBase('application', 'octet-stream')
    att.set_payload(attachment.read())
    encoders.encode_base64(att)

    att.add_header('Content-Disposition', f'attachment; filename = dados.xlsx')
    attachment.close()

    msg.attach(att)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
