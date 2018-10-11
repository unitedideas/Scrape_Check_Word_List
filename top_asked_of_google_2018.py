from selenium import webdriver

options = webdriver.ChromeOptions()

options.add_argument('/Users/shanecheek/Desktop/projects/easy_com_names/chromedriver')
options.add_argument('headless')
browser = webdriver.Chrome(options=options)

#### settings:
data_css_selector = 'td:nth-child(2)'
from_url = 'https://www.mondovo.com/keywords/most-asked-questions-on-google'
file_name = 'top_asked_of_google_2018.txt'

list_of_names = []

#### google domain search
base_url = "https://domains.google.com/m/registrar/search?hl=en-US&tab=0&searchTerm="

browser.get(from_url)  # navigate to the page
browser.implicitly_wait(10)
results = browser.find_elements_by_css_selector(data_css_selector)
for word in results:
    if word.text.isalnum():
        word = word.text
        list_of_names.append(word)
    else:
        word = word.text.replace(" ", "")
        list_of_names.append(word)

txt_file = open(file_name, "a+")
print('Done creating the list')
listlen = str(len(list_of_names))
print('List is ' + listlen + " long")
count = 1
for name in list_of_names[::-1]:
    print(str(count) + ' / ' + str(listlen))
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
    count += 1
txt_file.close()
