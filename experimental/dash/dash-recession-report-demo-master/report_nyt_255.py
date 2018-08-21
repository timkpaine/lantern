# -*- coding: utf-8 -*-
import pandas as pd

import dash
from dash import Dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import colorlover as cl
import numpy as np
from flask import Flask
from flask_cors import CORS
import os

df_jobs = pd.read_csv('nyt_255_ces.csv')
df_wages = pd.read_csv('nyt_255_wages.csv')

series = {
    'absolute_wages': {},
    'absolute_jobs': {},
    'relative_job': {},
    'relative_wages': {},
    'meta': {},
    'job_growth': {}
}
for i in range(len(df_jobs)):
    jobs_meta = df_jobs.iloc[i, 0:11]
    jobs_row = df_jobs.iloc[i, 11:]
    name = jobs_meta.nytlabel
    cescode = jobs_meta.cescode

    wages_row = df_wages[df_wages.seriesid == cescode].iloc[0, 1:]

    # Collect data
    series['absolute_wages'][cescode] = wages_row
    series['absolute_jobs'][cescode] = jobs_row
    series['relative_job'][cescode] = 100. * (jobs_row[-1] - jobs_row[0]) / jobs_row[-1]
    series['relative_wages'][cescode] = 100. * (wages_row[-1] - wages_row[0]) / wages_row[-1]
    series['meta'][cescode] = jobs_meta
    series['job_growth'][cescode] = jobs_row[-1] - jobs_row[0]


def create_figure(highlight_cescode=None, skip_labels=[], show_only=[]):
    max_wage = max(df_wages['2006-03-01'])
    min_wage = min(df_wages['2006-03-01'])
    # Construct the charts
    scale = cl.scales['5']['div']['RdBu']
    traces = []
    annotations = []
    for cescode in series['absolute_wages'].keys():
        growth = series['relative_job'][cescode]
        # Construct initial chart

        # x's initial position is the initial wage
        # and its width is constant to signifiy time
        initial_wage = series['absolute_wages'][cescode][0]
        relative_wage = (initial_wage - min_wage) / max_wage
        x = np.linspace(
            relative_wage,
            relative_wage + 0.2,
            len(series['absolute_wages'][cescode])
        )

        # convert growth over time to a relative scale and
        # jobs created across all industries to relative scale
        relative_growth_across_time = ((series['absolute_jobs'][cescode] -
                          series['absolute_jobs'][cescode][0]) /
                          series['absolute_jobs'][cescode][-1])

        max_jobs_created = max(series['job_growth'].values())
        min_jobs_created = min(series['job_growth'].values())
        jobs = series['absolute_jobs'][cescode]
        relative_growth_across_industry = ((jobs[-1] - jobs[0]) - min_jobs_created) / max_jobs_created
        y = relative_growth_across_time + (relative_growth_across_industry * 2)

        if growth > 20:
            color = scale[4]
            legendgroup = '>20%'
            name = 'Greater than 20%'
        elif growth > 10:
            color = scale[3]
            legendgroup = '>10%'
            name = 'Between 10% and 20%'
        elif growth > -10:
            color = 'lightgrey'
            legendgroup = '>-10%'
            name = 'Between -10% and 10%'
        elif growth > -20:
            color = scale[1]
            legendgroup = '>-20%'
            name = 'Between -20% and -10%'
        else:
            color = scale[0]
            legendgroup = '<-20%'
            name = 'Less than -20%'

        if highlight_cescode and cescode not in highlight_cescode:
            color = 'lightgrey'

        hoverinfo = 'text'
        width = 1
        if highlight_cescode and cescode in highlight_cescode:
            width = 2.5
            if color == 'lightgrey':
                color = 'grey'
            hoverinfo = 'text'
        elif highlight_cescode:
            width = 0.5
            hoverinfo = 'none'

        label = series['meta'][cescode].nytlabel

        traces.append({
            'x': x,
            'y': y,
            'mode': 'lines',
            'line': {
                'color': color,
                'width': width
            },
            'text': [
                ('<b>{}</b><br>'
                 'Overall job growth: {}%<br>'
                 'Wages: ${} / hour<br>'
                 'Jobs: {}k<br>{}').format(
                    label,
                    np.around(growth, decimals=1),
                    np.around(wage_in_year, decimals=1),
                    jobs_in_year,
                    year
                )
                for year, jobs_in_year, wage_in_year in zip(
                    list(jobs.index),
                    list(jobs),
                    list(series['absolute_wages'][cescode])
                )
            ],
            'legendgroup': legendgroup,
            'name': name,
            'hoverinfo': hoverinfo,
            'showlegend': (
                False if legendgroup in [t['legendgroup'] for t in traces]
                else True
            )
        })

        if (highlight_cescode and cescode in highlight_cescode and
                (skip_labels and label not in skip_labels) or
                (show_only and label in show_only)):
            annotations.append({
                'x': traces[-1]['x'][-1], 'xref': 'x', 'xanchor': 'left',
                'y': traces[-1]['y'][-1], 'yref': 'y', 'yanchor': 'top',
                'showarrow': False,
                'text': label,
                'font': {'size': 12},
                'bgcolor': 'rgba(255, 255, 255, 0.5)'
            })

    # reorder traces to reorder legend items
    if not highlight_cescode:
        def get_trace_index(traces, legendgroup):
            for i, trace in enumerate(traces):
                if trace['showlegend'] and trace['legendgroup'] == legendgroup:
                    return i
        traces.insert(0, traces.pop(get_trace_index(traces, '<-20%')))
        traces.insert(0, traces.pop(get_trace_index(traces, '>-20%')))
        traces.insert(0, traces.pop(get_trace_index(traces, '>-10%')))
        traces.insert(0, traces.pop(get_trace_index(traces, '>10%')))
        traces.insert(0, traces.pop(get_trace_index(traces, '>20%')))
    else:
        # move highlighted traces to the end
        for i, trace in enumerate(traces):
            if trace['line']['width'] != 2.5:
                traces.insert(0, traces.pop(i))


    if not highlight_cescode:
        annotations = [{
            'x': 0.8, 'xref': 'paper', 'xanchor': 'left',
            'y': 0.95, 'yref': 'paper', 'yanchor': 'bottom',
            'text': '<b>Job Growth</b>',
            'showarrow': False
        }]

    layout = {
        'xaxis': {
            'showgrid': False,
            'showline': False,
            'zeroline': False,
            'showticklabels': False,
            'ticks': '',
            'title': '← Lower Wages        Industries        Higher Wages →'
        },
        'yaxis': {
            'showgrid': False,
            'showticklabels': False,
            'zeroline': False,
            'ticks': '',
            'title': 'Jobs'
        },
        'showlegend': not bool(highlight_cescode),
        'hovermode': 'closest',
        'legend': {
            'x': 0.8,
            'y': 0.95,
            'xanchor': 'left'
        },
        'annotations': annotations,
        'margin': {'t': 20, 'b': 20, 'r': 0, 'l': 20},
        'font': {'size': 12}
    }

    return {'data': traces, 'layout': layout}


app = Dash(__name__)
server = app.server

app.css.append_css({
    'external_url': (
        'https://cdn.rawgit.com/chriddyp/0247653a7c52feb4c48437e1c1837f75'
        '/raw/a68333b876edaf62df2efa7bac0e9b3613258851/dash.css'
    )
})

layout = html.Div([

    dcc.Markdown('''
    # How the Recession Reshaped the Economy, in 255 Charts

    Five years since the end of the Great Recession,
    the economy has finally regained the nine million jobs it lost.
    But not all industries recovered equally.
    Each line below shows how the number of jobs has changed for
    a particular industry over the past 10 years.
    Scroll down to see how the recession reshaped the nation’s job market,
    industry by industry.

    > This interactive report is a rendition of a
    > [New York Times original](https://www.nytimes.com/interactive/2014/06/05/upshot/how-the-recession-reshaped-the-economy-in-255-charts.html).
    > This app demonstrates how to build high-quality, interactive
    > reports using the Dash framework in Python.

    ***
    '''.replace('  ', ''), className='container',
    containerProps={'style': {'maxWidth': '650px'}}),

    dcc.Markdown('''
    ## A Mixed Recovery

    Industries in the health care and energy sectors grew substantially
    over the last five years, while jobs in real estate and
    construction continued to shrink.
    Industries that paid in the middle of the wage spectrum
    generally lost jobs. And while the economy overall
    is back to its pre-recession level, it hasn't added the
    roughly 10 million jobs needed to keep up with growth
    in the working-age population.
    '''.replace('  ', ''), className='container',
    containerProps={'style': {'maxWidth': '650px'}}),

    dcc.Graph(
        figure=create_figure(), id='overview',
        style={'height': '90vh'}
    ),

    dcc.Markdown('''
    ***
    ## More Bad — and Good — Jobs
    Americans often lament the quality of jobs today, and some
    low-paying industries — like **fast food**, where annual average pay
    is less than $22,000 — are growing.
    But so are some high-paying sectors, such as **consulting**,
    **computing** and **biotech**.
    '''.replace('  ', ''), className='container',
    containerProps={'style': {'maxWidth': '650px'}}),

    dcc.Graph(
        figure=create_figure(
            list(df_jobs[df_jobs.alternacategory == 'wages'].cescode),
            skip_labels=[
                'Full-service restaurants',
                'Engineering and drafting services',
                'Beer, wine and liquor stores',
                'Supermarkets and other grocery stores',
                'Used merchandise stores'
            ]
        ), id='mixed',
        style={'height': '90vh'}
    ),

    dcc.Markdown('''
    ***
    ## The Medical Economy
    The middle-wage industries that have added jobs are
    overwhelmingly in health care.
    Labs, home-care providers and dentist offices all pay
    between $18 and $29 an hour on average —
    and all have grown.
    But these gains have not offset losses in other middle-wage
    industries, such as airlines and construction.
    '''.replace('  ', ''), className='container',
    containerProps={'style': {'maxWidth': '650px'}}),

    dcc.Graph(
        figure=create_figure(
            list(df_jobs[df_jobs.alternacategory == 'health'].cescode),
            [],
            [
                'Home health care services',
                'Offices of physicians',
                'General and surgical hospitals',
                'Diagnostic imaging centers',
                'Offices of dentists',
                'Outpatient care centers, except mental health'
            ]
        ), id='health',
        style={'height': '90vh'}
    ),

    dcc.Markdown('''
    ***
    ## A Long Housing Bust
    Home prices have rebounded from their crisis lows,
    but home building remains at historically low levels.
    Overall, industries connected with construction and
    real estate have lost 19 percent of their jobs since
    the recession began — hundreds of thousands more than
    health care has added.
    '''.replace('  ', ''), className='container',
    containerProps={'style': {'maxWidth': '650px'}}),

    dcc.Graph(
        figure=create_figure(
            list(df_jobs[df_jobs.alternacategory == 'housing'].cescode),
            [],
            [
                'General contractors for new homes',
                'Land subdivision',
                'Furniture stores',
                'Residential remodelers',
                'Architectural services',
                'Wood product manufacturing',
                'For'
            ]
        ), id='real-estate',
        style={'height': '90vh'}
    ),

    dcc.Markdown('''
    ***
    ## Black Gold Rush
    While it took a hit from the recession,
    oil and gas extraction — and its associated jobs —
    have been booming,
    transforming economies in resource-rich places like West Texas
    and North Dakota.
    Many of these industries have average salaries above $70,000.
    '''.replace('  ', ''), className='container',
    containerProps={'style': {'maxWidth': '650px'}}),

    dcc.Graph(
        figure=create_figure(
            list(df_jobs[df_jobs.alternacategory == 'oil'].cescode),
            [
                'Oil and gas pipeline construction',
                'Natural gas distribution'
            ]
        ), id='oil',
        style={'height': '90vh'}
    ),

    dcc.Markdown('''
    ***
    ## Digital Revolution
    Bookstores, printers and publishers of newspapers and magazines
    have lost a combined 400,000 jobs since the recession began.
    Internet publishers — including web-search firms — offset
    only a fraction of the losses, adding 76,000 jobs.
    Electronic shopping and auctions made up the
     fastest-growing industry, tripling in employment in 10 years.
    '''.replace('  ', ''), className='container',
    containerProps={'style': {'maxWidth': '650px'}}),

    dcc.Graph(
        figure=create_figure(
            list(df_jobs[df_jobs.alternacategory == 'media'].cescode),
            [
                'Video and photography services',
                'Radio, television, cable and other broadcasting'
            ]
        ), id='media',
        style={'height': '90vh'}
    ),

    dcc.Markdown('''
    ***
    ## Grooming Boom
    In the midst of recession, Americans held on to simple luxuries —
    for themselves and their pets.
    Nail salons, which made up one of the most resilient industries,
    were closely rivaled by pet boarding, grooming and training.
    '''.replace('  ', ''), className='container',
    containerProps={'style': {'maxWidth': '650px'}}),

    dcc.Graph(
        figure=create_figure(
            list(df_jobs[df_jobs.alternacategory == 'booming'].cescode),
            ['Pharmacies and drug stores']
        ), id='booming',
        style={'height': '90vh'}
    ),

    dcc.Markdown('''
    ***
    ## And More
    Discover patterns yourself by filtering through industries with
    the dropdown below.
    '''.replace('  ', ''), className='container',
    containerProps={'style': {'maxWidth': '650px'}}),

    html.Div(
        dcc.Dropdown(
            options=[
                {'label': c, 'value': c}
                for c in sorted(list(df_jobs.nytlabel.unique()))
            ],
            value=['Florists', 'Bookstores and news dealers'],
            multi=True,
            id='category-filter',
        ), className='container', style={'maxWidth': '650px'}),
    html.Div(id='filtered-content'),

    dcc.Markdown('''
    ***
    ## Made with Dash

    This report was written in Python with the Dash framework.
    Dash abstracts away all of the server logic, API calls, CSS,
    HTML, and Javascript that is usually required to produce a rich web
    application. This application was written in a single python file
    containing around 500 lines of code. This includes the data analysis,
    markup, and interactive visualizations. See for yourself below.

    Interested in what you see?
    [Get in touch](https://plot.ly/products/consulting-and-oem/).
    '''.replace('  ', ''),
        className='container',
        containerProps={'style': {'maxWidth': '650px'}}
    ),

    html.Div(
        dcc.SyntaxHighlighter(
            open('report_nyt_255.py', 'r').read(),
            language='python'
        ),
        className='container',
        style={'maxWidth': '650px', 'borderLeft': 'thin solid lightgrey'}
    )

])


app.layout = layout


@app.callback(
    Output('filtered-content', 'children'),
    [Input('category-filter', 'value')])
def filter(selected_values):
    figure = create_figure(
        list(df_jobs[
            df_jobs.nytlabel.isin(selected_values)
        ].cescode) if selected_values else None,
        skip_labels=['-'],
    )

    for trace in figure['data']:
        trace['hoverinfo'] = 'text'

    return dcc.Graph(
        id='filtered-graph',
        figure=figure
    )



if __name__ == '__main__':
    app.run_server(debug=True, threaded=True)
