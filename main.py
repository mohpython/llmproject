import os

def read_content(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"File '{file_name}' not found. Please check the file path.")
        return None

def read_text_and_annotation(base_path, file_prefix):
    text_file_path = os.path.join(base_path, f"{file_prefix}.txt")
    annotation_file_path = os.path.join(base_path, f"{file_prefix}.ann")

    text_content = read_content(text_file_path)
    annotation_content = read_content(annotation_file_path)

    return text_content, annotation_content

# Example usage
base_path = "mer-a"
file_prefix = "2004_1770"

text_content, annotation_content = read_text_and_annotation(base_path, file_prefix)

if text_content is not None and annotation_content is not None:
    print(f"Content of the text file ({file_prefix}.txt):")
    print(text_content)

    print(f"\nContent of the annotation file ({file_prefix}.ann):")
    print(annotation_content)
