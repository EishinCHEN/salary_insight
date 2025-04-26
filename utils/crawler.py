import requests
from bs4 import BeautifulSoup
import pandas as pd

def fetch_104_jobs(keyword, max_pages=40):
    job_data = []

    for page in range(1, max_pages + 1):
        url = f"https://www.104.com.tw/jobs/search/?jobsource=index_s&keyword={keyword}&mode=s&page={page}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        articles = soup.find_all("div", class_ = "info-container")  

        if not articles:
            break  

        for job in articles:
            org_salary_desc = job.select('a[data-gtm-joblist^="職缺-薪資"]')
            salary_type = ""
            salary_arrange = ""
            min_salary = ""
            max_salary = ""
            if len(org_salary_desc) > 0:
                salary_desc = org_salary_desc[0].text
                # 辨識給薪方式
                if salary_desc == "待遇面議":
                    salary_type = "面議"
                    min_salary = 0
                    max_salary = 0
                else :
                    salary_type = salary_desc[:2]
                    # 擷取薪資上下限
                    for char in salary_desc:
                        if char.isnumeric() or char == "~":
                            salary_arrange += char
                    if salary_arrange.find("~") > 0:
                        min_salary = int(salary_arrange[:salary_arrange.find("~")])
                        max_salary = int(salary_arrange[salary_arrange.find("~") + 1:])
                job_data.append({"計薪方式": salary_type, "薪資下限": min_salary, "薪資上限": max_salary})

    df = pd.DataFrame(job_data)
    return df