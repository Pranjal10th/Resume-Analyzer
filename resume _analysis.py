import tkinter as tk
from tkinter import filedialog, messagebox, ttk, scrolledtext
import os
import shutil
import re
import textract
import PyPDF2
import docx
import pandas as pd
import webbrowser

# Extract text from file
def extract_text(filepath):
    try:
        if filepath.endswith('.pdf'):
            with open(filepath, 'rb') as f:
                reader = PyPDF2.PdfReader(f)
                return ' '.join(page.extract_text() or '' for page in reader.pages)
        elif filepath.endswith('.docx'):
            doc = docx.Document(filepath)
            return ' '.join(para.text for para in doc.paragraphs)
    except:
        return ""
    return ""

# Extract Name, Email, Phone
def extract_details(text):
    email = re.findall(r'\b[\w.-]+?@\w+?\.\w+?\b', text)
    lines = text.strip().split('\n')
    name = lines[0] if lines else 'Not Found'
    return name.strip(), email[0] if email else 'Not Found'

# Experience Matching
def experience_matches(text, exp):
    patterns = [
        rf'{exp}\s*\+?\s*(years?|yrs?)',
        rf'over\s*{exp}\s*(years?|yrs?)',
        rf'at\s*least\s*{exp}\s*(years?|yrs?)',
        rf'minimum\s*{exp}\s*(years?|yrs?)',
    ]
    return any(re.search(pat, text.lower()) for pat in patterns)

# Suggestions
def generate_suggestions(missing_skills):
    if not missing_skills:
        return "Try improving resume clarity and keyword optimization."
    tips = [f"Learn {skill.title()} from wscube tech.com/Coursera/YouTube." for skill in missing_skills]
    return "\n".join(tips)

def shortlist_candidates():
    folder = folder_entry.get()
    skills = skills_entry.get().split(',')
    education = education_entry.get().lower()
    experience = experience_entry.get()

    if not folder or not skills or not experience or not education:
        messagebox.showwarning("Input Missing", "Please fill all fields!")
        return

    try:
        experience = int(experience)
    except ValueError:
        messagebox.showwarning("Invalid Experience", "Experience must be a number!")
        return

    criteria = {'skills': skills, 'experience': experience, 'education': education}

    shortlisted.clear()
    not_shortlisted.clear()
    shortlisted_tree.delete(*shortlisted_tree.get_children())
    not_shortlisted_tree.delete(*not_shortlisted_tree.get_children())

    short_dir = os.path.join(folder, 'Shortlisted')
    not_short_dir = os.path.join(folder, 'Not_Shortlisted')
    os.makedirs(short_dir, exist_ok=True)
    os.makedirs(not_short_dir, exist_ok=True)

    for file in os.listdir(folder):
        filepath = os.path.join(folder, file)
        if not file.endswith(('.pdf', '.docx')):
            continue
        text = extract_text(filepath).lower()
        name, email = extract_details(text)
        words = set(text.split())
        missing_skills = [skill for skill in skills if skill.lower() not in words]
        exp_match = experience_matches(text, experience)
        edu_match = education in text

        if not missing_skills and exp_match and edu_match:
            shutil.copy(filepath, short_dir)
            shortlisted.append((name, email, filepath))
            shortlisted_tree.insert('', 'end', values=(name, email))
        else:
            shutil.copy(filepath, not_short_dir)
            not_shortlisted.append((name, email, filepath, missing_skills))
            not_shortlisted_tree.insert('', 'end', values=(name, email))

def open_resume(event):
    item = shortlisted_tree.focus()
    if item:
        idx = shortlisted_tree.index(item)
        filepath = shortlisted[idx][2]
        os.system(f'xdg-open "{filepath}"' if os.name != 'nt' else f'start "" "{filepath}"')

def show_missing_skills(event):
    item = not_shortlisted_tree.focus()
    if item:
        idx = not_shortlisted_tree.index(item)
        name, email, path, missing = not_shortlisted[idx]
        tips = generate_suggestions(missing)
        info = f"Missing Skills: {', '.join(missing) if missing else 'None'}\n\nSuggested Skills:\n{tips}"
        messagebox.showinfo(f"{name} - Improvement Tips", info)

root = tk.Tk()
root.title("Resume Shortlister")
root.geometry("900x600")

tk.Label(root, text="Folder:").grid(row=0, column=0, sticky='w')
folder_entry = tk.Entry(root, width=60)
folder_entry.grid(row=0, column=1, padx=5)
tk.Button(root, text="Browse", command=lambda: folder_entry.insert(0, filedialog.askdirectory())).grid(row=0, column=2)

tk.Label(root, text="Skills (comma separated):").grid(row=1, column=0, sticky='w')
skills_entry = tk.Entry(root, width=60)
skills_entry.grid(row=1, column=1, padx=5)

tk.Label(root, text="Experience (years):").grid(row=2, column=0, sticky='w')
experience_entry = tk.Entry(root, width=60)
experience_entry.grid(row=2, column=1, padx=5)

tk.Label(root, text="Education:").grid(row=3, column=0, sticky='w')
education_entry = tk.Entry(root, width=60)
education_entry.grid(row=3, column=1, padx=5)

tk.Button(root, text="Start Shortlisting", command=shortlist_candidates).grid(row=4, column=1, pady=10)

tk.Label(root, text="Shortlisted Candidates").grid(row=5, column=0)
tk.Label(root, text="Not Shortlisted Candidates").grid(row=5, column=1)

shortlisted = []
not_shortlisted = []

shortlisted_tree = ttk.Treeview(root, columns=('Name', 'Email'), show='headings')
shortlisted_tree.heading('Name', text='Name')
shortlisted_tree.heading('Email', text='Email')
shortlisted_tree.grid(row=6, column=0, padx=10, pady=10)
shortlisted_tree.bind('<Double-1>', open_resume)

not_shortlisted_tree = ttk.Treeview(root, columns=('Name', 'Email'), show='headings')
not_shortlisted_tree.heading('Name', text='Name')
not_shortlisted_tree.heading('Email', text='Email')
not_shortlisted_tree.grid(row=6, column=1, padx=10, pady=10)
not_shortlisted_tree.bind('<Double-1>', show_missing_skills)

root.mainloop()
