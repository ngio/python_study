# chatGPT - python email sending app 2
import tkinter as tk
import smtplib
from tkinter import messagebox

# Create the main GUI window
root = tk.Tk()
root.title("Email Sending App")

# Function to send an email
def send_email():
    try:
        # Get email and password from the user
        sender_email = sender_email_entry.get()
        password = password_entry.get()
        recipient_email = recipient_email_entry.get()
        subject = subject_entry.get()
        message = message_text.get("1.0", "end")

        # Connect to the SMTP server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        # Log in to the email account
        server.login(sender_email, password)

        # Compose the email
        email_text = f"Subject: {subject}\n\n{message}"
        
        # Send the email
        server.sendmail(sender_email, recipient_email, email_text)
        
        # Close the SMTP server
        server.quit()

        # Display a success message
        messagebox.showinfo("Success", "Email sent successfully!")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create and place widgets
sender_email_label = tk.Label(root, text="Your Email:")
sender_email_label.pack()

sender_email_entry = tk.Entry(root)
sender_email_entry.pack()

password_label = tk.Label(root, text="Your Password:")
password_label.pack()

password_entry = tk.Entry(root, show="*")
password_entry.pack()

recipient_email_label = tk.Label(root, text="Recipient's Email:")
recipient_email_label.pack()

recipient_email_entry = tk.Entry(root)
recipient_email_entry.pack()

subject_label = tk.Label(root, text="Subject:")
subject_label.pack()

subject_entry = tk.Entry(root)
subject_entry.pack()

message_label = tk.Label(root, text="Message:")
message_label.pack()

message_text = tk.Text(root, height=5, width=40)
message_text.pack()

send_button = tk.Button(root, text="Send Email", command=send_email)
send_button.pack()

root.mainloop()
