import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

#starts a dash app (built with Flask)
app = dash.Dash()

#always going to have, the html of your project
app.layout = html.Div(children=[
	dcc.Input(id='input', value='Enter Something', type='text'),
	html.Div(id='output')
	])

#decorators/wrapper
@app.callback(
	Output(component_id='output', component_property='children'),
	[Input(component_id='input', component_property='value')])
def update_value(input_data):
	try:
		return str(float(input_data)**2)
	except:
		return 'Some Error'

#runs appp
if __name__ == '__main__':
	app.run_server(debug=False)
