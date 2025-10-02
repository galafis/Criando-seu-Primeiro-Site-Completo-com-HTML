import os
from bs4 import BeautifulSoup

def test_files_exist():
    base_path = 'Criando-seu-Primeiro-Site-Completo-com-HTML/src'
    expected_files = ['index.html', 'sobre.html', 'atendimento.html', 'contato.html', 'style.css']
    for file_name in expected_files:
        file_path = os.path.join(base_path, file_name)
        assert os.path.exists(file_path), f"File not found: {file_path}"

def test_html_structure():
    base_path = 'Criando-seu-Primeiro-Site-Completo-com-HTML/src'
    html_files = ['index.html', 'sobre.html', 'atendimento.html', 'contato.html']
    for file_name in html_files:
        file_path = os.path.join(base_path, file_name)
        with open(file_path, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f, 'html.parser')
            assert soup.find('html'), f"HTML tag not found in {file_name}"
            assert soup.find('head'), f"HEAD tag not found in {file_name}"
            assert soup.find('body'), f"BODY tag not found in {file_name}"
            assert soup.find('link', {'rel': 'stylesheet', 'href': 'style.css'}), f"style.css link not found in {file_name}"

    print("All HTML and CSS files exist and have basic valid structure.")

if __name__ == '__main__':
    test_files_exist()
    test_html_structure()

