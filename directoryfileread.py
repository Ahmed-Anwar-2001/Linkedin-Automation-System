from dependency import *
from readdocx import *
from readpdf import *
    

def read_files(directory):
    data = []
    files_content = []
    for file in os.listdir(directory):
        if file.endswith(".pdf"):
            file_path = os.path.join(directory, file)
            print(file_path)
            files_content = read_pdf(file_path)
        elif file.endswith(".docx"):
            file_path = os.path.join(directory, file)
            files_content = load_docx(file_path)
        else:
            files_content = []
        data+=files_content
    return data