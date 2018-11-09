import dash
import dash_core_components as dcc
import dash_html_components as html

#starts a dash app (built with Flask)
app = dash.Dash()

#always going to have, the html of your project
app.layout = html.Div(children=[
	html.H1('Dash Tutorial'),
	dcc.Graph(id='Example',
		figure={
		'data': [
			{'x':[1, 2, 3, 4, 5], 'y':[5, 6, 7, 2, 1], 'type':'line', 'name':'boats'},
			{'x':[1, 2, 3, 4, 5], 'y':[8, 3, 2, 3, 5], 'type':'bar', 'name':'cars'}
			],
		'layout': {
		'title': 'Basic Dash Example'
		}
		})
	])

#runs appp
if __name__ == '__main__':
	app.run_server(debug=False)

