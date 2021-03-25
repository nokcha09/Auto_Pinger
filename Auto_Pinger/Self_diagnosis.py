# 본 코드의 저작권은 NOKCHA에게 있으며 무단복제 및 배포를 하시면 법적 처벌을 받을 수 있습니다.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time


# 아래 설명에 따라서 변수를 적어주세요
# 주의 ""를 삭제하면 코드 오류가 발생합니다.

# 자신의 학교를 적어주세요
school = ""
# 자신의 이름을 적어주세요
name = ""
# 자신의 생일을 적어주세요
birthday = ""
# 자신의 자가진단 비밀번호를 적어주세요
PW = ""

# 01 : 서울특별시
# 02 : 부산광역시
# 03 : 대구광역시
# 04 : 인천광역시
# 05 : 광주광역시
# 06 : 대전광역시
# 07 : 울산광역시
# 08 : 세종특별자치시
# 10 : 경기도
# 11 : 강원도
# 12 : 충청북도
# 13 : 충청남도
# 14 : 전라북도
# 15 : 전라남도
# 16 : 경상북도
# 17 : 경상남도
# 18 : 제주특별자치도
# 위의 정보를 참고해 지역을 적어주세요
area = ""

# 1 : 유치원
# 2 : 초등학교
# 3 : 중학교
# 4 : 고등학교
# 5 : 특수학교등
# 위의 정보를 참고해 학교를 적어주세요
grade = ""


# 축하 합니다. 모든 코드 작성을 완료 하였습니다.
# 이제 나가서 파이썬 파일을 실행해 보세요


print("")
print("")
print("오토 자가진단 프로그램 V.1")
print("녹차의 프로그램을 이용해 주셔서 감사합니다.")
print("본 코드의 저작권은 NOKCHA에게 있으며 무단복제 및 배포를 하시면 법적 처벌을 받을 수 있습니다.")
print("")
print("")


options = Options()

options.add_argument("--incognito")
options.add_argument("headless")

driver = webdriver.Chrome(executable_path='./chromedriver', chrome_options=options)
driver.set_window_size(500, 1000)

url = 'https://hcs.eduro.go.kr/#/loginHome'
driver.get(url)

driver.find_element_by_id('btnConfirm2').click()
driver.find_element_by_id('schul_name_input').click()

Select(driver.find_element_by_id('sidolabel')).select_by_value(value=area)

Select(driver.find_element_by_id('crseScCode')).select_by_value(value=grade)

driver.find_element_by_class_name('searchArea').send_keys(school)
driver.find_element_by_class_name('searchBtn').click()

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "layerSchoolArea"))
    )
finally:
    time.sleep(0.1)
    driver.find_element_by_class_name('layerSchoolArea').click()
    driver.find_element_by_class_name('layerFullBtn').click()


driver.find_element_by_id('user_name_input').send_keys(name)
driver.find_element_by_id('birthday_input').send_keys(birthday)
driver.find_element_by_id('btnConfirm').click()


try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "input_text_common"))
    )
finally:
    time.sleep(0.2)
    driver.find_element_by_class_name('input_text_common').send_keys(PW)
    driver.find_element_by_id('btnConfirm').click()

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="container"]/div/section[2]/div[2]/ul/li'))
    )
finally:
    driver.find_element_by_xpath('//*[@id="container"]/div/section[2]/div[2]/ul/li/a/em').click()

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'survey_q3a1'))
    )
finally:
    driver.find_element_by_id('survey_q1a1').click()
    driver.find_element_by_id('survey_q2a1').click()
    driver.find_element_by_id('survey_q3a1').click()
    driver.find_element_by_id('btnConfirm').click()

time.sleep(1)
driver.save_screenshot("Complet.png")


driver.quit()


# 본 코드의 저작권은 NOKCHA에게 있으며 무단복제 및 배포를 하시면 법적 처벌을 받을 수 있습니다.