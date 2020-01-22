try:

    import tkinter as tk
    from tkinter import ttk
    import pandas as pd
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
except Exception as e:
    print("Some modules  are missing {}".format(e))

# Class to display all GUI widgets


class GUI(object):

    def __init__(self):
        self.app = tk.Tk()
        # Setting the Output Page Dimensions
        self.app.geometry("850x800")
        self.dataset = Dataset()
        self.graph = Graph()

    def create_widget(self):

        chk_value = tk.BooleanVar()
        chk_value.set(True)
        season = tk.Checkbutton(self.app, text='Summer', var=chk_value)
        season.grid(column=0, row=0)

        chk_value1 = tk.BooleanVar()
        chk_value1.set(False)
        season1 = tk.Checkbutton(self.app, text='Winter', var=chk_value1)
        season1.grid(column=2, row=0)

        def okay():
            selected_season = chk_value.get()
            selected_season1 = chk_value1.get()
            if selected_season:
                season_value = "Summer"
            elif selected_season1:
                season_value = "Winter"
            else:
                season_value = "Both"

            print(season_value)

            # Combo Box for Start Season selection
            year = self.dataset.get_year(season_value)
            label_top = tk.Label(self.app, text="Select Start Year")
            label_top.grid(column=0, row=1, sticky="NSEW", padx=10, pady=10)
            year.insert(0, "ALL")
            start_year_combo = ttk.Combobox(self.app, values=year, width=20, height=35)
            start_year_combo.grid(row=2, column=0, sticky="NSEW", padx=10, pady=10)
            start_year_combo.current(0)

            # Combo Box for End Year selection
            year = self.dataset.get_year(season_value)
            label_top = tk.Label(self.app, text="Select End Year")
            label_top.grid(column=1, row=1, sticky="NSEW", padx=10, pady=10)
            year.insert(0, "ALL")
            end_year_combo = ttk.Combobox(self.app, values=year, width=20, height=35)
            end_year_combo.grid(row=2, column=1, sticky="NSEW", padx=10, pady=10)
            end_year_combo.current(0)

            # Combo Box for City selection
            label_top = tk.Label(self.app, text="Select a City")
            label_top.grid(row=1, column=2, sticky="NSEW", padx=10)
            city = self.dataset.get_city(season_value)
            city.insert(0, "ALL")
            city_combo = ttk.Combobox(self.app, values=city, width=20, height=35)
            city_combo.grid(column=2, row=2, sticky="NSEW", padx=10, pady=10)
            city_combo.current(0)

            # Combo Box for Sport selection
            label_top = tk.Label(self.app, text="Choose a Sport")
            label_top.grid(row=1, column=3, sticky="NSEW", padx=10, pady=10)
            sport = self.dataset.get_sport(season_value)
            sport.insert(0, "ALL")
            sport_combo = ttk.Combobox(self.app, values=sport, width=20, height=35)
            sport_combo.grid(column=3, row=2, sticky="NSEW", padx=10, pady=10)
            sport_combo.current(0)

            # Combo Box for Discipline selection
            label_top = tk.Label(self.app, text="Choose a Discipline")
            label_top.grid(row=1, column=4, sticky="NSEW", padx=10, pady=10)
            discipline = self.dataset.get_discipline(season_value)
            discipline.insert(0, "ALL")
            discipline_combo = ttk.Combobox(self.app, values=discipline, width=20, height=35)
            discipline_combo.grid(column=4, row=2, sticky="NSEW", padx=10, pady=10)
            discipline_combo.current(0)

            # Combo Box for Athlete selection
            label_top = tk.Label(self.app, text="Choose a Athlete")
            label_top.grid(row=3, column=0, sticky="NSEW", padx=10, pady=10)
            athlete = self.dataset.get_athlete(season_value)
            athlete.insert(0, "ALL")
            athlete_combo = ttk.Combobox(self.app, values=athlete, width=20, height=35)
            athlete_combo.grid(column=0, row=4, sticky="NSEW", padx=10, pady=10)
            athlete_combo.current(0)

            # Combo Box for specific Country selection
            label_top = tk.Label(self.app, text="Choose a Country")
            label_top.grid(row=3, column=1, sticky="NSEW", padx=10, pady=10)
            country = self.dataset.get_country(season_value)
            country.insert(0, "ALL")
            country_combo = ttk.Combobox(self.app, values=country, width=20, height=35)
            country_combo.grid(column=1, row=4, sticky="NSEW", padx=10, pady=10)
            country_combo.current(0)

            # Combo Box for Gender selection
            label_top = tk.Label(self.app, text="Choose a Gender", font=("Arial Bold", 10))
            label_top.grid(row=3, column=2, sticky="NSEW", padx=10, pady=10)
            gender = self.dataset.get_gender(season_value)
            gender.insert(0, "BOTH")
            gender_combo = ttk.Combobox(self.app, values=gender, width=20, height=35)
            gender_combo.grid(column=2, row=4, sticky="NSEW", padx=10, pady=10)
            gender_combo.current(0)

            # Combo Box for Event selection
            label_top = tk.Label(self.app, text="Choose a Event")
            label_top.grid(row=3, column=3, sticky="NSEW", padx=10, pady=10)
            event = self.dataset.get_event(season_value)
            event.insert(0, "ALL")
            event_combo = ttk.Combobox(self.app, values=event, width=20, height=35)
            event_combo.grid(column=3, row=4, sticky="NSEW", padx=10, pady=10)
            event_combo.current(0)

            # Combo Box for Medal selection
            label_top = tk.Label(self.app, text="Choose a Medal")
            label_top.grid(row=3, column=4, sticky="NSEW", padx=10, pady=10)
            medal = self.dataset.get_medal(season_value)
            medal.insert(0, "ALL")
            medal_combo = ttk.Combobox(self.app, values=medal, width=20, height=35)
            medal_combo.grid(column=4, row=4, sticky="NSEW", padx=10, pady=10)
            medal_combo.current(0)


            def ok():
                # Accepting Medal Value
                medal_value = medal_combo.get()
                # Accepting Event Value
                event_value = event_combo.get()
                # Accepting Gender Value
                gender_value = gender_combo.get()
                # Accepting City Value
                city_value = city_combo.get()
                # Accepting End Year Value
                end_year_value = end_year_combo.get()
                # Accepting End Year Value
                start_year_value = start_year_combo.get()
                # Accepting Sport Value
                sport_value = sport_combo.get()
                # Accepting Discipline Value
                discipline_value = discipline_combo.get()
                # Accepting Athlete Value
                athlete_value = athlete_combo.get()
                # Accepting Country Value
                country_value = country_combo.get()
                if start_year_value != "ALL" and end_year_value != "ALL" and country_value != "ALL" \
                        and city_value == "ALL" and sport_value == "ALL":
                    if season_value == "Summer":
                        selected_df = self.dataset.df_summer
                        self.graph.create_graph2(self.app, selected_df, country_value, start_year_value, end_year_value)
                    elif season_value == "Winter":
                        selected_df = self.dataset.df_winter
                        self.graph.create_graph2(self.app, selected_df, country_value, start_year_value, end_year_value)
                    else:
                        selected_df = self.dataset.both_result
                        self.graph.create_graph2(self.app, selected_df, country_value, start_year_value, end_year_value)
                else:
                    if season_value == "Summer":
                        selected_df = self.dataset.df_summer
                        self.graph.create_graph(self.app, selected_df, medal_value, event_value, gender_value
                                                , city_value, start_year_value, end_year_value, sport_value,
                                                discipline_value, athlete_value,
                                                country_value)
                    elif season_value == "Winter":
                        selected_df = self.dataset.df_winter
                        self.graph.create_graph(self.app, selected_df, medal_value, event_value, gender_value
                                                , city_value, start_year_value, end_year_value, sport_value,
                                                discipline_value, athlete_value,
                                                country_value)
                    else:
                        selected_df = self.dataset.both_result
                        self.graph.create_graph(self.app, selected_df, medal_value, event_value, gender_value
                                                , city_value, start_year_value, end_year_value, sport_value,
                                                discipline_value, athlete_value,
                                                country_value)

            button = tk.Button(self.app, text="LETS GO", command=ok,  bg="purple", fg="black")
            button.grid(column=2, row=5, sticky="NSEW", padx=10, pady=10)

        # --------------------------------GRAPH---------------------------------------------
        # self.graph.create_graph(self.app, self.dataset.df_summer)
        # options = ['Men']

        button = tk.Button(self.app, text="SELECT!", command=okay, bg="blue", fg="black")
        button.grid(column=4, row=0, sticky="NSEW", padx=10, pady=10)
        self.app.mainloop()


class Dataset(object):

    def __init__(self):
        self.df_summer = pd.read_csv("summer.csv")
        self.df_winter = pd.read_csv("winter.csv")
        self.both = [self.df_summer,self.df_winter]
        self.both_result = pd.concat(self.both)

    def get_year(self, season):
        if season == "Summer":
            year = self.df_summer['Year'].unique().tolist()
        elif season == "Winter":
            year = self.df_winter['Year'].unique().tolist()
        else:
            year = self.both_result['Year'].unique().tolist()
        return year

    def get_city(self, season):
        if season == "Summer":
            city = self.df_summer['City'].unique().tolist()
        elif season == "Winter":
            city = self.df_winter['City'].unique().tolist()
        else:
            City = self.both_result['City'].unique().tolist()
        return city

    def get_sport(self, season):
        if season == "Summer":
            sport = self.df_summer['Sport'].unique().tolist()
        elif season == "Winter":
            sport = self.df_winter['Sport'].unique().tolist()
        else:
            sport= self.both_result['sport'].unique().tolist()
        return sport

    def get_discipline(self, season):
        if season == "Summer":
            discipline = self.df_summer['Discipline'].unique().tolist()
        elif season == "Winter":
            discipline = self.df_winter['Discipline'].unique().tolist()
        else:
            discipline= self.both_result['Discipline'].unique().tolist()
        return discipline

    def get_athlete(self, season):
        if season == "Summer":
            athlete = self.df_summer['Athlete'].unique().tolist()
        elif season == "Winter":
            athlete = self.df_winter['Athlete'].unique().tolist()
        else:
            athlete = self.both_result['Athlete'].unique().tolist()
        return athlete

    def get_country(self, season):
        if season == "Summer":
            country = self.df_summer['Country'].unique().tolist()
        elif season == "Winter":
            country = self.df_winter['Country'].unique().tolist()
        else:
            country = self.both_result['Country'].unique().tolist()
        return country

    def get_gender(self, season):
        if season == "Summer":
            gender = self.df_summer['Gender'].unique().tolist()
        elif season == "Winter":
            gender = self.df_winter['Gender'].unique().tolist()
        else:
            gender = self.both_result['Athlete'].unique().tolist()
        return gender

    def get_event(self, season):
        if season == "Summer":
            event = self.df_summer['Event'].unique().tolist()
        elif season == "Winter":
            event = self.df_winter['Event'].unique().tolist()
        else:
            event = self.both_result['Event'].unique().tolist()

        return event

    def get_medal(self, season):
        if season == "Summer":
            medal = self.df_summer['Medal'].unique().tolist()
        elif season == "Winter":
            medal = self.df_winter['Medal'].unique().tolist()
        else:
            medal = self.both_result['Medal'].unique().tolist()

        return medal


class Graph(object):

    def __init__(self):
        pass

    def create_graph2(self, app, df, country_value, start_year_value, end_year_value):
        figure1 = plt.Figure(figsize=(6, 8), dpi=60)
        ax1 = figure1.add_subplot(111)
        bar2 = FigureCanvasTkAgg(figure1, app)
        bar2.get_tk_widget().grid(column=1, row=7, columnspan=3, sticky="NSEW", padx=10, pady=10)
        option_country = [country_value]
        summer = df.loc[df['Country'].isin(option_country)]
        options2 = [start_year_value]
        if options2 != ['ALL']:
            options2 = int(start_year_value)
            summer2 = summer.loc[summer['Year'] > options2]
        else:
            summer2 = summer
        options3 = [end_year_value]
        if options3 != ['ALL']:
            options3 = int(end_year_value)
            summer4 = summer2.loc[summer2['Year'] < options3]
        else:
            summer4 = summer2
        summer20 = summer4.groupby(['Year', 'Medal'])['Country'].count()
        summer20.plot(kind='bar', legend=True, ax=ax1, color='r')

    def create_graph(self, app, df, medal_value, event_value, gender_value
                    , city_value, start_year_value, end_year_value, sport_value, discipline_value, athlete_value,
                     country_value):
        figure1 = plt.Figure(figsize=(4, 5), dpi=80)
        ax1 = figure1.add_subplot(111)
        bar1 = FigureCanvasTkAgg(figure1, app)
        bar1.get_tk_widget().grid(column=1, row=7, columnspan=3, sticky="NSEW", padx=10, pady=10)
        print('Initial \n', df.head())

        def gender_check(summer_original):
            options = [gender_value]
            if options != ['BOTH']:
                summer = summer_original.loc[summer_original['Gender'].isin(options)]
            else:
                summer = summer_original.copy(deep=True)
                print('Testing \n', summer.head())
            return summer

        summer1 = gender_check(df)
        print('1st \n', summer1.head())
        options1 = [city_value]
        if options1 != ['ALL']:
            summer2 = summer1.loc[summer1['City'].isin(options1)]
        else:
            summer2 = summer1
        print('2 \n', summer2.head())
        options2 = [start_year_value]
        if options2 != ['ALL']:
            options2 = int(start_year_value)
            summer3 = summer2.loc[summer1['Year'] > options2]
        else:
            summer3 = summer2
        options3 = [end_year_value]
        if options3 != ['ALL']:
            options3 = int(end_year_value)
            summer4 = summer3.loc[summer1['Year'] < options3]
        else:
            summer4 = summer3
        options4 = [sport_value]
        if options4 != ['ALL']:
            summer5 = summer4.loc[summer1['Sport'].isin(options4)]
        else:
            summer5 = summer4

        options5 = [discipline_value]
        if options5 != ['ALL']:
            summer6 = summer5.loc[summer1['Discipline'].isin(options5)]
        else:
            summer6 = summer5

        options6 = [athlete_value]
        if options6 != ['ALL']:
            summer7 = summer6.loc[summer1['Athlete'].isin(options6)]
        else:
            summer7 = summer6

        options7 = [country_value]
        if options7 != ['ALL']:
            summer8 = summer7.loc[summer1['Country'].isin(options7)]
        else:
            summer8 = summer7

        options8 = [event_value]
        if options8 != ['ALL']:
            summer9 = summer8.loc[summer1['Country'].isin(options8)]
        else:
            summer9 = summer8

        options9 = [medal_value]
        if options9 != ['ALL']:
            summer10 = summer9.loc[summer1['Country'].isin(options9)]
        else:
            summer10 = summer9

        no_summer = summer10.groupby('Medal')['Athlete'].count()
        no_summer.plot(kind='bar', legend=True, ax=ax1)
        if gender_value == "Men":
            ax1.set_title('Men Athletes Vs Medals')
        elif gender_value == "Women":
            ax1.set_title('Women Athletes Vs Medals')
        else:
            ax1.set_title('Men/Women Athletes Vs Medals')


if __name__ == "__main__":
    gui = GUI()
    gui.create_widget()

