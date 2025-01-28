# from .modules.email import *
from modules import latex
import csv

with open('data.csv', 'r') as file:
    # Data preparation
    ## read from csv
    reader = csv.reader(file)
    
    ## read header
    header = next(reader)
    
    ## read score nickname (skip first 3 columns)
    score_nickname = next(reader)[3:]

    ## read score weight
    score_weight = next(reader)[3:]
    
    ## read data of each student
    for row in reader:
        name = row[0]
        nim = row[1]
        email_address = row[2]
        scores = row[3:]

        latex.add_identity(name, nim)
        latex.add_table(score_nickname, score_weight, scores)
        latex.compile_latex(nim)

