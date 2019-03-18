
results_dict = {}

# df = main.data_frame(dict_1,1)
x = df['Potential']
y = df['Current']
# Peaks are here [list]
peak_index = core.peak_detection_fxn(y)
# Split x,y to get baselines
x1,x2 = core.split(x)
y1,y2 = core.split(y)
y_base1 = core.linear_background(x1,y1)
y_base2 = core.linear_background(x2,y2)
# Calculations based on baseline and peak
values = core.peak_values(x,y)
Et = values[0]
Eb = values[2]
dE = core.del_potential(x,y)
half_E = min(Et,Eb) + core.half_wave_potential(x,y)
ia = core.peak_heights(x,y)[0]
ic = core.peak_heights(x,y)[1]
ratio_i = core.peak_ratio(x,y)
results_dict['Peak Current Ratio'] = ratio_i
results_dict['Ipc'] = ic
results_dict['Ipa'] = ia
results_dict['Epc'] = Eb
results_dict['Epa'] = Et
results_dict['∆E'] = dE
results_dict['Redox Potential'] = half_E
if dE>0.3:
    results_dict['Reversible'] = 'No'
else:
    results_dict['Reversible'] = 'Yes'

if half_E>0 and  'Yes' in results_dict.values():
    results_dict['Type'] = 'Catholyte'
elif 'Yes' in results_dict.values():
    results_dict['Type'] = 'Anolyte'
#return results_dict