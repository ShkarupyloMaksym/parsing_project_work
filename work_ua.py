import re

import requests
from bs4 import BeautifulSoup


def average(arr):
    if len(arr)==0:
        return 0
    return sum(arr) / len(arr)


class Work_ua:
    def __init__(self, *name_job):
        self.name_job = []
        for i in name_job:
            if type(i) == str:
                self.name_job.append([i])
            else:
                self.name_job.append(i)

    def jobs(self, number):
        number = int(number)
        numbers, links = [], []
        for name_job in self.name_job:
            for page_number in range(1, number + 1):
                site = requests.get('https://www.work.ua/jobs-dnipro-{job_name}/?page={page_number}'.format(
                    page_number=page_number, job_name=name_job[0].replace(' ', '+')))
                soup = BeautifulSoup(site.content, 'html.parser')
                a = soup.findAll('div', class_=re.compile('card card-hover card-visited wordwrap job-link'))
                for j in a:
                    # print([i for i in j.findAll('a')])
                    b = j.find_all(href=re.compile('/jobs/'))[0]
                    if b.text in name_job:
                        b = b.parent.parent
                        b = b.findAll('div', class_=None)
                        if not b:
                            continue
                        b = b[0]
                        b = b.findAll('b')
                        if not b:
                            continue
                        b = b[0]
                        link = b.parent.parent.find_all(href=re.compile('/jobs/'))[0]
                        links.append(link['href'])

                        b = b.text
                        # print(b)
                        for i in ['грн', ' ', '\u202f', '\xa0', '\u2009']:
                            b = b.replace(i, '')
                        if '–' in b:
                            # print(b)
                            b = [int(i) for i in b.split('–')]
                            b = average(b)
                        numbers.append(int(b))
        print(numbers)
        # numbers.remove(min(numbers))
        print(average(numbers))
        print(links)
        return [round(average(numbers), 2), numbers, links]


    def resumes(self, number):
        try:
            number = int(number)
        except:
            return 0
        numbers, links = [], []
        for name_job in self.name_job:
            for page_number in range(1, number + 1):
                site = requests.get('https://www.work.ua/resumes-dnipro-{job_name}/?page={page_number}'.format(
                    page_number=page_number, job_name=name_job[0].replace(' ', '+')))
                soup = BeautifulSoup(site.content, 'html.parser')
                a = soup.findAll('div', class_=re.compile('card card-hover resume-link card-visited wordwrap'))
                for j in a:
                    # print([i for i in j.findAll('a')])
                    b = j.find_all(href=re.compile('/resumes/'))[0]
                    if b.text in name_job:
                        b = b.parent
                        if not 'Повна зайнятість' in b.parent.findAll('div', class_='text-muted')[0].text:
                            continue
                        b = b.findAll('span', class_='nowrap')
                        if not b:
                            continue
                        b = b[0]
                        link = b.parent.parent.find_all(href=re.compile('/resumes/'))[0]
                        links.append(link['href'])

                        b = b.text
                        # print(b)
                        for i in ['грн', ' ', '\u202f', '\xa0', '\u2009']:
                            b = b.replace(i, '')
                        if '–' in b:
                            # print(b)
                            b = [int(i) for i in b.split('–')]
                            b = average(b)
                        numbers.append(int(b))
        print(numbers)
        # numbers.remove(min(numbers))
        print(average(numbers))
        print(links)
        return [round(average(numbers), 2), numbers, links]
