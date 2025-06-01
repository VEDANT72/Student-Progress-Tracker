class EmailSender:
    def __init__(self, smtp_server, smtp_port, login, password):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.login = login
        self.password = password

    def send_email(self, to_address, subject, body, attachment):
        import smtplib
        from email.message import EmailMessage

        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = self.login
        msg['To'] = to_address
        msg.set_content(body)

        with open(attachment, 'rb') as att:
            msg.add_attachment(att.read(), maintype='application', subtype='pdf', filename=attachment)

        with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
            server.starttls()
            server.login(self.login, self.password)
            server.send_message(msg)