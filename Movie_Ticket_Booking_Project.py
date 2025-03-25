# 1. Movie Ticket Booking
# ---->> no of ticket needed, username,mailid,total amt to pay,bill sent to mail,choice of choosing any movie name,databse connection, 

import smtplib
import mysql.connector
from email.message import EmailMessage

# Connecting to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",          
    password="******",  
    database="CinemaBooking"
)
cursor = db.cursor()

# Function to send the bill via email
def send_email(buyer_name, buyer_email, movie_name, seat_type, num_seats, total_bill):
    sender_email = "**********@gmail.com"  
    sender_password = "*************"  

    subject = f"Your Movie Ticket Booking Confirmation - {movie_name}"
    body = f"""
    Hello {buyer_name},

    Thank you for booking your movie ticket with us!

    🎬 Movie: {movie_name}
    🏷 Seat Type: {seat_type}
    🎟 Number of Seats: {num_seats}
    💰 Total Amount: ₹{total_bill}

    Your booking is confirmed. Enjoy your movie!

    Regards,
    Sriya Stuti Cinema Hall
    """

    msg = EmailMessage()
    msg.set_content(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = buyer_email

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_password)
            server.send_message(msg)
        print(f"📩 Bill has been sent to {buyer_email} successfully!")
    except Exception as e:
        print(f"⚠ Error sending email: {e}")

# Function to store booking details in MySQL
def store_booking(buyer_name, buyer_email, movie_name, seat_type, num_seats, total_bill):
    query = "INSERT INTO Bookings (buyer_name, email, movie_name, seat_type, num_seats, total_bill) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (buyer_name, buyer_email, movie_name, seat_type, num_seats, total_bill)
    cursor.execute(query, values)
    db.commit()
    print("✅ Booking details saved in the database!")

# Function to select seat type and calculate bill
def movie_seat_type(buyer_name, buyer_email, movie_name):
    print(f"Congratulations {buyer_name}!! You have selected booking for '{movie_name}'.")
    print("***Description***")
    print("Price per seat according to levels: ")
    print("1. SILVER (Near the screen) : 110/-")
    print("2. GOLD (Middle of the hall, served with a welcome drink) : 200/-")
    print("3. DIAMOND (Reclined seat, served with family popcorn and cold drink) : 300/-")

    seat_types = {1: "SILVER", 2: "GOLD", 3: "DIAMOND"}
    seat_prices = {1: 110, 2: 200, 3: 300}

    seat_choice = int(input("Select any one type (1/2/3) : "))

    if seat_choice in seat_types:
        num_seats = int(input(f"How many {seat_types[seat_choice]} seats do you want? : "))
        total_bill = num_seats * seat_prices[seat_choice]
        print(f"Your total bill is: {num_seats} * {seat_prices[seat_choice]} = ₹{total_bill}")

        # Store data in MySQL database
        store_booking(buyer_name, buyer_email, movie_name, seat_types[seat_choice], num_seats, total_bill)

        # Send email with bill details
        send_email(buyer_name, buyer_email, movie_name, seat_types[seat_choice], num_seats, total_bill)
    else:
        print("⚠ Please enter a valid seat type.")

# Function to choose a movie
def choose_movie_name():
    print("*************** WELCOME TO SRIYA STUTI CINEMA HALL *****************")
    print("________________________________________________________________________")
    print("The available movies are:")

    movies = {
        1: "CHHAVA",
        2: "SKY FORCE",
        3: "RRR",
        4: "MR. MAJNU",
        5: "DEAR COMMRADE",
        6: "MS DHONI: The Untold Story",
        7: "MAHARAJA",
        8: "DHADAK",
        9: "TIGER ZINDA HAI",
        10: "DILWALE"
    }

    for key, value in movies.items():
        print(f"{key}. {value}")

    choice = input("Do you want to book a ticket? (yes/no): ").strip().lower()

    if choice == "yes":
        buyer_name = input("Enter your full name: ")
        buyer_email = input("Enter your Email ID: ")
        movie_number = int(input("Enter the movie number you want to book a ticket for (1-10): "))

        if movie_number in movies:
            movie_name = movies[movie_number]
            movie_seat_type(buyer_name, buyer_email, movie_name)
            print(f"Thank you so much {buyer_name} for choosing our service. Enjoy watching '{movie_name}'!")
        else:
            print("⚠ Invalid choice! Please choose a number between 1-10.")
    elif choice == "no":
        print("Thank you for visiting! Hope to see you again.")  
    else:
        print("⚠ Invalid input! Please enter 'yes' or 'no'.")

choose_movie_name()

# Closing database connection 
cursor.close()
db.close()







































# import smtplib
# from email.message import EmailMessage

# # Function to send the bill to the buyer's email
# def send_email(buyer_name, buyer_email, movie_name, seat_type, num_seats, total_bill):
#     sender_email = "sneha.snehamayee@gmail.com"  # Replace with your email
#     sender_password = "mofk vayr juwe eqvk"  # Replace with your email app password

#     # Formatting the email
#     subject = f"Your Movie Ticket Booking Confirmation - {movie_name}"
#     body = f"""
#     Hello {buyer_name},

#     Thank you for booking your movie ticket with us!

#     🎬 Movie: {movie_name}
#     🏷 Seat Type: {seat_type}
#     🎟 Number of Seats: {num_seats}
#     💰 Total Amount: ₹{total_bill}

#     Your booking is confirmed. Enjoy your movie!

#     Regards,
#     Sriya Stuti Cinema Hall
#     """

#     msg = EmailMessage()
#     msg.set_content(body)
#     msg["Subject"] = subject
#     msg["From"] = sender_email
#     msg["To"] = buyer_email

#     try:
#         # Establish connection and send email
#         with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
#             server.login(sender_email, sender_password)
#             server.send_message(msg)
#         print(f"📩 Bill has been sent to {buyer_email} successfully!")
#     except Exception as e:
#         print(f"⚠ Error sending email: {e}")

# # Function to select seat type and calculate bill
# def movie_seat_type(buyer_name, buyer_email, movie_name):
#     print(f"Congratulations {buyer_name}!! You have selected booking for '{movie_name}'.")
#     print("***Description***")
#     print("Price per seat according to levels: ")
#     print("1. SILVER (Near the screen) : 110/-")
#     print("2. GOLD (Middle of the hall, served with a welcome drink) : 200/-")
#     print("3. DIAMOND (Reclined seat, served with family popcorn and cold drink) : 300/-")

#     seat_types = {1: "SILVER", 2: "GOLD", 3: "DIAMOND"}
#     seat_prices = {1: 110, 2: 200, 3: 300}

#     seat_choice = int(input("Select any one type (1/2/3) : "))

#     if seat_choice in seat_types:
#         num_seats = int(input(f"How many {seat_types[seat_choice]} seats do you want? : "))
#         total_bill = num_seats * seat_prices[seat_choice]
#         print(f"Your total bill is: {num_seats} * {seat_prices[seat_choice]} = ₹{total_bill}")

#         # Send email with bill details
#         send_email(buyer_name, buyer_email, movie_name, seat_types[seat_choice], num_seats, total_bill)
#     else:
#         print("⚠ Please enter a valid seat type.")

# # Function to choose movie
# def choose_movie_name():
#     print("*************** WELCOME TO SRIYA STUTI CINEMA HALL *****************")
#     print("________________________________________________________________________")
#     print("The available movies are:")
    
#     movies = {
#         1: "CHHAVA",
#         2: "SKY FORCE",
#         3: "RRR",
#         4: "MR. MAJNU",
#         5: "DEAR COMRADE",
#         6: "MS DHONI: The Untold Story",
#         7: "MAHARAJA",
#         8: "DHADAK",
#         9: "TIGER ZINDA HAI",
#         10: "DILWALE"
#     }
    
#     for key, value in movies.items():
#         print(f"{key}. {value}")

#     choice = input("Do you want to book a ticket? (yes/no): ").strip().lower()
    
#     if choice == "yes":
#         buyer_name = input("Enter your full name: ")
#         buyer_email = input("Enter your Email ID: ")
#         movie_number = int(input("Enter the movie number you want to book a ticket for (1-10): "))

#         if movie_number in movies:
#             movie_name = movies[movie_number]
#             movie_seat_type(buyer_name, buyer_email, movie_name)
#             print(f"Thank you so much {buyer_name} for choosing our service. Enjoy watching '{movie_name}'!")
#         else:
#             print("⚠ Invalid choice! Please choose a number between 1-10.")
#     elif choice == "no":
#         print("Thank you for visiting! Hope to see you again.")  
#     else:
#         print("⚠ Invalid input! Please enter 'yes' or 'no'.")

# choose_movie_name()

























# def movie_seat_type(buyer_name,movie_name):
#     print(f"Congratulations {buyer_name} !! You have selected booking for {movie_name}")
#     print("***Description***")
#     print("Price per seat according to levels : --")
#     print("1.SILVER (Near the screen) : 110/-")
#     print("2.GOLD (Middle of the hall and served with a welcome drink) : 200/-")
#     print("3.DIAMOND (Reclined Seat at height of the hall and server with a family popcorn and coldrink) : 300/-")
#     # print("Select any one type (silver/gold/diamond) : ")
#     type = int(input("Select any one type (1/2/3) : "))
#     if type == 1 :
#         # print(f"How many seats u want of {type} type : ")
#         number_silver_seats = int(input(f"How many seats u want of SILVER type : "))
#         silver_bill = number_silver_seats * 110 
#         print(f"Your totall bill is : {number_silver_seats} * 110 = {silver_bill} ")
#     elif type == 2:
#         number_gold_seats = int(input(f"How many seats u want of GOLD type : "))
#         gold_bill = number_gold_seats * 200 
#         print(f"Your totall bill is : {number_gold_seats} * 200 = {gold_bill} ")
#     elif type == 3 :
#         number_diamond_seats = int(input(f"How many seats u want of DIAMOND type : "))
#         diamond_bill = number_diamond_seats * 300 
#         print(f"Your totall bill is : {number_diamond_seats} * 300 = {diamond_bill} ")
#     else:
#         print("Please enter a valid seat type !!")
# # movie_seat_type()

# def choose_movie_name():
#     print("*************** WELCOME TO SRIYA STUTI CINEMA HALL *****************")
#     print("________________________________________________________________________")
#     print("The name of available movies are :----")
#     # print("1. CHHAVA \n 2. SKY FORCE \n 3. RRR \n 4. MR. MAJNU \n 5. DEAR COMMARADE \n 6. MS DHONI : The Untold Story \n 7. MAHARAJA \n 8. DHADAK \n 9. TIGER ZINDA HAI \n 10. DILWALE \n"  )
    
#     movies = {
#         1: "CHHAVA",
#         2: "SKY FORCE",
#         3: "RRR",
#         4: "MR. MAJNU",
#         5: "DEAR COMRADE",
#         6: "MS DHONI: The Untold Story",
#         7: "MAHARAJA",
#         8: "DHADAK",
#         9: "TIGER ZINDA HAI",
#         10: "DILWALE"
#     }
    
#     for key, value in movies.items():
#         print(f"{key}. {value}")
        
#     choice = input("Do you want to book a ticket ?? (yes/no) : ")
    
#     if choice == "yes":
#         buyer_name = input("Enter your fullname : ")
#         emailid = input("Enter your Email ID : ")
#         movie_number = int(input("Enter the movie number you want to book a ticket for (1-10): "))
        
#         if movie_number in movies :
#             movie_name = movies[movie_number]
#             movie_seat_type(buyer_name,movie_name)
#             print(f"Thank you so much {buyer_name} for choosing our service . Enjoy watching '{movie_name}'!")
#         else:
#             print("Invalid choice! Please choose a number between 1-10.")
            
#     else:
#         print(f"Thank you for visiting. Hope to see you again.")
# choose_movie_name()

# def payment():
#     buyername = input("Enter your full name : ")
#     mailid = input("Enter your email ID : ")