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

https://github.com/Hugo-Hattori/Customer_Profile_Analysis/blob/c4ff758575da7633a1ee8035707a4df652a561c3/Customer_Profile_Analysis.py#L3-L7

## Data Processing
<p>Using the DataFrame.info() method we can observe two major problems: </p>

<ol>
    <li>The column "Salário Anual (R$)" is a Dtype object and not a Dtype int64;</li>
    <li>There're 35 entries where "Profissão" information is null, so these
are not very useful data.</li>
</ol>

https://github.com/Hugo-Hattori/Customer_Profile_Analysis/blob/c4ff758575da7633a1ee8035707a4df652a561c3/Customer_Profile_Analysis.py#L12-L15

## Data Analysis
<p>By using the DataFrame.describe() method we can see that the average
score achieved is around 52, so this will be our main benchmark.</p>

![image](https://github.com/Hugo-Hattori/Customer_Profile_Analysis/assets/136493140/6ba3b76d-cb23-4998-bbad-17d4cb81821a)


<p>Using .histogram() method from plotly.express package we can perform a
graphic analysis, comparing the Score with the other parameters such as
Age (Idade) or Yearly Income (Salário Anual).</p>

![Captura de tela 2023-06-21 204934](https://github.com/Hugo-Hattori/Customer_Profile_Analysis/assets/136493140/f6ca3094-538c-4123-ae7c-bef6e65ef7d9)
![Captura de tela 2023-06-21 205007](https://github.com/Hugo-Hattori/Customer_Profile_Analysis/assets/136493140/00240d36-acf2-451a-b597-88dc1849d24e)
![Captura de tela 2023-06-21 205039](https://github.com/Hugo-Hattori/Customer_Profile_Analysis/assets/136493140/fbac0d3e-24d2-4f9b-bc0f-aa28d1766d2f)
![Captura de tela 2023-06-21 205057](https://github.com/Hugo-Hattori/Customer_Profile_Analysis/assets/136493140/6e3784a4-381e-4854-bb11-2e0c6735d51b)

## Conclusion
<p>Analysing the Age X Score, Profession X Score, Work Experience X Score
and Family Size X Score graphics we can conclude that the ICP is above
15 years old, works in the Entertainment Industry or is an Artist, has between
10 to 15 years of work experience, and has a family size no larger than 7.</p>

<p> Note: this is a project developed for academic purposes, therefore the
data contained in "Clientes.csv" is fictitious and used only to learn Pandas and 
Plotly packages applications.</p>
