import mysql.connector
import smtplib
import datetime
x = datetime.datetime.now()

# MySQL connection
mydb=mysql.connector.connect(host="localhost",
    user="root",
    password="12345",
    database="cinemas"
)
mycursor = mydb.cursor()

def gst_calculation(amt):
    gst = amt * 0.18
    return gst


def email_msg(email, total):
    try:
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("nivetha142003@gmail.com", "nivethakrishnan")
        msg = f"Thank you for choosing Besant Cinemas\nYour total amount is {total}\nYour seat is confirmed"
        s.sendmail("nivetha142003@gmail.com", email, msg)
        s.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

def insert():
    print("\t\t\t-------------------------NIVI CINEMAS---------------------------------------")
    print("")
    print("-----------The running movies in our theatre---------")
    print("\n**aranmaai** \n**ghilli*** \n**pt_sir\n**karudan\n")
    name = input("\n Enter your Name: ")
    email = input("\n Enter your e-mail: ")
    movie_list = ["aranmanai", "ghilli", "karudan", "ptsir"]
    movie = input("\n Enter the movie name: ").lower()
    if movie in movie_list:
        sql = "INSERT INTO movie (name, email, movie_name, no_of_ticket, select_class, total) VALUES (%s, %s, %s, %s, %s, %s)"
        movie_name = movie
        movie_date = input("\n Enter the date [dd/mm/yyyy]:")
        movie_time = input("\n Which timing you want:\n=>Morning show\n=>Afternoon show\n=>Night show:")
        no_of_ticket = int(input("\nEnter how many tickets you want: "))
        print("\n---------AVAILABLE CLASS---------")
        print("\n=>First class = ₹150\n=>Second class = ₹130\n=>Third class  = ₹120 ")
        print("\n----------If you want----------\nFirst class tickets then select '1'\nSecond class tickets then select '2'\nThird class tickets then select '3'\n")
        select_class = input("Enter the class: ")
        if select_class == "1":
            amt = no_of_ticket * 150
        elif select_class == "2":
            amt = no_of_ticket * 130
        elif select_class == "3":
            amt = no_of_ticket * 120
        else:
            print("Please select the available classes")
            return
        gst = gst_calculation(amt)
        total = amt + gst

        val = (name, email, movie_name, no_of_ticket, select_class, total)
        mycursor.execute(sql, val)
        mydb.commit()

        file=open("bill.txt","w")
        with open("bill.txt", "w") as file:
            print("\t\t\t--------------------------------------------------------------------------------------")
            file.write("\t\t\t\t\t\t------------------------NIVI CINEMAS-------------------\n\n*\n")
            file.write(f"\t\t\t\t\t\t\t\t{x}\nNAME:\t{name}\nEMAIL:\t{email}\nMOVIE:\t{movie}\nDATE:\t{movie_date}\nSHOWTIME:\t{movie_time}\nNO_OF_TICKETS:\t{no_of_ticket}\nCLASS:\t{select_class}\nTOTAL:\t{total}")
            file.write("\n*\n\n\t\t\t\t\t\t----------------THANK YOU BOOKING TICKETS IN NIVI CINEMAS--------------")
        email_msg(email, total)
    else:
        print(f"Sorry... {movie} movie is not available")

insert()
