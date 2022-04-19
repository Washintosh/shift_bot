from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from schedule.utils import get_clicks

class Schedule(webdriver.Chrome):
  def __init__(self, driver_path = r"C:\Users\Washington\Downloads", teardown=False):
    print("Program started")
    self.driver_path = driver_path
    self.teardown = teardown
    os.environ["PATH"] += self.driver_path
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    super(Schedule, self).__init__(options=options)
    self.implicitly_wait(15)
    self.maximize_window()
    print("Accessing website...")
    self.get("https://gpfecuador.shiftlabor.com/Login.aspx")
    print("Website accessed successfully")
  
  def __exit__(self, exc_type, exc_value, trace):
    if self.teardown:
      self.quit()

  def logging(self):
    print("Logging in...")
    username_input = self.find_element(by=By.ID, value = "UserName")
    username_input.send_keys("wxyagualm")
    password_input = self.find_element(by=By.ID, value = "Password")
    password_input.send_keys("wyagual.2022")
    login_button = self.find_element(by=By.ID, value = "idLoginBoton03")
    login_button.click()
    print("Logged in successfully")

  def horario_tienda(self, region, LN, tienda):
    self.find_element(by=By.ID, value = "icono_abrir_menu").click()
    self.find_element(by=By.ID, value = "mf_cab_div_02").click()
    self.find_element(by=By.ID, value = "mf_cab_ll_02_01").click()
    self.find_element(by=By.ID, value = "lblTituloJerarquiaSeleccionada01").click()
    self.find_element(by=By.CSS_SELECTOR, value = f"div[onclick*='{region}']").click()
    self.find_element(by=By.ID, value = "lblTituloJerarquiaSeleccionada02").click()
    self.find_element(by=By.CSS_SELECTOR, value = f"div[onclick*='{LN}']").click()
    self.find_element(by=By.ID, value = "lblTituloJerarquiaSeleccionada03").click()
    self.find_element(by=By.CSS_SELECTOR, value = f"div[onclick*='{tienda}']").click()
    # self.find_element(by=By.CSS_SELECTOR, value = "div[onclick='ShiftUC.administracionGrillaHorarioEstablecimiento.OnClickEditar(1, 0, horarioGeneral_grillaHorarioEstablecimientoComercial_cmbBuscadorUnidades);']").click()
    # for type in ["Normal", "Feriado"]:
    #   for day in range(7):
    #     actual_time = self.find_element(
    #       by=By.CSS_SELECTOR,
    #       value = f"input[id*='{type}IniDia{day}']"
    #     ).get_attribute("value")
    #     desired_time = "00:30"
    #     number_clicks = get_clicks(actual_time, desired_time)
    #     if number_clicks > 0:
    #       for _ in range(number_clicks):
    #         self.find_element(
    #           by=By.ID,
    #           value = f"buttoninc_horarioGeneral_grillaHorarioEstablecimientoComercial_CABHorario_spin{type}IniDia{day}Img").click()
    #     else:
    #       for _ in range(-number_clicks):
    #         self.find_element(
    #           by=By.ID,
    #           value = f"buttondec_horarioGeneral_grillaHorarioEstablecimientoComercial_CABHorario_spin{type}IniDia{day}Img").click()
              
    # self.find_element(by=By.ID, value = "horarioGeneral_grillaHorarioEstablecimientoComercial_CABHorario_btnGuardar_2").click()
    # self.find_element(by=By.ID, value = "horarioGeneral_grillaHorarioEstablecimientoComercial_btnExitoAceptar_2").click()

    # #horario turnos
    # self.find_element(
    #   by=By.ID,
    #   value = "horarioGeneral_pestanasHorarioEstablecimiento_pesPanelInfoc_1"
    # ).click()
    # self.find_element(by=By.CSS_SELECTOR, value = "div[onclick='ShiftUC.administracionGrillaHorarioEstablecimiento.OnClickEditar(2, 0, horarioGeneral_grillaHorarioEstablecimientoOperacional_cmbBuscadorUnidades);']").click()
    # for type in ["Normal", "Feriado"]:
    #   for day in range(7):
    #     actual_time = self.find_element(
    #       by=By.CSS_SELECTOR,
    #       value = f"input[id*='{type}IniDia{day}']"
    #     ).get_attribute("value")
    #     desired_time = "00:50"
    #     number_clicks = get_clicks(actual_time, desired_time)
    #     if number_clicks > 0:
    #       for _ in range(number_clicks):
    #         self.find_element(
    #           by=By.ID,
    #           value = f"buttoninc_horarioGeneral_grillaHorarioEstablecimientoOperacional_CABHorario_spin{type}IniDia{day}Img").click()
    #     else:
    #       for _ in range(-number_clicks):
    #         self.find_element(
    #           by=By.ID,
    #           value = f"buttondec_horarioGeneral_grillaHorarioEstablecimientoOperacional_CABHorario_spin{type}IniDia{day}Img").click()
    # self.find_element(by=By.ID, value = "horarioGeneral_grillaHorarioEstablecimientoOperacional_CABHorario_btnGuardar_2").click()
    # self.find_element(by=By.ID, value = "horarioGeneral_grillaHorarioEstablecimientoOperacional_btnExitoAceptar_2").click()

    #horario de descanso
    self.find_element(by=By.ID, value = "horarioGeneral_pestanasHorarioEstablecimiento_pesPanelInfoc_2").click()
    self.find_element(by=By.CSS_SELECTOR, value = "div[onclick='ShiftUC.administracionGrillaHorarioEstablecimiento.OnClickEditar(3, 0, horarioGeneral_grillaHorarioEstablecimientoAsignacionDescanso_cmbBuscadorUnidades);']").click()
    self.find_element(by=By.ID, value = "horarioGeneral_grillaHorarioEstablecimientoAsignacionDescanso_btnAgregarNuevoDescanso_2").click()
    self.find_element(by=By.ID, value = "horarioGeneral_grillaHorarioEstablecimientoAsignacionDescanso_spinInicioAgregarDescanso_horarioAsignacionDescansotextbox_I").send_keys(Keys.NUMPAD1, Keys.NUMPAD2)
    self.find_element(by=By.ID, value = "horarioGeneral_grillaHorarioEstablecimientoAsignacionDescanso_spinTerminoAgregarDescanso_horarioAsignacionDescansotextbox_I").send_keys("12")
      