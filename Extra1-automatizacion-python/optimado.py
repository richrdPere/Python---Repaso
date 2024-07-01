import psutil
import pygetwindow as gw
import pyautogui as bot
import locale
import pyperclip
import time
from pywinauto import Application, keyboard
from subprocess import Popen
from datetime import datetime, timedelta
import pywinauto.application as app
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configuration
APP_PATH = r"C:\Program Files (x86)\Schneider Electric\Power Monitoring Expert\system\bin\reportgen.exe"
EXCEL_FILE = "DATA INSTANTANEA.xls"
EXTRANET_URL = "https://www.coes.org.pe/extranet/WebForm/Account/Login.aspx"
EXTRANET_USERNAME = "ccd@egemsa.com.pe"
EXTRANET_PASSWORD = "OjTuXh"

def check_process_and_window(process_name: str, window_title: str) -> bool:
    """
    Verifica si el proceso y la ventana están en ejecución.
    """
    for process in psutil.process_iter(['name']):
        if process.info['name'] == process_name:
            for window in gw.getAllTitles():
                if window == window_title:
                    return True
    return False

def open_ion_reporter():
    """
    Abre la aplicación ION Reporter.
    """
    if check_process_and_window("reportgen.exe", "ION Reporter"):
        window = gw.getWindowsWithTitle("ION Reporter")[0]
        window.close()
    Popen(APP_PATH, shell=True)
    time.sleep(1)
    return Application(backend='uia').connect(path=APP_PATH).window(title='ION Reporter')

def extract_excel_data():
    """
    Extrae los datos de las hojas "GRUPOS" y "TENSIONES" del archivo de Excel.
    """
    app = Application(backend='uia').connect(path=APP_PATH)
    dialog = app.window(title='ION Reporter')
    data_instantanea_item = dialog.child_window(title="DATA INSTANTANEA", control_type="ListItem")
    data_instantanea_item.select()
    time.sleep(2)
    data_instantanea_enter = dialog.child_window(title="Generate...", auto_id="5", control_type="Button")
    data_instantanea_enter.click()
    time.sleep(2)

    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
    fh_actual = datetime.now()
    f_inicio = (fh_actual - timedelta(hours=3)).strftime("%Y-%b-%d")
    h_inicio = (fh_actual - timedelta(hours=3)).strftime("%H:00:00")
    f_final = (fh_actual + timedelta(days=1)).strftime("%Y-%b-%d")
    h_final = fh_actual.strftime("%H:%M:%S")
    
    for _ in range(3):
        bot.press('TAB')
    time.sleep(1)
    bot.write(h_inicio)
    time.sleep(1)
    bot.press('TAB')
    for _ in range(11):
        bot.press('DELETE')
    time.sleep(1)
    bot.write(f_inicio)
    time.sleep(1)
    bot.press('TAB')
    for _ in range(11):
        bot.press('DELETE')
    time.sleep(1)
    bot.write(f_final)
    time.sleep(1)
    bot.press('TAB')
    time.sleep(1)
    bot.press('ENTER')
    time.sleep(2)
    bot.press('ENTER')
    time.sleep(2)
    bot.hotkey('CTRL', 'PAGEDOWN')

    # Copiar datos de GENERACIÓN
    keyboard.send_keys('^I')
    time.sleep(0.1)
    bot.write("'[DATA INSTANTANEA.xls]GRUPOS'!C3:J8")
    bot.press('ENTER')
    keyboard.send_keys('^C')
    GENE = pyperclip.paste()
    bot.press('ESCAPE')

    # Copiar datos de TENSIONES
    keyboard.send_keys('^I')
    bot.write("'[DATA INSTANTANEA.xls]TENSIONES'!C3:F8")
    bot.press('ENTER')
    time.sleep(0.1)
    keyboard.send_keys('^C')
    TENS = pyperclip.paste()
    bot.press('ESCAPE')
    time.sleep(1)
    # Cerrar archivo Excel
    bot.hotkey('ALT', 'F4')
    bot.press('TAB')
    bot.press('ENTER')
    return GENE, TENS

def login_extranet():
    """
    Inicia sesión en la Extranet COES.
    """
    driver = webdriver.Chrome()
    driver.get(EXTRANET_URL)
    wait = WebDriverWait(driver, 10)
    usuario_input = wait.until(EC.presence_of_element_located((By.ID, "MainContent_TextBoxUserLogin")))
    contrasena_input = wait.until(EC.presence_of_element_located((By.ID, "MainContent_TextBoxUserPassword")))
    usuario_input.send_keys(EXTRANET_USERNAME)
    contrasena_input.send_keys(EXTRANET_PASSWORD)
    contrasena_input.send_keys(Keys.ENTER)
    return driver

def load_power_data(driver, fh_actual):
    """
    Carga los datos de Potencia IDCC en la Extranet COES.
    """
    # Código para cargar datos de Potencia IDCC
    h_actual = int(fh_actual.strftime("%H"))
    d_actual = int(fh_actual.strftime("%d"))
    h_inicio = int((fh_actual - timedelta(hours=3)).strftime("%H"))
    d_semana = int((fh_actual - timedelta(hours=3)).weekday() + 1)  # Sumamos 1 para que lunes sea 1 y domingo sea 7
    n_semana = int((int((fh_actual - timedelta(hours=3)).strftime("%d")) - d_semana + 13)/7)
    celda = h_inicio*2 + 4
    
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[4]/div[1]/ul/li[3]/a'))).click()
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[4]/div[1]/ul/li[3]/ul/li[1]/a'))).click()
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[4]/div[1]/ul/li[3]/ul/li[1]/ul/li[1]/a'))).click()
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[4]/div[1]/ul/li[3]/ul/li[1]/ul/li[1]/ul/li[6]/a'))).click()
    time.sleep(5)
    if h_actual == 0:
        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[4]/section/div[1]/div[2]/div[2]/div/div/div[3]/div/div/div[1]/div/div/div[3]/div[2]/span/button'))).click()
        time.sleep(2)
        if d_actual == 1:
            WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/table[1]/tbody/tr/td[1]'))).click()
            time.sleep(2)
        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,f'/html/body/div[3]/table[2]/tbody/tr[{n_semana+1}]/td[{d_semana}]'))).click()
        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,f'/html/body/div[1]/div[4]/section/div[1]/div[2]/div[2]/div/div/div[4]/div/div[2]/div/div[1]/div/div/div/table/tbody/tr[28]/td[2]'))).click()
        time.sleep(1)
        abajo=int(h_inicio-12)*2
        for _ in range(abajo):
            bot.press('DOWN')
        time.sleep(3)
    else:
        if h_inicio < 15:
            WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,f'/html/body/div[1]/div[4]/section/div[1]/div[2]/div[2]/div/div/div[4]/div/div[2]/div/div[1]/div/div/div/table/tbody/tr[{celda}]/td[2]'))).click()
            time.sleep(1)
        else: 
            WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,f'/html/body/div[1]/div[4]/section/div[1]/div[2]/div[2]/div/div/div[4]/div/div[2]/div/div[1]/div/div/div/table/tbody/tr[28]/td[2]'))).click()
            time.sleep(1)
            abajo=int(h_inicio-12)*2
            for _ in range(abajo):
                bot.press('DOWN')
    pass

def load_voltage_data(driver, fh_actual):
    """
    Carga los datos de Tensión en la Extranet COES.
    """
    # Código para cargar datos de Tensión
    h_actual = int(fh_actual.strftime("%H"))
    d_actual = int(fh_actual.strftime("%d"))
    h_inicio = int((fh_actual - timedelta(hours=3)).strftime("%H"))
    d_semana = int((fh_actual - timedelta(hours=3)).weekday() + 1)  # Sumamos 1 para que lunes sea 1 y domingo sea 7
    n_semana = int((int((fh_actual - timedelta(hours=3)).strftime("%d")) - d_semana + 13)/7)
    celda = h_inicio*2 + 4
    
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[4]/div[1]/ul/li[3]/a'))).click()
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[4]/div[1]/ul/li[3]/ul/li[1]/a'))).click()
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[4]/div[1]/ul/li[3]/ul/li[1]/ul/li[1]/a'))).click()
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[4]/div[1]/ul/li[3]/ul/li[1]/ul/li[1]/ul/li[9]/a'))).click()
    time.sleep(5)

    if h_actual == 0:
        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[4]/section/div[1]/div[2]/div[2]/div[1]/div/div[3]/div/div/div[1]/div/div/div[3]/div[2]/span/button'))).click()
        time.sleep(3)
        if d_actual == 1:
            WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/table[1]/tbody/tr/td[1]'))).click()
            time.sleep(1)
        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,f'/html/body/div[3]/table[2]/tbody/tr[{n_semana+1}]/td[{d_semana}]'))).click()
        time.sleep(3)
        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,f'/html/body/div[1]/div[4]/section/div[1]/div[2]/div[2]/div[1]/div/div[5]/div/div[1]/div/div/div/table/tbody/tr[28]/td[2]'))).click()
        time.sleep(2)
        abajo=int(h_inicio-12)*2
        for _ in range(abajo):
            bot.press('DOWN')
    else :
        if h_actual == 3:
            time.sleep(1) 
        else:
            WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[4]/section/div[1]/div[2]/div[2]/div[1]/div/div[3]/div/div/div[3]/div/div/div[1]/a/div/img'))).click()

        if h_inicio < 15:
            WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,f'/html/body/div[1]/div[4]/section/div[1]/div[2]/div[2]/div[1]/div/div[5]/div/div[1]/div/div/div/table/tbody/tr[{celda}]/td[2]'))).click()
            time.sleep(1)
        else:
            WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,f'/html/body/div[1]/div[4]/section/div[1]/div[2]/div[2]/div[1]/div/div[5]/div/div[1]/div/div/div/table/tbody/tr[28]/td[2]'))).click()
            time.sleep(1)
            abajo=int(h_inicio-12)*2
            for _ in range(abajo):
                bot.press('DOWN')
    pass

def main():
    try:
        open_ion_reporter()
        gene, tens = extract_excel_data()
        driver = login_extranet()
        time.sleep(1)
        load_power_data(driver, datetime.now())
        time.sleep(2)
        # Pegar los datos copiados
        pyperclip.copy(gene)
        keyboard.send_keys('^V')
        time.sleep(1)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[4]/section/div[1]/div[2]/div[2]/div/div/div[3]/div/div/div[3]/div/div/div[4]/a/div/img'))).click()
        time.sleep(2)
        bot.press('ENTER')
        time.sleep(3)
        
        load_voltage_data(driver, datetime.now())
        pyperclip.copy(tens)
        keyboard.send_keys('^V')
        time.sleep(1)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[4]/section/div[1]/div[2]/div[2]/div[1]/div/div[3]/div/div/div[3]/div/div/div[4]/a/div/img'))).click()
        time.sleep(2)
        bot.press('ENTER')
        time.sleep(2)

    except Exception as e:
        print(f"Error: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()