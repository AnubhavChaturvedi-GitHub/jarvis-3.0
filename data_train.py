import re

def read_paragraph_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        paragraph = file.read()
    return paragraph

def save_paragraph_to_file(paragraph, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(paragraph)

def find_matching_sentence(paragraph, query):
    # Preprocess the paragraph to handle variations in input
    paragraph = paragraph.replace('\n', ' ')
    paragraph = re.sub(r'\s+', ' ', paragraph)

    # Search for a sentence containing the query
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', paragraph)
    for sentence in sentences:
        if query.lower() in sentence.lower():
            return sentence

    return "I'm sorry, I couldn't find relevant information for that query in the paragraph."

if __name__ == "__main__":
    # File paths
    input_file_path = "input_paragraph.txt"
    output_file_path = "output_paragraph.txt"

    # Read paragraph from file
    paragraph = read_paragraph_from_file(input_file_path)

    # Ask a question
    query = input("Ask a question: ")
    answer = find_matching_sentence(paragraph, query)

    # Print the answer
    print("Answer:", answer)
