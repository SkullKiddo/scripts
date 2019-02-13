import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

def hayNotas():
    import winsound
    while True:
        duration = 1000  # millisecond
        freq = 880  # Hz
        winsound.Beep(freq, duration)
        time.sleep(0.5)

driver = webdriver.Firefox(executable_path='C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\geckodriver.exe')
driver.get("https://sedeapl.dgt.gob.es/WEB_NOTP_CONSULTA/consultaNota.faces")
DNI = driver.find_element_by_id("formularioBusquedaNotas:nifnie")
fecha = driver.find_element_by_id("formularioBusquedaNotas:fechaExamen")
permiso = Select(driver.find_element_by_id("formularioBusquedaNotas:clasepermiso"))
nacimiento = driver.find_element_by_id("formularioBusquedaNotas:fechaNacimiento")

DNI.clear()
fecha.clear()
nacimiento.clear()

DNI.send_keys("DNI")
fecha.send_keys("FECHA")
permiso.select_by_visible_text('tipo')
nacimiento.send_keys("FECHA")


while True:
    boton = driver.find_element_by_name("formularioBusquedaNotas:j_id51")
    boton.click()
    try:
        respuesta = driver.find_element_by_id("formularioBusquedaNotas:messages")
        if respuesta.text != 'No hay ningún registro para los datos introducidos.\nRecuerde que las notas permanecen publicadas durante quince días.':
            hayNotas()
    except:
        hayNotas()
    finally:
        print("vuelvo a provar")
        time.sleep(30)
        