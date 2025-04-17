from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader

loader = DirectoryLoader(
    path = 'books',
    glob = '*.pdf',
    loader_cls = PyPDFLoader
    
)

docs = list(loader.lazy_load())



for document in docs:
    print(document.metadata)

print(len(docs))
print(docs[322].page_content)
print(docs[322].metadata)



# Extract content from 'audio_analyst_trainee_JD.pdf'
pdf_text = ""

for doc in docs:
    if doc.metadata['source'] == "books/audio_analyst_trainee_JD.pdf":
        pdf_text += doc.page_content + "\n\n"  # Append text with spacing

# Print the full extracted text
print(pdf_text)
print('-'*50)


# Extract content from only page 0 of 'audio_analyst_trainee_JD.pdf'
for doc in docs:
    if doc.metadata['source'] == "books/audio_analyst_trainee_JD.pdf" and doc.metadata['page'] == 0:
        print(doc.page_content)  # Print only page 0 content
        break  # Stop after finding the required page
print('-'*50)


# Extract from the other source of the folder
for doc in docs:
    if doc.metadata['source'] == 'books/Building Machine Learning Systems with Python - Second Edition.pdf' and doc.metadata['page'] == 323:
        print(doc.page_content)
        break
print('-'*50)
