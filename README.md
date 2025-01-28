# LaTeX_ScoreAutoReport
A simple Python script to automate the generation and email distribution of students' score breakdown for a course in the form of PDFs made with LaTeX.

# Background
For a course I took, the lecturer provided the detailed students' scores in a spreadsheet that can be viewed by everyone. However, students sometimes prefer to not share their scores with others. To respect their privacy, I created this script to automate the generation and email distribution of the students' score breakdown in the form of PDFs made with LaTeX.

# Installation
1. Clone this repository:
    ```bash
    git clone https://github.com/nayakazna/LaTeX_ScoreAutoReport.git
    ```
2. Make sure you have Python installed. This script is tested on Python 3.8.5 but should work on other versions as long as it has `os`, `csv`, `smtplib`, and `email` installed (these packages are included in the Python standard library). You can check your Python version by running:
    ```bash
    python --version
    ```
3. Make sure you have LaTeX installed. This script uses `pdflatex` to compile the LaTeX template. You can check if you have LaTeX installed by running:
    ```bash
    pdflatex --version
    ```
    If you don't have LaTeX installed, you can download it [here](https://www.latex-project.org/get/).
4. (Optional) Modify the email and LaTeX template in accordance with your needs (see [Template Modification](#template-modification)).

# Usage
1. Prepare the students' scores in a CSV file. The CSV file should have the following columns (see [data.csv](data.csv) for an example):
    - `nama`: Student's name
    - `nim`: Student's ID
    - `email`: Student's email
    - the rest of the columns are the scores for each category
    - The first row should be the header
    - The second row contains the 'nickname' of the category i.e. the name of the category that will be displayed in the PDF
    - The third row contains the weight of the category (written in decimal notation, must sums up to 1)
    - The rest of the rows contain the data of the students
2. If you are using Gmail and have enabled 2-step verification, you need to create an app password. Follow the instructions [here](https://support.google.com/accounts/answer/185833?hl=en). The app password is the password you will use in the script used instead of your actual password.
3. Run the script:
    ```bash
    python main.py
    ```
4. Enter your email and password when prompted.
5. Wait and see!

# Template Modification
## Email Template
The email template can be modified in the 35-36th line of [`main.py`](main.py).
```python
35 subject = 'Rincian Nilai IF2123 Aljabar Linear dan Geometri'
36 body = f'Berikut adalah rincian nilai Anda untuk mata kuliah IF2123 Aljabar Linear dan Geometri.\n\nTerima kasih.'

```

## LaTeX Template
The original LaTeX template is in Indonesian. You can modify it in [`template.tex`](template.tex).
The header for the table can be modified in line 12-14 of [`latexutils.py`](modules/latexutils.py).
```python
12 kategori = 'Kategori' # Category, in Indonesian
13 bobot = 'Bobot' # Weight, in Indonesian
14 nilai = 'Nilai' # Score, in Indonesian
```

# Images
An example of the generated PDF files.
![image](https://github.com/user-attachments/assets/2617dc37-3863-4387-95b3-860ad36a6bf9)
![image](https://github.com/user-attachments/assets/a8d7b02f-6bcc-4ec5-a2df-ed5e24c0bf68)
