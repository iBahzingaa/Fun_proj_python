import tkinter as tk  # imported gui framework

# Login Funktion.
# Gui für das Login Fenster wird aufgebaut.
def checklist_screen():
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




    login_screen.mainloop()


# calling function Loginform
checklist_screen()
