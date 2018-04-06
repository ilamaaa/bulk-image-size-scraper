from selenium import webdriver
import json

#You can get the chromedriver from https://sites.google.com/a/chromium.org/chromedriver/
driver = webdriver.Chrome(executable_path="chromedriver")

driver.implicitly_wait(10)

#list of pages you want to get the image dimensions for
pages = ["https://www.google.com"]
output = []

for page in pages:
    driver.get(page)
    imgs = driver.find_elements_by_tag_name('img')
    print("visiting page:", page, "it has:",len(imgs),"Images")

    dict = {"URL": page,
            "images": []}

    for img in imgs:
        sc = img.get_attribute('src')
        al = img.get_attribute('alt')
        w = img.get_attribute('width')
        h = img.get_attribute('height')
        nw = img.get_attribute('naturalWidth')
        nh = img.get_attribute('naturalHeight')
        img_dic = {"Source": sc,
                   "Alt Text": al,
                   "Width": w,
                   "Height": h,
                   "Natural Width": nw,
                   "Natural Height": nh}
        dict["images"].append(img_dic)
    output.append(dict)

output = json.dumps(output, indent=4)

print(output)