# Resume-Analyzer
# PROBLEM STATEMENT:
Smart Resume Analyzer for Career Growth: Users find it hard to know what skills or experience they’re missing for their dream roles.
How can an AI system help users analyse their resume and suggest personalized improvements or learning paths?                                              

# Overview
This project is designed to automate the process of shortlisting candidates based on their resumes. The tool provides a simple and user-friendly Graphical User Interface (GUI) built with Tkinter.

The application allows HR teams or recruiters to input selection criteria like required skills, education level, and minimum years of experience. It then scans all resumes in a selected folder, extracts relevant details, and filters candidates accordingly.

Shortlisted and non-shortlisted resumes are automatically moved into separate folders for easy access.
# Key Features
User-friendly GUI for input and interaction.

Supports .pdf and .docx resume formats.

Extracts:

Name

Email

Skills

Experience

Education

Automatically creates:

Shortlisted/ Folder

Not_Shortlisted/ Folder

Shows lists of:

Shortlisted Candidates

Not Shortlisted Candidates

Provides improvement suggestions for non-shortlisted candidates.

# Function Documentation
1. extract_text(filepath)
   
    Purpose:
Extracts raw text content from .pdf or .docx resume files.

2. extract_details(text)

    Purpose:
Extracts Name and Email from the provided text of a resume.

3. experience_matches(text, exp)

    Purpose:
Checks whether the candidate's resume mentions at least the required years of experience.

4. generate_suggestions(missing_skills)
   
    Purpose:
Provides skill improvement suggestions based on missing skills in the resume.

5. shortlist_candidates()
   
    Purpose:
   
       Resume screening
   
       Extracting data
   
       Matching skills, experience & education
   
       Shortlisting or Rejecting candidates
   
       Displaying results in GUI
   
       Copying resumes to respective folders

# GUI Documentation
The GUI has the following fields:

- Folder Path: A field to enter the folder path containing the resumes.
- Skills: A field to enter the required skills (comma-separated).
- Experience: A field to enter the required experience (years).
- Education: A field to enter the required education.

The GUI also has a "Shortlist Candidates" button that triggers the shortlisting logic.

# Usage
To use this code, follow these steps:

1. Run the code to launch the GUI.
2. Select a folder containing resumes by clicking the "Browse" button.
3. Enter the required skills, experience, and education in the corresponding fields.
4. Click the "Shortlist Candidates" button to start the shortlisting process.
5. The shortlisted resumes will be copied to a new "Shortlisted" folder within the selected folder.
6. Those candidate who are not shotlisted their resume will be copied to a new "Not Shortlisted" folder within the selected folder.
# Dependencies
Library	Purpose

tkinter	GUI design

textract	Text extraction (Optional use)

PyPDF2	PDF text extraction

python-docx	DOCX text extraction

pandas	Data handling (Optional)

shutil	Copying files

re	Regex for pattern matching
