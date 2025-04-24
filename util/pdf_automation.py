from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
from webdriver_manager.chrome import ChromeDriverManager
import os
import time
import threading
import shutil
import sys
from .session_data import SessionData

class PDFAutomation:
    def __init__(self):
        # Get the session data instance
        self.session_data = SessionData()
        self.download_path = self.session_data.get_download_path()
        self._lock = threading.Lock()
        self._is_running = False  # Add running state flag
        
        # Configure Chrome options with absolute path
        self.chrome_options = Options()
        self.chrome_options.add_experimental_option("prefs", {
            "download.default_directory": self.download_path,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True,
            "plugins.always_open_pdf_externally": True,  # Ensure PDFs are downloaded instead of opened
            "profile.default_content_settings.popups": 0
        })
        # Run in headless mode
        # self.chrome_options.add_argument("--headless=new")  # Use new headless mode
        self.chrome_options.add_argument("--disable-gpu")
        self.chrome_options.add_argument("--no-sandbox")
        self.chrome_options.add_argument("--disable-dev-shm-usage")
        self.chrome_options.add_argument("--window-size=1920,1080")

    def wait_for_download(self, timeout=10):
        """Wait for the PDF download to complete."""
        start_time = time.time()
        while time.time() - start_time < timeout:
            downloaded_files = [f for f in os.listdir(self.download_path) if f.endswith('.pdf')]
            if downloaded_files:
                time.sleep(1)  # Give it a moment to finish writing
                return True
            time.sleep(0.5)
        return False

    def download_pdf(self):
        session_data = SessionData()
        with self._lock:  # Ensure thread safety
            driver = None
            try:
                print(f"Download directory set to: {self.download_path}")
                print("Opening Chrome in background...")
                service = Service(ChromeDriverManager().install())
                driver = webdriver.Chrome(service=service, options=self.chrome_options)
                
                try:
                    # Navigate directly to QuickClaim in the new window
                    print("Navigating to QuickClaim login...")
                    driver.get('http://localhost:5173')
                    
                    # Wait for login form and fill credentials
                    print("Handling login...")
                    wait = WebDriverWait(driver, 10)
                    
                    # Find and fill username
                    username_field = wait.until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='text']"))
                    )
                    username_field.clear()
                    username_field.send_keys("manjunath")
                    
                    # Find and fill password
                    password_field = driver.find_element(By.CSS_SELECTOR, "input[type='password']")
                    password_field.clear()
                    password_field.send_keys("1234")
                    
                    # Click sign in button
                    sign_in_button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary, button[type='submit']")
                    sign_in_button.click()
                    
                    # Wait for and click Image Requests link
                    print("Clicking Image Requests link...")
                    time.sleep(2)
                    image_requests_link = wait.until(
                        EC.element_to_be_clickable((By.LINK_TEXT, "Image Requests"))
                    )
                    image_requests_link.click()
                    
                    # Wait for the PDF link to be clickable
                    print("Waiting for PDF link...")
                    time.sleep(2)
                    
                    # Check for Positive/Negative text
                    print("Checking claim status...")
                    status_element = wait.until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, "span.text-xs"))
                    )
                    
                    status_text = status_element.text.strip()

                    if(status_text == "Positive"):
                        session_data.positive_pdf = True
                        pdf_filename = "claimsp.pdf"
                    else:
                        session_data.positive_pdf = False
                        pdf_filename = "claimsn.pdf"

                    print(f"Claim status: {status_text}, will save as {pdf_filename}")
                    
                    pdf_link = wait.until(
                        EC.element_to_be_clickable((By.LINK_TEXT, "Print Document to PDF"))
                    )
                    
                    # Click the link and wait for download
                    print("Clicking PDF link...")
                    pdf_link.click()
                    
                    # Wait for download to complete
                    print("Waiting for download to complete...")
                    if self.wait_for_download():
                        # Get the latest downloaded PDF
                        downloaded_files = [f for f in os.listdir(self.download_path) if f.endswith('.pdf')]
                        if downloaded_files:
                            latest_file = max(
                                [os.path.join(self.download_path, f) for f in downloaded_files],
                                key=os.path.getctime
                            )
                            target_file = os.path.join(self.download_path, pdf_filename)
                            
                            # Remove existing file if it exists
                            if os.path.exists(target_file):
                                os.remove(target_file)
                                
                            # Rename the downloaded file
                            shutil.move(latest_file, target_file)
                            
                            print(f"Success: PDF saved as {target_file}")
                            return True, f"PDF downloaded successfully to {target_file}"
                    
                    print("Error: Download timeout or no PDF file was downloaded")
                    return False, "No PDF file was downloaded"
                    
                except TimeoutException as e:
                    print(f"Timeout error: {str(e)}")
                    return False, f"Operation timed out: {str(e)}"
                except WebDriverException as e:
                    print(f"WebDriver error: {str(e)}")
                    return False, f"Browser automation error: {str(e)}"
                except Exception as e:
                    print(f"Error during automation: {str(e)}")
                    return False, f"Error during PDF download: {str(e)}"
                    
                finally:
                    if driver:
                        try:
                            driver.quit()
                        except:
                            pass
                    
            except Exception as e:
                print(f"Error initializing browser: {str(e)}")
                return False, f"Error initializing browser: {str(e)}"

    def run_download(self):
        return self.download_pdf() 