import io
import os

import requests
import PyPDF2


def get_description(url):
    test_url = url
    pdf_response = requests.get(test_url)
    pdf_content = pdf_response.content
    pdf_reader = PyPDF2.PdfReader(io.BytesIO(pdf_content))

    tmp_file = io.open("tmp_file.txt", "w", encoding='utf-8')

    for i in range(len(pdf_reader.pages)):
        page_text = pdf_reader.pages[i].extract_text()
        tmp_file.write(page_text)

    tmp_file.close()
    tmp_file = io.open("tmp_file.txt", "r", encoding='utf-8')
    text = tmp_file.read()
    tmp_file.close()
    os.remove("tmp_file.txt")

    return text


if __name__ == "__main__":
    print(get_description("https://www.mos.ru/upload/documents/files/6710/AktGIKE_Romanov_per_8_2.pdf"))
