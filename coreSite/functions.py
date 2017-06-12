import requests
def sendEmail(email, subject, message):
    email = str(email)
    subject = str(subject)
    message = str(message)
    message = "Sent by: "+ email + "Message: "+ message
    return requests.post(
        "https://api.mailgun.net/v3/sandboxe88f12da1e33450ebdf37691bc19af8a.mailgun.org/messages",
        auth=("api", "key-8660cf22e9d71b7ed25c2d5a82d2ab29"),
        data={"from": "Mailgun Sandbox <mailgun@sandboxe88f12da1e33450ebdf37691bc19af8a.mailgun.org>",
              "to": "Shubham <shubham@gupte.me>",
              "subject": subject,
              "text": message})
