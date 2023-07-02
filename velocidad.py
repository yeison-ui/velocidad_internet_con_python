import speedtest

def medir_velocidad_internet():
    prueba = speedtest.Speedtest()
    velocidad_descarga = prueba.download() / 1024 / 1024  # Convertir bytes a megabits
    velocidad_carga = prueba.upload() / 1024 / 1024  # Convertir bytes a megabits

    print("Velocidad de descarga: {:.2f} Mbps".format(velocidad_descarga))
    print("Velocidad de carga: {:.2f} Mbps".format(velocidad_carga))

medir_velocidad_internet()
