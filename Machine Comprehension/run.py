import dash
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from urllib.parse import quote as urlquote
import flask
from flask import Flask, send_from_directory, send_file, request, session, _request_ctx_stack
import requests

import base64
import datetime
import io
import os
import string
import random
import re

from desktop_layout import layout as desktop_layout
# from mobile_layout import _apply_mobile_layout
from callbacks import *
from app import app, server, cache, register_before_request
from passages import passages

app.layout = desktop_layout

## Write callbacks

### Select passage from dropdown
@app.callback(
    Output('input_text', 'value'),
    [Input('passage_dropdown', 'value')]
)
def modify_input_text(dropdown_value):
    if dropdown_value:
        return passages.get(dropdown_value)        

@app.callback(
    [
        Output("output_text", "children"),
        Output('memory-output', 'data')
    ],
    [
        Input("input_text", "value"),
        Input("input_question", "value"),
        Input("submit_button", "n_clicks"),
        Input("model_dropdown", "value")
    ],
    [
        State('memory-output', 'data')
    ]
)
def get_prediction(context, query, n_clicks, model, data):
    if data is None:
        data = {}
        data['clicks'] = 1
        return [''], data

    if n_clicks and data['clicks'] <= n_clicks:
        data['clicks'] = n_clicks + 1
        if model == "bidaf_dd":
            return [bidaf_answer(context, query)], data
        elif model == "distilbert_dd":
            return [distilbert_answer(context, query)], data
        elif model == "roberta_dd":
            return [roberta_answer(context, query)], data
        elif model == "albert_dd":
            return [albert_answer(context, query)], data

    else:
        print (data, n_clicks)
        return [''], data
       
@app.callback(Output('card-content', 'children'),
             [Input('tabs', 'active_tab')])
def get_about_model(model): 
    return about_models(model)

if __name__ == '__main__':
    app.server.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))