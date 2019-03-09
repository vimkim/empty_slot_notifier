from time import sleep
from bs4 import BeautifulSoup
import re

def extract(html):
    # html = open('output.html', 'r')
    soup = BeautifulSoup(html, "html.parser")

    '''
    for td in soup.find_all('td'):
        print(td)
    '''
    tds = soup.find_all('td')
    tds = [i.text for i in tds]
    re_rm_ws = re.compile('\s*')

    # f = open('course_list.txt', 'w')
    course_list = [[]]
    for i,l in enumerate(tds):
        j = i % 19
        if j == 1 or j == 2 or j == 5:
            # print(l.strip(), end='/', file=f)
            course_list[-1].append(l.strip())
        elif j == 4:
            l = re_rm_ws.sub('', l)
            course_list[-1].append(l)
            # print(l, end='/', file=f)
        elif j == 18:
            # print(l.strip(), file=f)
            course_list[-1].append(l.strip())
            course_list.append([])
    del course_list[-1]
    return course_list


def filter_courses(wishlist):
    f = open('course_list.txt', 'r')
    for line in f:
        if line[0:10] in wishlist:
            print(line.strip())

"""this is main function."""

f = open('wishlist.txt')
wishlist = []
for line in f:
    wishlist.append(line.strip())
print(wishlist)

# open driver
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://sugang.korea.ac.kr")

input("press enter after finishing login")

submit_xpath = "/html/body/div/div[2]/form/div[1]/div[1]/span[2]/input"

def compare_course_list(prev_list, curr_list):
    if len(prev_list[0]) == 0:
        for course in curr_list:
            print(course)
        return

    change_count = 0
    for i, (j, k) in enumerate(zip(prev_list, curr_list)):
        if j[-1] != k[-1]:
            print('O:', j, "changed to", k[-1])
            change_count += 1
    if change_count == 0:
        print('nothing changed')
    elif change_count >= 1:
        print(' ALERT ALERT ALERT ')
        print(' ALERT ALERT ALERT ')
        print(' ALERT ALERT ALERT ')




# counter
i = 1
prev_list = [[]]
while(True):
    driver.switch_to.default_content()
    driver.switch_to.frame('firstF')
    driver.switch_to.frame('ILec')
    submit_button = driver.find_elements_by_xpath(submit_xpath)[0]
    submit_button.click()

    # request
    #html = driver.execute_script("""return document.getElementsByTagName('frame')['firstF'].contentDocument.getElementsByTagName('frame')["ILec"].contentDocument.getElementsByTagName('table')[0].innerHTML""")
    html = driver.execute_script("""return document.getElementsByTagName('table')[0].innerHTML""")

    #f = open('output.html', 'w')
    #f.write(html)

    course_list = extract(html)

    compare_course_list(prev_list, course_list)
    prev_list = course_list

    # filter_courses(wishlist)
    print(i, "times")
    i += 1

    sleep(10)
