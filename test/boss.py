from selenium import webdriver
from lxml import etree
import time
import csv

browser = webdriver.Chrome()
browser.get('https://www.zhipin.com/job_detail/?query=python&city=100010000&industry=&position=')


def run(write):
    urls = browser.find_elements_by_css_selector('.info-primary .name a')

    for url in urls:

        link = url.get_attribute('href')
        browser.execute_script('window.open()')
        browser.switch_to.window(browser.window_handles[1])
        browser.get(link)
        try:
            job = browser.find_element_by_css_selector('.info-primary div h1').text
            salary = browser.find_element_by_css_selector('.info-primary div span').text
            jobtags = '/'.join(tag.text for tag in browser.find_elements_by_css_selector('.job-tags span') if tag.text)

            companyinfo = browser.find_element_by_css_selector('.job-sec.company-info div').text
            jobsec = browser.find_element_by_css_selector('.job-sec div').text
            address = browser.find_element_by_css_selector('.location-address').text
        except:
            pass

        print(job, salary, jobtags)

        write.writerow((job, salary, jobtags, companyinfo, jobsec, address))

        time.sleep(0.5)
        browser.close()
        browser.switch_to.window(browser.window_handles[0])
        time.sleep(0.5)


def save_scv():
    fp = open('boss_zhipin.csv', 'a', newline='', encoding='gbk')
    writer = csv.writer(fp)
    header = ('工作', '薪水', '工作标签', '公司介绍', '职位描述', '工作地址')
    writer.writerow(header)
    return writer


def main():
    write = save_scv()
    while True:
        next_page = browser.find_elements_by_css_selector('.page a')[-1]

        run(write)

        if not next_page.get_attribute('class') == 'next':
            print('页面爬取完成')
            break
        browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        next_page.click()


if __name__ == '__main__':
    main()
