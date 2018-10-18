from selenium import webdriver

options = webdriver.ChromeOptions()

options.add_argument('/Users/shanecheek/Desktop/projects/easy_com_names/chromedriver')
options.add_argument('headless')
browser = webdriver.Chrome(options=options)

list_of_names = []
base_url = "https://domains.google.com/m/registrar/search?hl=en-US&tab=0&searchTerm="
# url = "https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/PG/2006/04/1-10000"
# url = "https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/PG/2006/04/10001-20000"
# url = "https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/PG/2006/04/20001-30000"
url = "https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/PG/2006/04/30001-40000"

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

txt_file = open("top_used_words_com_from_2015.txt", "a+")
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
