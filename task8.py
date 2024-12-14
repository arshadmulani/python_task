import re
def extract_emails_from_file(file_path):
    try:
        with open(file_path,'r') as file:
            content=file.read()
        email_pattern=r'[a-zA-Z0-9._%+-]=@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        emails=re.findall(email_pattern, content)
        return emails
    except FileNotFoundError:
        print("File not found. Please provide a vaild file path.")
        return[]
file_path="E:/Arshad/Semester-7/emails.txt"
emails=extract_emails_from_file(file_path)
print(emails)
