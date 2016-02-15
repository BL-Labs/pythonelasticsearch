import csv

# NB THIS FILE HAS TWO ERRORS IN IT!
# One of the tasks is to make this work properly

# Creating a variable to hold the filename that we are going to read in patch data from
PATCH="patch_data"

def get_lookup_dictionary():
  # create an empty dictionary to hold the lookup information
  patch_dict = {}

  with open(PATCH) as p:
    # Using a DictReader so that we can get the data by name of the header.
    csv_p = csv.DictReader(p)
    for row in csv_p:
      # This uses the "sysnum" data as a key set to be the value of the title data
      patch_dict[row['sysnum']] = row['correcttitle']
  return patch_dict

if __name__ == "__main__":
  # This is some rudimentary test code
  p = get_lookup_dictionary()
  assert p['002581303'] == "Onze Gouden Eeuw. De Republiek der Vereenigde Nederlanden in haar bloeitijd ... Geïllustreerd onder toezicht van J. H. W. Unger"
  assert p['002893249'] == "Napoléon et son temps ... Ouvrage illustré ... Neuvième mille"
  print("The dictionary has been loaded into memory correctly")

