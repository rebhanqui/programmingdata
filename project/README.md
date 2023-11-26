Average calls numbers based on data from work January to October 2023

January:
Incoming Daily Average: 8496/31 = 274
Missed Daily Average: 956/31 = 30
Outbound Daily Average: 1266/31 = 40
Average Staff Rostered per day = 2

February:
Incoming Daily Average: 6388/28 = 228
Missed Daily Average: 1027/28 = 36
Outbound Daily Average: 1189/28 = 42
Average Staff Rostered per day = 2

March:
Incoming Daily Average: 5778/31 = 186
Missed Daily Average: 1106/31 = 35
Outbound Daily Average: 1105/31 = 35
Average Staff Rostered per day = 2

April:
Incoming Daily Average: 5950/30 = 198
Missed Daily Average: 908/30 = 30
Outbound Daily Average: 965/30 = 32
Average Staff Rostered per day = 2

May:
Incoming Daily Average: 5446/31 = 175
Missed Daily Average: 827/31 = 26
Outbound Daily Average: 916/31 = 29
Average Staff Rostered per day = 2

June:
Incoming Daily Average: 5263/30 = 175
Missed Daily Average: 570/30 = 19
Outbound Daily Average: 1022/30 = 34
Average Staff Rostered per day = 2

July:
Incoming Daily Average: 5537/31 = 178
Missed Daily Average: 626/31 = 20
Outbound Daily Average: 905/31 = 29
Average Staff Rostered per day = 3

August:
Incoming Daily Average: 5661/31 = 182
Missed Daily Average: 492/31 = 15
Outbound Daily Average: 1026/31 = 33
Average Staff Rostered per day = 2

September:
Incoming Daily Average: 7095/30 = 236
Missed Daily Average: 959/30 = 31
Outbound Daily Average: 917/30 = 30
Average Staff Rostered per day = 2

October:
Incoming Daily Average: 6976/31 = 225
Missed Daily Average: 698/31 = 22
Outbound Daily Average: 1194/31 = 38
Average Staff Rostered per day = 2

#daily average calls of each month of known data to synthesise
#to do this i added up the daily staff rostered each month and divided by the days in the month (calculated in terminal with //) and the same with the monthly call totals // by number of days that month
january_average_calls = 274
january_average_missed = 30
january_average_outbound = 40 
january_average_staff = 2

february_average_calls = 228
february_average_missed = 36
february_average_outbound = 42
february_average_staff = 2

march_average_calls = 186
march_average_missed = 35
march_average_outbound = 35
march_average_staff = 2

april_average_calls = 198
april_average_missed = 30
april_average_outbound = 32
april_average_staff = 2

may_average_calls = 175
may_average_missed = 26
may_average_outbound = 29
may_average_staff = 2

june_average_calls = 175
june_average_missed = 19
june_average_outbound = 34
june_average_staff = 2

july_average_calls = 178
july_average_missed = 20
july_average_outbound = 29
july_average_staff = 3

august_average_calls = 182
august_average_missed = 15
august_average_outbound = 33
august_average_staff = 2

september_average_calls = 236
september_average_missed = 31
september_average_outbound = 30
september_average_staff = 2

october_average_calls = 225
october_average_missed = 22
october_average_outbound = 38
october_average_staff = 2

#synthetic averages created using numpy random module and uniform distribution
#rounding off the smallest average number for each variable to generate a random array of seven numbers for each day of the week
synthetic_january_average_calls = np.random.uniform(170, 300, 7)
synthetic_january_average_missed = np.random.uniform(10, 40, 7)
synthetic_january_average_outbound = np.random.uniform(25, 45, 7)
#putting the staff numbers between 2 and 5 to show if having more on is better later on
synthetic_january_average_staff = np.random.uniform(2, 5, 7)

synthetic_february_average_calls = np.random.uniform(170, 300, 7)
synthetic_february_average_missed = np.random.uniform(10, 40, 7)
synthetic_february_average_outbound = np.random.uniform(25, 45, 7)
synthetic_february_average_staff = np.random.uniform(2, 5, 7)

synthetic_march_average_calls = np.random.uniform(170, 300, 7)
synthetic_march_average_missed = np.random.uniform(10, 40, 7)
synthetic_march_average_outbound = np.random.uniform(25, 45, 7)
synthetic_march_average_staff = np.random.uniform(2, 5, 7)

synthetic_april_average_calls = np.random.uniform(170, 300, 7)
synthetic_april_average_missed = np.random.uniform(10, 40, 7)
synthetic_april_average_outbound = np.random.uniform(25, 45, 7)
synthetic_april_average_staff = np.random.uniform(2, 5, 7)

synthetic_may_average_calls = np.random.uniform(170, 300, 7)
synthetic_may_average_missed = np.random.uniform(10, 40, 7)
synthetic_may_average_outbound = np.random.uniform(25, 45, 7)
synthetic_may_average_staff = np.random.uniform(2, 5, 7)

synthetic_june_average_calls = np.random.uniform(170, 300, 7)
synthetic_june_average_missed = np.random.uniform(10, 40, 7)
synthetic_june_average_outbound = np.random.uniform(25, 45, 7)
synthetic_june_average_staff = np.random.uniform(2, 5, 7)

synthetic_july_average_calls = np.random.uniform(170, 300, 7)
synthetic_july_average_missed = np.random.uniform(10, 40, 7)
synthetic_july_average_outbound = np.random.uniform(25, 45, 7)
synthetic_july_average_staff = np.random.uniform(2, 5, 7)

synthetic_august_average_calls = np.random.uniform(170, 300, 7)
synthetic_august_average_missed = np.random.uniform(10, 40, 7)
synthetic_august_average_outbound = np.random.uniform(25, 45, 7)
synthetic_august_average_staff = np.random.uniform(2, 5, 7)

synthetic_september_average_calls = np.random.uniform(170, 300, 7)
synthetic_september_average_missed = np.random.uniform(10, 40, 7)
synthetic_september_average_outbound = np.random.uniform(25, 45, 7)
synthetic_september_average_staff = np.random.uniform(2, 5, 7)

synthetic_october_average_calls = np.random.uniform(170, 300, 7)
synthetic_october_average_missed = np.random.uniform(10, 40, 7)
synthetic_october_average_outbound = np.random.uniform(25, 45, 7)
synthetic_october_average_staff = np.random.uniform(2, 5, 7)

#https://matplotlib.org/stable/gallery/lines_bars_and_markers/categorical_variables.html