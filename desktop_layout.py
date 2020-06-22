import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from passages import passages

### Header

### Title
header = dbc.Row(
            dbc.Col(
                [
                    html.H1('Machine Comprehension')
                ], style = {'text-align':'center',
                'padding':'3% 0% 0% 3%',
                'font-family':'Verdana'} 
            )
)

body_paragraph = dbc.Row(
    [
        dbc.Col(
            [
                html.P(
                    [
                    "Welcome to my Machine Comprehension web application. ",
                    html.Br(),
                    "See how a modern Machine Learning model finds answers in a passage."
                    ]
                )
            ]
        )
    ],
    style = {'text-align':'center'}
)

        
### Input text
input_text = dbc.Row(
    [
        dbc.Col(
            [
                dcc.Textarea(
                    id = "input_text",
                    placeholder =  "Write or paste your passage here or select an example passage from the dropdown below",
                    style = {'padding':'2% 1% 2% 1%',
                            'width': '100%', 
                            'height': 200}
)
            ]
        )
    ],
    style = {'padding':'2% 0% 2% 0%'}
)

### Dropdown for selecting passages
passage_dropdown = dbc.Row(
    [
        dbc.Col(
            [
                dcc.Dropdown(
                    id='passage_dropdown',
                    options=[{'label':key, 'value' : key} for key in passages],
                    placeholder = 'Select a passage or write your own'
            )
            ]
        )
    ]
)

### Input_question
input_question = dbc.Row(
    [
        dbc.Col(
            [
                dbc.Input(
                    id='input_question',
                    value = 'What is this passage about?',
                    style = {'padding':'2% 0% 2% 0%'}
                )
            ]
        )
    ],
    style = {'padding':'2% 0% 2% 0%'}
)

### Submit button
submit_button = dbc.Row(
    [
        dbc.Button("Submit", id = 'submit_button', size="md",
        color="primary", disabled = False,
        className = "mt-3 mx-auto")
    ],
    justify = 'center'
)

### Output text
output_text = dbc.Row(
    [
        dbc.Col(
            [
                html.P(id='output_text', 
                children=['']
                )
            ]
        )
    ],
    style = {'text-align':'center', 'padding': '5% 0% 5% 0%'}
)

### Footer


### Bring it together
layout = dbc.Container(
    [
        dcc.Store(id='memory-output', storage_type='memory'),
        header,
        body_paragraph,
        input_text,
        passage_dropdown,
        input_question,
        submit_button,
        output_text
    ],
    fluid = False
)