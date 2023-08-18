# chatGPT - python email sending app 
import tkinter as tk
from tkinter import messagebox
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email():
    sender_email = sender_email_entry.get()
    sender_password = sender_password_entry.get()
    recipient_email = recipient_email_entry.get()
    subject = subject_entry.get()
    message = message_text.get("1.0", tk.END)
    
    try:
        # Set up the SMTP server
        smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
        smtp_server.starttls()
        smtp_server.login(sender_email, sender_password)
        
        # Create the email
        email = MIMEMultipart()
        email["From"] = sender_email
        email["To"] = recipient_email
        email["Subject"] = subject
        email.attach(MIMEText(message, "plain"))
        
        # Send the email
        smtp_server.sendmail(sender_email, recipient_email, email.as_string())
        smtp_server.quit()
        
        messagebox.showinfo("Success", "Email sent successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create the main GUI window
root = tk.Tk()
root.title("Email Sending App")

# Create and place widgets
sender_email_label = tk.Label(root, text="Sender Email:")
sender_email_label.pack()

sender_email_entry = tk.Entry(root)
sender_email_entry.pack()

sender_password_label = tk.Label(root, text="Sender Password:")
sender_password_label.pack()

sender_password_entry = tk.Entry(root, show="*")
sender_password_entry.pack()

recipient_email_label = tk.Label(root, text="Recipient Email:")
recipient_email_label.pack()

recipient_email_entry = tk.Entry(root)
recipient_email_entry.pack()

subject_label = tk.Label(root, text="Subject:")
subject_label.pack()

subject_entry = tk.Entry(root)
subject_entry.pack()

message_label = tk.Label(root, text="Message:")
message_label.pack()

message_text = tk.Text(root, height=10, width=40)
message_text.pack()

send_button = tk.Button(root, text="Send Email", command=send_email)
send_button.pack()

root.mainloop()