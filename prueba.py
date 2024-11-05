from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

class FalabellaTest:
    def __init__(self):
        # Configuración inicial
        print("\n=== INICIANDO PRUEBAS AUTOMATIZADAS DE FALABELLA ===")
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-notifications")
        
        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, 10)
        self.actions = ActionChains(self.driver)

    def print_step(self, step_name):
        """Imprime el paso actual de manera visible"""
        print("\n" + "="*50)
        print(f"EJECUTANDO: {step_name}")
        print("="*50)
        time.sleep(1)

    def test_busqueda_y_filtrado(self):
        """Escenario 1: Búsqueda y Filtrado"""
        try:
            self.print_step("1. PRUEBA DE BÚSQUEDA Y FILTRADO")
            
           
            print("→ Abriendo página principal de Falabella...")
            self.driver.get("https://www.falabella.com")
            time.sleep(3)

            # Buscar producto
            print("→ Realizando búsqueda de producto...")
            search_box = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='text']"))
            )
            search_box.clear()
            search_box.send_keys("laptop gaming")
            search_box.send_keys(Keys.RETURN)
            time.sleep(3)

            # Aplicar filtros
            print("→ Aplicando filtros...")
            filtros = self.wait.until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "button[class*='filter']"))
            )
            if filtros:
                filtros[0].click()
                print("  Filtro aplicado exitosamente")
            time.sleep(2)

        except Exception as e:
            print(f"Error en búsqueda y filtrado: {str(e)}")

    def test_navegacion_paginas(self):
        """Escenario 2: Navegación entre páginas"""
        try:
            self.print_step("2. PRUEBA DE NAVEGACIÓN ENTRE PÁGINAS")
            
            # Buscar botón de siguiente página
            print("→ Buscando controles de paginación...")
            next_button = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a[title*='Siguiente']"))
            )
            print("→ Navegando a la siguiente página...")
            next_button.click()
            time.sleep(3)

            print("→ Verificando cambio de página...")
            # Verificar que estamos en una nueva página
            current_url = self.driver.current_url
            print(f"  URL actual: {current_url}")

        except Exception as e:
            print(f"Error en navegación: {str(e)}")

    def test_formulario_contacto(self):
        """Escenario 3: Formulario de Contacto"""
        try:
            self.print_step("3. PRUEBA DE FORMULARIO DE CONTACTO")
            
            # Navegar a la página de contacto
            print("→ Navegando a la página de contacto...")
            self.driver.get("https://www.falabella.com.co/falabella-co/page/centro-de-ayuda")
            time.sleep(3)

            # Llenar formulario
            print("→ Llenando formulario de contacto...")
            campos_formulario = {
                "nombre": "Test Usuario",
                "email": "test@test.com",
                "mensaje": "Este es un mensaje de prueba automatizado"
            }

            for campo, valor in campos_formulario.items():
                try:
                    input_field = self.wait.until(
                        EC.presence_of_element_located((By.NAME, campo))
                    )
                    input_field.send_keys(valor)
                    print(f"  Campo {campo} completado")
                except:
                    print(f"  No se pudo completar el campo {campo}")

        except Exception as e:
            print(f"Error en formulario de contacto: {str(e)}")

    def test_popups_y_alertas(self):
        """Escenario 4: Manejo de Popups y Alertas"""
        try:
            self.print_step("4. PRUEBA DE MANEJO DE POPUPS Y ALERTAS")
            
            print("→ Buscando y manejando popups...")
            popup_selectors = [
                "button[class*='popup-close']",
                "button[class*='modal-close']",
                "#testId-accept-cookies-btn",
                "button[aria-label*='Cerrar']"
            ]

            for selector in popup_selectors:
                try:
                    popup = self.wait.until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
                    )
                    popup.click()
                    print(f"  Popup cerrado: {selector}")
                    time.sleep(1)
                except:
                    continue

        except Exception as e:
            print(f"Error en manejo de popups: {str(e)}")

    def test_frames(self):
        """Escenario 5: Manejo de Frames e iframes"""
        try:
            self.print_step("5. PRUEBA DE MANEJO DE FRAMES")
            
            # Buscar frames en la página
            print("→ Buscando frames en la página...")
            frames = self.driver.find_elements(By.TAG_NAME, "iframe")
            
            if frames:
                print(f"  Se encontraron {len(frames)} frames")
                
                for i, frame in enumerate(frames):
                    try:
                        print(f"→ Cambiando al frame {i+1}...")
                        self.driver.switch_to.frame(frame)
                        print("  Dentro del frame")
                        
                        # Volver al contenido principal
                        self.driver.switch_to.default_content()
                        print("  Volviendo al contenido principal")
                    except:
                        print(f"  No se pudo acceder al frame {i+1}")
            else:
                print("  No se encontraron frames en la página")

        except Exception as e:
            print(f"Error en manejo de frames: {str(e)}")

    def test_elementos_dinamicos(self):
        """Escenario 6: Manejo de Elementos Dinámicos"""
        try:
            self.print_step("6. PRUEBA DE ELEMENTOS DINÁMICOS")
            
            print("→ Probando scroll infinito...")
            # Scroll hasta el final de la página
            for _ in range(3):
                self.driver.execute_script(
                    "window.scrollTo(0, document.body.scrollHeight);"
                )
                print("  Realizando scroll...")
                time.sleep(2)

            print("→ Verificando carga de elementos dinámicos...")
            productos = self.driver.find_elements(By.CSS_SELECTOR, "div[data-pod]")
            print(f"  Productos cargados: {len(productos)}")

        except Exception as e:
            print(f"Error en elementos dinámicos: {str(e)}")

    def ejecutar_pruebas(self):
        """Ejecutar todas las pruebas"""
        try:
            self.test_popups_y_alertas()  # Primero manejar popups
            self.test_busqueda_y_filtrado()
            self.test_navegacion_paginas()
            self.test_formulario_contacto()
            self.test_frames()
            self.test_elementos_dinamicos()

        except Exception as e:
            print(f"Error general en las pruebas: {str(e)}")
        
        finally:
            print("\n=== FINALIZANDO PRUEBAS ===")
            print("Cerrando navegador en 5 segundos...")
            time.sleep(5)
            self.driver.quit()

def main():
    test = FalabellaTest()
    test.ejecutar_pruebas()

if __name__ == "__main__":
    main()