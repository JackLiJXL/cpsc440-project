from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter

def lines_to_relevant_strings(lines, docs, segment_length):
    contained = set()
    for doc in docs:
        for line in lines:
            if line in doc.page_content:
                contained.add(doc.page_content)
    return list(contained)

def percentage_contained(groundtruth, result):
    num = 0
    denum = len(groundtruth)
    if denum == 0:
        print("Did not find corresponding segments")
    for segment in groundtruth:
        if segment in result:
            num += 1
    return num / denum
