 
# This file is auto-generated from a Python script that parses a PhysiCell configuration (.xml) file.
#
# Edit at your own risk.
#
import os
from ipywidgets import Label,Text,Checkbox,Button,HBox,VBox,FloatText,IntText,BoundedIntText,BoundedFloatText,Layout,Box,Dropdown
    
class CellTypesTab(object):

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
        widget_layout_long = {'width': '20%'}
        units_button_layout ={'width':'15%'}
        desc_button_layout={'width':'45%'}
        divider_button_layout={'width':'40%'}
        divider_button_layout={'width':'60%'}
        box_layout = Layout(display='flex', flex_flow='row', align_items='stretch', width='100%')

        self.cell_type_dropdown = Dropdown(description='Cell type:',)
        self.cell_type_dropdown.style = {'description_width': '%sch' % str(len(self.cell_type_dropdown.description) + 1)}

        cell_type_names_layout={'width':'30%'}
        cell_type_names_style={'description_width':'initial'}
        self.parent_name = Text(value='None',description='inherits properties from parent type:',disabled=True, style=cell_type_names_style, layout=cell_type_names_layout)

        explain_inheritance = Label(value='    This cell line inherits its properties from its parent type. Any settings below override those inherited properties.')  # , style=cell_type_names_style, layout=cell_type_names_layout)

        self.cell_type_parent_row = HBox([self.cell_type_dropdown, self.parent_name])
        self.cell_type_parent_dict = {}

        self.cell_type_dict = {}
        self.cell_type_dict['default'] = 'default'
        self.cell_type_dict['A'] = 'A'
        self.cell_type_dict['B'] = 'B'
        self.cell_type_dict['C'] = 'C'
        self.cell_type_dropdown.options = self.cell_type_dict

        self.cell_type_dropdown.observe(self.cell_type_cb)

        self.cell_type_parent_dict['default'] = 'None'
        self.cell_type_parent_dict['A'] = 'default'
        self.cell_type_parent_dict['B'] = 'default'
        self.cell_type_parent_dict['C'] = 'default'


        self.cell_def_vboxes = []
        #  >>>>>>>>>>>>>>>>> <cell_definition> = default
        #  ------------------------- 
        div_row1 = Button(description='phenotype:cycle (model: live; code=5)', disabled=True, layout=divider_button_layout)
        div_row1.style.button_color = 'orange'
        name_btn = Button(description='Phase 0 -> Phase 0 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float0 = FloatText(value='0.00072', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float0, units_btn, ]
        box0 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row2 = Button(description='phenotype:death', disabled=True, layout=divider_button_layout)
        div_row2.style.button_color = 'orange'
        death_model1 = Button(description='model: apoptosis', disabled=True, layout={'width':'30%'})
        death_model1.style.button_color = '#ffde6b'
        name_btn = Button(description='death rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float1 = FloatText(value='5.31667e-05', step='1e-05', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float1, units_btn, ]
        box1 = Box(children=row, layout=box_layout)

        name_btn = Button(description='unlysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float2 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float2, units_btn, ]
        box2 = Box(children=row, layout=box_layout)

        name_btn = Button(description='lysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float3 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float3, units_btn, ]
        box3 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cytoplasmic_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float4 = FloatText(value='1.66667e-02', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float4, units_btn, ]
        box4 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float5 = FloatText(value='5.83333e-03', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float5, units_btn, ]
        box5 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcification_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float6 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float6, units_btn, ]
        box6 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_rupture_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float7 = FloatText(value='2.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float7, units_btn, ]
        box7 = Box(children=row, layout=box_layout)

        death_model2 = Button(description='model: necrosis', disabled=True, layout={'width':'30%'})
        death_model2.style.button_color = '#ffde6b'
        name_btn = Button(description='death rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float8 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float8, units_btn, ]
        box8 = Box(children=row, layout=box_layout)

        name_btn = Button(description='unlysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float9 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float9, units_btn, ]
        box9 = Box(children=row, layout=box_layout)

        name_btn = Button(description='lysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float10 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float10, units_btn, ]
        box10 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cytoplasmic_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float11 = FloatText(value='1.66667e-02', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float11, units_btn, ]
        box11 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float12 = FloatText(value='5.83333e-03', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float12, units_btn, ]
        box12 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcification_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float13 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float13, units_btn, ]
        box13 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_rupture_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float14 = FloatText(value='2.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float14, units_btn, ]
        box14 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row3 = Button(description='phenotype:volume', disabled=True, layout=divider_button_layout)
        div_row3.style.button_color = 'orange'
        name_btn = Button(description='total', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float15 = FloatText(value='2494', step='100', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float15, units_btn, ]
        box15 = Box(children=row, layout=box_layout)

        name_btn = Button(description='fluid_fraction', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float16 = FloatText(value='0.75', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float16, units_btn, ]
        box16 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float17 = FloatText(value='540', step='10', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float17, units_btn, ]
        box17 = Box(children=row, layout=box_layout)

        name_btn = Button(description='fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float18 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float18, units_btn, ]
        box18 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cytoplasmic_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float19 = FloatText(value='0.0045', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float19, units_btn, ]
        box19 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float20 = FloatText(value='0.0055', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float20, units_btn, ]
        box20 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcified_fraction', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float21 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float21, units_btn, ]
        box21 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcification_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float22 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float22, units_btn, ]
        box22 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_rupture_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float23 = FloatText(value='2.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float23, units_btn, ]
        box23 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row4 = Button(description='phenotype:mechanics', disabled=True, layout=divider_button_layout)
        div_row4.style.button_color = 'orange'
        name_btn = Button(description='cell_cell_adhesion_strength', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float24 = FloatText(value='0.4', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float24, units_btn, ]
        box24 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cell_cell_repulsion_strength', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float25 = FloatText(value='10.0', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float25, units_btn, ]
        box25 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_maximum_adhesion_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float26 = FloatText(value='1.25', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float26, units_btn, ]
        box26 = Box(children=row, layout=box_layout)

        self.bool0 = Checkbox(description='enabled', value=False,layout=name_button_layout)
        name_btn = Button(description='set_relative_equilibrium_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float27 = FloatText(value='1.8', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [self.bool0, name_btn, self.float27, units_btn, ]
        box27 = Box(children=row, layout=box_layout)

        self.bool1 = Checkbox(description='enabled', value=False,layout=name_button_layout)
        name_btn = Button(description='set_absolute_equilibrium_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float28 = FloatText(value='15.12', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [self.bool1, name_btn, self.float28, units_btn, ]
        box28 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row5 = Button(description='phenotype:motility', disabled=True, layout=divider_button_layout)
        div_row5.style.button_color = 'orange'

        name_btn = Button(description='speed', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float29 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='micron/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float29, units_btn]
        box29 = Box(children=row, layout=box_layout)

        name_btn = Button(description='persistence_time', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float30 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float30, units_btn]
        box30 = Box(children=row, layout=box_layout)

        name_btn = Button(description='migration_bias', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float31 = FloatText(value='.5', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float31, units_btn]
        box31 = Box(children=row, layout=box_layout)
        self.bool2 = Checkbox(description='enabled', value=False,layout=name_button_layout)
        self.bool3 = Checkbox(description='use_2D', value=True,layout=name_button_layout)

        chemotaxis_btn = Button(description='chemotaxis', disabled=True, layout={'width':'30%'})
        chemotaxis_btn.style.button_color = '#ffde6b'

        self.bool4 = Checkbox(description='enabled', value=False,layout=name_button_layout)

        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.chemotaxis_substrate1 = Text(value='resource', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.chemotaxis_substrate1]
        box32 = Box(children=row, layout=box_layout)

        name_btn = Button(description='direction', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.chemotaxis_direction1 = Text(value='1', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.chemotaxis_direction1]
        box33 = Box(children=row, layout=box_layout)
        #  ------------------------- 
        div_row6 = Button(description='phenotype:secretion', disabled=True, layout=divider_button_layout)
        div_row6.style.button_color = 'orange'
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.text0 = Text(value='resource', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text0]
        box34 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float32 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float32, units_btn]
        box35 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float33 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='substrate density', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float33, units_btn]
        box36 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uptake_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float34 = FloatText(value='10', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float34, units_btn]
        box37 = Box(children=row, layout=box_layout)
        name_btn = Button(description='net_export_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float35 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='total substrate/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float35, units_btn]
        box38 = Box(children=row, layout=box_layout)
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.text1 = Text(value='signal A', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text1]
        box39 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float36 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float36, units_btn]
        box40 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float37 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='substrate density', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float37, units_btn]
        box41 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uptake_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float38 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float38, units_btn]
        box42 = Box(children=row, layout=box_layout)
        name_btn = Button(description='net_export_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float39 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='total substrate/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float39, units_btn]
        box43 = Box(children=row, layout=box_layout)
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.text2 = Text(value='signal B', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text2]
        box44 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float40 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float40, units_btn]
        box45 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float41 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='substrate density', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float41, units_btn]
        box46 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uptake_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float42 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float42, units_btn]
        box47 = Box(children=row, layout=box_layout)
        name_btn = Button(description='net_export_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float43 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='total substrate/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float43, units_btn]
        box48 = Box(children=row, layout=box_layout)
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.text3 = Text(value='signal C', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text3]
        box49 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float44 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float44, units_btn]
        box50 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_target', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float45 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='substrate density', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float45, units_btn]
        box51 = Box(children=row, layout=box_layout)
        name_btn = Button(description='uptake_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float46 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float46, units_btn]
        box52 = Box(children=row, layout=box_layout)
        name_btn = Button(description='net_export_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float47 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='total substrate/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float47, units_btn]
        box53 = Box(children=row, layout=box_layout)
        #  ------------------------- 
        div_row7 = Button(description='phenotype:molecular', disabled=True, layout=divider_button_layout)
        div_row7.style.button_color = 'orange'

#      ================== <custom_data>, if present ==================

        div_row8 = Button(description='Custom Data',disabled=True, layout=divider_button_layout)
        div_row8.style.button_color = 'cyan'
        name_btn = Button(description='relative_sated_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float48 = FloatText(value='1.5', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float48, units_btn, description_btn] 

        box54 = Box(children=row, layout=box_layout)

        self.cell_def_vbox0 = VBox([
          div_row1, box0, div_row2, death_model1,box1, box2, box3, box4, box5, box6, box7, death_model2,box8, box9, box10, box11, box12, box13, box14, div_row3, box15, box16, box17, box18, box19, box20, box21, box22, box23, div_row4, box24, box25, box26, box27, box28, div_row5, box29,box30,box31,self.bool2,self.bool3,chemotaxis_btn,self.bool4,box32,box33,div_row6, box34,box35,box36,box37,box38,box39,box40,box41,box42,box43,box44,box45,box46,box47,box48,box49,box50,box51,box52,box53,div_row7, div_row8,          box54,
        ])
        # ------------------------------------------
        self.cell_def_vboxes.append(self.cell_def_vbox0)

        #  >>>>>>>>>>>>>>>>> <cell_definition> = A
        #  ------------------------- 
        div_row9 = Button(description='phenotype:cycle (model: live; code=5)', disabled=True, layout=divider_button_layout)
        div_row9.style.button_color = 'orange'
        name_btn = Button(description='Phase 0 -> Phase 0 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float49 = FloatText(value='0.00072', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float49, units_btn, ]
        box55 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row10 = Button(description='phenotype:death', disabled=True, layout=divider_button_layout)
        div_row10.style.button_color = 'orange'
        death_model1 = Button(description='model: apoptosis', disabled=True, layout={'width':'30%'})
        death_model1.style.button_color = '#ffde6b'
        name_btn = Button(description='death rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float50 = FloatText(value='0.00001', step='1e-06', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float50, units_btn, ]
        box56 = Box(children=row, layout=box_layout)

        death_model2 = Button(description='model: necrosis', disabled=True, layout={'width':'30%'})
        death_model2.style.button_color = '#ffde6b'
        name_btn = Button(description='death rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float51 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float51, units_btn, ]
        box57 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row11 = Button(description='phenotype:volume', disabled=True, layout=divider_button_layout)
        div_row11.style.button_color = 'orange'
        #  ------------------------- 
        div_row12 = Button(description='phenotype:mechanics', disabled=True, layout=divider_button_layout)
        div_row12.style.button_color = 'orange'
        name_btn = Button(description='cell_cell_adhesion_strength', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float52 = FloatText(value='0.4', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float52, units_btn, ]
        box58 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cell_cell_repulsion_strength', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float53 = FloatText(value='10.0', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float53, units_btn, ]
        box59 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_maximum_adhesion_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float54 = FloatText(value='1.5', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float54, units_btn, ]
        box60 = Box(children=row, layout=box_layout)

        self.bool5 = Checkbox(description='enabled', value=True,layout=name_button_layout)
        name_btn = Button(description='set_relative_equilibrium_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float55 = FloatText(value='1.8', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [self.bool5, name_btn, self.float55, units_btn, ]
        box61 = Box(children=row, layout=box_layout)

        self.bool6 = Checkbox(description='enabled', value=False,layout=name_button_layout)
        name_btn = Button(description='set_absolute_equilibrium_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float56 = FloatText(value='15.12', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [self.bool6, name_btn, self.float56, units_btn, ]
        box62 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row13 = Button(description='phenotype:motility', disabled=True, layout=divider_button_layout)
        div_row13.style.button_color = 'orange'

        name_btn = Button(description='speed', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float57 = FloatText(value='0.25', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='micron/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float57, units_btn]
        box63 = Box(children=row, layout=box_layout)

        name_btn = Button(description='persistence_time', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float58 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float58, units_btn]
        box64 = Box(children=row, layout=box_layout)

        name_btn = Button(description='migration_bias', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float59 = FloatText(value='.5', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float59, units_btn]
        box65 = Box(children=row, layout=box_layout)
        self.bool7 = Checkbox(description='enabled', value=False,layout=name_button_layout)

        chemotaxis_btn = Button(description='chemotaxis', disabled=True, layout={'width':'30%'})
        chemotaxis_btn.style.button_color = '#ffde6b'

        self.bool8 = Checkbox(description='enabled', value=False,layout=name_button_layout)

        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.chemotaxis_substrate2 = Text(value='signal B', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.chemotaxis_substrate2]
        box66 = Box(children=row, layout=box_layout)

        name_btn = Button(description='direction', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.chemotaxis_direction2 = Text(value='1', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.chemotaxis_direction2]
        box67 = Box(children=row, layout=box_layout)
        #  ------------------------- 
        div_row14 = Button(description='phenotype:secretion', disabled=True, layout=divider_button_layout)
        div_row14.style.button_color = 'orange'
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.text4 = Text(value='signal A', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text4]
        box68 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float60 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float60, units_btn]
        box69 = Box(children=row, layout=box_layout)
        #  ------------------------- 
        div_row15 = Button(description='phenotype:molecular', disabled=True, layout=divider_button_layout)
        div_row15.style.button_color = 'orange'

#      ================== <custom_data>, if present ==================

        self.cell_def_vbox1 = VBox([
          div_row9, box55, div_row10, death_model1,box56, death_model2,box57, div_row11, div_row12, box58, box59, box60, box61, box62, div_row13, box63,box64,box65,self.bool7,chemotaxis_btn,self.bool8,box66,box67,div_row14, box68,box69,div_row15,         ])
        # ------------------------------------------
        self.cell_def_vboxes.append(self.cell_def_vbox1)

        #  >>>>>>>>>>>>>>>>> <cell_definition> = B
        #  ------------------------- 
        div_row16 = Button(description='phenotype:cycle (model: live; code=5)', disabled=True, layout=divider_button_layout)
        div_row16.style.button_color = 'orange'
        name_btn = Button(description='Phase 0 -> Phase 0 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float61 = FloatText(value='0.00072', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float61, units_btn, ]
        box70 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row17 = Button(description='phenotype:death', disabled=True, layout=divider_button_layout)
        div_row17.style.button_color = 'orange'
        death_model1 = Button(description='model: apoptosis', disabled=True, layout={'width':'30%'})
        death_model1.style.button_color = '#ffde6b'
        name_btn = Button(description='death rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float62 = FloatText(value='5.31667e-05', step='1e-05', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float62, units_btn, ]
        box71 = Box(children=row, layout=box_layout)

        death_model2 = Button(description='model: necrosis', disabled=True, layout={'width':'30%'})
        death_model2.style.button_color = '#ffde6b'
        name_btn = Button(description='death rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float63 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float63, units_btn, ]
        box72 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row18 = Button(description='phenotype:volume', disabled=True, layout=divider_button_layout)
        div_row18.style.button_color = 'orange'
        #  ------------------------- 
        div_row19 = Button(description='phenotype:mechanics', disabled=True, layout=divider_button_layout)
        div_row19.style.button_color = 'orange'
        name_btn = Button(description='cell_cell_adhesion_strength', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float64 = FloatText(value='0.4', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float64, units_btn, ]
        box73 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cell_cell_repulsion_strength', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float65 = FloatText(value='10.0', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float65, units_btn, ]
        box74 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_maximum_adhesion_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float66 = FloatText(value='1.25', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float66, units_btn, ]
        box75 = Box(children=row, layout=box_layout)

        self.bool9 = Checkbox(description='enabled', value=False,layout=name_button_layout)
        name_btn = Button(description='set_relative_equilibrium_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float67 = FloatText(value='1.8', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [self.bool9, name_btn, self.float67, units_btn, ]
        box76 = Box(children=row, layout=box_layout)

        self.bool10 = Checkbox(description='enabled', value=False,layout=name_button_layout)
        name_btn = Button(description='set_absolute_equilibrium_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float68 = FloatText(value='15.12', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [self.bool10, name_btn, self.float68, units_btn, ]
        box77 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row20 = Button(description='phenotype:motility', disabled=True, layout=divider_button_layout)
        div_row20.style.button_color = 'orange'

        name_btn = Button(description='speed', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float69 = FloatText(value='0.25', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='micron/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float69, units_btn]
        box78 = Box(children=row, layout=box_layout)

        name_btn = Button(description='persistence_time', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float70 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float70, units_btn]
        box79 = Box(children=row, layout=box_layout)

        name_btn = Button(description='migration_bias', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float71 = FloatText(value='.5', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float71, units_btn]
        box80 = Box(children=row, layout=box_layout)
        self.bool11 = Checkbox(description='enabled', value=False,layout=name_button_layout)

        chemotaxis_btn = Button(description='chemotaxis', disabled=True, layout={'width':'30%'})
        chemotaxis_btn.style.button_color = '#ffde6b'

        self.bool12 = Checkbox(description='enabled', value=False,layout=name_button_layout)

        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.chemotaxis_substrate3 = Text(value='signal C', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.chemotaxis_substrate3]
        box81 = Box(children=row, layout=box_layout)

        name_btn = Button(description='direction', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.chemotaxis_direction3 = Text(value='1', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.chemotaxis_direction3]
        box82 = Box(children=row, layout=box_layout)
        #  ------------------------- 
        div_row21 = Button(description='phenotype:secretion', disabled=True, layout=divider_button_layout)
        div_row21.style.button_color = 'orange'
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.text5 = Text(value='signal B', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text5]
        box83 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float72 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float72, units_btn]
        box84 = Box(children=row, layout=box_layout)
        #  ------------------------- 
        div_row22 = Button(description='phenotype:molecular', disabled=True, layout=divider_button_layout)
        div_row22.style.button_color = 'orange'

#      ================== <custom_data>, if present ==================

        self.cell_def_vbox2 = VBox([
          div_row16, box70, div_row17, death_model1,box71, death_model2,box72, div_row18, div_row19, box73, box74, box75, box76, box77, div_row20, box78,box79,box80,self.bool11,chemotaxis_btn,self.bool12,box81,box82,div_row21, box83,box84,div_row22,         ])
        # ------------------------------------------
        self.cell_def_vboxes.append(self.cell_def_vbox2)

        #  >>>>>>>>>>>>>>>>> <cell_definition> = C
        #  ------------------------- 
        div_row23 = Button(description='phenotype:cycle (model: live; code=5)', disabled=True, layout=divider_button_layout)
        div_row23.style.button_color = 'orange'
        name_btn = Button(description='Phase 0 -> Phase 0 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float73 = FloatText(value='0.00072', step='0.0001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float73, units_btn, ]
        box85 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row24 = Button(description='phenotype:death', disabled=True, layout=divider_button_layout)
        div_row24.style.button_color = 'orange'
        death_model1 = Button(description='model: apoptosis', disabled=True, layout={'width':'30%'})
        death_model1.style.button_color = '#ffde6b'
        name_btn = Button(description='death rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float74 = FloatText(value='5.31667e-05', step='1e-05', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float74, units_btn, ]
        box86 = Box(children=row, layout=box_layout)

        death_model2 = Button(description='model: necrosis', disabled=True, layout={'width':'30%'})
        death_model2.style.button_color = '#ffde6b'
        name_btn = Button(description='death rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float75 = FloatText(value='0.01', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float75, units_btn, ]
        box87 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row25 = Button(description='phenotype:volume', disabled=True, layout=divider_button_layout)
        div_row25.style.button_color = 'orange'
        #  ------------------------- 
        div_row26 = Button(description='phenotype:mechanics', disabled=True, layout=divider_button_layout)
        div_row26.style.button_color = 'orange'
        name_btn = Button(description='cell_cell_adhesion_strength', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float76 = FloatText(value='0.4', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float76, units_btn, ]
        box88 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cell_cell_repulsion_strength', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float77 = FloatText(value='10.0', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float77, units_btn, ]
        box89 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_maximum_adhesion_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float78 = FloatText(value='1.25', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float78, units_btn, ]
        box90 = Box(children=row, layout=box_layout)

        self.bool13 = Checkbox(description='enabled', value=False,layout=name_button_layout)
        name_btn = Button(description='set_relative_equilibrium_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float79 = FloatText(value='1.8', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [self.bool13, name_btn, self.float79, units_btn, ]
        box91 = Box(children=row, layout=box_layout)

        self.bool14 = Checkbox(description='enabled', value=False,layout=name_button_layout)
        name_btn = Button(description='set_absolute_equilibrium_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float80 = FloatText(value='15.12', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [self.bool14, name_btn, self.float80, units_btn, ]
        box92 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row27 = Button(description='phenotype:motility', disabled=True, layout=divider_button_layout)
        div_row27.style.button_color = 'orange'

        name_btn = Button(description='speed', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float81 = FloatText(value='0.25', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='micron/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float81, units_btn]
        box93 = Box(children=row, layout=box_layout)

        name_btn = Button(description='persistence_time', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float82 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float82, units_btn]
        box94 = Box(children=row, layout=box_layout)

        name_btn = Button(description='migration_bias', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float83 = FloatText(value='.5', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float83, units_btn]
        box95 = Box(children=row, layout=box_layout)
        self.bool15 = Checkbox(description='enabled', value=False,layout=name_button_layout)

        chemotaxis_btn = Button(description='chemotaxis', disabled=True, layout={'width':'30%'})
        chemotaxis_btn.style.button_color = '#ffde6b'

        self.bool16 = Checkbox(description='enabled', value=False,layout=name_button_layout)

        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.chemotaxis_substrate4 = Text(value='signal A', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.chemotaxis_substrate4]
        box96 = Box(children=row, layout=box_layout)

        name_btn = Button(description='direction', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.chemotaxis_direction4 = Text(value='1', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.chemotaxis_direction4]
        box97 = Box(children=row, layout=box_layout)
        #  ------------------------- 
        div_row28 = Button(description='phenotype:secretion', disabled=True, layout=divider_button_layout)
        div_row28.style.button_color = 'orange'
        name_btn = Button(description='substrate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.text6 = Text(value='signal C', disabled=False, style=style, layout=widget_layout_long)
        row = [name_btn, self.text6]
        box98 = Box(children=row, layout=box_layout)
        name_btn = Button(description='secretion_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float84 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float84, units_btn]
        box99 = Box(children=row, layout=box_layout)
        #  ------------------------- 
        div_row29 = Button(description='phenotype:molecular', disabled=True, layout=divider_button_layout)
        div_row29.style.button_color = 'orange'

#      ================== <custom_data>, if present ==================

        self.cell_def_vbox3 = VBox([
          div_row23, box85, div_row24, death_model1,box86, death_model2,box87, div_row25, div_row26, box88, box89, box90, box91, box92, div_row27, box93,box94,box95,self.bool15,chemotaxis_btn,self.bool16,box96,box97,div_row28, box98,box99,div_row29,         ])
        # ------------------------------------------
        self.cell_def_vboxes.append(self.cell_def_vbox3)



        row = [name_btn, self.float84, units_btn]
        box99 = Box(children=row, layout=box_layout)

        self.tab = VBox([
          self.cell_type_parent_row, explain_inheritance, 
self.cell_def_vbox0, self.cell_def_vbox1, self.cell_def_vbox2, self.cell_def_vbox3,         ])
    #------------------------------
    def cell_type_cb(self, change):
        if change['type'] == 'change' and change['name'] == 'value':
            # print("changed to %s" % change['new'])
            self.parent_name.value = self.cell_type_parent_dict[change['new']]
            idx_selected = list(self.cell_type_parent_dict.keys()).index(change['new'])
            # print('index=',idx_selected)
            # self.vbox1.layout.visibility = 'hidden'  # vs. visible
            # self.vbox1.layout.visibility = None 

            # There's probably a better way to do this, but for now,
            # we hide all vboxes containing the widgets for the different cell defs
            # and only display the contents of the selected one.
            for vb in self.cell_def_vboxes:
                vb.layout.display = 'none'   # vs. 'contents'
            self.cell_def_vboxes[idx_selected].layout.display = 'contents'   # vs. 'contents'


    #------------------------------
    def display_cell_type_default(self):
        # print("display_cell_type_default():")
        #print("    self.cell_type_parent_dict = ",self.cell_type_parent_dict)

        # There's probably a better way to do this, but for now,
        # we hide all vboxes containing the widgets for the different cell defs
        # and only display the contents of 'default'
        for vb in self.cell_def_vboxes:
            vb.layout.display = 'none'   # vs. 'contents'
        self.cell_def_vboxes[0].layout.display = 'contents'


    # Populate the GUI widgets with values from the XML
    def fill_gui(self, xml_root):
        uep = xml_root.find('.//cell_definitions')  # find unique entry point

        # ------------------ cell_definition: default
        # ---------  cycle (live)
        self.float0.value = float(uep.find('.//cell_definition[1]//phenotype//cycle//phase_transition_rates//rate[1]').text)
        # ---------  death 
        self.float1.value = float(uep.find('.//cell_definition[1]//phenotype//death//model[1]//death_rate').text)
        self.float2.value = float(uep.find('.//cell_definition[1]//phenotype//death//model[1]//parameters//unlysed_fluid_change_rate').text)
        self.float3.value = float(uep.find('.//cell_definition[1]//phenotype//death//model[1]//parameters//lysed_fluid_change_rate').text)
        self.float4.value = float(uep.find('.//cell_definition[1]//phenotype//death//model[1]//parameters//cytoplasmic_biomass_change_rate').text)
        self.float5.value = float(uep.find('.//cell_definition[1]//phenotype//death//model[1]//parameters//nuclear_biomass_change_rate').text)
        self.float6.value = float(uep.find('.//cell_definition[1]//phenotype//death//model[1]//parameters//calcification_rate').text)
        self.float7.value = float(uep.find('.//cell_definition[1]//phenotype//death//model[1]//parameters//relative_rupture_volume').text)
        self.float8.value = float(uep.find('.//cell_definition[1]//phenotype//death//model[2]//death_rate').text)
        self.float9.value = float(uep.find('.//cell_definition[1]//phenotype//death//model[2]//parameters//unlysed_fluid_change_rate').text)
        self.float10.value = float(uep.find('.//cell_definition[1]//phenotype//death//model[2]//parameters//lysed_fluid_change_rate').text)
        self.float11.value = float(uep.find('.//cell_definition[1]//phenotype//death//model[2]//parameters//cytoplasmic_biomass_change_rate').text)
        self.float12.value = float(uep.find('.//cell_definition[1]//phenotype//death//model[2]//parameters//nuclear_biomass_change_rate').text)
        self.float13.value = float(uep.find('.//cell_definition[1]//phenotype//death//model[2]//parameters//calcification_rate').text)
        self.float14.value = float(uep.find('.//cell_definition[1]//phenotype//death//model[2]//parameters//relative_rupture_volume').text)
        # ---------  volume 
        self.float15.value = float(uep.find('.//cell_definition[1]//phenotype//volume//total').text)
        self.float16.value = float(uep.find('.//cell_definition[1]//phenotype//volume//fluid_fraction').text)
        self.float17.value = float(uep.find('.//cell_definition[1]//phenotype//volume//nuclear').text)
        self.float18.value = float(uep.find('.//cell_definition[1]//phenotype//volume//fluid_change_rate').text)
        self.float19.value = float(uep.find('.//cell_definition[1]//phenotype//volume//cytoplasmic_biomass_change_rate').text)
        self.float20.value = float(uep.find('.//cell_definition[1]//phenotype//volume//nuclear_biomass_change_rate').text)
        self.float21.value = float(uep.find('.//cell_definition[1]//phenotype//volume//calcified_fraction').text)
        self.float22.value = float(uep.find('.//cell_definition[1]//phenotype//volume//calcification_rate').text)
        self.float23.value = float(uep.find('.//cell_definition[1]//phenotype//volume//relative_rupture_volume').text)
        # ---------  mechanics 
        self.float24.value = float(uep.find('.//cell_definition[1]//phenotype//mechanics//cell_cell_adhesion_strength').text)
        self.float25.value = float(uep.find('.//cell_definition[1]//phenotype//mechanics//cell_cell_repulsion_strength').text)
        self.float26.value = float(uep.find('.//cell_definition[1]//phenotype//mechanics//relative_maximum_adhesion_distance').text)
        self.bool0.value = ('true' == (uep.find('.//cell_definition[1]//phenotype//mechanics//options//set_relative_equilibrium_distance').attrib['enabled'].lower()))
        self.bool1.value = ('true' == (uep.find('.//cell_definition[1]//phenotype//mechanics//options//set_absolute_equilibrium_distance').attrib['enabled'].lower()))
        # ---------  motility 
        self.float29.value = float(uep.find('.//cell_definition[1]//phenotype//motility//speed').text)
        self.float30.value = float(uep.find('.//cell_definition[1]//phenotype//motility//persistence_time').text)
        self.float31.value = float(uep.find('.//cell_definition[1]//phenotype//motility//migration_bias').text)
        self.bool2.value = ('true' == (uep.find('.//cell_definition[1]//phenotype//motility//options//enabled').text.lower()))
        self.bool3.value = ('true' == (uep.find('.//cell_definition[1]//phenotype//motility//options//use_2D').text.lower()))
        self.bool4.value = ('true' == (uep.find('.//cell_definition[1]//phenotype//motility//options//chemotaxis//enabled').text.lower()))
        self.chemotaxis_substrate1.value = uep.find('.//cell_definition[1]//phenotype//motility//options//chemotaxis//substrate').text
        self.chemotaxis_direction1.value = uep.find('.//cell_definition[1]//phenotype//motility//options//chemotaxis//direction').text
        # ---------  secretion 
        self.text0.value = uep.find('.//cell_definition[1]//phenotype//secretion//substrate[1]').attrib['name']
        self.float32.value = float(uep.find('.//cell_definition[1]//phenotype//secretion//substrate[1]//secretion_rate').text)
        self.float33.value = float(uep.find('.//cell_definition[1]//phenotype//secretion//substrate[1]//secretion_target').text)
        self.float34.value = float(uep.find('.//cell_definition[1]//phenotype//secretion//substrate[1]//uptake_rate').text)
        self.float35.value = float(uep.find('.//cell_definition[1]//phenotype//secretion//substrate[1]//net_export_rate').text)
        self.text1.value = uep.find('.//cell_definition[1]//phenotype//secretion//substrate[2]').attrib['name']
        self.float36.value = float(uep.find('.//cell_definition[1]//phenotype//secretion//substrate[2]//secretion_rate').text)
        self.float37.value = float(uep.find('.//cell_definition[1]//phenotype//secretion//substrate[2]//secretion_target').text)
        self.float38.value = float(uep.find('.//cell_definition[1]//phenotype//secretion//substrate[2]//uptake_rate').text)
        self.float39.value = float(uep.find('.//cell_definition[1]//phenotype//secretion//substrate[2]//net_export_rate').text)
        self.text2.value = uep.find('.//cell_definition[1]//phenotype//secretion//substrate[3]').attrib['name']
        self.float40.value = float(uep.find('.//cell_definition[1]//phenotype//secretion//substrate[3]//secretion_rate').text)
        self.float41.value = float(uep.find('.//cell_definition[1]//phenotype//secretion//substrate[3]//secretion_target').text)
        self.float42.value = float(uep.find('.//cell_definition[1]//phenotype//secretion//substrate[3]//uptake_rate').text)
        self.float43.value = float(uep.find('.//cell_definition[1]//phenotype//secretion//substrate[3]//net_export_rate').text)
        self.text3.value = uep.find('.//cell_definition[1]//phenotype//secretion//substrate[4]').attrib['name']
        self.float44.value = float(uep.find('.//cell_definition[1]//phenotype//secretion//substrate[4]//secretion_rate').text)
        self.float45.value = float(uep.find('.//cell_definition[1]//phenotype//secretion//substrate[4]//secretion_target').text)
        self.float46.value = float(uep.find('.//cell_definition[1]//phenotype//secretion//substrate[4]//uptake_rate').text)
        self.float47.value = float(uep.find('.//cell_definition[1]//phenotype//secretion//substrate[4]//net_export_rate').text)
        # ---------  molecular
        # ------------------ cell_definition: A
        # ---------  cycle (live)
        self.float49.value = float(uep.find('.//cell_definition[2]//phenotype//cycle//phase_transition_rates//rate[1]').text)
        # ---------  death 
        self.float50.value = float(uep.find('.//cell_definition[2]//phenotype//death//model[1]//death_rate').text)
        self.float51.value = float(uep.find('.//cell_definition[2]//phenotype//death//model[2]//death_rate').text)
        # ---------  volume 
        # ---------  mechanics 
        self.float52.value = float(uep.find('.//cell_definition[2]//phenotype//mechanics//cell_cell_adhesion_strength').text)
        self.float53.value = float(uep.find('.//cell_definition[2]//phenotype//mechanics//cell_cell_repulsion_strength').text)
        self.float54.value = float(uep.find('.//cell_definition[2]//phenotype//mechanics//relative_maximum_adhesion_distance').text)
        self.bool5.value = ('true' == (uep.find('.//cell_definition[2]//phenotype//mechanics//options//set_relative_equilibrium_distance').attrib['enabled'].lower()))
        self.bool6.value = ('true' == (uep.find('.//cell_definition[2]//phenotype//mechanics//options//set_absolute_equilibrium_distance').attrib['enabled'].lower()))
        # ---------  motility 
        self.float57.value = float(uep.find('.//cell_definition[2]//phenotype//motility//speed').text)
        self.float58.value = float(uep.find('.//cell_definition[2]//phenotype//motility//persistence_time').text)
        self.float59.value = float(uep.find('.//cell_definition[2]//phenotype//motility//migration_bias').text)
        self.bool7.value = ('true' == (uep.find('.//cell_definition[2]//phenotype//motility//options//enabled').text.lower()))
        self.bool8.value = ('true' == (uep.find('.//cell_definition[2]//phenotype//motility//options//chemotaxis//enabled').text.lower()))
        self.chemotaxis_substrate2.value = uep.find('.//cell_definition[2]//phenotype//motility//options//chemotaxis//substrate').text
        self.chemotaxis_direction2.value = uep.find('.//cell_definition[2]//phenotype//motility//options//chemotaxis//direction').text
        # ---------  secretion 
        self.text4.value = uep.find('.//cell_definition[2]//phenotype//secretion//substrate[1]').attrib['name']
        self.float60.value = float(uep.find('.//cell_definition[2]//phenotype//secretion//substrate[1]//secretion_rate').text)
        # ---------  molecular
        # ------------------ cell_definition: B
        # ---------  cycle (live)
        self.float61.value = float(uep.find('.//cell_definition[3]//phenotype//cycle//phase_transition_rates//rate[1]').text)
        # ---------  death 
        self.float62.value = float(uep.find('.//cell_definition[3]//phenotype//death//model[1]//death_rate').text)
        self.float63.value = float(uep.find('.//cell_definition[3]//phenotype//death//model[2]//death_rate').text)
        # ---------  volume 
        # ---------  mechanics 
        self.float64.value = float(uep.find('.//cell_definition[3]//phenotype//mechanics//cell_cell_adhesion_strength').text)
        self.float65.value = float(uep.find('.//cell_definition[3]//phenotype//mechanics//cell_cell_repulsion_strength').text)
        self.float66.value = float(uep.find('.//cell_definition[3]//phenotype//mechanics//relative_maximum_adhesion_distance').text)
        self.bool9.value = ('true' == (uep.find('.//cell_definition[3]//phenotype//mechanics//options//set_relative_equilibrium_distance').attrib['enabled'].lower()))
        self.bool10.value = ('true' == (uep.find('.//cell_definition[3]//phenotype//mechanics//options//set_absolute_equilibrium_distance').attrib['enabled'].lower()))
        # ---------  motility 
        self.float69.value = float(uep.find('.//cell_definition[3]//phenotype//motility//speed').text)
        self.float70.value = float(uep.find('.//cell_definition[3]//phenotype//motility//persistence_time').text)
        self.float71.value = float(uep.find('.//cell_definition[3]//phenotype//motility//migration_bias').text)
        self.bool11.value = ('true' == (uep.find('.//cell_definition[3]//phenotype//motility//options//enabled').text.lower()))
        self.bool12.value = ('true' == (uep.find('.//cell_definition[3]//phenotype//motility//options//chemotaxis//enabled').text.lower()))
        self.chemotaxis_substrate3.value = uep.find('.//cell_definition[3]//phenotype//motility//options//chemotaxis//substrate').text
        self.chemotaxis_direction3.value = uep.find('.//cell_definition[3]//phenotype//motility//options//chemotaxis//direction').text
        # ---------  secretion 
        self.text5.value = uep.find('.//cell_definition[3]//phenotype//secretion//substrate[1]').attrib['name']
        self.float72.value = float(uep.find('.//cell_definition[3]//phenotype//secretion//substrate[1]//secretion_rate').text)
        # ---------  molecular
        # ------------------ cell_definition: C
        # ---------  cycle (live)
        self.float73.value = float(uep.find('.//cell_definition[4]//phenotype//cycle//phase_transition_rates//rate[1]').text)
        # ---------  death 
        self.float74.value = float(uep.find('.//cell_definition[4]//phenotype//death//model[1]//death_rate').text)
        self.float75.value = float(uep.find('.//cell_definition[4]//phenotype//death//model[2]//death_rate').text)
        # ---------  volume 
        # ---------  mechanics 
        self.float76.value = float(uep.find('.//cell_definition[4]//phenotype//mechanics//cell_cell_adhesion_strength').text)
        self.float77.value = float(uep.find('.//cell_definition[4]//phenotype//mechanics//cell_cell_repulsion_strength').text)
        self.float78.value = float(uep.find('.//cell_definition[4]//phenotype//mechanics//relative_maximum_adhesion_distance').text)
        self.bool13.value = ('true' == (uep.find('.//cell_definition[4]//phenotype//mechanics//options//set_relative_equilibrium_distance').attrib['enabled'].lower()))
        self.bool14.value = ('true' == (uep.find('.//cell_definition[4]//phenotype//mechanics//options//set_absolute_equilibrium_distance').attrib['enabled'].lower()))
        # ---------  motility 
        self.float81.value = float(uep.find('.//cell_definition[4]//phenotype//motility//speed').text)
        self.float82.value = float(uep.find('.//cell_definition[4]//phenotype//motility//persistence_time').text)
        self.float83.value = float(uep.find('.//cell_definition[4]//phenotype//motility//migration_bias').text)
        self.bool15.value = ('true' == (uep.find('.//cell_definition[4]//phenotype//motility//options//enabled').text.lower()))
        self.bool16.value = ('true' == (uep.find('.//cell_definition[4]//phenotype//motility//options//chemotaxis//enabled').text.lower()))
        self.chemotaxis_substrate4.value = uep.find('.//cell_definition[4]//phenotype//motility//options//chemotaxis//substrate').text
        self.chemotaxis_direction4.value = uep.find('.//cell_definition[4]//phenotype//motility//options//chemotaxis//direction').text
        # ---------  secretion 
        self.text6.value = uep.find('.//cell_definition[4]//phenotype//secretion//substrate[1]').attrib['name']
        self.float84.value = float(uep.find('.//cell_definition[4]//phenotype//secretion//substrate[1]//secretion_rate').text)
        # ---------  molecular


    # Read values from the GUI widgets to enable editing XML
    def fill_xml(self, xml_root):
        uep = xml_root.find('.//cell_definitions')  # find unique entry point

        # ------------------ cell_definition: default
        # ---------  cycle (live)
        uep.find('.//cell_definition[1]//phenotype//cycle//phase_transition_rates//rate[1]').text = str(self.float0.value)
        # ---------  death 
        uep.find('.//cell_definition[1]//phenotype//death//model[1]//death_rate').text = str(self.float1.value)
        uep.find('.//cell_definition[1]//phenotype//death//model[1]//parameters//unlysed_fluid_change_rate').text = str(self.float2.value)
        uep.find('.//cell_definition[1]//phenotype//death//model[1]//parameters//lysed_fluid_change_rate').text = str(self.float3.value)
        uep.find('.//cell_definition[1]//phenotype//death//model[1]//parameters//cytoplasmic_biomass_change_rate').text = str(self.float4.value)
        uep.find('.//cell_definition[1]//phenotype//death//model[1]//parameters//nuclear_biomass_change_rate').text = str(self.float5.value)
        uep.find('.//cell_definition[1]//phenotype//death//model[1]//parameters//calcification_rate').text = str(self.float6.value)
        uep.find('.//cell_definition[1]//phenotype//death//model[1]//parameters//relative_rupture_volume').text = str(self.float7.value)
        uep.find('.//cell_definition[1]//phenotype//death//model[2]//death_rate').text = str(self.float8.value)
        uep.find('.//cell_definition[1]//phenotype//death//model[2]//parameters//unlysed_fluid_change_rate').text = str(self.float9.value)
        uep.find('.//cell_definition[1]//phenotype//death//model[2]//parameters//lysed_fluid_change_rate').text = str(self.float10.value)
        uep.find('.//cell_definition[1]//phenotype//death//model[2]//parameters//cytoplasmic_biomass_change_rate').text = str(self.float11.value)
        uep.find('.//cell_definition[1]//phenotype//death//model[2]//parameters//nuclear_biomass_change_rate').text = str(self.float12.value)
        uep.find('.//cell_definition[1]//phenotype//death//model[2]//parameters//calcification_rate').text = str(self.float13.value)
        uep.find('.//cell_definition[1]//phenotype//death//model[2]//parameters//relative_rupture_volume').text = str(self.float14.value)
        # ---------  volume 
        uep.find('.//cell_definition[1]//phenotype//volume//total').text = str(self.float15.value)
        uep.find('.//cell_definition[1]//phenotype//volume//fluid_fraction').text = str(self.float16.value)
        uep.find('.//cell_definition[1]//phenotype//volume//nuclear').text = str(self.float17.value)
        uep.find('.//cell_definition[1]//phenotype//volume//fluid_change_rate').text = str(self.float18.value)
        uep.find('.//cell_definition[1]//phenotype//volume//cytoplasmic_biomass_change_rate').text = str(self.float19.value)
        uep.find('.//cell_definition[1]//phenotype//volume//nuclear_biomass_change_rate').text = str(self.float20.value)
        uep.find('.//cell_definition[1]//phenotype//volume//calcified_fraction').text = str(self.float21.value)
        uep.find('.//cell_definition[1]//phenotype//volume//calcification_rate').text = str(self.float22.value)
        uep.find('.//cell_definition[1]//phenotype//volume//relative_rupture_volume').text = str(self.float23.value)
        # ---------  mechanics 
        uep.find('.//cell_definition[1]//phenotype//mechanics//cell_cell_adhesion_strength').text = str(self.float24.value)
        uep.find('.//cell_definition[1]//phenotype//mechanics//cell_cell_repulsion_strength').text = str(self.float25.value)
        uep.find('.//cell_definition[1]//phenotype//mechanics//relative_maximum_adhesion_distance').text = str(self.float26.value)
        uep.find('.//cell_definition[1]//phenotype//mechanics//options//set_relative_equilibrium_distance').attrib['enabled'] = str(self.bool0.value)
        uep.find('.//cell_definition[1]//phenotype//mechanics//options//set_absolute_equilibrium_distance').attrib['enabled'] = str(self.bool1.value)
        # ---------  motility 
        uep.find('.//cell_definition[1]//phenotype//motility//speed').text = str(self.float29.value)
        uep.find('.//cell_definition[1]//phenotype//motility//persistence_time').text = str(self.float30.value)
        uep.find('.//cell_definition[1]//phenotype//motility//migration_bias').text = str(self.float31.value)
        uep.find('.//cell_definition[1]//phenotype//motility//options//enabled').text = str(self.bool2.value)
        uep.find('.//cell_definition[1]//phenotype//motility//options//use_2D').text = str(self.bool3.value)
        uep.find('.//cell_definition[1]//phenotype//motility//options//chemotaxis//enabled').text = str(self.bool4.value)
        uep.find('.//cell_definition[1]//phenotype//motility//options//chemotaxis//substrate').text = str(self.chemotaxis_substrate1.value)
        uep.find('.//cell_definition[1]//phenotype//motility//options//chemotaxis//direction').text = str(self.chemotaxis_direction1.value)
        # ---------  secretion 
        uep.find('.//cell_definition[1]//phenotype//secretion//substrate[1]').attrib['name'] = str(self.text0.value)
        uep.find('.//cell_definition[1]//phenotype//secretion//substrate[1]//secretion_rate').text = str(self.float32.value)
        uep.find('.//cell_definition[1]//phenotype//secretion//substrate[1]//secretion_target').text = str(self.float33.value)
        uep.find('.//cell_definition[1]//phenotype//secretion//substrate[1]//uptake_rate').text = str(self.float34.value)
        uep.find('.//cell_definition[1]//phenotype//secretion//substrate[1]//net_export_rate').text = str(self.float35.value)
        uep.find('.//cell_definition[1]//phenotype//secretion//substrate[2]').attrib['name'] = str(self.text1.value)
        uep.find('.//cell_definition[1]//phenotype//secretion//substrate[2]//secretion_rate').text = str(self.float36.value)
        uep.find('.//cell_definition[1]//phenotype//secretion//substrate[2]//secretion_target').text = str(self.float37.value)
        uep.find('.//cell_definition[1]//phenotype//secretion//substrate[2]//uptake_rate').text = str(self.float38.value)
        uep.find('.//cell_definition[1]//phenotype//secretion//substrate[2]//net_export_rate').text = str(self.float39.value)
        uep.find('.//cell_definition[1]//phenotype//secretion//substrate[3]').attrib['name'] = str(self.text2.value)
        uep.find('.//cell_definition[1]//phenotype//secretion//substrate[3]//secretion_rate').text = str(self.float40.value)
        uep.find('.//cell_definition[1]//phenotype//secretion//substrate[3]//secretion_target').text = str(self.float41.value)
        uep.find('.//cell_definition[1]//phenotype//secretion//substrate[3]//uptake_rate').text = str(self.float42.value)
        uep.find('.//cell_definition[1]//phenotype//secretion//substrate[3]//net_export_rate').text = str(self.float43.value)
        uep.find('.//cell_definition[1]//phenotype//secretion//substrate[4]').attrib['name'] = str(self.text3.value)
        uep.find('.//cell_definition[1]//phenotype//secretion//substrate[4]//secretion_rate').text = str(self.float44.value)
        uep.find('.//cell_definition[1]//phenotype//secretion//substrate[4]//secretion_target').text = str(self.float45.value)
        uep.find('.//cell_definition[1]//phenotype//secretion//substrate[4]//uptake_rate').text = str(self.float46.value)
        uep.find('.//cell_definition[1]//phenotype//secretion//substrate[4]//net_export_rate').text = str(self.float47.value)
        # ---------  molecular
        # ------------------ cell_definition: A
        # ---------  cycle (live)
        uep.find('.//cell_definition[2]//phenotype//cycle//phase_transition_rates//rate[1]').text = str(self.float49.value)
        # ---------  death 
        uep.find('.//cell_definition[2]//phenotype//death//model[1]//death_rate').text = str(self.float50.value)
        uep.find('.//cell_definition[2]//phenotype//death//model[2]//death_rate').text = str(self.float51.value)
        # ---------  volume 
        # ---------  mechanics 
        uep.find('.//cell_definition[2]//phenotype//mechanics//cell_cell_adhesion_strength').text = str(self.float52.value)
        uep.find('.//cell_definition[2]//phenotype//mechanics//cell_cell_repulsion_strength').text = str(self.float53.value)
        uep.find('.//cell_definition[2]//phenotype//mechanics//relative_maximum_adhesion_distance').text = str(self.float54.value)
        uep.find('.//cell_definition[2]//phenotype//mechanics//options//set_relative_equilibrium_distance').attrib['enabled'] = str(self.bool5.value)
        uep.find('.//cell_definition[2]//phenotype//mechanics//options//set_absolute_equilibrium_distance').attrib['enabled'] = str(self.bool6.value)
        # ---------  motility 
        uep.find('.//cell_definition[2]//phenotype//motility//speed').text = str(self.float57.value)
        uep.find('.//cell_definition[2]//phenotype//motility//persistence_time').text = str(self.float58.value)
        uep.find('.//cell_definition[2]//phenotype//motility//migration_bias').text = str(self.float59.value)
        uep.find('.//cell_definition[2]//phenotype//motility//options//enabled').text = str(self.bool7.value)
        uep.find('.//cell_definition[2]//phenotype//motility//options//chemotaxis//enabled').text = str(self.bool8.value)
        uep.find('.//cell_definition[2]//phenotype//motility//options//chemotaxis//substrate').text = str(self.chemotaxis_substrate2.value)
        uep.find('.//cell_definition[2]//phenotype//motility//options//chemotaxis//direction').text = str(self.chemotaxis_direction2.value)
        # ---------  secretion 
        uep.find('.//cell_definition[2]//phenotype//secretion//substrate[1]').attrib['name'] = str(self.text4.value)
        uep.find('.//cell_definition[2]//phenotype//secretion//substrate[1]//secretion_rate').text = str(self.float60.value)
        # ---------  molecular
        # ------------------ cell_definition: B
        # ---------  cycle (live)
        uep.find('.//cell_definition[3]//phenotype//cycle//phase_transition_rates//rate[1]').text = str(self.float61.value)
        # ---------  death 
        uep.find('.//cell_definition[3]//phenotype//death//model[1]//death_rate').text = str(self.float62.value)
        uep.find('.//cell_definition[3]//phenotype//death//model[2]//death_rate').text = str(self.float63.value)
        # ---------  volume 
        # ---------  mechanics 
        uep.find('.//cell_definition[3]//phenotype//mechanics//cell_cell_adhesion_strength').text = str(self.float64.value)
        uep.find('.//cell_definition[3]//phenotype//mechanics//cell_cell_repulsion_strength').text = str(self.float65.value)
        uep.find('.//cell_definition[3]//phenotype//mechanics//relative_maximum_adhesion_distance').text = str(self.float66.value)
        uep.find('.//cell_definition[3]//phenotype//mechanics//options//set_relative_equilibrium_distance').attrib['enabled'] = str(self.bool9.value)
        uep.find('.//cell_definition[3]//phenotype//mechanics//options//set_absolute_equilibrium_distance').attrib['enabled'] = str(self.bool10.value)
        # ---------  motility 
        uep.find('.//cell_definition[3]//phenotype//motility//speed').text = str(self.float69.value)
        uep.find('.//cell_definition[3]//phenotype//motility//persistence_time').text = str(self.float70.value)
        uep.find('.//cell_definition[3]//phenotype//motility//migration_bias').text = str(self.float71.value)
        uep.find('.//cell_definition[3]//phenotype//motility//options//enabled').text = str(self.bool11.value)
        uep.find('.//cell_definition[3]//phenotype//motility//options//chemotaxis//enabled').text = str(self.bool12.value)
        uep.find('.//cell_definition[3]//phenotype//motility//options//chemotaxis//substrate').text = str(self.chemotaxis_substrate3.value)
        uep.find('.//cell_definition[3]//phenotype//motility//options//chemotaxis//direction').text = str(self.chemotaxis_direction3.value)
        # ---------  secretion 
        uep.find('.//cell_definition[3]//phenotype//secretion//substrate[1]').attrib['name'] = str(self.text5.value)
        uep.find('.//cell_definition[3]//phenotype//secretion//substrate[1]//secretion_rate').text = str(self.float72.value)
        # ---------  molecular
        # ------------------ cell_definition: C
        # ---------  cycle (live)
        uep.find('.//cell_definition[4]//phenotype//cycle//phase_transition_rates//rate[1]').text = str(self.float73.value)
        # ---------  death 
        uep.find('.//cell_definition[4]//phenotype//death//model[1]//death_rate').text = str(self.float74.value)
        uep.find('.//cell_definition[4]//phenotype//death//model[2]//death_rate').text = str(self.float75.value)
        # ---------  volume 
        # ---------  mechanics 
        uep.find('.//cell_definition[4]//phenotype//mechanics//cell_cell_adhesion_strength').text = str(self.float76.value)
        uep.find('.//cell_definition[4]//phenotype//mechanics//cell_cell_repulsion_strength').text = str(self.float77.value)
        uep.find('.//cell_definition[4]//phenotype//mechanics//relative_maximum_adhesion_distance').text = str(self.float78.value)
        uep.find('.//cell_definition[4]//phenotype//mechanics//options//set_relative_equilibrium_distance').attrib['enabled'] = str(self.bool13.value)
        uep.find('.//cell_definition[4]//phenotype//mechanics//options//set_absolute_equilibrium_distance').attrib['enabled'] = str(self.bool14.value)
        # ---------  motility 
        uep.find('.//cell_definition[4]//phenotype//motility//speed').text = str(self.float81.value)
        uep.find('.//cell_definition[4]//phenotype//motility//persistence_time').text = str(self.float82.value)
        uep.find('.//cell_definition[4]//phenotype//motility//migration_bias').text = str(self.float83.value)
        uep.find('.//cell_definition[4]//phenotype//motility//options//enabled').text = str(self.bool15.value)
        uep.find('.//cell_definition[4]//phenotype//motility//options//chemotaxis//enabled').text = str(self.bool16.value)
        uep.find('.//cell_definition[4]//phenotype//motility//options//chemotaxis//substrate').text = str(self.chemotaxis_substrate4.value)
        uep.find('.//cell_definition[4]//phenotype//motility//options//chemotaxis//direction').text = str(self.chemotaxis_direction4.value)
        # ---------  secretion 
        uep.find('.//cell_definition[4]//phenotype//secretion//substrate[1]').attrib['name'] = str(self.text6.value)
        uep.find('.//cell_definition[4]//phenotype//secretion//substrate[1]//secretion_rate').text = str(self.float84.value)
        # ---------  molecular
