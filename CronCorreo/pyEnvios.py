import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

#   server = smtplib.SMTP_SSL('smtp.gmail.com', 587)
#   server.starttls()
#   server.login('vergaravargas.martin@gmail.com', '')
#   server.sendmail('sammy-teillier@hotmail.com', 'sammy-teillier@hotmail.com', mensaje.as_string())
#   server.quit()

def enviar_correo(destinatario, asunto, cuerpo, archivo_adjunto_path=None):
    # Configuración del servidor SMTP y credenciales
    servidor_smtp = 'smtp.gmail.com'
    puerto_smtp = 587  # Ajusta el puerto según las especificaciones del servidor
    usuario_smtp = os.environ.get('gmail')
    contraseña_smtp = os.environ.get('gmailKey')

    # Configurar el mensaje
    mensaje = MIMEMultipart()
    mensaje['From'] = usuario_smtp
    mensaje['To'] = destinatario
    mensaje['Subject'] = asunto
    mensaje.attach(MIMEText(cuerpo, 'plain'))

    # Adjuntar el archivo si se proporciona
    if archivo_adjunto_path:
        with open(archivo_adjunto_path, 'rb') as archivo:
            #nombre_archivo = os.path.basename(archivo_adjunto_path)
            #adjunto = MIMEApplication(archivo.read(), Name=nombre_archivo)
            #adjunto['Content-Disposition'] = f'attachment; filename={adjunto["Name"]}'
            #mensaje.attach(adjunto)

            adjunto = MIMEApplication(archivo.read())
            adjunto.add_header('Content-Disposition', f'attachment; filename="{os.path.basename(archivo_adjunto_path)}"')
            mensaje.attach(adjunto)

    # Iniciar conexión con el servidor SMTP
    with smtplib.SMTP(servidor_smtp, puerto_smtp) as servidor:
        servidor.starttls()  # Habilitar el cifrado TLS
        servidor.login(usuario_smtp, contraseña_smtp)
        cuerpo_del_mensaje = mensaje.as_string()
        servidor.sendmail(usuario_smtp, destinatario, cuerpo_del_mensaje)

    print(f'Correo enviado exitosamente a {destinatario}')

# Ejemplo de uso
destinatario = 'vergaravargas.siblings@gmail.com'
asunto = 'Asunto del correo'
cuerpo = 'Este es el cuerpo del correo.'
archivo = 'Informe_del_sistema.txt'

enviar_correo(destinatario, asunto, cuerpo, archivo)



#CORREOS:
#   jibone98@gmail.com
#   vergaravargas.siblings@gmail.com