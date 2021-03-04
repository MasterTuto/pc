import smtplib
from pathlib import Path
from  email.message import EmailMessage

class Email:
    allow_access_url = "https://myaccount.google.com/u/1/lesssecureapps"
    error_message = ""

    def __init__(self, user: str, password: str):
        self.user = user
        self.password = password
        self.smtp = smtplib.SMTP("smtp.gmail.com", 587)
        self.smtp.starttls()
        self.email = EmailMessage()
    
    def login(self) -> bool:
        try:
            self.smtp.login(self.user, self.password)
            return True
        except smtplib.SMTPAuthenticationError:
            error_message = "Email ou senha incorretos!"
        except smtplib.SMTPException:
            error_message = "Nao foi possivel fazer login, tente permitir o login de apps menos segundos em:\n\t"+allow_access_url
        
        return False

    def attach_zip(self, filename: Path) -> bool:
        try:
            with filename.open("rb") as zipattachment:
                self.email.add_attachment(
                    zipattachment.read(),
                    maintype="application",
                    subtype="zip",
                    filename=filename.name
                )
            return True
        except FileNotFoundError as fnfe:
            self.error_message = "Arquivo zip nao encontrado, tente executar o argumento \"-zip\" antes."
        except Exception as e:
            self.error_message = str(e)
        return False

    def send_email(self, destin: str, subject: str) -> bool:
        self.email['To'] = destin
        self.email['Subject'] = subject
        self.email['From'] = self.user

        try:
            self.smtp.send_message(self.email)
            return True
        except smtplib.SMTPRecipientsRefused:
            self.error_message = "Ninguem recebeu o email"
        except smtplib.SMTPHeloError:
            self.error_message = "Nao foi possivel se conectar ao servidor"
        except smtplib.SMTPHeloError:
            self.error_message = "O servidor nao aceitou o seu email"
        except smtplib.SMTPDataError:
            self.error_message = "Ocorreu algum erro no conteudo desse email"
        except smtplib.SMTPNotSupportedError:
            self.error_message = "Pelo visto a Google nao suporta esse protocolo de email :/"
        
        return False