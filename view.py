from flask import render_template, Blueprint, redirect, url_for, session, flash, abort, jsonify, request
from datetime import datetime
import mysql.connector
import db
import os

config = db.connect_to_database()


bp = Blueprint('view', __name__)

@bp.route('/account', methods=['GET', 'POST'])
def account():
    if 'email' not in session or 'verification_code' in session:
        flash('Maak eerst de verificatie af alsjeblieft', 'error')
        return redirect(url_for('auth.verify'))
    
    user_id = session['user_id']
    
    connect = mysql.connector.connect(**config)
    cursor = connect.cursor()
    
    query = "SELECT firstname, prefix, lastname FROM user WHERE id = %s;"
    param = (user_id, )
    cursor.execute(query, param)
    user = cursor.fetchone()
    connect.close()
    
    if request.method == 'POST':
        firstname = request.form["firstname"]
        prefix = request.form["prefix"]
        lastname = request.form["lastname"]
        
        
        if prefix == '':
            prefix = None
            
        if '' in (firstname, lastname):
            flash('Vul alsjeblieft de verplichte velden in', 'error')
            return render_template('account.html', user=user)
        else:
            connect = mysql.connector.connect(**config)
            cursor = connect.cursor()
            update_query = "UPDATE user SET firstname = %s, prefix = %s, lastname = %s WHERE id = %s;"
            update_param = (firstname, prefix, lastname, user_id)
            cursor.execute(update_query, update_param)
            connect.commit()
            connect.close()
            flash('Account gegevens zijn opgelsagen', 'success')
            
    connect = mysql.connector.connect(**config)
    cursor = connect.cursor()
    query = "SELECT firstname, prefix, lastname FROM user WHERE id = %s;"
    param = (user_id, )
    cursor.execute(query, param)
    user = cursor.fetchone()
    connect.close()
    return render_template('account.html', user=user)
    
    
@bp.route('/dashboard')
def dashboard_page():
    if 'email' not in session or 'verification_code' in session:
        flash('Maak eerst de verificatie af, alsjeblieft', 'error')
        return redirect(url_for('auth.verify'))
    
    else:
        return render_template("dashboard.html")
    

@bp.route('/aanvragen', methods=['GET', 'POST'])
def aanvragen():
    if 'email' not in session:
        flash('Je moet ingelogd zijn om deze actie uit te voeren.', 'error')
        return redirect(url_for('auth.login'))
    
    if 'verification_code' in session:
        flash('Maak eerst de verificatie af, alsjeblieft', 'error')
        return redirect(url_for('auth.verify'))
    
    
    if request.method == 'POST':
        # Get form data
        onderwerp = request.form.get('onderwerp')
        bericht = request.form.get('bericht')
        email = session['email']

        
        if not onderwerp or not bericht:
            flash("Vul eerst de velden in", 'error')
            return redirect(url_for('view.aanvragen'))
        # Create a directory to store user submissions if it doesn't exist
        
        submissions_folder = 'Aanvragen'
        if not os.path.exists(submissions_folder):
            os.makedirs(submissions_folder)

        # Create a unique filename based on timestamp
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        filename = f"{email}_{timestamp}.txt"
        filepath = os.path.join(submissions_folder, filename)

            # Write form data to a text file
        with open(filepath, 'w') as file:
            file.write(f"Sender name: {email}\n")
            file.write(f"Subject: {onderwerp}\n\n")
            file.write(f"Message: {bericht}\n")

        flash('Je aanvraag is verstuurd!', 'success')
        return render_template("aanvragen.html", success_message="Aanvraag succesvol ingediend!")
    
    return render_template("aanvragen.html")


# Controleer of de gebruiker is ingelogd voordat ze toegang krijgen tot de homepagina
@bp.route('/')
def home():
    if 'email' in session:
        email = session['email']

        # Fetch the user's first name from the database
        connect = mysql.connector.connect(**config)
        cursor = connect.cursor()
        query = "SELECT firstname FROM user WHERE email = %s;"
        param = (email, )
        cursor.execute(query, param)
        first_name = cursor.fetchone()[0]
        connect.close()
        return render_template('home.html', first_name=first_name)
    else:
        return redirect(url_for('auth.login'))
    

    

@bp.route('/bedrijf', methods=["GET", "POST"])
def profile():
    if 'email' not in session or 'verification_code' in session:
        flash('Maak eerst de verificatie af, alsjeblieft', 'error')
        return redirect(url_for('auth.verify'))
    
    if 'email' in session:
        user_id = session['user_id']
        
        connect = mysql.connector.connect(**config)
        cursor = connect.cursor()
        
        query = "SELECT firstname, prefix, lastname, bankrekening, KvK, bedrijfsnaam, email FROM user WHERE id = %s;"
        param = (user_id, )
        cursor.execute(query, param)
        user = cursor.fetchone()
        connect.close()
        
        if request.method == 'POST':
            email = request.form['email']
            bankrekening = request.form["bankrekening"]
            KvK = request.form["KvK"]
            bedrijfsnaam = request.form["bedrijfsnaam"]
            
            
            if prefix == '':
                prefix = None
                
            if '' in (email, bankrekening, KvK, bedrijfsnaam):
                flash('Vul alsjeblieft de verplichte velden in', 'error')
                return render_template('profile.html', user=user)
        
    return render_template('profile.html', user=user)


@bp.route("/vragen")
def vragen():
    if 'email' not in session or 'verification_code' in session:
        flash('Maak eerst de verificatie af, alsjeblieft', 'error')
        return redirect(url_for('auth.verify'))
    
    else:
        return render_template("chat.html")
    



