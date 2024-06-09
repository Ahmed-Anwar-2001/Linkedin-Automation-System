from langchain_community.document_loaders import PyPDFLoader

def read_pdf(path):
    loader = PyPDFLoader(path, extract_images=True)
    pages = loader.load()
    return pages
