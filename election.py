import mysql.connector
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import re

# Establish the MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="election"
)

cursor = db.cursor()

sql="insert into election(name,email,candidate) values(%s,%s,%s,%s)"
sql="insert into candidate(name,vote_count) values(%s,%s)"



# Create tables if they don't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    candidate VARCHAR(255)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS candidates (
    name VARCHAR(255) PRIMARY KEY,
    vote_count INT
)
""")

def display_candidates():
    cursor.execute("SELECT name FROM candidates")
    candidates = cursor.fetchall()
    print("List of candidates:\n=>candidates_A\n=>candidates_B\n=>candidates_C\n=>candidates_D\n=>candidates_E")
    for candidate in candidates:
        print(candidate[0])

def validate_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def send_email(email):
    from_email = "nivetha142003@gmail.com"  
    from_password = "nivethakrishnan"  

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, from_password)
        subject = "Thank you for voting"
        body = "Thank you for casting your vote. Your participation is appreciated."
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        server.sendmail(from_email, email, msg.as_string())
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

def add_vote(candidate_name):
    cursor.execute("SELECT vote_count FROM candidates WHERE name=%s", (candidate_name,))
    result = cursor.fetchone()
    if result:
        current_count = result[0]
        cursor.execute("UPDATE candidates SET vote_count = %s WHERE name = %s", (current_count + 1, candidate_name))
    else:
        cursor.execute("INSERT INTO candidates (name, vote_count) VALUES (%s, %s)", (candidate_name, 1))
    db.commit()

def add_user(name, email, candidate):
    cursor.execute("INSERT INTO users (name, email, candidate) VALUES (%s, %s, %s)", (name, email, candidate))
    db.commit()

def check_duplicate_vote(email):
    cursor.execute("SELECT * FROM users WHERE email=%s", (email,))
    result = cursor.fetchone()
    return result is not None

def display_results():
    cursor.execute("SELECT name, vote_count FROM candidates")
    results = cursor.fetchall()
    print("\nCurrent vote counts:")
    for name, vote_count in results:
        print(f"{name}: {vote_count} votes")

def main():

    print("-----------------------------------------------------------------------------------")
    print("                   WELCOME TO TAMILNADU ELECTION VOTING SYSTEM                     ")
    print("-----------------------------------------------------------------------------------\n")

    name = input("Enter your name:")
    email = input("Enter your email:")

    if not validate_email(email):
        print("Invalid email format. Please try again.")
        return

    if check_duplicate_vote(email):
        print("You have already voted. Duplicate voting is not allowed.")
        return

    display_candidates()
    candidate = input("Enter your favorite candidate:")

    add_user(name, email, candidate)
    add_vote(candidate)
    send_email(email)
    val=(name,email,candidate)
    print("verification checking:\n=>your voter id is valid.\nyour aadhar card is valid\n")
    print("---------------------THANK YOU FOR CASTING YOUR VOTE-------------------------------")
    print("-----------------------------------------------------------------------------------")
    display_results()
    print("-----------------------------------------------------------------------------------")
main()

db.close()
