import Functions

def InputYear():
    year = int(input('Input the Year: '))
    while True:
        if Functions.Valid_Year(year) == False:
            print('Invalid Year',
                '\nYou can use "Year Array" function in Miscellaneous category')
            year = int(input('Input the Year: '))
        else:
            break
    return year

def InputCountry(year):
    country = input('Enter Country Name: ')
    #country = country.capitalize()
    while True:
        if country not in Functions.Country_Array[year]:
            print('Invalid Country Name',
                '\nYou can use "Country List" function in Miscellaneous category')
            country = input('Enter Country Name: ')
        else:
            break
    return country

def InputCountryG():
    country = input('Enter Country Name: ')
    #country = country.capitalize()
    while True:
        if country not in Functions.AllCountries_List:
            print('Invalid Country Name',
                '\nYou can use "Country List" function in Miscellaneous category')
            country = input('Enter Country Name: ')
        else:
            break
    return country

def PrintInst():
    print('-'*50)
    print('Navigation Instructions: ',
          '\nEnter response numbers according to your choice',
          '\nEnter "MainMenu" anytime to go back to main menu',
          '\nEnter "Help" anytime to get these Instructions Again',
          '\nEnter "Exit" to exit the current page',)
          #'\nEnter "Quit" to quit the program anytime')

def MainMenu():
    print('-'*50)
    print('OLYMPIC ANALYSIS')
    print('1. View Database')
    print('2. Data Analysis')
    print('3. Graphical Analysis')
    print('4. Miscellaneous')
    
    while True:
        resp = input('Enter Response: ')
        try:
            rType = type(int(resp))
        except:
            rType = type(resp)
            
        if rType==str:
            if resp=='MainMenu':
                MainMenu()
                break
            elif resp=='Exit':
                MainMenu()
                break
            elif resp=='Help':
                PrintInst()
                MainMenu()
                break
            else:
                print('Invalid Input')
                
        elif int(resp)==1:
            print(Functions.df)
            while True:
                resp1 = input('Enter "Exit" to go back to Main Menu...')
                if resp1=='Exit':
                    MainMenu()
                    break
                elif resp1=='MainMenu':
                    MainMenu()
                    break
                elif resp1=='Help':
                    PrintInst()
                    break
                else:
                    print('Invalid Response...')
                    break
        elif int(resp)==2:
            DataAnalysis()
            break
        elif int(resp)==3:
            GraphAnalysis()
            break
        elif int(resp)==4:
            MiscFunctions()
            break
        else:
            print('Invalid Input')

def DataAnalysis():
    print('-'*50)
    print('DATA ANALYSIS')
    print("1. Specified Country's performance in some year")
    print('2. Details about the First rank of specified year')
    print('3. Details about the Second rank of specified year')
    print('4. Details about the Third rank of specified year')
    print('5. Rank of specified year and country')
    print('6. Medals won by specified country in some year')
    
    while True:
        resp = input('Enter Response: ')
        try:
            rType = type(int(resp))
        except:
            rType = type(resp)
            
        if rType==str:
            if resp=='MainMenu':
                MainMenu()
                break
            elif resp=='Help':
                PrintInst()
                DataAnalysis()
                break
            elif resp=='Exit':
                MainMenu()
                break
            else:
                print('Invalid Response...')
                
        elif int(resp)==1:
            year = InputYear()
            country = InputCountry(year)
            print('-'*50)
            print(Functions.Country_Info(country,year))
            break
        elif int(resp)==2:
            year = InputYear()
            print('-'*50)
            print(Functions.First_Place(year))
            break
        elif int(resp)==3:
            year = InputYear()
            print('-'*50)
            print(Functions.Second_Place(year))
            break
        elif int(resp)==4:
            year = InputYear()
            print('-'*50)
            print(Functions.Third_Place(year))
            break
        elif int(resp)==5:
            year = InputYear()
            country = InputCountry(year)
            print('-'*50)
            print(country,"'s rank in",year, 'was',Functions.Rank(year,country))
            break
        elif int(resp)==6:
            year = InputYear()
            country = InputCountry(year)
            print('-'*50)
            print(country,'won',Functions.Medals_Won(country,year),'medals in',year)
            break
        else:
            print('Invalid Response...')
        
    print()
    while True:
        resp1 = input('Enter "Exit" to go back to Data Analysis Menu...')
        if resp1=='Exit':
            DataAnalysis()
            break
        elif resp1=='MainMenu':
            MainMenu()
            break
        elif resp1=='Help':
            PrintInst()
        else:
            print('Invalid Response...')

def GraphAnalysis():
    print('-'*50)
    print('GRAPHICAL ANALYSIS')
    print('1. Total Medals Bar Graph of specified country')
    print('2. Point vs Years Line Graph of a country')
    print('3. Point vs Years Scatter Graph of a country')
    print('4. Medals Won by different countries Bar Graph of some year')
    print('5. Medal Distribution among different countries PieChart of some year')
    
    while True:
        resp = input('Enter Response: ')
        try:
            rType = type(int(resp))
        except:
            rType = type(resp)
            
        if rType==str:
            if resp=='MainMenu':
                MainMenu()
                break
            elif resp=='Help':
                PrintInst()
                GraphAnalysis()
                break
            elif resp=='Exit':
                MainMenu()
                break
            else:
                print('Invalid Response...')
                
        
        elif int(resp)==1:
            country = InputCountryG()
            print('-'*50)
            Functions.TotalMedal_BarGraph(country)
            break
        elif int(resp)==2:
            country = InputCountryG()
            print('-'*50)
            Functions.Point_LineGraph(country)
            break
        elif int(resp)==3:
            country = InputCountryG()
            print('-'*50)
            Functions.Point_ScatterGraph(country)
            break
        elif int(resp)==4:
            year = InputYear()
            print('-'*50)
            Functions.YearWise_MedalBar(year)
            break
        elif int(resp)==5:
            year = InputYear()
            print('-'*50)
            Functions.MedalDist_PieChart(year)
            break
        else:
            print('Invalid Response...')
        
    print()
    while True:
        resp1 = input('Enter "Exit" to go back to Graphical Analysis Menu...')
        if resp1=='Exit':
            GraphAnalysis()
            break
        elif resp1=='MainMenu':
            MainMenu()
            break
        elif resp1=='Help':
            PrintInst()
        else:
            print('Invalid Response...')
            
def MiscFunctions():
    print('-'*50)
    print('MISCELLANEOUS FUNCTIONS')
    print('1. Country List by Year')
    print('2. All Countries List')
    print('3. Year Array')
    print('4. Information on the Point System used')
    print('5. Information on the Ranking System used')
    #print('6. MadeBy')
    
    while True:
        resp = input('Enter Response: ')
        try:
            rType = type(int(resp))
        except:
            rType = type(resp)
            
        if rType==str:
            if resp=='MainMenu':
                MainMenu()
                break
            elif resp=='Help':
                PrintInst()
                MiscFunctions()
                break
            elif resp=='Exit':
                MainMenu()
                break
            else:
                print('Invalid Response...')
                
        if int(resp)==1:
            year = InputYear()
            print('-'*50)
            print('List of all countries that participated in the olympics in the year',year,': ')
            print(Functions.Country_Array[year])
            break
        elif int(resp)==2:
            print('-'*50)
            print('List of all countries that have participated in the olympics so far: ')
            print(Functions.AllCountries_List)
            break
        elif int(resp)==3:
            print('-'*50)
            print('List of all the years in which the olympics have been held: ')
            print(Functions.Year_Array)
            break
        elif int(resp)==4:
            print('-'*50)
            print('Since there is no standardised Point system in the olympics,',
                '\nThis program uses a Weighted Point system to calculate rankings where ',
                '\nA Gold Medal is worth 3 points',
                '\nA Silver Medal is worth 2 points',
                '\nA Bronze Medal is worth 1 point')
            break
        elif int(resp)==5:
            print('-'*50)
            print('Since there is no standardised Ranking system in the olympics,',
                "\n This program ranks different countries as per the points they've gained according to the point system used",
                '\n You can read about the point system used from the "Point System" function in the Miscellaneous Tab')
            break
        else:
            print('Invalid Response...')
        
    print()
    while True:
        resp1 = input('Enter "Exit" to go back to Miscellaneous Functions Menu...')
        if resp1=='Exit':
            MiscFunctions()
            break
        elif resp1=='MainMenu':
            MainMenu()
            break
        elif resp1=='Help':
            PrintInst()
        else:
            print('Invalid Response...')
            
    
PrintInst()
MainMenu()