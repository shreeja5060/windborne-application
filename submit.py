import requests

url = "https://windmc.windbornesystems.com/career_applications.json"

payload = {
    "career_application": {
        "name": "Shreeja Singh",
        "email": "shreeja.jsr10@gmail.com",
        "role": "Machine Learning Research Engineer",
        "resume_url": "https://raw.githubusercontent.com/shreeja5060/windborne-application/main/SHREEJA%20SINGH_Machine%20Learning%20Research%20Engineer_20260714.pdf",
        "submission_url": "https://raw.githubusercontent.com/shreeja5060/windborne-application/main/submissions.md",
        "portfolio_url": "https://shreeja-portfolio.netlify.app/",
        "notes": "MS Computer Science student at Illinois Institute of Technology. Interested in ML research, AI agents, RAG systems, and weather forecasting."
    }
}

response = requests.post(url, json=payload)

print("Status Code:", response.status_code)
print(response.text)
