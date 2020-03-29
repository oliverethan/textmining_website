import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
from dash.dependencies import Input, Output
# from dash.dependencies import Event
import plotly
import pickle
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

print('HELLO')

left_tweets = pd.read_csv('left_trolls.csv')
right_tweets = pd.read_csv('right_trolls.csv')


l_hashtag_summary = pickle.load(open("precomputed-data/l_hashtag_summary.pickle", "rb"))
r_hashtag_summary = pickle.load(open("precomputed-data/r_hashtag_summary.pickle", "rb"))

l_df = pd.DataFrame(l_hashtag_summary['top_hashtags'],  columns = ['hashtag', 'count'])
r_df = pd.DataFrame(r_hashtag_summary['top_hashtags'],  columns = ['hashtag', 'count'])


hashtag_fig = make_subplots(rows=1, cols=2)

hashtag_fig.add_trace(
    go.Bar(
            x=l_df.iloc[50::-1]['count'],
            y=l_df.iloc[50::-1]['hashtag'],
            orientation='h', name="Left Trolls",
            marker=dict(
                color='#0015BC',
            )
    ),
    row=1, col=1,
    
    )

hashtag_fig.add_trace(
    go.Bar(
            x=r_df.iloc[50::-1]['count'],
            y=r_df.iloc[50::-1]['hashtag'],
            orientation='h', name="Right Trolls",
    marker=dict(
            color='#E9141D',
        )),
    row=1, col=2,
    
    )

hashtag_fig.update_layout(height=1300, title_text="Top Hashtags")




app.layout = html.Div( children=[
    html.H1(className='center', children='Russian Troll Tweets Analysis '),

    html.Div(className='container', children=[
    html.Div(className='smartphone sleft', 
        children=[
        html.Img(src='https://cdn2.iconfinder.com/data/icons/minimalism/512/twitter.png' , className='twit', ),
        html.Blockquote( id = 'l_tweet_one', className='twitter-tweet',),
        html.Blockquote( id = 'l_tweet_two', className='twitter-tweet',),
        html.Blockquote( id = 'l_tweet_three', className='twitter-tweet',),
        dcc.Interval(
            id='interval-component_1',
            interval=1*6143, # in milliseconds
            n_intervals=0
        ),
        dcc.Interval(
            id='interval-component_2',
            interval=1*5505, # in milliseconds
            n_intervals=1000
        ),
        dcc.Interval(
            id='interval-component_3',
            interval=1*7217, # in milliseconds
            n_intervals=2000
        ),

         ] ),
    html.H2(className='center', children='3 Million Tweets'),

    html.Div(className='rsmartphone sright',
        children=[
        html.Img(src='https://cdn2.iconfinder.com/data/icons/minimalism/512/twitter.png' , className='twit'),
        html.Blockquote( id = 'r_tweet_one', className='twitter-tweet',),
        html.Blockquote( id = 'r_tweet_two', className='twitter-tweet',),
        html.Blockquote( id = 'r_tweet_three', className='twitter-tweet',),
        # dcc.Interval(
        #     id='interval-component_4',
        #     interval=1*5113, # in milliseconds
        #     n_intervals=0
        # ),
        # dcc.Interval(
        #     id='interval-component_5',
        #     interval=1*7525, # in milliseconds
        #     n_intervals=1000
        # ),
        # dcc.Interval(
        #     id='interval-component_6',
        #     interval=1*6237, # in milliseconds
        #     n_intervals=2000
        # ),

         ] ),

            ]
        ),


    html.Div(children='''
        On Febuary 2019 the Federal Government indicted a russian troll farm known as the Internet Research Agency. The farm posted over 3 million tweets in an
        attempt to influence the United States election. Here is an analysis of them Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec et dui accumsan est auctor aliquam vitae ut ipsum. Duis rutrum dolor et ligula facilisis, ac placerat lorem laoreet. Pellentesque varius lacus id nisl volutpat rutrum. Nulla eu accumsan tellus, vitae mattis diam. Donec vel ligula erat. Nunc tellus velit, lacinia interdum pulvinar non, eleifend at magna. Curabitur nec consectetur risus. Duis vestibulum, est eget fermentum tincidunt, massa mi interdum turpis, a molestie tortor dolor et nisi. Pellentesque nulla velit, malesuada vitae augue quis, vulputate imperdiet eros. Etiam sollicitudin metus in tellus placerat, ut commodo quam malesuada. Phasellus tincidunt pharetra erat eget pretium. Curabitur blandit orci eget mauris pharetra pretium. Etiam non tellus ac nulla pharetra mollis. In tincidunt, quam et molestie feugiat, sem mauris malesuada leo, in elementum tellus eros nec leo. Proin maximus tellus at enim tempor, a bibendum erat vulputate.

Integer a orci quis risus placerat tempor sit amet eu nibh. Etiam gravida nisl interdum, pellentesque arcu eu, convallis dolor. Quisque sit amet pellentesque velit. In a velit diam. Ut quis dui non magna tincidunt consectetur a vel justo. In faucibus odio ac eros sagittis maximus. Donec in ultrices diam. Aliquam ultricies risus vehicula nisi condimentum consequat. Vivamus augue nisi, interdum facilisis ultrices eu, blandit vitae tellus. Sed at consectetur justo. Quisque venenatis nec mauris tristique convallis. Nunc elit turpis, dignissim eget elementum ac, varius gravida tellus. Suspendisse ut ex ante.
    ''', style= {"margin": "10px 5px"}),

    dcc.Graph(
        id='example-graph-2',
        figure=hashtag_fig
    ),

])


@app.callback(Output('l_tweet_one', 'children'),
              [Input('interval-component_1', 'n_intervals')])
def update_metrics(n):
    print('update called')
    bold = {'font-weight': 'bold'}
    idx = np.random.randint(0, len(left_tweets)) 
    return [ html.P(left_tweets.iloc[idx]['content']) ,
             html.P('- ' + left_tweets.iloc[idx]['author'] , style= bold)
                        ] 

@app.callback(Output('l_tweet_two', 'children'),
              [Input('interval-component_2', 'n_intervals')])
def update_metrics(n):
    print('update called')
    bold = {'font-weight': 'bold'}
    idx = np.random.randint(0, len(left_tweets)) 
    return [ html.P(left_tweets.iloc[idx]['content']) ,
             html.P('- ' + left_tweets.iloc[idx]['author'] , style= bold)
                        ] 

@app.callback(Output('l_tweet_three', 'children'),
              [Input('interval-component_3', 'n_intervals')])
def update_metrics(n):
    print('update called')
    bold = {'font-weight': 'bold'}
    idx = np.random.randint(0, len(left_tweets)) 
    return [ html.P(left_tweets.iloc[idx]['content']) ,
             html.P('- ' + left_tweets.iloc[idx]['author'] , style= bold)
                        ] 




@app.callback(Output('r_tweet_one', 'children'),
              [Input('interval-component_2', 'n_intervals')])
def update_metrics(n):
    print('update called')
    bold = {'font-weight': 'bold'}
    idx = np.random.randint(0, len(right_tweets)) 
    return [ html.P(right_tweets.iloc[idx]['content']) ,
             html.P('- ' + right_tweets.iloc[idx]['author'] , style= bold)
                        ] 

@app.callback(Output('r_tweet_two', 'children'),
              [Input('interval-component_1', 'n_intervals')])
def update_metrics(n):
    print('update called')
    bold = {'font-weight': 'bold'}
    idx = np.random.randint(0, len(right_tweets)) 
    return [ html.P(right_tweets.iloc[idx]['content']) ,
             html.P('- ' + right_tweets.iloc[idx]['author'] , style= bold)
                        ] 

@app.callback(Output('r_tweet_three', 'children'),
              [Input('interval-component_3', 'n_intervals')])
def update_metrics(n):
    print('update called')
    bold = {'font-weight': 'bold'}
    idx = np.random.randint(0, len(right_tweets)) 
    return [ html.P(right_tweets.iloc[idx]['content']) ,
             html.P('- ' + right_tweets.iloc[idx]['author'] , style= bold)
             ]


if __name__ == '__main__':
    app.run_server(debug=True,  dev_tools_silence_routes_logging = False)




# @app.callback(Output('live-update-graph-scatter', 'figure'),
#               events=[Event('interval-component', 'interval')])









#     <div class="smartphone">
#   <div class="content">
#     Hello
#   </div>
# </div>