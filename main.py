from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import time

def benzersiz(liste):
    benzersizListe = list(set(liste))
    return benzersizListe

options = webdriver.FirefoxOptions()
options.add_argument('--headless')
driver = webdriver.Firefox(options=options)

url = input("siteyi yaz: ")
sayfa_sayisi = int(input("Konu kaç sayfa: "))
b= 1
ad_liste = []


for c in range(1,sayfa_sayisi+1):
    driver.get(f"{url}-{b}")
    time.sleep(3)
    tum = driver.find_elements(By.CSS_SELECTOR, "article > aside")
    for i in tum:
        try:
            ad = i.find_element(By.CSS_SELECTOR, "div.ki-kullaniciadi > a")
            ad_liste.append(ad.text)
        except:
            pass
    b +=1


konu_sahibi = ad_liste[0]
# Tekrarlanan kullanıcıları siler
benzersizListem = benzersiz(ad_liste)
#konu sahibini siler
benzersizListem.remove(konu_sahibi)
üyeler = '\n'.join(benzersizListem)
# konuya mesaj yazanları konu sahibi hariç uye.txt dosyasına yazdırır
with open("uye.txt","w",encoding="utf-8") as f:
    f.write(üyeler)

driver.quit()
