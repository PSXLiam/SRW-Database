import pandas as pd


# Add Pilot to Database
def add_pilot(df):
    # Collect New Data from User Input
    name = input("Enter Pilot Name: ")
    level = input("Pilot Level: ")
    accel = input("Does this pilot have Accel? ")
    bless = input("Does this pilot have Bless? ")
    cheer = input("Does this pilot have Cheer? ")
    dgain = input("Dodge Morale Gain: ")
    attackhit = input("Attack(Hit) Morale Gain: ")
    gethit = input("Get Hit Morale Gain: ")
    attackmiss = input("Attack(Miss) Morale Gain: ")
    destroytarget = input("Destroy Target Morale Gain: ")
    allydestroy = input("Ally Destroyed Morale Gain: ")

    # Turn New Data into a Dataset
    new_pilot = pd.DataFrame(
        {'Name': name, 'Level': level, 'Designated Unit': '', 'Accel': accel, 'Bless': bless, 'Cheer': cheer,
         'Dodge Gain': dgain, 'Attack(Hit) Gain': attackhit, 'Get Hit Gain': gethit, 'Attack(Miss) Gain': attackmiss,
         'Destroy Target Gain': destroytarget, 'Ally Destroyed Gain': allydestroy, 'Available': 'YES'}, index=[0])

    # Append Dataset to Database
    df = df.append(new_pilot, ignore_index=True)
    df.to_csv('SRWOG1_PilotDatabaseEDIT.csv')


# Add Mech to Database
def add_mech(df):
    # Collect New Data from User Input
    name = input("Enter Mech Name: ")
    hp = input("HP: ")
    energy = input("Energy: ")
    mobility = input("Mobility: ")
    armor = input("Armor: ")
    move = input("Move: ")
    size = input("Size: ")
    cost = input("Repair Cost: ")
    wspace = input("Weapon Space: ")
    parts = input("Total Part Slots: ")
    air = input("Skill in Air: ")
    gnd = input("Skill on Ground: ")
    wtr = input("Skill in Water: ")
    spc = input("Skill in Space: ")

    # Turn New Data into a Dataset
    new_mech = pd.DataFrame(
        {'Name': name, 'Designated Pilot': '', 'HP': hp, 'Energy': energy, 'Mobility': mobility, 'Armor': armor,
         'Move': move, 'Size': size, 'Cost': cost, 'W Space': wspace, 'Part Slots': parts, 'Air': air, 'Gnd': gnd,
         'Wtr': wtr, 'Spc': spc, 'Available': 'YES'}, index=[0])

    # Append Dataset to Database
    df = df.append(new_mech, ignore_index=True)
    df.to_csv('SRWOG1_MechDatabaseEDIT.csv')


# Remove Pilot from Database
def remove_pilot(df):
    name = input("Enter Name of pilot you wish to remove: ")
    name_index = df.loc[df['Name'].str.contains(name, regex=True)]
    df = df.drop(name_index.index)
    df.to_csv('SRWOG1_PilotDatabaseEDIT.csv')


# Remove Mech from Database
def remove_mech(df):
    name = input("Enter Name of mech you wish to remove: ")
    name_index = df.loc[df['Name'].str.contains(name, regex=True)]
    df = df.drop(name_index.index)
    df.to_csv('SRWOG1_MechDatabaseEDIT.csv')


# Save updates to Database
def save_update():
    print("Updating Database to Main....")
    df = pd.read_csv('SRWOG1_PilotDatabaseEDIT.csv', index_col=0)
    df.to_csv('SRWOG1_PilotDatabase.csv')
    df = pd.read_csv('SRWOG1_MechDatabaseEDIT.csv', index_col=0)
    df.to_csv('SRWOG1_MechDatabase.csv')


# Assign Pilot to Mech
def pilot_assign(df_p, df_m):
    pilot = input("Enter Name of pilot you wish to assign: ")
    pilot_index = df_p.loc[df_p['Name'].str.contains(pilot, regex=True)]
    mech = input("Enter Name of the mech you wish to assign the pilot to: ")
    mech_index = df_m.loc[df_m['Name'].str.contains(mech, regex=True)]


# Check Complete Unit Stats #ERROR
def unit_check(df_p, df_m):
    name = input("Enter the Name of pilot you wish to see complete status of: ")
    print(df_p.loc[[df_p['Name'].str.contains(name, regex=True)]])
    print(df_m.loc[[df_m['Designated Pilot'].str.contains(name, regex=True)]])


# Create Menu
def menu():
    print("Welcome, \n A.Add to Database\n R.Remove from Database\n C.Check Unit Status\n Q.Quit")
    choice = input("Enter your Selection: ")

    if choice == "A":
        choice = input("(P)ilot or (M)ech?")
        if choice == "P":
            add_pilot(dfPilotsB)
        if choice == "M":
            add_mech(dfMechsB)
    if choice == "R":
        choice = input("(P)ilot or (M)ech?")
        if choice == "P":
            remove_pilot(dfPilotsB)
        if choice == "M":
            remove_mech(dfMechsB)
    if choice == "C":
        unit_check(dfPilotsB, dfMechsB)
        return
    if choice == "Q":
        # save_update()
        return
    else: print("Invalid User Input\n")
    menu()


# Read in Databases
dfPilots = pd.read_csv('SRWOG1_PilotDatabase.csv', index_col=0)
dfMechs = pd.read_csv('SRWOG1_MechDatabase.csv', index_col=0)

# Copy of Sheets (made to test code)
dfPilotsB = dfPilots.copy()
dfPilotsB.to_csv('SRWOG1_PilotDatabaseEDIT.csv')
dfMechsB = dfMechs.copy()
dfMechsB.to_csv('SRWOG1_MechDatabaseEDIT.csv')

# Load up Menu
menu()


