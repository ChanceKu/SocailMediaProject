from module import *

options = Options()
options.chrome_executable_path= "D:\Python\chromedriver.exe"
# options.add_argument("--start-maximized")
# options.add_argument("window-size=1920,1080")
# option.add_argument("--disable-notifications")
# option.add_argument("--disable-popup-blocking")
# option.add_argument('--headless=new') # 打開背景模式
driver = webdriver.Chrome(options=options)

url = "https://www.google.com/maps"
driver.get(url)

search_input = "台南餐廳"
# class="tactile-searchbox-input"
elem_1 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, "tactile-searchbox-input")))    #等待搜尋格出現
elem_1.send_keys(search_input)  #在搜尋格輸入
time.sleep(1)
elem_2 = driver.find_element(By.CLASS_NAME, "mL3xi")        #按下搜尋
elem_2.click()

# Find all elements with class name "hfpxzc"
results = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "hfpxzc"))
)  

# create list
comments_data = []
i = 3
#續個打開搜尋結果
for result in results[:i]:
    label = result.get_attribute("aria-label")
    # Simulate the key press of Ctrl (or Command on macOS) while clicking on the link
    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL).click(result).key_up(Keys.CONTROL).perform()
    # Switch to the new tab
    driver.switch_to.window(driver.window_handles[-1])

    # 按"評論"
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[3]/div/div/button[2]/div[2]/div[2]"))).click()

    # 按排序->最新
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[3]/div[7]/div[2]/button/span/span"))).click()
    driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[1]/div[2]").click()

    time.sleep(1)
    
    #打開全文
    try:
        button = driver.find_elements(By.TAG_NAME, 'button')
        for m in button:
            if m.text == "全文":
                m.click()
    except:
        print("error:1")
        pass
    
    # get place's name
    input_element = driver.find_element(By.CLASS_NAME, "tactile-searchbox-input")
    place = input_element.get_attribute("value")

    # get comments
    comments = driver.find_elements(By.CLASS_NAME, 'jftiEf')
    for comment in comments:
        # get name
        name = comment.find_element(By.CLASS_NAME, "d4r55 ")
        # get review
        try:
            review = comment.find_element(By.CLASS_NAME, "wiI7pd")
            review = review.text.replace("\n"," ")
        except:
            review = "None"

        # Count the number of elements with the class "vzX5Ic" to get the rating
        rating = 0
        rating = len(comment.find_elements(By.CLASS_NAME, 'vzX5Ic'))

        # Time
        review_time = comment.find_element(By.CLASS_NAME, "rsqaWe")

        # 服務
        try:
            service = comment.find_elements(By.CLASS_NAME, "RfDO5c")
        except:
            service = "None"

        try:
            #各細節
            skip = False
            detail = []
            for i in range(0, len(service)):
                if skip == False:
                    if "：" in service[i].text:
                        split_string = service[i].text.split("：")
                        ser = split_string[0]
                        vice = split_string[1]
                        detail.append(ser)
                        detail.append(vice)
                    else:
                        ser = service[i].text
                        vice = service[i+1].text
                        detail.append(ser)
                        detail.append(vice)                
                        skip = True
                    # print(ser, ":", vice)
                else:
                    skip = False
        except:
            print("Error:3")
        
        try:
            comments_data.append({
                "地點":place,
                "名字":name.text,
                "評分":rating,
                "時間":review_time.text,
                "評論":review,
                **{detail[i]:detail[i+1] for i in range(0, len(detail), 2)}})
        except:
            print("Error:2")
    
    # close tab
    driver.close()

    print("tab closed")
    # Switch back to the original tab
    driver.switch_to.window(driver.window_handles[0])   

# print(comments_data)

# 存儲成json
with open("Gmaps.json", "w", encoding="utf-8") as f:
    json.dump(comments_data, f, ensure_ascii=False)

# pandas存儲成csv
df = pd.DataFrame(comments_data)
df.to_csv('Gmaps.csv', index=False, encoding="utf-8")