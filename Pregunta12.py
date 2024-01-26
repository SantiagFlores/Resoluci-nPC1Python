#Problema 12:
# Implemente un programa que solicite al usuario el nombre de un archivo y luego genere el tipo de
#archivo MIME correspondiente. Si el nombre del archivo termina en cualquiera de estos sufijos (sin
#importar el uso de mayúsculas y minúsculas) :
#- .gif
#- .jpg
#- .jpeg
#- .png
#- .pdf
#- .txt
#- .zip
#Si el nombre del archivo termina con algún otro sufijo que no se encuentra en la lista o no tiene
#ningún sufijo, en su lugar su programa deberá devolver application/octet-stream.

# Solicitar al usuario el nombre del archivo
nombre_archivo = input("Ingrese el nombre del archivo: ")

# Obtener la extensión del archivo (sufijo)
if '.' in nombre_archivo:
    sufijo = nombre_archivo.split('.')[-1].lower()
else:
    sufijo = None

# Mapear las extensiones a los tipos MIME correspondientes
tipos_mime = {
    'gif': 'image/gif',
    'jpg': 'image/jpeg',
    'jpeg': 'image/jpeg',
    'png': 'image/png',
    'pdf': 'application/pdf',
    'txt': 'text/plain',
    'zip': 'application/zip'
}

# Obtener el tipo MIME correspondiente o devolver 'application/octet-stream'
tipo_mime = tipos_mime.get(sufijo, 'application/octet-stream')

# Mostrar el resultado
print(f"El tipo MIME del archivo {nombre_archivo} es: {tipo_mime}")
