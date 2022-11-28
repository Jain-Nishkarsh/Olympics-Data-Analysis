# OLYMPICS-DATA-ANALYSIS

*This is a project that I made in school for my Informatics Practices class*

### Purpose
This is a program designed to manipulate the data from the Summer Olympics Games (1894 - 2020). The purpose of this project is to create a user-friendly program that is capable of manipulating numerous rows of data and displays the required data in desirable format.

The data is stored as an easy to read, edit and format **csv (comma separated value) file**. Using the application on the front end, the data can be manipulated and filtered with user friendly interactive commands.

This program being simple in design and working does not require much user-training and can be used as a powerful tool for manipulating the data of the Olympics Games

The main program was created using a Python Jupyter Notebook. Python libraries **Matplotlib, Pandas and Numpy** were also used to make many functions and commands possible.

---
### Data Used

This data was taken from [Kaggle.com](https://www.kaggle.com/)

Example Data File:
![DataExample](https://github.com/Jain-Nishkarsh/Olympics-Data-Analysis/blob/main/Readme_Metadata/Data_Example_Image.png)

Data Field Description:
![DataFieldDescription](https://github.com/Jain-Nishkarsh/Olympics-Data-Analysis/blob/main/Readme_Metadata/DataDescription_Image.png)

---
### Functions Used in this Program

| **Functions**                 | **Arguments** | **Purpose**                                                                                        |
|-------------------------------|---------------|----------------------------------------------------------------------------------------------------|
|       First_Place(year)       |      Year     |                       Displays the statistics of the first place of the year                       |
|       Second_Place(year)      |      Year     |                       Displays the statistics of the second place of the year                      |
|       Third_Place(year)       |      Year     |                       Displays the statistics of the third place of the year                       |
|       Rank(year,country)      | Year, Country |                     Prints the rank of the specified country in the year given                     |
|    Medals_Won(country,year)   | Year, Country |                Prints out medals won by the specified country in the specified Year                |
| TotalMedals_BarGraph(country) |    Country    | Plots a bar graph of total number of medals (Gold, silver and bronze) won by the specified country |
|    Point_LineGraph(country)   |    Country    |                   Plots a Line graph of the Points in each Olympics of a country                   |
|  Point_ScatterGraph(country)  |    Country    |                  Plots a Scatter graph of the Points in each Olympics of a country                 |
|    Yearwise_MedalBar(year)    |      Year     |            Plots a Bar graph of the Medals won by different countries in specified year            |
|    MedalDist_PieChart(year)   |      Year     |   Plots a Pie chart of the Distribution of Medals among different countries in the year specified  |
|          Print_Data()         |      None     |                                      Prints out the Dataframe                                      |
|         Country_List()        |      None     |            Prints out a List of all the countries that have participated in the Olympics           |
|          Year_Array()         |      None     |                  Prints out an array of all the years when the Olympics were held                  |
|   Country_Info(country,year)  | Country, Year |              Prints out the performance of the specified country in the specified year             |
|         PointSystem()         |      None     |                    Gives information about the Point system used in the program                    |
|        RankingSystem()        |      None     |                   Gives information about the Ranking system used in the program                   |
