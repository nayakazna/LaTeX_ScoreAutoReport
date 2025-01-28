import os

def add_identity(name: str, id: str):
    # Update the name and id in the LaTeX template
    with open('info.tex', 'w') as file:
        file.write(f'\\newcommand{{\\studentname}}{{{name}}}\n')
        file.write(f'\\newcommand{{\\studentid}}{{{id}}}\n')

def add_table(score_nickname: list, score_weight: list, scores: list):
    # Add the table of scores to info.tex that will be included in the LaTeX template
    # You can customize the table header here
    kategori = 'Kategori' # Category, in Indonesian
    bobot = 'Bobot' # Weight, in Indonesian
    nilai = 'Nilai' # Score, in Indonesian
    
    with open('info.tex', 'a') as file:
        file.write('\\newcommand{\\scoretable}{\n')
        file.write('\\begin{center}\n')
        file.write('\\footnotesize\n')
        file.write('\\begin{tblr}{hlines,vlines}\n')

        # Write the category
        file.write('\\textbf{'+ kategori +'}')
        for nickname in score_nickname:
            file.write(' & \\textsc{' + nickname + '}')
        file.write('\\\\\n')

        # Write the weight
        file.write('\\textbf{' + bobot + '}')
        for weight in score_weight:
            file.write(f'& {weight}')
        file.write('\\\\\n')

        # Write the scores
        file.write('\\textbf{' + nilai + '}')
        for score in scores:
            file.write(f'& {score}')
        file.write('\\\\\n')

        file.write('\\end{tblr}\n')
        file.write('\\end{center}\n')
        file.write('}')

def compile_latex(filename: str):
    # Compile the LaTeX file into PDF
    # You can access the PDF file in the `outputs` folder
    os.system(f'pdflatex --jobname={filename} --output-directory=outputs template.tex')
    # Clean up unused files
    os.remove(f'outputs/{filename}.log')
    os.remove(f'outputs/{filename}.aux')
