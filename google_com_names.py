from selenium import webdriver

options = webdriver.ChromeOptions()

options.add_argument('/Users/shanecheek/Desktop/projects/easy_com_names/chromedriver')
options.add_argument('headless')
browser = webdriver.Chrome(options=options)

list_of_names = []
base_url = "https://domains.google.com/m/registrar/search?hl=en-US&tab=0&searchTerm="
url = "https://www.mondovo.com/keywords/most-searched-words-on-google"
browser.get(url)  # navigate to the page
browser.implicitly_wait(10)
results = browser.find_elements_by_css_selector("td:nth-child(2)")

for word in results:
    if word.text.isalnum():
        word = word.text
        list_of_names.append(word)
    else:
        word = word.text.replace(" ", "")
        list_of_names.append(word)

txt_file = open("google_com_names_available.txt", "a+")
print('Done with the list')
print('List is ' + str(len(list_of_names)) + " long")

for name in list_of_names:
    url = base_url + name + ".com"
    if name.isalnum():
        try:
            browser.get(url)  # navigate to the page
            browser.implicitly_wait(10)
            result = browser.find_element_by_css_selector('h3:nth-child(1)').text
            print(result)
            if 'unavailable' in result:
                pass
            else:
                txt_file.write(result + '\n')
        except:
            print('Error in name')
    else:
        print('Not alphanumeric')

txt_file.close()
