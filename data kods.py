
import pandas as pd


file_path = 'data.csv'

data =pd.read_csv(file_path)

auxiliary_data = data[data['industry'] == 'Auxiliary']

max_value = auxiliary_data['value'].max()

print(f"Maksimālā vērtība kolonnā 'value' biznesa nozarei 'Auxiliary' ir: {max_value}")

file_path = 'data.csv'

file_path = 'data.csv'


data = pd.read_csv(file_path)

level_2_data = data[data['level'] == 2]

values_list = level_2_data['value'].tolist()

total_values_count = len(values_list)

print(f"Kopējais nolasīto vērtību skaits: {total_values_count}")

file_path = 'data.csv'


data = pd.read_csv(file_path)

mining_data = data[data['industry'] == 'Mining']

value_list = mining_data['value'].tolist()

top_3_values = sorted(value_list, reverse=True)[:3]

min_of_top_3 = min(top_3_values)

print(f"TOP 3 minimālā vērtība: {min_of_top_3}")

file_path = 'data.csv'

data = pd.read_csv(file_path)

agriculture_data = data[data['industry'] == 'Agriculture']

value_list = agriculture_data['value'].tolist()

every_other_value = value_list[::2]

sum_of_every_other = sum(every_other_value)

print(f"Katru otro elementu summa: {sum_of_every_other}")
