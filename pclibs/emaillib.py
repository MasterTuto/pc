class Email:
    allow_access_url = "https://myaccount.google.com/u/1/lesssecureapps"

    def __init__(self, user: str, password: str):
        self.user = user
        self.password = password
    
    def login() -> bool:
        pass
    
    def attach_zip(self, filename: str) -> bool:
        pass

    def send_email(self, destin: str) -> bool:
        pass