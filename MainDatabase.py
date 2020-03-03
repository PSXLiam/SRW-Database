import pandas as pd

# read in databases
dfPilots = pd.read_csv('SRWOG1_PilotDatabase.csv', index_col=0)
dfMechs = pd.read_csv('SRWOG1_MechDatabase.csv', index_col=0)

# Copy of Sheets is made to test code
dfPilotsB = dfPilots.copy()
dfPilotsB.to_csv('SRWOG1_PilotDatabaseEDIT.csv')
dfMechsB = dfMechs.copy()
dfMechsB.to_csv('SRWOG1_MechDatabaseEDIT.csv')
# print(dfPilotsB)
# print(dfMechsB)


def add_pilot(df):  # Add Pilot
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

    new_pilot = pd.DataFrame(
        {'Name': name, 'Level': level, 'Designated Unit': '', 'Accel': accel, 'Bless': bless, 'Cheer': cheer,
         'Dodge Gain': dgain, 'Attack(Hit) Gain': attackhit, 'Get Hit Gain': gethit, 'Attack(Miss) Gain': attackmiss,
         'Destroy Target Gain': destroytarget, 'Ally Destroyed Gain': allydestroy, 'Available': 'YES'}, index=[0])

    # print(new_pilot)
    df = df.append(new_pilot, ignore_index=True)
    # print(df)
    df.to_csv('SRWOG1_PilotDatabaseEDIT.csv')


def add_mech(df):  # Add mech
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

    new_mech = pd.DataFrame(
        {'Name': name, 'Designated Pilot': '', 'HP': hp, 'Energy': energy, 'Mobility': mobility, 'Armor': armor,
         'Move': move, 'Size': size, 'Cost': cost, 'W Space': wspace, 'Part Slots': parts, 'Air': air, 'Gnd': gnd,
         'Wtr': wtr, 'Spc': spc, 'Available': 'YES'}, index=[0])

    # print(new_mech)
    df = df.append(new_mech, ignore_index=True)
    # print(df)
    df.to_csv('SRWOG1_MechDatabaseEDIT.csv')


def remove_pilot(df):  # Remove pilot
    name = input("Enter Name of pilot you wish to remove: ")
    name_index = df.loc[df['Name'].str.contains(name, regex=True)]
    # print(name_index.index)
    df = df.drop(name_index.index)
    # print(df)
    df.to_csv('SRWOG1_PilotDatabaseEDIT.csv')


def remove_mech(df):  # Remove mech
    name = input("Enter Name of mech you wish to remove: ")
    name_index = df.loc[df['Name'].str.contains(name, regex=True)]
    # print(name_index.index)
    df = df.drop(name_index.index)
    # print(df)
    df.to_csv('SRWOG1_MechDatabaseEDIT.csv')


def save_update():
    print("Updating Database to Main....")
    df = pd.read_csv('SRWOG1_PilotDatabaseEDIT.csv', index_col=0)
    df.to_csv('SRWOG1_PilotDatabase.csv')
    df = pd.read_csv('SRWOG1_MechDatabaseEDIT.csv', index_col=0)
    df.to_csv('SRWOG1_MechDatabase.csv')


# add_pilot(dfPilotsB)
# add_mech(dfMechsB)
remove_pilot(dfPilotsB)
# remove_mech(dfMechsB)
save_update()

