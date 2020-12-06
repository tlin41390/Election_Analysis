
counties = ["Arapahoe","Denver","Jefferson"]

counties_dict ={"Arapahoe":422829, "Denver": 463353,"Jefferson": 432438}

for counties,values in counties_dict.items():
    print(counties +" county has "+ str(values)+ " registered voters")