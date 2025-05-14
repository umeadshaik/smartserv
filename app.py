

from flask import Flask, render_template, request, redirect, session
import os
import sqlite3
from flask import send_from_directory

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for session

UPLOAD_FOLDER = 'uploads'
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)


# Route for the index page
@app.route('/')
def index():
    return render_template('index.html')  # This should open the index page

# Route for the booking service page
@app.route('/book_service.html')
def book_service():
    return render_template('book_service.html')  # This should open the book_service page

# Route for handling the form submission
@app.route('/submit', methods=['POST'])
def submit():
    fullName = request.form['fullName']
    phoneNumber = request.form['phoneNumber']
    address = request.form['address']
    serviceType = request.form['serviceType']
    preferredDate = request.form['preferredDate']
    preferredTime = request.form['preferredTime']
    problemDescription = request.form['problemDescription']

    mediaFile = request.files['mediaUpload']
    mediaFileName = ""
    if mediaFile and mediaFile.filename != '':
        mediaFileName = mediaFile.filename
        media_path = os.path.join(UPLOAD_FOLDER, mediaFileName)
        mediaFile.save(media_path)

    # Save to SQLite database
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO bookings (fullName, phoneNumber, address, serviceType, preferredDate, preferredTime, problemDescription, mediaFileName)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (fullName, phoneNumber, address, serviceType, preferredDate, preferredTime, problemDescription, mediaFileName))
    conn.commit()
    conn.close()
    return redirect('/submit.html')
@app.route('/submit.html')
def submit_page():
    return render_template('submit.html') 

# Admin dashboard route
@app.route('/admin.html')
def admin_dashboard():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bookings")
    bookings = cursor.fetchall()
    conn.close()

    return render_template('admin.html', bookings=bookings)

if __name__ == '__main__':
    app.run(debug=True)

