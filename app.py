from flask import Flask, render_template, request, redirect
import csv
import os

app = Flask(__name__)

# Route to render the booking form                                                              
@app.route('/')    
def book_service():
    return render_template('book_service.html')

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    fullName = request.form['fullName']
    phoneNumber = request.form['phoneNumber']
    address = request.form['address']
    serviceType = request.form['serviceType']
    preferredDate = request.form['preferredDate']
    preferredTime = request.form['preferredTime']
    problemDescription = request.form['problemDescription']

    # Handle file upload
    mediaFile = request.files['mediaUpload']
    if mediaFile.filename != '':  # Check if a file is uploaded
        media_path = os.path.join('uploads', mediaFile.filename)
        mediaFile.save(media_path)

    # Save booking details to CSV
    with open('bookings.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([fullName, phoneNumber, address, serviceType, preferredDate, preferredTime, problemDescription, mediaFile.filename])

    return "Booking submitted successfully!"

# Start the Flask app
if __name__ == '__main__':
    app.run(debug=True)

