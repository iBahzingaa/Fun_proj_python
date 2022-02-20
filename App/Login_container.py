import tkinter as tk  # imported gui framework
from Checklist_page_container import checklist_screen

# Prüft das eingegebene Passwort und den Username.
# Gibt eine Message aus, je nachdem ob alle Felder gefüllt wurden, die Daten richtig oder falsch sind.
def login():
    # Daten aus den Feldern Username und Password holen
    uname = username.get()
    pwd = password.get()

    # Prüfe Felder
    if uname == '' or pwd == '':
        message.set("Nicht alle Felder sind gefüllt.")
    else:
        if uname == "admin" and pwd == "admin":
            message.set("Login erfolgreich")
            checklist_screen()
        else:
            message.set("Falsches Passwort oder Username.")


# Login Funktion.
# Gui für das Login Fenster wird aufgebaut.
def loginForm():
    global login_screen
    login_screen = tk.Tk()

    # Deklarieren der Variablen
    global message
    global username
    global password
    username = tk.StringVar()
    password = tk.StringVar()
    message = tk.StringVar()

    # Setzen des Namens von dem Dialog.
    login_screen.title("Login Dialog")

    # Setzen der Größe des Fensters.
    login_screen.geometry("330x250")

    # Layout des Dialoges
    tk.Label(login_screen, width="300", text = "Bitte geben Sie ihren Username und Passwort ein",
             bg="green", fg="white").pack()
    # Username Label
    tk.Label(login_screen, text="Username * ").place(x=20, y=40)
    # Username Textfeld
    tk.Entry(login_screen, textvariable=username).place(x=90, y=42)
    # Password Label
    tk.Label(login_screen, text="Passwort * ").place(x=20, y=80)
    # Password Textfeld
    tk.Entry(login_screen, textvariable=password, show="*").place(x=90, y=82)
    # Label um Loginstatus anzuzeigen [success/failed]
    tk.Label(login_screen, text="", textvariable=message).place(x=95, y=100)
    # Login Button
    tk.Button(login_screen, text="Login", width=10, height=1, bg="green", command=login).place(x=105, y=130)
    login_screen.mainloop()


# calling function Loginform
loginForm()
