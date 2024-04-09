import fitz #Leer archivos PDF
import re   #Búsqueda de patrones en un documento

import os #System management
import glob #System management
import pandas as pd #Data handling


Carpeta_dir= 'G:\\Mi unidad\\Mis finanzas\\Piso Plaza Nolasco\\Facturas endesa\\'
os.chdir(Carpeta_dir)
file = glob.glob("*.pdf") # We search for ".csv" files
file.sort()

print(file)

archivos =[]
for x in file:
    f = fitz.open(Carpeta_dir + x)
    page_one = f.load_page(0)
    page_text= page_one.getText()
    archivos.append(page_text)
    f.close()

pattern_referencia = r'Referencia: \d{1,14}/\d{1,5}'
factor_referencia = 11


pattern_emision = r'Fecha emisión factura: \d{1,2}/\d{1,2}/\d{1,4}'
factor_emision = 23

pattern_facturacion = r'Periodo de facturación: del \d{1,2}/\d{1,2}/\d{1,4} a \d{1,2}/\d{1,2}/\d{1,4}'
factor_facturacion = 28

pattern_consumo_total = r'Consumo total\n\d{1,4}'
factor_consumo_total = 14

pattern_consumo_llano = r'Consumo llano\n\d{1,4}'
factor_consumo_llano = 14

pattern_consumo_valle = r'Consumo valle\n\d{1,4}'
factor_consumo_valle = 14

pattern_consumo_punta = r'Consumo punta\n\d{1,4}'
factor_consumo_punta = 14


def busquedaImporte(page_text):
    # Busca el patrón del importe teniendo en cuenta que va después de total
    pattern = r'Total\n\d{1,4},\d{2,4}'
    match = re.search(pattern, page_text)
    # Para encontrar el inicial se suma 6 ya que hay que quitar total
    spanInicial = match.span()[0] + 6
    spanFinal = match.span()[1]

    return page_text[spanInicial:spanFinal]

def busqueda_valores(page_text, pattern, factor):
    # Busca el patrón del importe teniendo en cuenta que va después de total
    match = re.search(pattern, page_text)
    # Para encontrar el inicial se suma 6 ya que hay que quitar total
    spanInicial = match.span()[0] + factor
    spanFinal = match.span()[1]

    return page_text[spanInicial:spanFinal]

#Para quitar la extensión del archivo
wordPDF = len(file[1]) - 4

datos=[]
n = 0
for archivo in archivos:

    referencia = busqueda_valores(archivo, pattern_referencia, factor_referencia)
    fechaEmision = busqueda_valores(archivo, pattern_emision, factor_emision)
    importe = busquedaImporte(archivo)
    #Solo pone las fechas del periodo de facturación inicial y final
    periodoFacturacionInicio = busqueda_valores(archivo, pattern_facturacion, factor_facturacion)[:11]
    periodoFacturacionFin = busqueda_valores(archivo, pattern_facturacion, factor_facturacion)[13:]

    consumo_total = busqueda_valores(archivo, pattern_consumo_total, factor_consumo_total)
    consumo_punto = busqueda_valores(archivo, pattern_consumo_punta, factor_consumo_punta)
    consumo_valle = busqueda_valores(archivo, pattern_consumo_valle, factor_consumo_valle)
    try:
        consumo_llano = busqueda_valores(archivo, pattern_consumo_llano, factor_consumo_llano)
    except:
        consumo_llano = 0

    datos.append([file[n][:wordPDF], referencia, fechaEmision, periodoFacturacionInicio, periodoFacturacionFin,
                  consumo_total, consumo_punto, consumo_valle, consumo_llano, importe])
    n = n + 1
'''
#Imprime los datos de la última factura
print(f"La referencia de la factura es: {referencia}")
print(f"Fecha de emisión: {fechaEmision}")
print(f"Periodo de facturación: {periodoFacturacionInicio} a {periodoFacturacionFin}")
print(f"El importe: {importe} €")
'''

datosTabulados = pd.DataFrame(datos, columns=['Archivo pdf', 'Referencia', 'Fecha de emisión', 'Periodo de facturación Inicio',
                                              'Periodo de facturación Final', 'consumo_total', 'consumo_punto',
                                              'consumo_valle', 'consumo_llano','Importe'])
try:
    datosTabulados.to_csv(Carpeta_dir+"facturasendesa.csv")
except:
    print('No se ha podido guardar el archivo csv')
    pass
