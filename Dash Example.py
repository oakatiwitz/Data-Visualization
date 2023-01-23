import dash
import dash_html_components as html
import dash_core_components as dcc

# Create a das apllication
app = dash.Dash()

# Get the layout of tha application and adjust it.
# This is the division in our layout and from here we will add
# elements to the page.
app.layout = html.Div([
              # Title to our application using HTML H1 component
              html.H1('Data Visulaization in Python',
              # Adding CSS style using stylr parameter wchich take input
              # through dictionary.
              style={'color': 'blue', 'fontsize': 40,
                    'border-style': 'outset'
                }),
              # Adding dropdown
              html.Label('Dropdown'),
              dcc.Dropdown(
              options=[
              {'label': 'Option 1', 'value': '1'},
              {'label': 'Option 2', 'value': '2'},
              {'label': 'Option 3', 'value': '3'},
              ],
              value='3'
              ),
              # Adding Slider
              dcc.Slider(
              min=0,
              max=5,
              marks={i: '{}'.format(i) for i in range(5)},
              value=2,  
              )
              ],
              )
              
if __name__ == '__main__':
    # Grab the application and run the server
    app.run_server(port=8002, host='127.0.0.1', debug=True)

