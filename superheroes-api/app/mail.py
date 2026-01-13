from flask_mail import Mail, Message

mail = Mail()

def send_test_email(app):
    with app.app_context():
        msg = Message(
            "Superheroes API",
            sender="your_email@gmail.com",
            recipients=["recipient@gmail.com"]
        )
        msg.body = "Flask Mail is working!"
        mail.send(msg)
