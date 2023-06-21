# Customer Profile Analysis
<p>This project's goal is to increase a company's revenue by identifying the
Ideal Customer Profile (ICP) also known as the most valuable customer for the company.</p>

<p>To this purpose, each client presented in the database was given a score from
1 to 100, with 100 being the most valuable client and 1 the least valuable.</p>

### Packages used:
+ pandas
+ plotly.express
+ plotly.io

## Importing the Database
<p>First we need to import the database, visualize and process the data using
the pandas package. In this scenario the .csv file contains special
characters and is separated by semicolon instead of comma so the keyword
arguments "enconding" and "sep" are not default. Also, the dataframe
contains a column with empty values, so we need to drop it.</p>



## Data Processing
<p>Using the DataFrame.info() method we can observe two major problems: </p>

<ol>
    <li>The column "Salário Anual (R$)" is a Dtype object and not a Dtype int64;</li>
    <li>There're 35 entries where "Profissão" information is null, so these
are not very useful data.</li>
</ol>



## Data Analysis
<p>By using the DataFrame.describe() method we can see that the average
score achieved is 52 so this will be our main benchmark.</p>



<p>Using .histogram() method from plotly.express package we can perform a
graphic analysis, comparing the Score with the other parameters such as
Age (Idade) or Yearly Income (Salário Anual).</p>



## Conclusion
<p>Analysing the Age X Score, Profession X Score, Work Experience X Score
and Family Size X Score graphics we can conclude that the ICP is above
15 years old, works in the Entertainment Industry or is an Artist, has between
10 to 15 years of work experience, and has a family size no larger than 7.</p>

<p> Note: this is a project developed for academic purposes, therefore the
data contained in "Clientes.csv" is fictitious and used only to learn Pandas 
Plotly packages applications.</p>
