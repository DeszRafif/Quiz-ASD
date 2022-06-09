#No 2

import re
a = """We are hiring Test/QA Engineers with 1-3 years of experience in Manual Testing(Web, Mobile & API).
If anyone((Especially who lost the job due to COVID) looking for a change, please share me the resume at
mailmesiva25@gmail.com Company:Open Financial Technologies Location: BangaloreNote: Fintech Experience
would be a higher priority"""

email =re.findall(r'[\w.-]+@[\w.-]+',a)
print(email)
