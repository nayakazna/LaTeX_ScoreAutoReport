# LaTeX_ScoreAutoReport
A simple Python script to automate the generation and email distribution of students' score breakdown for a course in the form of PDFs made with LaTeX.

# Background
For a course I took, the lecturer provided the detailed students' scores in a spreadsheet that can be viewed by everyone. However, students sometimes prefer to not share their scores with others. To respect their privacy, I created this script to automate the generation and email distribution of the students' score breakdown in the form of PDFs made with LaTeX.

# Installation
Install the required packages by running:
```bash
pip install -r requirements.txt
```

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
3. See [Template Modification](#template-modification) to modify the email and LaTeX template in accordance with your needs.
4. Run the script:
    ```bash
    python main.py
    ```

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