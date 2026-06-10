from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate

llm = ChatOllama(model="llama3")

template = PromptTemplate(
    input_variables=["resume_text"],
    template="""
You are an expert resume analyzer.

Rules:
- Analyze the resume carefully
- Return output in JSON format only
- Do NOT write anything outside JSON
- Keep the points simple and useful
- If information is missing, use empty string "" or empty list []
- Extract only information present in the resume

Format:
{{
  "name": "",
  "summary": "",
  "education": [],
  "experience": [],
  "skills": [],
  "projects": [],
  "strengths": [],
  "suggestions": [],
  "recommended_roles": []
}}

Resume:
{resume_text}
"""
)

print("Paste your resume below. Type END on a new line when finished:\n")

lines = []
while True:
    line = input()
    if line.strip().upper() == "END":
        break
    lines.append(line)

resume_text = "\n".join(lines)

response = llm.invoke(template.format(resume_text=resume_text))

print("\nAI Output:\n")
print(response.content)
