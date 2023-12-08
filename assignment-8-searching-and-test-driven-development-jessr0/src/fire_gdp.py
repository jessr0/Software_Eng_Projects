import csv


class HashTable:
    """Initializes custom hash table for datasets"""
    def __init__(self):
        self.size = 10
        self.table = [None] * self.size

    def get_hash(self, key):
        key_str = str(key)
        hash_value = 0
        prime_multiplier = 31
        for c in key:
            hash_value = (hash_value * prime_multiplier + ord(c)) % 10**9 + 7
        return hash_value % self.size

    def insert(self, key, value):
        hash_key = self.get_hash(key)
        if self.table[hash_key] is None:
            self.table[hash_key] = []
        self.table[hash_key].append((key, value))

    def retrieve(self, key):
        hash_key = self.get_hash(key)
        if self.table[hash_key] is not None:
            for pair in self.table[hash_key]:
                if pair[0] == key:
                    return pair[1]
        return None


def remove_commas(string):
    """Removes commas from numerical values in datasets"""
    return string.replace(",", "")


def get_data(file_name, query_value=None, query_column=None):
    """Queries CSV by column header and value and returns as hash tables"""
    data = []
    with open(file_name) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        try:
            headers = next(csvreader)
        except StopIteration:
            return data
        if query_column not in headers:
            raise KeyError(f"Column '{query_column}' not found.")
        for row in csvreader:
            row_hash_table = HashTable()

            for header, cell in zip(headers, row):
                row_hash_table.insert(header, cell)
#            print("Row Hash Table:", row_hash_table.table)

            if (query_value is None or query_column is None or
               row_hash_table.retrieve(query_column) == query_value):
                data.append(row_hash_table)
    return data


def get_fire_gdp_year_data(fire_file_name,
                           gdp_file_name,
                           target_country,
                           fire_year_col_name,
                           fire_savanna_col_name,
                           fire_forest_col_name):
    """Returns array of info from desired country from hash tables"""

    fire_data = get_data(fire_file_name,
                         query_value=target_country,
                         query_column='Area')
    gdp_data = get_data(gdp_file_name,
                        query_value=target_country,
                        query_column='\ufeffCountry')

    fires = []
    gdps = []
    years = []

    for fire_row in fire_data:
        year = fire_row.retrieve(fire_year_col_name)
        savanna = fire_row.retrieve(fire_savanna_col_name)
        forest = fire_row.retrieve(fire_forest_col_name)

        if year and savanna and forest:
            gdp_value = gdp_data[0].retrieve(year)
            if gdp_value and gdp_value != '...':
                fires.append(float(savanna) + float(forest))
                years.append(int(year))
                gdps.append(float(remove_commas(gdp_value)))

    return [fires, gdps, years]
