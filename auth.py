from flask import (
    Flask, render_template, redirect, url_for, Blueprint, request, session, flash, current_app
)
from datetime import timedelta
import mysql.connector, bcrypt, random, os, ssl, smtplib
import db
from dotenv import load_dotenv
from email.message import EmailMessage


config = db.connect_to_database()
bp = Blueprint('auth', __name__)

# login back-end
@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Create a connection to the database
        connect = mysql.connector.connect(**config)
        cursor = connect.cursor()

        # Fetch user details from the database
        query = "SELECT id, password, firstname FROM user WHERE email = %s;"
        param = (email,)
        cursor.execute(query, param)
        user = cursor.fetchone()
        connect.close()
        
        if user is not None:
            user_id, hashed_password, firstname = user

            # Verify the password
            if bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')):
                send_login_notification(email, firstname)
                # Password is correct, set the session
                session['user_id'] = user_id
                session['email'] = email
                
                # let the user now that he has logged in successfully    
                flash("Er is een email gestuurd met de verificatie code naar uw e-mail box", "info")
                return redirect(url_for('auth.verify'))

            
            else:
                flash('Verkeerde email en/of wachtwoord', 'error')
                return redirect(url_for('auth.login'))
                
    return render_template('login.html')

def send_login_notification(email, firstname):
    dotenv_path = os.path.join(os.path.dirname(__file__), 'hide_data.env')
    load_dotenv(dotenv_path)
    email_sender = os.getenv('EMAIL_SENDER')
    email_password = os.getenv('EMAIL_PASSWORD')
    
    verification_code = str(random.randint(100000, 999999))
    session['verification_code'] = verification_code
    
    subject = f"bol partnerplatform verificatie code: {verification_code}"
    body = f"""Hier is je verificatie code {firstname}!<br><br>Vul deze zes-cijferige code in op het verificatie scherm om je identiteit te bevestigen en toegang te krijgen tot je account.<br><br>
    <strong style='font-size: 30px;'>{verification_code}</strong><br><br>Dankjewel dat je gebruik maakt van bol.com en meewerkt met onze veiligheids maatregelen. <br> Met vriendelijke groet, <br> bol.com partnerplatform team."""
    
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email 
    em['Subject'] = subject
    em.set_content(body, subtype='html') 
    
    context = ssl.create_default_context()
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email, em.as_string())


@bp.route('/verify', methods=('GET', 'POST'))
def verify():
    if 'email' not in session or 'verification_code' not in session:
        flash('Geen toegang, probeer het opnieuw', 'error')
        return redirect(url_for('auth.verify'))

    if request.method == 'POST':
        user_code = request.form['verification_code']
        if user_code == session['verification_code']:
            session.permanent = True
            current_app.permanent_session_liftime = timedelta(minutes=10)
            # Code is correct, clear the session variable
            session.pop('verification_code', None)
            flash('Verificatie succesvol afgerond! Welkom', 'success')
            return redirect(url_for('view.home'))
        else:
            flash('Code is fout, probeer het opnieuw', 'error')
            return redirect(url_for('auth.verify'))

    return render_template('verify.html') 

@bp.route('/logout')
def logout():
    if 'email' in session:
        # clear the session to logout the user
        session.clear()
        flash('Succesvol uitgelogd', 'info')
    return redirect(url_for('auth.login'))
