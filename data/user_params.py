 
# This file is auto-generated from a Python script that parses a PhysiCell configuration (.xml) file.
#
# Edit at your own risk.
#
import os
from ipywidgets import Label,Text,Checkbox,Button,HBox,VBox,FloatText,IntText,BoundedIntText,BoundedFloatText,Layout,Box
    
class UserTab(object):

    def __init__(self):
        
        micron_units = Label('micron')   # use "option m" (Mac, for micro symbol)

        constWidth = '180px'
        tab_height = '500px'
        stepsize = 10

        #style = {'description_width': '250px'}
        style = {'description_width': '25%'}
        layout = {'width': '400px'}

        name_button_layout={'width':'25%'}
        widget_layout = {'width': '15%'}
        widget2_layout = {'width': '10%'}
        units_button_layout ={'width':'15%'}
        desc_button_layout={'width':'45%'}
        divider_button_layout={'width':'40%'}

        param_name1 = Button(description='random_seed', disabled=True, layout=name_button_layout)
        param_name1.style.button_color = 'lightgreen'

        self.random_seed = IntText(
          value=0,
          step=1,
          style=style, layout=widget_layout)

        div_row1 = Button(description='---Initialization settings---', disabled=True, layout=divider_button_layout)

        param_name2 = Button(description='number_of_A', disabled=True, layout=name_button_layout)
        param_name2.style.button_color = 'tan'

        self.number_of_A = IntText(
          value=25,
          step=1,
          style=style, layout=widget_layout)

        param_name3 = Button(description='number_of_B', disabled=True, layout=name_button_layout)
        param_name3.style.button_color = 'lightgreen'

        self.number_of_B = IntText(
          value=25,
          step=1,
          style=style, layout=widget_layout)

        param_name4 = Button(description='number_of_C', disabled=True, layout=name_button_layout)
        param_name4.style.button_color = 'tan'

        self.number_of_C = IntText(
          value=25,
          step=1,
          style=style, layout=widget_layout)

        param_name5 = Button(description='max_distance_from_origin', disabled=True, layout=name_button_layout)
        param_name5.style.button_color = 'lightgreen'

        self.max_distance_from_origin = FloatText(
          value=150,
          step=10,
          style=style, layout=widget_layout)

        div_row2 = Button(description='---Coloring settings---', disabled=True, layout=divider_button_layout)

        param_name6 = Button(description='A_color', disabled=True, layout=name_button_layout)
        param_name6.style.button_color = 'tan'

        self.A_color = Text(
          value='magenta',
          style=style, layout=widget_layout)

        param_name7 = Button(description='B_color', disabled=True, layout=name_button_layout)
        param_name7.style.button_color = 'lightgreen'

        self.B_color = Text(
          value='green',
          style=style, layout=widget_layout)

        param_name8 = Button(description='C_color', disabled=True, layout=name_button_layout)
        param_name8.style.button_color = 'tan'

        self.C_color = Text(
          value='cyan',
          style=style, layout=widget_layout)

        param_name9 = Button(description='standard_plots', disabled=True, layout=name_button_layout)
        param_name9.style.button_color = 'lightgreen'

        self.standard_plots = Checkbox(
          value=False,
          style=style, layout=widget_layout)

        div_row3 = Button(description='---Overall signaling settings---', disabled=True, layout=divider_button_layout)

        param_name10 = Button(description='hill_power', disabled=True, layout=name_button_layout)
        param_name10.style.button_color = 'tan'

        self.hill_power = FloatText(
          value=5,
          step=0.1,
          style=style, layout=widget_layout)

        param_name11 = Button(description='half_max', disabled=True, layout=name_button_layout)
        param_name11.style.button_color = 'lightgreen'

        self.half_max = FloatText(
          value=0.1,
          step=0.01,
          style=style, layout=widget_layout)

        div_row4 = Button(description='---cell type A settings---', disabled=True, layout=divider_button_layout)

        param_name12 = Button(description='A_base_cycle', disabled=True, layout=name_button_layout)
        param_name12.style.button_color = 'tan'

        self.A_base_cycle = FloatText(
          value=0.00072,
          step=0.0001,
          style=style, layout=widget_layout)

        param_name13 = Button(description='A_max_cycle', disabled=True, layout=name_button_layout)
        param_name13.style.button_color = 'lightgreen'

        self.A_max_cycle = FloatText(
          value=0.0072,
          step=0.001,
          style=style, layout=widget_layout)

        param_name14 = Button(description='A_cycle_A', disabled=True, layout=name_button_layout)
        param_name14.style.button_color = 'tan'

        self.A_cycle_A = Text(
          value='neutral',
          style=style, layout=widget_layout)

        param_name15 = Button(description='A_cycle_B', disabled=True, layout=name_button_layout)
        param_name15.style.button_color = 'lightgreen'

        self.A_cycle_B = Text(
          value='neutral',
          style=style, layout=widget_layout)

        param_name16 = Button(description='A_cycle_C', disabled=True, layout=name_button_layout)
        param_name16.style.button_color = 'tan'

        self.A_cycle_C = Text(
          value='neutral',
          style=style, layout=widget_layout)

        param_name17 = Button(description='A_cycle_pressure_threshold', disabled=True, layout=name_button_layout)
        param_name17.style.button_color = 'lightgreen'

        self.A_cycle_pressure_threshold = FloatText(
          value=2.0,
          step=0.1,
          style=style, layout=widget_layout)

        param_name18 = Button(description='A_base_death', disabled=True, layout=name_button_layout)
        param_name18.style.button_color = 'tan'

        self.A_base_death = FloatText(
          value=5.31667e-05,
          step=1e-05,
          style=style, layout=widget_layout)

        param_name19 = Button(description='A_max_death', disabled=True, layout=name_button_layout)
        param_name19.style.button_color = 'lightgreen'

        self.A_max_death = FloatText(
          value=5.31667e-04,
          step=0.0001,
          style=style, layout=widget_layout)

        param_name20 = Button(description='A_death_A', disabled=True, layout=name_button_layout)
        param_name20.style.button_color = 'tan'

        self.A_death_A = Text(
          value='neutral',
          style=style, layout=widget_layout)

        param_name21 = Button(description='A_death_B', disabled=True, layout=name_button_layout)
        param_name21.style.button_color = 'lightgreen'

        self.A_death_B = Text(
          value='neutral',
          style=style, layout=widget_layout)

        param_name22 = Button(description='A_death_C', disabled=True, layout=name_button_layout)
        param_name22.style.button_color = 'tan'

        self.A_death_C = Text(
          value='neutral',
          style=style, layout=widget_layout)

        param_name23 = Button(description='A_death_R', disabled=True, layout=name_button_layout)
        param_name23.style.button_color = 'lightgreen'

        self.A_death_R = Text(
          value='neutral',
          style=style, layout=widget_layout)

        param_name24 = Button(description='A_apoptosis_pressure_threshold', disabled=True, layout=name_button_layout)
        param_name24.style.button_color = 'tan'

        self.A_apoptosis_pressure_threshold = FloatText(
          value=100.0,
          step=10,
          style=style, layout=widget_layout)

        param_name25 = Button(description='A_necrosis_threshold', disabled=True, layout=name_button_layout)
        param_name25.style.button_color = 'lightgreen'

        self.A_necrosis_threshold = FloatText(
          value=0.4,
          step=0.1,
          style=style, layout=widget_layout)

        param_name26 = Button(description='A_base_speed', disabled=True, layout=name_button_layout)
        param_name26.style.button_color = 'tan'

        self.A_base_speed = FloatText(
          value=0.1,
          step=0.01,
          style=style, layout=widget_layout)

        param_name27 = Button(description='A_max_speed', disabled=True, layout=name_button_layout)
        param_name27.style.button_color = 'lightgreen'

        self.A_max_speed = FloatText(
          value=1,
          step=0.1,
          style=style, layout=widget_layout)

        param_name28 = Button(description='A_speed_A', disabled=True, layout=name_button_layout)
        param_name28.style.button_color = 'tan'

        self.A_speed_A = Text(
          value='neutral',
          style=style, layout=widget_layout)

        param_name29 = Button(description='A_speed_B', disabled=True, layout=name_button_layout)
        param_name29.style.button_color = 'lightgreen'

        self.A_speed_B = Text(
          value='neutral',
          style=style, layout=widget_layout)

        param_name30 = Button(description='A_speed_C', disabled=True, layout=name_button_layout)
        param_name30.style.button_color = 'tan'

        self.A_speed_C = Text(
          value='neutral',
          style=style, layout=widget_layout)

        param_name31 = Button(description='A_speed_R', disabled=True, layout=name_button_layout)
        param_name31.style.button_color = 'lightgreen'

        self.A_speed_R = Text(
          value='neutral',
          style=style, layout=widget_layout)

        param_name32 = Button(description='A_base_secretion', disabled=True, layout=name_button_layout)
        param_name32.style.button_color = 'tan'

        self.A_base_secretion = FloatText(
          value=0,
          step=0.01,
          style=style, layout=widget_layout)

        param_name33 = Button(description='A_max_secretion', disabled=True, layout=name_button_layout)
        param_name33.style.button_color = 'lightgreen'

        self.A_max_secretion = FloatText(
          value=1,
          step=0.1,
          style=style, layout=widget_layout)

        param_name34 = Button(description='A_signal_A', disabled=True, layout=name_button_layout)
        param_name34.style.button_color = 'tan'

        self.A_signal_A = Text(
          value='neutral',
          style=style, layout=widget_layout)

        param_name35 = Button(description='A_signal_B', disabled=True, layout=name_button_layout)
        param_name35.style.button_color = 'lightgreen'

        self.A_signal_B = Text(
          value='neutral',
          style=style, layout=widget_layout)

        param_name36 = Button(description='A_signal_C', disabled=True, layout=name_button_layout)
        param_name36.style.button_color = 'tan'

        self.A_signal_C = Text(
          value='neutral',
          style=style, layout=widget_layout)

        param_name37 = Button(description='A_signal_R', disabled=True, layout=name_button_layout)
        param_name37.style.button_color = 'lightgreen'

        self.A_signal_R = Text(
          value='neutral',
          style=style, layout=widget_layout)

        div_row5 = Button(description='---cell type B settings---', disabled=True, layout=divider_button_layout)

        param_name38 = Button(description='B_base_cycle', disabled=True, layout=name_button_layout)
        param_name38.style.button_color = 'tan'

        self.B_base_cycle = FloatText(
          value=0.00072,
          step=0.0001,
          style=style, layout=widget_layout)

        param_name39 = Button(description='B_max_cycle', disabled=True, layout=name_button_layout)
        param_name39.style.button_color = 'lightgreen'

        self.B_max_cycle = FloatText(
          value=0.0072,
          step=0.001,
          style=style, layout=widget_layout)

        param_name40 = Button(description='B_cycle_A', disabled=True, layout=name_button_layout)
        param_name40.style.button_color = 'tan'

        self.B_cycle_A = Text(
          value='neutral',
          style=style, layout=widget_layout)

        param_name41 = Button(description='B_cycle_B', disabled=True, layout=name_button_layout)
        param_name41.style.button_color = 'lightgreen'

        self.B_cycle_B = Text(
          value='neutral',
          style=style, layout=widget_layout)

        param_name42 = Button(description='B_cycle_C', disabled=True, layout=name_button_layout)
        param_name42.style.button_color = 'tan'

        self.B_cycle_C = Text(
          value='neutral',
          style=style, layout=widget_layout)

        param_name43 = Button(description='B_cycle_pressure_threshold', disabled=True, layout=name_button_layout)
        param_name43.style.button_color = 'lightgreen'

        self.B_cycle_pressure_threshold = FloatText(
          value=2.0,
          step=0.1,
          style=style, layout=widget_layout)

        param_name44 = Button(description='B_base_death', disabled=True, layout=name_button_layout)
        param_name44.style.button_color = 'tan'

        self.B_base_death = FloatText(
          value=5.31667e-05,
          step=1e-05,
          style=style, layout=widget_layout)

        param_name45 = Button(description='B_max_death', disabled=True, layout=name_button_layout)
        param_name45.style.button_color = 'lightgreen'

        self.B_max_death = FloatText(
          value=5.31667e-04,
          step=0.0001,
          style=style, layout=widget_layout)

        param_name46 = Button(description='B_death_A', disabled=True, layout=name_button_layout)
        param_name46.style.button_color = 'tan'

        self.B_death_A = Text(
          value='neutral',
          style=style, layout=widget_layout)

        param_name47 = Button(description='B_death_B', disabled=True, layout=name_button_layout)
        param_name47.style.button_color = 'lightgreen'

        self.B_death_B = Text(
          value='neutral',
          style=style, layout=widget_layout)

        param_name48 = Button(description='B_death_C', disabled=True, layout=name_button_layout)
        param_name48.style.button_color = 'tan'

        self.B_death_C = Text(
          value='neutral',
          style=style, layout=widget_layout)

        param_name49 = Button(description='B_death_R', disabled=True, layout=name_button_layout)
        param_name49.style.button_color = 'lightgreen'

        self.B_death_R = Text(
          value='neutral',
          style=style, layout=widget_layout)

        param_name50 = Button(description='B_apoptosis_pressure_threshold', disabled=True, layout=name_button_layout)
        param_name50.style.button_color = 'tan'

        self.B_apoptosis_pressure_threshold = FloatText(
          value=100.0,
          step=10,
          style=style, layout=widget_layout)

        param_name51 = Button(description='B_necrosis_threshold', disabled=True, layout=name_button_layout)
        param_name51.style.button_color = 'lightgreen'

        self.B_necrosis_threshold = FloatText(
          value=0.4,
          step=0.1,
          style=style, layout=widget_layout)

        param_name52 = Button(description='B_base_speed', disabled=True, layout=name_button_layout)
        param_name52.style.button_color = 'tan'

        self.B_base_speed = FloatText(
          value=0.1,
          step=0.01,
          style=style, layout=widget_layout)

        param_name53 = Button(description='B_max_speed', disabled=True, layout=name_button_layout)
        param_name53.style.button_color = 'lightgreen'

        self.B_max_speed = FloatText(
          value=1,
          step=0.1,
          style=style, layout=widget_layout)

        param_name54 = Button(description='B_speed_A', disabled=True, layout=name_button_layout)
        param_name54.style.button_color = 'tan'

        self.B_speed_A = Text(
          value='neutral',
          style=style, layout=widget_layout)

        param_name55 = Button(description='B_speed_B', disabled=True, layout=name_button_layout)
        param_name55.style.button_color = 'lightgreen'

        self.B_speed_B = Text(
          value='neutral',
          style=style, layout=widget_layout)

        param_name56 = Button(description='B_speed_C', disabled=True, layout=name_button_layout)
        param_name56.style.button_color = 'tan'

        self.B_speed_C = Text(
          value='neutral',
          style=style, layout=widget_layout)

        param_name57 = Button(description='B_speed_R', disabled=True, layout=name_button_layout)
        param_name57.style.button_color = 'lightgreen'

        self.B_speed_R = Text(
          value='neutral',
          style=style, layout=widget_layout)

        param_name58 = Button(description='B_base_secretion', disabled=True, layout=name_button_layout)
        param_name58.style.button_color = 'tan'

        self.B_base_secretion = FloatText(
          value=0,
          step=0.01,
          style=style, layout=widget_layout)

        param_name59 = Button(description='B_max_secretion', disabled=True, layout=name_button_layout)
        param_name59.style.button_color = 'lightgreen'

        self.B_max_secretion = FloatText(
          value=1,
          step=0.1,
          style=style, layout=widget_layout)

        param_name60 = Button(description='B_signal_A', disabled=True, layout=name_button_layout)
        param_name60.style.button_color = 'tan'

        self.B_signal_A = Text(
          value='neutral',
          style=style, layout=widget_layout)

        param_name61 = Button(description='B_signal_B', disabled=True, layout=name_button_layout)
        param_name61.style.button_color = 'lightgreen'

        self.B_signal_B = Text(
          value='neutral',
          style=style, layout=widget_layout)

        param_name62 = Button(description='B_signal_C', disabled=True, layout=name_button_layout)
        param_name62.style.button_color = 'tan'

        self.B_signal_C = Text(
          value='neutral',
          style=style, layout=widget_layout)

        param_name63 = Button(description='B_signal_R', disabled=True, layout=name_button_layout)
        param_name63.style.button_color = 'lightgreen'

        self.B_signal_R = Text(
          value='neutral',
          style=style, layout=widget_layout)

        div_row6 = Button(description='---cell type C settings---', disabled=True, layout=divider_button_layout)

        param_name64 = Button(description='C_base_cycle', disabled=True, layout=name_button_layout)
        param_name64.style.button_color = 'tan'

        self.C_base_cycle = FloatText(
          value=0.00072,
          step=0.0001,
          style=style, layout=widget_layout)

        param_name65 = Button(description='C_max_cycle', disabled=True, layout=name_button_layout)
        param_name65.style.button_color = 'lightgreen'

        self.C_max_cycle = FloatText(
          value=0.0072,
          step=0.001,
          style=style, layout=widget_layout)

        param_name66 = Button(description='C_cycle_A', disabled=True, layout=name_button_layout)
        param_name66.style.button_color = 'tan'

        self.C_cycle_A = Text(
          value='neutral',
          style=style, layout=widget_layout)

        param_name67 = Button(description='C_cycle_B', disabled=True, layout=name_button_layout)
        param_name67.style.button_color = 'lightgreen'

        self.C_cycle_B = Text(
          value='neutral',
          style=style, layout=widget_layout)

        param_name68 = Button(description='C_cycle_C', disabled=True, layout=name_button_layout)
        param_name68.style.button_color = 'tan'

        self.C_cycle_C = Text(
          value='neutral',
          style=style, layout=widget_layout)

        param_name69 = Button(description='C_cycle_pressure_threshold', disabled=True, layout=name_button_layout)
        param_name69.style.button_color = 'lightgreen'

        self.C_cycle_pressure_threshold = FloatText(
          value=2.0,
          step=0.1,
          style=style, layout=widget_layout)

        param_name70 = Button(description='C_base_death', disabled=True, layout=name_button_layout)
        param_name70.style.button_color = 'tan'

        self.C_base_death = FloatText(
          value=5.31667e-05,
          step=1e-05,
          style=style, layout=widget_layout)

        param_name71 = Button(description='C_max_death', disabled=True, layout=name_button_layout)
        param_name71.style.button_color = 'lightgreen'

        self.C_max_death = FloatText(
          value=5.31667e-04,
          step=0.0001,
          style=style, layout=widget_layout)

        param_name72 = Button(description='C_death_A', disabled=True, layout=name_button_layout)
        param_name72.style.button_color = 'tan'

        self.C_death_A = Text(
          value='neutral',
          style=style, layout=widget_layout)

        param_name73 = Button(description='C_death_B', disabled=True, layout=name_button_layout)
        param_name73.style.button_color = 'lightgreen'

        self.C_death_B = Text(
          value='neutral',
          style=style, layout=widget_layout)

        param_name74 = Button(description='C_death_C', disabled=True, layout=name_button_layout)
        param_name74.style.button_color = 'tan'

        self.C_death_C = Text(
          value='neutral',
          style=style, layout=widget_layout)

        param_name75 = Button(description='C_death_R', disabled=True, layout=name_button_layout)
        param_name75.style.button_color = 'lightgreen'

        self.C_death_R = Text(
          value='neutral',
          style=style, layout=widget_layout)

        param_name76 = Button(description='C_apoptosis_pressure_threshold', disabled=True, layout=name_button_layout)
        param_name76.style.button_color = 'tan'

        self.C_apoptosis_pressure_threshold = FloatText(
          value=100.0,
          step=10,
          style=style, layout=widget_layout)

        param_name77 = Button(description='C_necrosis_threshold', disabled=True, layout=name_button_layout)
        param_name77.style.button_color = 'lightgreen'

        self.C_necrosis_threshold = FloatText(
          value=0.4,
          step=0.1,
          style=style, layout=widget_layout)

        param_name78 = Button(description='C_base_speed', disabled=True, layout=name_button_layout)
        param_name78.style.button_color = 'tan'

        self.C_base_speed = FloatText(
          value=0.1,
          step=0.01,
          style=style, layout=widget_layout)

        param_name79 = Button(description='C_max_speed', disabled=True, layout=name_button_layout)
        param_name79.style.button_color = 'lightgreen'

        self.C_max_speed = FloatText(
          value=1,
          step=0.1,
          style=style, layout=widget_layout)

        param_name80 = Button(description='C_speed_A', disabled=True, layout=name_button_layout)
        param_name80.style.button_color = 'tan'

        self.C_speed_A = Text(
          value='neutral',
          style=style, layout=widget_layout)

        param_name81 = Button(description='C_speed_B', disabled=True, layout=name_button_layout)
        param_name81.style.button_color = 'lightgreen'

        self.C_speed_B = Text(
          value='neutral',
          style=style, layout=widget_layout)

        param_name82 = Button(description='C_speed_C', disabled=True, layout=name_button_layout)
        param_name82.style.button_color = 'tan'

        self.C_speed_C = Text(
          value='neutral',
          style=style, layout=widget_layout)

        param_name83 = Button(description='C_speed_R', disabled=True, layout=name_button_layout)
        param_name83.style.button_color = 'lightgreen'

        self.C_speed_R = Text(
          value='neutral',
          style=style, layout=widget_layout)

        param_name84 = Button(description='C_base_secretion', disabled=True, layout=name_button_layout)
        param_name84.style.button_color = 'tan'

        self.C_base_secretion = FloatText(
          value=0,
          step=0.01,
          style=style, layout=widget_layout)

        param_name85 = Button(description='C_max_secretion', disabled=True, layout=name_button_layout)
        param_name85.style.button_color = 'lightgreen'

        self.C_max_secretion = FloatText(
          value=1,
          step=0.1,
          style=style, layout=widget_layout)

        param_name86 = Button(description='C_signal_A', disabled=True, layout=name_button_layout)
        param_name86.style.button_color = 'tan'

        self.C_signal_A = Text(
          value='neutral',
          style=style, layout=widget_layout)

        param_name87 = Button(description='C_signal_B', disabled=True, layout=name_button_layout)
        param_name87.style.button_color = 'lightgreen'

        self.C_signal_B = Text(
          value='neutral',
          style=style, layout=widget_layout)

        param_name88 = Button(description='C_signal_C', disabled=True, layout=name_button_layout)
        param_name88.style.button_color = 'tan'

        self.C_signal_C = Text(
          value='neutral',
          style=style, layout=widget_layout)

        param_name89 = Button(description='C_signal_R', disabled=True, layout=name_button_layout)
        param_name89.style.button_color = 'lightgreen'

        self.C_signal_R = Text(
          value='neutral',
          style=style, layout=widget_layout)

        div_row7 = Button(description='---Danger Zone (Advanced Settings)---', disabled=True, layout=divider_button_layout)

        param_name90 = Button(description='dt_diffusion', disabled=True, layout=name_button_layout)
        param_name90.style.button_color = 'tan'

        self.dt_diffusion = FloatText(
          value=0.01,
          step=0.001,
          style=style, layout=widget_layout)

        param_name91 = Button(description='dt_mechanics', disabled=True, layout=name_button_layout)
        param_name91.style.button_color = 'lightgreen'

        self.dt_mechanics = FloatText(
          value=0.1,
          step=0.01,
          style=style, layout=widget_layout)

        param_name92 = Button(description='dt_phenotype', disabled=True, layout=name_button_layout)
        param_name92.style.button_color = 'tan'

        self.dt_phenotype = FloatText(
          value=6,
          step=0.1,
          style=style, layout=widget_layout)

        units_button1 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button1.style.button_color = 'lightgreen'
        units_button2 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button2.style.button_color = 'lightgreen'
        units_button3 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button3.style.button_color = 'tan'
        units_button4 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button4.style.button_color = 'lightgreen'
        units_button5 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button5.style.button_color = 'tan'
        units_button6 = Button(description='micron', disabled=True, layout=units_button_layout) 
        units_button6.style.button_color = 'lightgreen'
        units_button7 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button7.style.button_color = 'lightgreen'
        units_button8 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button8.style.button_color = 'tan'
        units_button9 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button9.style.button_color = 'lightgreen'
        units_button10 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button10.style.button_color = 'tan'
        units_button11 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button11.style.button_color = 'lightgreen'
        units_button12 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button12.style.button_color = 'lightgreen'
        units_button13 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button13.style.button_color = 'tan'
        units_button14 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button14.style.button_color = 'lightgreen'
        units_button15 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button15.style.button_color = 'lightgreen'
        units_button16 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button16.style.button_color = 'tan'
        units_button17 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button17.style.button_color = 'lightgreen'
        units_button18 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button18.style.button_color = 'tan'
        units_button19 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button19.style.button_color = 'lightgreen'
        units_button20 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button20.style.button_color = 'tan'
        units_button21 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button21.style.button_color = 'lightgreen'
        units_button22 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button22.style.button_color = 'tan'
        units_button23 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button23.style.button_color = 'lightgreen'
        units_button24 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button24.style.button_color = 'tan'
        units_button25 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button25.style.button_color = 'lightgreen'
        units_button26 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button26.style.button_color = 'tan'
        units_button27 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button27.style.button_color = 'lightgreen'
        units_button28 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button28.style.button_color = 'tan'
        units_button29 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button29.style.button_color = 'lightgreen'
        units_button30 = Button(description='micron/min', disabled=True, layout=units_button_layout) 
        units_button30.style.button_color = 'tan'
        units_button31 = Button(description='micron/min', disabled=True, layout=units_button_layout) 
        units_button31.style.button_color = 'lightgreen'
        units_button32 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button32.style.button_color = 'tan'
        units_button33 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button33.style.button_color = 'lightgreen'
        units_button34 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button34.style.button_color = 'tan'
        units_button35 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button35.style.button_color = 'lightgreen'
        units_button36 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button36.style.button_color = 'tan'
        units_button37 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button37.style.button_color = 'lightgreen'
        units_button38 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button38.style.button_color = 'tan'
        units_button39 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button39.style.button_color = 'lightgreen'
        units_button40 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button40.style.button_color = 'tan'
        units_button41 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button41.style.button_color = 'lightgreen'
        units_button42 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button42.style.button_color = 'lightgreen'
        units_button43 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button43.style.button_color = 'tan'
        units_button44 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button44.style.button_color = 'lightgreen'
        units_button45 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button45.style.button_color = 'tan'
        units_button46 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button46.style.button_color = 'lightgreen'
        units_button47 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button47.style.button_color = 'tan'
        units_button48 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button48.style.button_color = 'lightgreen'
        units_button49 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button49.style.button_color = 'tan'
        units_button50 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button50.style.button_color = 'lightgreen'
        units_button51 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button51.style.button_color = 'tan'
        units_button52 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button52.style.button_color = 'lightgreen'
        units_button53 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button53.style.button_color = 'tan'
        units_button54 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button54.style.button_color = 'lightgreen'
        units_button55 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button55.style.button_color = 'tan'
        units_button56 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button56.style.button_color = 'lightgreen'
        units_button57 = Button(description='micron/min', disabled=True, layout=units_button_layout) 
        units_button57.style.button_color = 'tan'
        units_button58 = Button(description='micron/min', disabled=True, layout=units_button_layout) 
        units_button58.style.button_color = 'lightgreen'
        units_button59 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button59.style.button_color = 'tan'
        units_button60 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button60.style.button_color = 'lightgreen'
        units_button61 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button61.style.button_color = 'tan'
        units_button62 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button62.style.button_color = 'lightgreen'
        units_button63 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button63.style.button_color = 'tan'
        units_button64 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button64.style.button_color = 'lightgreen'
        units_button65 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button65.style.button_color = 'tan'
        units_button66 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button66.style.button_color = 'lightgreen'
        units_button67 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button67.style.button_color = 'tan'
        units_button68 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button68.style.button_color = 'lightgreen'
        units_button69 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button69.style.button_color = 'lightgreen'
        units_button70 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button70.style.button_color = 'tan'
        units_button71 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button71.style.button_color = 'lightgreen'
        units_button72 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button72.style.button_color = 'tan'
        units_button73 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button73.style.button_color = 'lightgreen'
        units_button74 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button74.style.button_color = 'tan'
        units_button75 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button75.style.button_color = 'lightgreen'
        units_button76 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button76.style.button_color = 'tan'
        units_button77 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button77.style.button_color = 'lightgreen'
        units_button78 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button78.style.button_color = 'tan'
        units_button79 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button79.style.button_color = 'lightgreen'
        units_button80 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button80.style.button_color = 'tan'
        units_button81 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button81.style.button_color = 'lightgreen'
        units_button82 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button82.style.button_color = 'tan'
        units_button83 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button83.style.button_color = 'lightgreen'
        units_button84 = Button(description='micron/min', disabled=True, layout=units_button_layout) 
        units_button84.style.button_color = 'tan'
        units_button85 = Button(description='micron/min', disabled=True, layout=units_button_layout) 
        units_button85.style.button_color = 'lightgreen'
        units_button86 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button86.style.button_color = 'tan'
        units_button87 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button87.style.button_color = 'lightgreen'
        units_button88 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button88.style.button_color = 'tan'
        units_button89 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button89.style.button_color = 'lightgreen'
        units_button90 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button90.style.button_color = 'tan'
        units_button91 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button91.style.button_color = 'lightgreen'
        units_button92 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button92.style.button_color = 'tan'
        units_button93 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button93.style.button_color = 'lightgreen'
        units_button94 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button94.style.button_color = 'tan'
        units_button95 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button95.style.button_color = 'lightgreen'
        units_button96 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button96.style.button_color = 'lightgreen'
        units_button97 = Button(description='min', disabled=True, layout=units_button_layout) 
        units_button97.style.button_color = 'tan'
        units_button98 = Button(description='min', disabled=True, layout=units_button_layout) 
        units_button98.style.button_color = 'lightgreen'
        units_button99 = Button(description='min', disabled=True, layout=units_button_layout) 
        units_button99.style.button_color = 'tan'

        desc_button1 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button1.style.button_color = 'lightgreen'
        desc_button2 = Button(description='initial number of A' , tooltip='initial number of A', disabled=True, layout=desc_button_layout) 
        desc_button2.style.button_color = 'tan'
        desc_button3 = Button(description='initial number of B' , tooltip='initial number of B', disabled=True, layout=desc_button_layout) 
        desc_button3.style.button_color = 'lightgreen'
        desc_button4 = Button(description='initial number of C' , tooltip='initial number of C', disabled=True, layout=desc_button_layout) 
        desc_button4.style.button_color = 'tan'
        desc_button5 = Button(description='max initial distance of cells from (0,0,0)' , tooltip='max initial distance of cells from (0,0,0)', disabled=True, layout=desc_button_layout) 
        desc_button5.style.button_color = 'lightgreen'
        desc_button6 = Button(description='color for A cells' , tooltip='color for A cells', disabled=True, layout=desc_button_layout) 
        desc_button6.style.button_color = 'tan'
        desc_button7 = Button(description='color for B cells' , tooltip='color for B cells', disabled=True, layout=desc_button_layout) 
        desc_button7.style.button_color = 'lightgreen'
        desc_button8 = Button(description='color for C cells' , tooltip='color for C cells', disabled=True, layout=desc_button_layout) 
        desc_button8.style.button_color = 'tan'
        desc_button9 = Button(description='Enable additional standard plots?' , tooltip='Enable additional standard plots?', disabled=True, layout=desc_button_layout) 
        desc_button9.style.button_color = 'lightgreen'
        desc_button10 = Button(description='Hill power for signal responses' , tooltip='Hill power for signal responses', disabled=True, layout=desc_button_layout) 
        desc_button10.style.button_color = 'tan'
        desc_button11 = Button(description='half max for signal responses' , tooltip='half max for signal responses', disabled=True, layout=desc_button_layout) 
        desc_button11.style.button_color = 'lightgreen'
        desc_button12 = Button(description='base cell cycling rate for type A' , tooltip='base cell cycling rate for type A', disabled=True, layout=desc_button_layout) 
        desc_button12.style.button_color = 'tan'
        desc_button13 = Button(description='maximum cell cycling rate for type A' , tooltip='maximum cell cycling rate for type A', disabled=True, layout=desc_button_layout) 
        desc_button13.style.button_color = 'lightgreen'
        desc_button14 = Button(description='impact of signal A on A cycling (promote, inhibit, or neutral)' , tooltip='impact of signal A on A cycling (promote, inhibit, or neutral)', disabled=True, layout=desc_button_layout) 
        desc_button14.style.button_color = 'tan'
        desc_button15 = Button(description='impact of signal B on A cycling (promote, inhibit, or neutral)' , tooltip='impact of signal B on A cycling (promote, inhibit, or neutral)', disabled=True, layout=desc_button_layout) 
        desc_button15.style.button_color = 'lightgreen'
        desc_button16 = Button(description='impact of signal C on A cycling (promote, inhibit, or neutral)' , tooltip='impact of signal C on A cycling (promote, inhibit, or neutral)', disabled=True, layout=desc_button_layout) 
        desc_button16.style.button_color = 'tan'
        desc_button17 = Button(description='pressure above threshold inhibits A cycling' , tooltip='pressure above threshold inhibits A cycling', disabled=True, layout=desc_button_layout) 
        desc_button17.style.button_color = 'lightgreen'
        desc_button18 = Button(description='base cell death rate for type A' , tooltip='base cell death rate for type A', disabled=True, layout=desc_button_layout) 
        desc_button18.style.button_color = 'tan'
        desc_button19 = Button(description='maximum cell death rate for type A' , tooltip='maximum cell death rate for type A', disabled=True, layout=desc_button_layout) 
        desc_button19.style.button_color = 'lightgreen'
        desc_button20 = Button(description='impact of signal A on A apoptosis (promote, inhibit, or neutral' , tooltip='impact of signal A on A apoptosis (promote, inhibit, or neutral', disabled=True, layout=desc_button_layout) 
        desc_button20.style.button_color = 'tan'
        desc_button21 = Button(description='impact of signal B on A apoptosis (promote, inhibit, or neutral' , tooltip='impact of signal B on A apoptosis (promote, inhibit, or neutral', disabled=True, layout=desc_button_layout) 
        desc_button21.style.button_color = 'lightgreen'
        desc_button22 = Button(description='impact of signal C on A apoptosis (promote, inhibit, or neutral' , tooltip='impact of signal C on A apoptosis (promote, inhibit, or neutral', disabled=True, layout=desc_button_layout) 
        desc_button22.style.button_color = 'tan'
        desc_button23 = Button(description='impact of resource on A apoptosis (promote, inhibit, or neutral' , tooltip='impact of resource on A apoptosis (promote, inhibit, or neutral', disabled=True, layout=desc_button_layout) 
        desc_button23.style.button_color = 'lightgreen'
        desc_button24 = Button(description='pressure above threshold triggers apoptosis' , tooltip='pressure above threshold triggers apoptosis', disabled=True, layout=desc_button_layout) 
        desc_button24.style.button_color = 'tan'
        desc_button25 = Button(description='necrosis of A cells begins below this resource threshold' , tooltip='necrosis of A cells begins below this resource threshold', disabled=True, layout=desc_button_layout) 
        desc_button25.style.button_color = 'lightgreen'
        desc_button26 = Button(description='base speed for type A' , tooltip='base speed for type A', disabled=True, layout=desc_button_layout) 
        desc_button26.style.button_color = 'tan'
        desc_button27 = Button(description='maximum speed for type A' , tooltip='maximum speed for type A', disabled=True, layout=desc_button_layout) 
        desc_button27.style.button_color = 'lightgreen'
        desc_button28 = Button(description='impact of signal A on A motility (promote, inhibit, or neutral' , tooltip='impact of signal A on A motility (promote, inhibit, or neutral', disabled=True, layout=desc_button_layout) 
        desc_button28.style.button_color = 'tan'
        desc_button29 = Button(description='impact of signal B on A motility (promote, inhibit, or neutral' , tooltip='impact of signal B on A motility (promote, inhibit, or neutral', disabled=True, layout=desc_button_layout) 
        desc_button29.style.button_color = 'lightgreen'
        desc_button30 = Button(description='impact of signal C on A motility (promote, inhibit, or neutral' , tooltip='impact of signal C on A motility (promote, inhibit, or neutral', disabled=True, layout=desc_button_layout) 
        desc_button30.style.button_color = 'tan'
        desc_button31 = Button(description='impact of resource on A motility (promote, inhibit, or neutral' , tooltip='impact of resource on A motility (promote, inhibit, or neutral', disabled=True, layout=desc_button_layout) 
        desc_button31.style.button_color = 'lightgreen'
        desc_button32 = Button(description='base secretion rate of signal A by type A' , tooltip='base secretion rate of signal A by type A', disabled=True, layout=desc_button_layout) 
        desc_button32.style.button_color = 'tan'
        desc_button33 = Button(description='max secretion rate of signal A by type A' , tooltip='max secretion rate of signal A by type A', disabled=True, layout=desc_button_layout) 
        desc_button33.style.button_color = 'lightgreen'
        desc_button34 = Button(description='impact of signal A on A secretion (promote, inhibit, or neutral' , tooltip='impact of signal A on A secretion (promote, inhibit, or neutral', disabled=True, layout=desc_button_layout) 
        desc_button34.style.button_color = 'tan'
        desc_button35 = Button(description='impact of signal B on A secretion (promote, inhibit, or neutral' , tooltip='impact of signal B on A secretion (promote, inhibit, or neutral', disabled=True, layout=desc_button_layout) 
        desc_button35.style.button_color = 'lightgreen'
        desc_button36 = Button(description='impact of signal C on A secretion (promote, inhibit, or neutral' , tooltip='impact of signal C on A secretion (promote, inhibit, or neutral', disabled=True, layout=desc_button_layout) 
        desc_button36.style.button_color = 'tan'
        desc_button37 = Button(description='impact of resource on A secretion (promote, inhibit, or neutral' , tooltip='impact of resource on A secretion (promote, inhibit, or neutral', disabled=True, layout=desc_button_layout) 
        desc_button37.style.button_color = 'lightgreen'
        desc_button38 = Button(description='base cell cycling rate for type B' , tooltip='base cell cycling rate for type B', disabled=True, layout=desc_button_layout) 
        desc_button38.style.button_color = 'tan'
        desc_button39 = Button(description='maximum cell cycling rate for type B' , tooltip='maximum cell cycling rate for type B', disabled=True, layout=desc_button_layout) 
        desc_button39.style.button_color = 'lightgreen'
        desc_button40 = Button(description='impact of signal A on B cycling (promote, inhibit, or neutral)' , tooltip='impact of signal A on B cycling (promote, inhibit, or neutral)', disabled=True, layout=desc_button_layout) 
        desc_button40.style.button_color = 'tan'
        desc_button41 = Button(description='impact of signal B on B cycling (promote, inhibit, or neutral)' , tooltip='impact of signal B on B cycling (promote, inhibit, or neutral)', disabled=True, layout=desc_button_layout) 
        desc_button41.style.button_color = 'lightgreen'
        desc_button42 = Button(description='impact of signal C on B cycling (promote, inhibit, or neutral)' , tooltip='impact of signal C on B cycling (promote, inhibit, or neutral)', disabled=True, layout=desc_button_layout) 
        desc_button42.style.button_color = 'tan'
        desc_button43 = Button(description='pressure above threshold inhibits B cycling' , tooltip='pressure above threshold inhibits B cycling', disabled=True, layout=desc_button_layout) 
        desc_button43.style.button_color = 'lightgreen'
        desc_button44 = Button(description='base cell death rate for type B' , tooltip='base cell death rate for type B', disabled=True, layout=desc_button_layout) 
        desc_button44.style.button_color = 'tan'
        desc_button45 = Button(description='maximum cell death rate for type B' , tooltip='maximum cell death rate for type B', disabled=True, layout=desc_button_layout) 
        desc_button45.style.button_color = 'lightgreen'
        desc_button46 = Button(description='impact of signal A on B apoptosis (promote, inhibit, or neutral' , tooltip='impact of signal A on B apoptosis (promote, inhibit, or neutral', disabled=True, layout=desc_button_layout) 
        desc_button46.style.button_color = 'tan'
        desc_button47 = Button(description='impact of signal B on B apoptosis (promote, inhibit, or neutral' , tooltip='impact of signal B on B apoptosis (promote, inhibit, or neutral', disabled=True, layout=desc_button_layout) 
        desc_button47.style.button_color = 'lightgreen'
        desc_button48 = Button(description='impact of signal C on B apoptosis (promote, inhibit, or neutral' , tooltip='impact of signal C on B apoptosis (promote, inhibit, or neutral', disabled=True, layout=desc_button_layout) 
        desc_button48.style.button_color = 'tan'
        desc_button49 = Button(description='impact of resource on B apoptosis (promote, inhibit, or neutral' , tooltip='impact of resource on B apoptosis (promote, inhibit, or neutral', disabled=True, layout=desc_button_layout) 
        desc_button49.style.button_color = 'lightgreen'
        desc_button50 = Button(description='pressure above threshold triggers apoptosis' , tooltip='pressure above threshold triggers apoptosis', disabled=True, layout=desc_button_layout) 
        desc_button50.style.button_color = 'tan'
        desc_button51 = Button(description='necrosis of B cells begins below this resource threshold' , tooltip='necrosis of B cells begins below this resource threshold', disabled=True, layout=desc_button_layout) 
        desc_button51.style.button_color = 'lightgreen'
        desc_button52 = Button(description='base speed for type B' , tooltip='base speed for type B', disabled=True, layout=desc_button_layout) 
        desc_button52.style.button_color = 'tan'
        desc_button53 = Button(description='maximum speed for type B' , tooltip='maximum speed for type B', disabled=True, layout=desc_button_layout) 
        desc_button53.style.button_color = 'lightgreen'
        desc_button54 = Button(description='impact of signal A on B motility (promote, inhibit, or neutral' , tooltip='impact of signal A on B motility (promote, inhibit, or neutral', disabled=True, layout=desc_button_layout) 
        desc_button54.style.button_color = 'tan'
        desc_button55 = Button(description='impact of signal B on B motility (promote, inhibit, or neutral' , tooltip='impact of signal B on B motility (promote, inhibit, or neutral', disabled=True, layout=desc_button_layout) 
        desc_button55.style.button_color = 'lightgreen'
        desc_button56 = Button(description='impact of signal C on B motility (promote, inhibit, or neutral' , tooltip='impact of signal C on B motility (promote, inhibit, or neutral', disabled=True, layout=desc_button_layout) 
        desc_button56.style.button_color = 'tan'
        desc_button57 = Button(description='impact of resource on B motility (promote, inhibit, or neutral' , tooltip='impact of resource on B motility (promote, inhibit, or neutral', disabled=True, layout=desc_button_layout) 
        desc_button57.style.button_color = 'lightgreen'
        desc_button58 = Button(description='base secretion rate of signal B by type B' , tooltip='base secretion rate of signal B by type B', disabled=True, layout=desc_button_layout) 
        desc_button58.style.button_color = 'tan'
        desc_button59 = Button(description='max secretion rate of signal B by type B' , tooltip='max secretion rate of signal B by type B', disabled=True, layout=desc_button_layout) 
        desc_button59.style.button_color = 'lightgreen'
        desc_button60 = Button(description='impact of signal A on B secretion (promote, inhibit, or neutral' , tooltip='impact of signal A on B secretion (promote, inhibit, or neutral', disabled=True, layout=desc_button_layout) 
        desc_button60.style.button_color = 'tan'
        desc_button61 = Button(description='impact of signal B on B secretion (promote, inhibit, or neutral' , tooltip='impact of signal B on B secretion (promote, inhibit, or neutral', disabled=True, layout=desc_button_layout) 
        desc_button61.style.button_color = 'lightgreen'
        desc_button62 = Button(description='impact of signal C on B secretion (promote, inhibit, or neutral' , tooltip='impact of signal C on B secretion (promote, inhibit, or neutral', disabled=True, layout=desc_button_layout) 
        desc_button62.style.button_color = 'tan'
        desc_button63 = Button(description='impact of resource on B secretion (promote, inhibit, or neutral' , tooltip='impact of resource on B secretion (promote, inhibit, or neutral', disabled=True, layout=desc_button_layout) 
        desc_button63.style.button_color = 'lightgreen'
        desc_button64 = Button(description='base cell cycling rate for type C' , tooltip='base cell cycling rate for type C', disabled=True, layout=desc_button_layout) 
        desc_button64.style.button_color = 'tan'
        desc_button65 = Button(description='maximum cell cycling rate for type C' , tooltip='maximum cell cycling rate for type C', disabled=True, layout=desc_button_layout) 
        desc_button65.style.button_color = 'lightgreen'
        desc_button66 = Button(description='impact of signal A on C cycling (promote, inhibit, or neutral)' , tooltip='impact of signal A on C cycling (promote, inhibit, or neutral)', disabled=True, layout=desc_button_layout) 
        desc_button66.style.button_color = 'tan'
        desc_button67 = Button(description='impact of signal B on C cycling (promote, inhibit, or neutral)' , tooltip='impact of signal B on C cycling (promote, inhibit, or neutral)', disabled=True, layout=desc_button_layout) 
        desc_button67.style.button_color = 'lightgreen'
        desc_button68 = Button(description='impact of signal C on C cycling (promote, inhibit, or neutral)' , tooltip='impact of signal C on C cycling (promote, inhibit, or neutral)', disabled=True, layout=desc_button_layout) 
        desc_button68.style.button_color = 'tan'
        desc_button69 = Button(description='pressure above threshold inhibits C cycling' , tooltip='pressure above threshold inhibits C cycling', disabled=True, layout=desc_button_layout) 
        desc_button69.style.button_color = 'lightgreen'
        desc_button70 = Button(description='base cell death rate for type C' , tooltip='base cell death rate for type C', disabled=True, layout=desc_button_layout) 
        desc_button70.style.button_color = 'tan'
        desc_button71 = Button(description='maximum cell death rate for type C' , tooltip='maximum cell death rate for type C', disabled=True, layout=desc_button_layout) 
        desc_button71.style.button_color = 'lightgreen'
        desc_button72 = Button(description='impact of signal A on C apoptosis (promote, inhibit, or neutral' , tooltip='impact of signal A on C apoptosis (promote, inhibit, or neutral', disabled=True, layout=desc_button_layout) 
        desc_button72.style.button_color = 'tan'
        desc_button73 = Button(description='impact of signal B on C apoptosis (promote, inhibit, or neutral' , tooltip='impact of signal B on C apoptosis (promote, inhibit, or neutral', disabled=True, layout=desc_button_layout) 
        desc_button73.style.button_color = 'lightgreen'
        desc_button74 = Button(description='impact of signal C on C apoptosis (promote, inhibit, or neutral' , tooltip='impact of signal C on C apoptosis (promote, inhibit, or neutral', disabled=True, layout=desc_button_layout) 
        desc_button74.style.button_color = 'tan'
        desc_button75 = Button(description='impact of resource on C apoptosis (promote, inhibit, or neutral' , tooltip='impact of resource on C apoptosis (promote, inhibit, or neutral', disabled=True, layout=desc_button_layout) 
        desc_button75.style.button_color = 'lightgreen'
        desc_button76 = Button(description='pressure above threshold triggers apoptosis' , tooltip='pressure above threshold triggers apoptosis', disabled=True, layout=desc_button_layout) 
        desc_button76.style.button_color = 'tan'
        desc_button77 = Button(description='necrosis of C cells begins below this resource threshold' , tooltip='necrosis of C cells begins below this resource threshold', disabled=True, layout=desc_button_layout) 
        desc_button77.style.button_color = 'lightgreen'
        desc_button78 = Button(description='base speed for type C' , tooltip='base speed for type C', disabled=True, layout=desc_button_layout) 
        desc_button78.style.button_color = 'tan'
        desc_button79 = Button(description='maximum speed for type C' , tooltip='maximum speed for type C', disabled=True, layout=desc_button_layout) 
        desc_button79.style.button_color = 'lightgreen'
        desc_button80 = Button(description='impact of signal A on C motility (promote, inhibit, or neutral' , tooltip='impact of signal A on C motility (promote, inhibit, or neutral', disabled=True, layout=desc_button_layout) 
        desc_button80.style.button_color = 'tan'
        desc_button81 = Button(description='impact of signal B on C motility (promote, inhibit, or neutral' , tooltip='impact of signal B on C motility (promote, inhibit, or neutral', disabled=True, layout=desc_button_layout) 
        desc_button81.style.button_color = 'lightgreen'
        desc_button82 = Button(description='impact of signal C on C motility (promote, inhibit, or neutral' , tooltip='impact of signal C on C motility (promote, inhibit, or neutral', disabled=True, layout=desc_button_layout) 
        desc_button82.style.button_color = 'tan'
        desc_button83 = Button(description='impact of resource on C motility (promote, inhibit, or neutral' , tooltip='impact of resource on C motility (promote, inhibit, or neutral', disabled=True, layout=desc_button_layout) 
        desc_button83.style.button_color = 'lightgreen'
        desc_button84 = Button(description='base secretion rate of signal C by type C' , tooltip='base secretion rate of signal C by type C', disabled=True, layout=desc_button_layout) 
        desc_button84.style.button_color = 'tan'
        desc_button85 = Button(description='max secretion rate of signal C by type C' , tooltip='max secretion rate of signal C by type C', disabled=True, layout=desc_button_layout) 
        desc_button85.style.button_color = 'lightgreen'
        desc_button86 = Button(description='impact of signal A on C secretion (promote, inhibit, or neutral' , tooltip='impact of signal A on C secretion (promote, inhibit, or neutral', disabled=True, layout=desc_button_layout) 
        desc_button86.style.button_color = 'tan'
        desc_button87 = Button(description='impact of signal B on C secretion (promote, inhibit, or neutral' , tooltip='impact of signal B on C secretion (promote, inhibit, or neutral', disabled=True, layout=desc_button_layout) 
        desc_button87.style.button_color = 'lightgreen'
        desc_button88 = Button(description='impact of signal C on C secretion (promote, inhibit, or neutral' , tooltip='impact of signal C on C secretion (promote, inhibit, or neutral', disabled=True, layout=desc_button_layout) 
        desc_button88.style.button_color = 'tan'
        desc_button89 = Button(description='impact of resource on C secretion (promote, inhibit, or neutral' , tooltip='impact of resource on C secretion (promote, inhibit, or neutral', disabled=True, layout=desc_button_layout) 
        desc_button89.style.button_color = 'lightgreen'
        desc_button90 = Button(description='diffusion time step size' , tooltip='diffusion time step size', disabled=True, layout=desc_button_layout) 
        desc_button90.style.button_color = 'tan'
        desc_button91 = Button(description='mechanics time step size' , tooltip='mechanics time step size', disabled=True, layout=desc_button_layout) 
        desc_button91.style.button_color = 'lightgreen'
        desc_button92 = Button(description='phenotype time step size' , tooltip='phenotype time step size', disabled=True, layout=desc_button_layout) 
        desc_button92.style.button_color = 'tan'

        row1 = [param_name1, self.random_seed, units_button1, desc_button1] 
        row2 = [param_name2, self.number_of_A, units_button3, desc_button2] 
        row3 = [param_name3, self.number_of_B, units_button4, desc_button3] 
        row4 = [param_name4, self.number_of_C, units_button5, desc_button4] 
        row5 = [param_name5, self.max_distance_from_origin, units_button6, desc_button5] 
        row6 = [param_name6, self.A_color, units_button8, desc_button6] 
        row7 = [param_name7, self.B_color, units_button9, desc_button7] 
        row8 = [param_name8, self.C_color, units_button10, desc_button8] 
        row9 = [param_name9, self.standard_plots, units_button11, desc_button9] 
        row10 = [param_name10, self.hill_power, units_button13, desc_button10] 
        row11 = [param_name11, self.half_max, units_button14, desc_button11] 
        row12 = [param_name12, self.A_base_cycle, units_button16, desc_button12] 
        row13 = [param_name13, self.A_max_cycle, units_button17, desc_button13] 
        row14 = [param_name14, self.A_cycle_A, units_button18, desc_button14] 
        row15 = [param_name15, self.A_cycle_B, units_button19, desc_button15] 
        row16 = [param_name16, self.A_cycle_C, units_button20, desc_button16] 
        row17 = [param_name17, self.A_cycle_pressure_threshold, units_button21, desc_button17] 
        row18 = [param_name18, self.A_base_death, units_button22, desc_button18] 
        row19 = [param_name19, self.A_max_death, units_button23, desc_button19] 
        row20 = [param_name20, self.A_death_A, units_button24, desc_button20] 
        row21 = [param_name21, self.A_death_B, units_button25, desc_button21] 
        row22 = [param_name22, self.A_death_C, units_button26, desc_button22] 
        row23 = [param_name23, self.A_death_R, units_button27, desc_button23] 
        row24 = [param_name24, self.A_apoptosis_pressure_threshold, units_button28, desc_button24] 
        row25 = [param_name25, self.A_necrosis_threshold, units_button29, desc_button25] 
        row26 = [param_name26, self.A_base_speed, units_button30, desc_button26] 
        row27 = [param_name27, self.A_max_speed, units_button31, desc_button27] 
        row28 = [param_name28, self.A_speed_A, units_button32, desc_button28] 
        row29 = [param_name29, self.A_speed_B, units_button33, desc_button29] 
        row30 = [param_name30, self.A_speed_C, units_button34, desc_button30] 
        row31 = [param_name31, self.A_speed_R, units_button35, desc_button31] 
        row32 = [param_name32, self.A_base_secretion, units_button36, desc_button32] 
        row33 = [param_name33, self.A_max_secretion, units_button37, desc_button33] 
        row34 = [param_name34, self.A_signal_A, units_button38, desc_button34] 
        row35 = [param_name35, self.A_signal_B, units_button39, desc_button35] 
        row36 = [param_name36, self.A_signal_C, units_button40, desc_button36] 
        row37 = [param_name37, self.A_signal_R, units_button41, desc_button37] 
        row38 = [param_name38, self.B_base_cycle, units_button43, desc_button38] 
        row39 = [param_name39, self.B_max_cycle, units_button44, desc_button39] 
        row40 = [param_name40, self.B_cycle_A, units_button45, desc_button40] 
        row41 = [param_name41, self.B_cycle_B, units_button46, desc_button41] 
        row42 = [param_name42, self.B_cycle_C, units_button47, desc_button42] 
        row43 = [param_name43, self.B_cycle_pressure_threshold, units_button48, desc_button43] 
        row44 = [param_name44, self.B_base_death, units_button49, desc_button44] 
        row45 = [param_name45, self.B_max_death, units_button50, desc_button45] 
        row46 = [param_name46, self.B_death_A, units_button51, desc_button46] 
        row47 = [param_name47, self.B_death_B, units_button52, desc_button47] 
        row48 = [param_name48, self.B_death_C, units_button53, desc_button48] 
        row49 = [param_name49, self.B_death_R, units_button54, desc_button49] 
        row50 = [param_name50, self.B_apoptosis_pressure_threshold, units_button55, desc_button50] 
        row51 = [param_name51, self.B_necrosis_threshold, units_button56, desc_button51] 
        row52 = [param_name52, self.B_base_speed, units_button57, desc_button52] 
        row53 = [param_name53, self.B_max_speed, units_button58, desc_button53] 
        row54 = [param_name54, self.B_speed_A, units_button59, desc_button54] 
        row55 = [param_name55, self.B_speed_B, units_button60, desc_button55] 
        row56 = [param_name56, self.B_speed_C, units_button61, desc_button56] 
        row57 = [param_name57, self.B_speed_R, units_button62, desc_button57] 
        row58 = [param_name58, self.B_base_secretion, units_button63, desc_button58] 
        row59 = [param_name59, self.B_max_secretion, units_button64, desc_button59] 
        row60 = [param_name60, self.B_signal_A, units_button65, desc_button60] 
        row61 = [param_name61, self.B_signal_B, units_button66, desc_button61] 
        row62 = [param_name62, self.B_signal_C, units_button67, desc_button62] 
        row63 = [param_name63, self.B_signal_R, units_button68, desc_button63] 
        row64 = [param_name64, self.C_base_cycle, units_button70, desc_button64] 
        row65 = [param_name65, self.C_max_cycle, units_button71, desc_button65] 
        row66 = [param_name66, self.C_cycle_A, units_button72, desc_button66] 
        row67 = [param_name67, self.C_cycle_B, units_button73, desc_button67] 
        row68 = [param_name68, self.C_cycle_C, units_button74, desc_button68] 
        row69 = [param_name69, self.C_cycle_pressure_threshold, units_button75, desc_button69] 
        row70 = [param_name70, self.C_base_death, units_button76, desc_button70] 
        row71 = [param_name71, self.C_max_death, units_button77, desc_button71] 
        row72 = [param_name72, self.C_death_A, units_button78, desc_button72] 
        row73 = [param_name73, self.C_death_B, units_button79, desc_button73] 
        row74 = [param_name74, self.C_death_C, units_button80, desc_button74] 
        row75 = [param_name75, self.C_death_R, units_button81, desc_button75] 
        row76 = [param_name76, self.C_apoptosis_pressure_threshold, units_button82, desc_button76] 
        row77 = [param_name77, self.C_necrosis_threshold, units_button83, desc_button77] 
        row78 = [param_name78, self.C_base_speed, units_button84, desc_button78] 
        row79 = [param_name79, self.C_max_speed, units_button85, desc_button79] 
        row80 = [param_name80, self.C_speed_A, units_button86, desc_button80] 
        row81 = [param_name81, self.C_speed_B, units_button87, desc_button81] 
        row82 = [param_name82, self.C_speed_C, units_button88, desc_button82] 
        row83 = [param_name83, self.C_speed_R, units_button89, desc_button83] 
        row84 = [param_name84, self.C_base_secretion, units_button90, desc_button84] 
        row85 = [param_name85, self.C_max_secretion, units_button91, desc_button85] 
        row86 = [param_name86, self.C_signal_A, units_button92, desc_button86] 
        row87 = [param_name87, self.C_signal_B, units_button93, desc_button87] 
        row88 = [param_name88, self.C_signal_C, units_button94, desc_button88] 
        row89 = [param_name89, self.C_signal_R, units_button95, desc_button89] 
        row90 = [param_name90, self.dt_diffusion, units_button97, desc_button90] 
        row91 = [param_name91, self.dt_mechanics, units_button98, desc_button91] 
        row92 = [param_name92, self.dt_phenotype, units_button99, desc_button92] 

        box_layout = Layout(display='flex', flex_flow='row', align_items='stretch', width='100%')
        box1 = Box(children=row1, layout=box_layout)
        box2 = Box(children=row2, layout=box_layout)
        box3 = Box(children=row3, layout=box_layout)
        box4 = Box(children=row4, layout=box_layout)
        box5 = Box(children=row5, layout=box_layout)
        box6 = Box(children=row6, layout=box_layout)
        box7 = Box(children=row7, layout=box_layout)
        box8 = Box(children=row8, layout=box_layout)
        box9 = Box(children=row9, layout=box_layout)
        box10 = Box(children=row10, layout=box_layout)
        box11 = Box(children=row11, layout=box_layout)
        box12 = Box(children=row12, layout=box_layout)
        box13 = Box(children=row13, layout=box_layout)
        box14 = Box(children=row14, layout=box_layout)
        box15 = Box(children=row15, layout=box_layout)
        box16 = Box(children=row16, layout=box_layout)
        box17 = Box(children=row17, layout=box_layout)
        box18 = Box(children=row18, layout=box_layout)
        box19 = Box(children=row19, layout=box_layout)
        box20 = Box(children=row20, layout=box_layout)
        box21 = Box(children=row21, layout=box_layout)
        box22 = Box(children=row22, layout=box_layout)
        box23 = Box(children=row23, layout=box_layout)
        box24 = Box(children=row24, layout=box_layout)
        box25 = Box(children=row25, layout=box_layout)
        box26 = Box(children=row26, layout=box_layout)
        box27 = Box(children=row27, layout=box_layout)
        box28 = Box(children=row28, layout=box_layout)
        box29 = Box(children=row29, layout=box_layout)
        box30 = Box(children=row30, layout=box_layout)
        box31 = Box(children=row31, layout=box_layout)
        box32 = Box(children=row32, layout=box_layout)
        box33 = Box(children=row33, layout=box_layout)
        box34 = Box(children=row34, layout=box_layout)
        box35 = Box(children=row35, layout=box_layout)
        box36 = Box(children=row36, layout=box_layout)
        box37 = Box(children=row37, layout=box_layout)
        box38 = Box(children=row38, layout=box_layout)
        box39 = Box(children=row39, layout=box_layout)
        box40 = Box(children=row40, layout=box_layout)
        box41 = Box(children=row41, layout=box_layout)
        box42 = Box(children=row42, layout=box_layout)
        box43 = Box(children=row43, layout=box_layout)
        box44 = Box(children=row44, layout=box_layout)
        box45 = Box(children=row45, layout=box_layout)
        box46 = Box(children=row46, layout=box_layout)
        box47 = Box(children=row47, layout=box_layout)
        box48 = Box(children=row48, layout=box_layout)
        box49 = Box(children=row49, layout=box_layout)
        box50 = Box(children=row50, layout=box_layout)
        box51 = Box(children=row51, layout=box_layout)
        box52 = Box(children=row52, layout=box_layout)
        box53 = Box(children=row53, layout=box_layout)
        box54 = Box(children=row54, layout=box_layout)
        box55 = Box(children=row55, layout=box_layout)
        box56 = Box(children=row56, layout=box_layout)
        box57 = Box(children=row57, layout=box_layout)
        box58 = Box(children=row58, layout=box_layout)
        box59 = Box(children=row59, layout=box_layout)
        box60 = Box(children=row60, layout=box_layout)
        box61 = Box(children=row61, layout=box_layout)
        box62 = Box(children=row62, layout=box_layout)
        box63 = Box(children=row63, layout=box_layout)
        box64 = Box(children=row64, layout=box_layout)
        box65 = Box(children=row65, layout=box_layout)
        box66 = Box(children=row66, layout=box_layout)
        box67 = Box(children=row67, layout=box_layout)
        box68 = Box(children=row68, layout=box_layout)
        box69 = Box(children=row69, layout=box_layout)
        box70 = Box(children=row70, layout=box_layout)
        box71 = Box(children=row71, layout=box_layout)
        box72 = Box(children=row72, layout=box_layout)
        box73 = Box(children=row73, layout=box_layout)
        box74 = Box(children=row74, layout=box_layout)
        box75 = Box(children=row75, layout=box_layout)
        box76 = Box(children=row76, layout=box_layout)
        box77 = Box(children=row77, layout=box_layout)
        box78 = Box(children=row78, layout=box_layout)
        box79 = Box(children=row79, layout=box_layout)
        box80 = Box(children=row80, layout=box_layout)
        box81 = Box(children=row81, layout=box_layout)
        box82 = Box(children=row82, layout=box_layout)
        box83 = Box(children=row83, layout=box_layout)
        box84 = Box(children=row84, layout=box_layout)
        box85 = Box(children=row85, layout=box_layout)
        box86 = Box(children=row86, layout=box_layout)
        box87 = Box(children=row87, layout=box_layout)
        box88 = Box(children=row88, layout=box_layout)
        box89 = Box(children=row89, layout=box_layout)
        box90 = Box(children=row90, layout=box_layout)
        box91 = Box(children=row91, layout=box_layout)
        box92 = Box(children=row92, layout=box_layout)

        self.tab = VBox([
          box1,
          div_row1,
          box2,
          box3,
          box4,
          box5,
          div_row2,
          box6,
          box7,
          box8,
          box9,
          div_row3,
          box10,
          box11,
          div_row4,
          box12,
          box13,
          box14,
          box15,
          box16,
          box17,
          box18,
          box19,
          box20,
          box21,
          box22,
          box23,
          box24,
          box25,
          box26,
          box27,
          box28,
          box29,
          box30,
          box31,
          box32,
          box33,
          box34,
          box35,
          box36,
          box37,
          div_row5,
          box38,
          box39,
          box40,
          box41,
          box42,
          box43,
          box44,
          box45,
          box46,
          box47,
          box48,
          box49,
          box50,
          box51,
          box52,
          box53,
          box54,
          box55,
          box56,
          box57,
          box58,
          box59,
          box60,
          box61,
          box62,
          box63,
          div_row6,
          box64,
          box65,
          box66,
          box67,
          box68,
          box69,
          box70,
          box71,
          box72,
          box73,
          box74,
          box75,
          box76,
          box77,
          box78,
          box79,
          box80,
          box81,
          box82,
          box83,
          box84,
          box85,
          box86,
          box87,
          box88,
          box89,
          div_row7,
          box90,
          box91,
          box92,
        ])

    # Populate the GUI widgets with values from the XML
    def fill_gui(self, xml_root):
        uep = xml_root.find('.//microenvironment_setup')  # find unique entry point
        vp = []   # pointers to <variable> nodes
        if uep:
            for var in uep.findall('variable'):
                vp.append(var)

        uep = xml_root.find('.//user_parameters')  # find unique entry point
        self.random_seed.value = int(uep.find('.//random_seed').text)
        self.number_of_A.value = int(uep.find('.//number_of_A').text)
        self.number_of_B.value = int(uep.find('.//number_of_B').text)
        self.number_of_C.value = int(uep.find('.//number_of_C').text)
        self.max_distance_from_origin.value = float(uep.find('.//max_distance_from_origin').text)
        self.A_color.value = (uep.find('.//A_color').text)
        self.B_color.value = (uep.find('.//B_color').text)
        self.C_color.value = (uep.find('.//C_color').text)
        self.standard_plots.value = ('true' == (uep.find('.//standard_plots').text.lower()) )
        self.hill_power.value = float(uep.find('.//hill_power').text)
        self.half_max.value = float(uep.find('.//half_max').text)
        self.A_base_cycle.value = float(uep.find('.//A_base_cycle').text)
        self.A_max_cycle.value = float(uep.find('.//A_max_cycle').text)
        self.A_cycle_A.value = (uep.find('.//A_cycle_A').text)
        self.A_cycle_B.value = (uep.find('.//A_cycle_B').text)
        self.A_cycle_C.value = (uep.find('.//A_cycle_C').text)
        self.A_cycle_pressure_threshold.value = float(uep.find('.//A_cycle_pressure_threshold').text)
        self.A_base_death.value = float(uep.find('.//A_base_death').text)
        self.A_max_death.value = float(uep.find('.//A_max_death').text)
        self.A_death_A.value = (uep.find('.//A_death_A').text)
        self.A_death_B.value = (uep.find('.//A_death_B').text)
        self.A_death_C.value = (uep.find('.//A_death_C').text)
        self.A_death_R.value = (uep.find('.//A_death_R').text)
        self.A_apoptosis_pressure_threshold.value = float(uep.find('.//A_apoptosis_pressure_threshold').text)
        self.A_necrosis_threshold.value = float(uep.find('.//A_necrosis_threshold').text)
        self.A_base_speed.value = float(uep.find('.//A_base_speed').text)
        self.A_max_speed.value = float(uep.find('.//A_max_speed').text)
        self.A_speed_A.value = (uep.find('.//A_speed_A').text)
        self.A_speed_B.value = (uep.find('.//A_speed_B').text)
        self.A_speed_C.value = (uep.find('.//A_speed_C').text)
        self.A_speed_R.value = (uep.find('.//A_speed_R').text)
        self.A_base_secretion.value = float(uep.find('.//A_base_secretion').text)
        self.A_max_secretion.value = float(uep.find('.//A_max_secretion').text)
        self.A_signal_A.value = (uep.find('.//A_signal_A').text)
        self.A_signal_B.value = (uep.find('.//A_signal_B').text)
        self.A_signal_C.value = (uep.find('.//A_signal_C').text)
        self.A_signal_R.value = (uep.find('.//A_signal_R').text)
        self.B_base_cycle.value = float(uep.find('.//B_base_cycle').text)
        self.B_max_cycle.value = float(uep.find('.//B_max_cycle').text)
        self.B_cycle_A.value = (uep.find('.//B_cycle_A').text)
        self.B_cycle_B.value = (uep.find('.//B_cycle_B').text)
        self.B_cycle_C.value = (uep.find('.//B_cycle_C').text)
        self.B_cycle_pressure_threshold.value = float(uep.find('.//B_cycle_pressure_threshold').text)
        self.B_base_death.value = float(uep.find('.//B_base_death').text)
        self.B_max_death.value = float(uep.find('.//B_max_death').text)
        self.B_death_A.value = (uep.find('.//B_death_A').text)
        self.B_death_B.value = (uep.find('.//B_death_B').text)
        self.B_death_C.value = (uep.find('.//B_death_C').text)
        self.B_death_R.value = (uep.find('.//B_death_R').text)
        self.B_apoptosis_pressure_threshold.value = float(uep.find('.//B_apoptosis_pressure_threshold').text)
        self.B_necrosis_threshold.value = float(uep.find('.//B_necrosis_threshold').text)
        self.B_base_speed.value = float(uep.find('.//B_base_speed').text)
        self.B_max_speed.value = float(uep.find('.//B_max_speed').text)
        self.B_speed_A.value = (uep.find('.//B_speed_A').text)
        self.B_speed_B.value = (uep.find('.//B_speed_B').text)
        self.B_speed_C.value = (uep.find('.//B_speed_C').text)
        self.B_speed_R.value = (uep.find('.//B_speed_R').text)
        self.B_base_secretion.value = float(uep.find('.//B_base_secretion').text)
        self.B_max_secretion.value = float(uep.find('.//B_max_secretion').text)
        self.B_signal_A.value = (uep.find('.//B_signal_A').text)
        self.B_signal_B.value = (uep.find('.//B_signal_B').text)
        self.B_signal_C.value = (uep.find('.//B_signal_C').text)
        self.B_signal_R.value = (uep.find('.//B_signal_R').text)
        self.C_base_cycle.value = float(uep.find('.//C_base_cycle').text)
        self.C_max_cycle.value = float(uep.find('.//C_max_cycle').text)
        self.C_cycle_A.value = (uep.find('.//C_cycle_A').text)
        self.C_cycle_B.value = (uep.find('.//C_cycle_B').text)
        self.C_cycle_C.value = (uep.find('.//C_cycle_C').text)
        self.C_cycle_pressure_threshold.value = float(uep.find('.//C_cycle_pressure_threshold').text)
        self.C_base_death.value = float(uep.find('.//C_base_death').text)
        self.C_max_death.value = float(uep.find('.//C_max_death').text)
        self.C_death_A.value = (uep.find('.//C_death_A').text)
        self.C_death_B.value = (uep.find('.//C_death_B').text)
        self.C_death_C.value = (uep.find('.//C_death_C').text)
        self.C_death_R.value = (uep.find('.//C_death_R').text)
        self.C_apoptosis_pressure_threshold.value = float(uep.find('.//C_apoptosis_pressure_threshold').text)
        self.C_necrosis_threshold.value = float(uep.find('.//C_necrosis_threshold').text)
        self.C_base_speed.value = float(uep.find('.//C_base_speed').text)
        self.C_max_speed.value = float(uep.find('.//C_max_speed').text)
        self.C_speed_A.value = (uep.find('.//C_speed_A').text)
        self.C_speed_B.value = (uep.find('.//C_speed_B').text)
        self.C_speed_C.value = (uep.find('.//C_speed_C').text)
        self.C_speed_R.value = (uep.find('.//C_speed_R').text)
        self.C_base_secretion.value = float(uep.find('.//C_base_secretion').text)
        self.C_max_secretion.value = float(uep.find('.//C_max_secretion').text)
        self.C_signal_A.value = (uep.find('.//C_signal_A').text)
        self.C_signal_B.value = (uep.find('.//C_signal_B').text)
        self.C_signal_C.value = (uep.find('.//C_signal_C').text)
        self.C_signal_R.value = (uep.find('.//C_signal_R').text)
        self.dt_diffusion.value = float(uep.find('.//dt_diffusion').text)
        self.dt_mechanics.value = float(uep.find('.//dt_mechanics').text)
        self.dt_phenotype.value = float(uep.find('.//dt_phenotype').text)


    # Read values from the GUI widgets to enable editing XML
    def fill_xml(self, xml_root):
        uep = xml_root.find('.//microenvironment_setup')  # find unique entry point
        vp = []   # pointers to <variable> nodes
        if uep:
            for var in uep.findall('variable'):
                vp.append(var)

        uep = xml_root.find('.//user_parameters')  # find unique entry point
        uep.find('.//random_seed').text = str(self.random_seed.value)
        uep.find('.//number_of_A').text = str(self.number_of_A.value)
        uep.find('.//number_of_B').text = str(self.number_of_B.value)
        uep.find('.//number_of_C').text = str(self.number_of_C.value)
        uep.find('.//max_distance_from_origin').text = str(self.max_distance_from_origin.value)
        uep.find('.//A_color').text = str(self.A_color.value)
        uep.find('.//B_color').text = str(self.B_color.value)
        uep.find('.//C_color').text = str(self.C_color.value)
        uep.find('.//standard_plots').text = str(self.standard_plots.value)
        uep.find('.//hill_power').text = str(self.hill_power.value)
        uep.find('.//half_max').text = str(self.half_max.value)
        uep.find('.//A_base_cycle').text = str(self.A_base_cycle.value)
        uep.find('.//A_max_cycle').text = str(self.A_max_cycle.value)
        uep.find('.//A_cycle_A').text = str(self.A_cycle_A.value)
        uep.find('.//A_cycle_B').text = str(self.A_cycle_B.value)
        uep.find('.//A_cycle_C').text = str(self.A_cycle_C.value)
        uep.find('.//A_cycle_pressure_threshold').text = str(self.A_cycle_pressure_threshold.value)
        uep.find('.//A_base_death').text = str(self.A_base_death.value)
        uep.find('.//A_max_death').text = str(self.A_max_death.value)
        uep.find('.//A_death_A').text = str(self.A_death_A.value)
        uep.find('.//A_death_B').text = str(self.A_death_B.value)
        uep.find('.//A_death_C').text = str(self.A_death_C.value)
        uep.find('.//A_death_R').text = str(self.A_death_R.value)
        uep.find('.//A_apoptosis_pressure_threshold').text = str(self.A_apoptosis_pressure_threshold.value)
        uep.find('.//A_necrosis_threshold').text = str(self.A_necrosis_threshold.value)
        uep.find('.//A_base_speed').text = str(self.A_base_speed.value)
        uep.find('.//A_max_speed').text = str(self.A_max_speed.value)
        uep.find('.//A_speed_A').text = str(self.A_speed_A.value)
        uep.find('.//A_speed_B').text = str(self.A_speed_B.value)
        uep.find('.//A_speed_C').text = str(self.A_speed_C.value)
        uep.find('.//A_speed_R').text = str(self.A_speed_R.value)
        uep.find('.//A_base_secretion').text = str(self.A_base_secretion.value)
        uep.find('.//A_max_secretion').text = str(self.A_max_secretion.value)
        uep.find('.//A_signal_A').text = str(self.A_signal_A.value)
        uep.find('.//A_signal_B').text = str(self.A_signal_B.value)
        uep.find('.//A_signal_C').text = str(self.A_signal_C.value)
        uep.find('.//A_signal_R').text = str(self.A_signal_R.value)
        uep.find('.//B_base_cycle').text = str(self.B_base_cycle.value)
        uep.find('.//B_max_cycle').text = str(self.B_max_cycle.value)
        uep.find('.//B_cycle_A').text = str(self.B_cycle_A.value)
        uep.find('.//B_cycle_B').text = str(self.B_cycle_B.value)
        uep.find('.//B_cycle_C').text = str(self.B_cycle_C.value)
        uep.find('.//B_cycle_pressure_threshold').text = str(self.B_cycle_pressure_threshold.value)
        uep.find('.//B_base_death').text = str(self.B_base_death.value)
        uep.find('.//B_max_death').text = str(self.B_max_death.value)
        uep.find('.//B_death_A').text = str(self.B_death_A.value)
        uep.find('.//B_death_B').text = str(self.B_death_B.value)
        uep.find('.//B_death_C').text = str(self.B_death_C.value)
        uep.find('.//B_death_R').text = str(self.B_death_R.value)
        uep.find('.//B_apoptosis_pressure_threshold').text = str(self.B_apoptosis_pressure_threshold.value)
        uep.find('.//B_necrosis_threshold').text = str(self.B_necrosis_threshold.value)
        uep.find('.//B_base_speed').text = str(self.B_base_speed.value)
        uep.find('.//B_max_speed').text = str(self.B_max_speed.value)
        uep.find('.//B_speed_A').text = str(self.B_speed_A.value)
        uep.find('.//B_speed_B').text = str(self.B_speed_B.value)
        uep.find('.//B_speed_C').text = str(self.B_speed_C.value)
        uep.find('.//B_speed_R').text = str(self.B_speed_R.value)
        uep.find('.//B_base_secretion').text = str(self.B_base_secretion.value)
        uep.find('.//B_max_secretion').text = str(self.B_max_secretion.value)
        uep.find('.//B_signal_A').text = str(self.B_signal_A.value)
        uep.find('.//B_signal_B').text = str(self.B_signal_B.value)
        uep.find('.//B_signal_C').text = str(self.B_signal_C.value)
        uep.find('.//B_signal_R').text = str(self.B_signal_R.value)
        uep.find('.//C_base_cycle').text = str(self.C_base_cycle.value)
        uep.find('.//C_max_cycle').text = str(self.C_max_cycle.value)
        uep.find('.//C_cycle_A').text = str(self.C_cycle_A.value)
        uep.find('.//C_cycle_B').text = str(self.C_cycle_B.value)
        uep.find('.//C_cycle_C').text = str(self.C_cycle_C.value)
        uep.find('.//C_cycle_pressure_threshold').text = str(self.C_cycle_pressure_threshold.value)
        uep.find('.//C_base_death').text = str(self.C_base_death.value)
        uep.find('.//C_max_death').text = str(self.C_max_death.value)
        uep.find('.//C_death_A').text = str(self.C_death_A.value)
        uep.find('.//C_death_B').text = str(self.C_death_B.value)
        uep.find('.//C_death_C').text = str(self.C_death_C.value)
        uep.find('.//C_death_R').text = str(self.C_death_R.value)
        uep.find('.//C_apoptosis_pressure_threshold').text = str(self.C_apoptosis_pressure_threshold.value)
        uep.find('.//C_necrosis_threshold').text = str(self.C_necrosis_threshold.value)
        uep.find('.//C_base_speed').text = str(self.C_base_speed.value)
        uep.find('.//C_max_speed').text = str(self.C_max_speed.value)
        uep.find('.//C_speed_A').text = str(self.C_speed_A.value)
        uep.find('.//C_speed_B').text = str(self.C_speed_B.value)
        uep.find('.//C_speed_C').text = str(self.C_speed_C.value)
        uep.find('.//C_speed_R').text = str(self.C_speed_R.value)
        uep.find('.//C_base_secretion').text = str(self.C_base_secretion.value)
        uep.find('.//C_max_secretion').text = str(self.C_max_secretion.value)
        uep.find('.//C_signal_A').text = str(self.C_signal_A.value)
        uep.find('.//C_signal_B').text = str(self.C_signal_B.value)
        uep.find('.//C_signal_C').text = str(self.C_signal_C.value)
        uep.find('.//C_signal_R').text = str(self.C_signal_R.value)
        uep.find('.//dt_diffusion').text = str(self.dt_diffusion.value)
        uep.find('.//dt_mechanics').text = str(self.dt_mechanics.value)
        uep.find('.//dt_phenotype').text = str(self.dt_phenotype.value)
