from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# 드라이버 설정
options = Options()
# VGA 가속화를 끔.
options.add_argument('disable-gpu')
# 브라우저 창을 숨김.
options.add_argument('--headless')
# --headless 상태에서, agent 정보를 표기하기 위해 필요하다고 함.
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Whale/3.12.129.46 Safari/537.36')

driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
# 해당 URL로 이동
driver.get(url='https://naver.com')
# 페이지 이동

print(driver.current_url)
# 이동되었는지 확인

driver.close()
# 종료