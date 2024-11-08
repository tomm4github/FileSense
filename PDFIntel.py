import PyPDF2


def extract_metadata(pdf_path):
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        metadata = pdf_reader.metadata
        return metadata


if __name__ == '__main__':
    pdf_path = '/Users/tommorgan/Desktop/Desktop/Thomas.H.MorganCV_.pdf'  # Replace with your PDF file path
    metadata = extract_metadata(pdf_path)

    for key, value in metadata.items():
        print(f'{key}: {value}')
