from desktop_layout import *

def _apply_mobile_layout():
    
    middle.fluid = True

    layout = dbc.Container(
        [top, middle, bottom],
        fluid = True
    )