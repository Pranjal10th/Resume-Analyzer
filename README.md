# Resume-Analyzer
# PROBLEM:Smart 
Resume Analyzer for Career Growth: Users find it hard to know what skills or experience they’re missing for their dream roles.
How can an AI system help users analyse their resume and suggest personalized improvements or learning paths?
#DOCUMENTATION ODF THE CODE

**📄 Resume Shortlister - Python GUI Tool**
Resume Shortlister is a simple, Tkinter-based Python application that helps HR teams or recruiters filter and shortlist candidates based on predefined criteria such as skills, experience, and education. 
It supports resumes in .pdf and .docx formats.

**🖥️ GUI Preview**


**🔧 Features**
📂 Folder Selection: Select a folder containing resumes.

✅ Skill Matching: Match resumes based on provided skill keywords.

📚 Education Filter: Filter resumes containing a specific education qualification.

⏳ Experience Check: Checks if the candidate meets the required years of experience.

📄 Resume Viewer: Double-click to open shortlisted resumes.

💡 Skill Suggestions: Provides improvement suggestions for non-shortlisted candidates.

**📁 File Support**
1) .pdf

2) .docx

Text extraction is handled using:

" PyPDF2 for PDFs "

" python-docx for DOCX "
**🔍 How It Works**

1] SELECT RESUME FOLDER – Choose a directory with all the resume files.

2] ENTER CRITERIA – Provide comma-separated skills, required education, and minimum years of experience.

3] CLICK "Start Shortlisting" – The tool will parse resumes, match them to the criteria, and classify them.

4] REVIEW RESULTS:

    > SHORTLISTED CANDIDATES: Double-click to open their resume.

    > NOT SHORTLISTED: Double-click to view missing skills and improvement suggestions.
    
**📦 Installation**
      ✅ Prerequisites
       > Make sure Python 3.x is installed. Install the required libraries:
       { pip install textract PyPDF2 python-docx pandas } 
       
**📂 Output**

After running the tool:

  >> Shortlisted/: Contains resumes that matched all criteria.

  >> Not_Shortlisted/: Contains those that didn’t match one or more requirements.

**🧠 Logic Overview**
Text Extraction:
  {  extract_text(filepath) }
  [ Extracts text from .pdf or .docx using PyPDF2 or python-docx.]
  
  **Matching Criteria**
  
SKILLS: Compares resume content with provided keywords.

EXPERIENCE: Uses regex to find matches like 3 years, over 3 yrs, etc.

EDUCATION: Checks for presence of education keyword in resume text.

**Output Handling**

> shortlisted[]: Stores matched candidate name, email, filepath.

> not_shortlisted[]: Stores rejected candidates along with missing skills.

 **📌 Example Input**
 
SKILLS: python, sql, machine learning

EXPERIENCE: 3 YEARS

EDUCATION: bachelorS Degree

**🛠️ Technologies Used**

Python 3

Tkinter – GUI

PyPDF2, python-docx – Text extraction

Regex – Matching patterns

shutil – File handling

pandas – Optional for future expansion















