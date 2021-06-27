from input_modification import insert, process_table, read_textfile
import numpy as np
import matplotlib.pyplot as plt

class Photovoltaic_Plugin:
	# Implementing area calculation

	'''
	______________
	Required Input
	______________
	
	# Financial Input Values
	Name | Value
	--- | ---
	construction time | num

	Is generated by Discounted_Cash_Flow

	# Irradiation Used
	Name | Value
	--- | ---
	Data | str or array

	Can be either the name of a file containing hourly power ratio data or an array containing such data.
	A suitable array can be retrieved from 'Hourly Irradiation > *type of tracking* > Value'

	# CAPEX Multiplier
	Name | Value
	--- | ---
	Multiplier | num

	process_table() is used.  CAPEX multiplier describes the cost reduction for every ten-fold increase of
	power relative to the CAPEX reference power.

	# Electrolyzer
	Name | Value
	--- | ---
	Nominal Power (kW) | num
	CAPEX Reference Power (kW) | num
	Power requirement increase per year | num
	Minimum capacity | num
	Conversion efficiency (kg H2/kWh) | num
	Replacement time (h) | num

	process_table() is used.

	# Photovoltaic
	Name | Value
	--- | ---
	Nominal Power (kW) | num
	CAPEX Reference Power (kW) | num
	Power loss per year | num
	Efficiency | num

	process_table() is used.

	______________
	Output
	______________

	Technical Operating Parameters and Specifications > Plant Design Capacity (kg of H2/day) > Value
	Technical Operating Parameters and Specifications >	Operating Capacity Factor (%) > Value
	Planned Replacement > Electrolyzer Stack Replacement > Frequency (years)
	Electrolyzer > Scaling Factor > Value
	Electrolyzer > Scaling Factor > Value
	Non-Depreciable Capital Costs > Land required (acres) > Value
	Non-Depreciable Capital Costs > Solar Collection Area (m2) > Value
	'''

	def __init__(pv, self, print_info):
		process_table(self.inp, 'Irradiation Used', 'Value')
		process_table(self.inp, 'CAPEX Multiplier', 'Value')
		process_table(self.inp, 'Electrolyzer', 'Value')
		process_table(self.inp, 'Photovoltaic', 'Value')

		pv.calculate_H2_production(self)
		pv.calculate_stack_replacement(self)
		pv.calculate_scaling_factors(self)
		pv.calculate_area(self)

		insert(self, 'Technical Operating Parameters and Specifications', 'Plant Design Capacity (kg of H2/day)', 'Value', pv.h2_production/365., __name__, print_info = print_info)
		insert(self, 'Technical Operating Parameters and Specifications', 'Operating Capacity Factor (%)', 'Value', 1., __name__, print_info = print_info)
	
		insert(self, 'Planned Replacement', 'Electrolyzer Stack Replacement', 'Frequency (years)', pv.replacement_frequency, __name__, print_info = print_info)

		insert(self, 'Electrolyzer', 'Scaling Factor', 'Value', pv.electrolyzer_scaling_factor, __name__, print_info = print_info)
		insert(self, 'Photovoltaic', 'Scaling Factor', 'Value', pv.pv_scaling_factor, __name__, print_info = print_info)

		insert(self, 'Non-Depreciable Capital Costs', 'Land required (acres)', 'Value', pv.area_acres, __name__, print_info = print_info)
		insert(self, 'Non-Depreciable Capital Costs', 'Solar Collection Area (m2)', 'Value', pv.area_m2, __name__, print_info = print_info)

	def calculate_H2_production(pv, self):

		if isinstance(self.inp['Irradiation Used']['Data']['Value'], str):
			data = read_textfile(self.inp['Irradiation Used']['Data']['Value'], delimiter = '	')[:,1]
		else:
			data = self.inp['Irradiation Used']['Data']['Value']

		yearly_data = []

		for year in self.operation_years:
			data_loss_corrected = pv.calculate_photovoltaic_loss_correction(self, data, year)
			power_generation = data_loss_corrected * self.inp['Photovoltaic']['Nominal Power (kW)']['Value']

			electrolyzer_power_demand, power_increase = pv.calculate_electrolyzer_power_demand(self, year) 
			electrolyzer_power_demand *= np.ones(len(power_generation))
			electrolyzer_power_consumption = np.amin(np.c_[power_generation, electrolyzer_power_demand], axis = 1)

			threshold = self.inp['Electrolyzer']['Minimum capacity']['Value']
			electrolyzer_capacity = electrolyzer_power_consumption / electrolyzer_power_demand
			electrolyzer_capacity[electrolyzer_capacity > threshold] = 1
			electrolyzer_capacity[electrolyzer_capacity <= threshold] = 0

			h2_produced = electrolyzer_power_consumption * self.inp['Electrolyzer']['Conversion efficiency (kg H2/kWh)']['Value'] / power_increase
			h2_produced *= electrolyzer_capacity

			yearly_data.append([year, np.sum(h2_produced), np.sum(electrolyzer_capacity)])

		pv.yearly_data = np.asarray(yearly_data)
		pv.h2_production = np.concatenate([np.zeros(self.inp['Financial Input Values']['construction time']['Value']), pv.yearly_data[:,1]])

	def calculate_photovoltaic_loss_correction(pv, self, data, year):

		return data * (1. - self.inp['Photovoltaic']['Power loss per year']['Value']) ** year

	def calculate_electrolyzer_power_demand(pv, self, year):

		increase = (1. + self.inp['Electrolyzer']['Power requirement increase per year']['Value']) ** year
		demand = increase * self.inp['Electrolyzer']['Nominal Power (kW)']['Value']

		return demand, increase

	def calculate_stack_replacement(pv, self):

		cumulative_running_time = np.cumsum(pv.yearly_data[:,2])
		stack_usage = cumulative_running_time / self.inp['Electrolyzer']['Replacement time (h)']['Value']

		number_of_replacements = np.floor_divide(stack_usage[-1], 1)
		pv.replacement_frequency = len(stack_usage) / (number_of_replacements + 1.)

	def calculate_scaling_factors(pv, self):

		pv.pv_scaling_factor = pv.scaling_factor(self, self.inp['Photovoltaic']['Nominal Power (kW)']['Value'], self.inp['Photovoltaic']['CAPEX Reference Power (kW)']['Value'])
		pv.electrolyzer_scaling_factor = pv.scaling_factor(self, self.inp['Electrolyzer']['Nominal Power (kW)']['Value'], self.inp['Electrolyzer']['CAPEX Reference Power (kW)']['Value'])
		
	def scaling_factor(pv, self, power, reference):
		
		number_of_tenfold_increases = np.log10(power/reference)

		return self.inp['CAPEX Multiplier']['Multiplier']['Value'] ** number_of_tenfold_increases

	def calculate_area(pv, self):
		'''Area calculation assuming 1000 W/m2 peak power'''

		peak_kW_per_m2 = self.inp['Photovoltaic']['Efficiency']['Value'] * 1.
		pv.area_m2 = self.inp['Photovoltaic']['Nominal Power (kW)']['Value'] / peak_kW_per_m2
		pv.area_acres = pv.area_m2 * 0.000247105
