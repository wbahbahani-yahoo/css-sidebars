import dash
from dash import html, dcc, Input, Output, State, callback
import dash_bootstrap_components as dbc

# Initialize the Dash app with a modern theme
app = dash.Dash(__name__,
                 external_stylesheets=[
                     dbc.themes.BOOTSTRAP,
                     "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css"
                 ])

# Custom CSS for animations and styling
app.index_string = '''
<!DOCTYPE html>
<html  dir="rtl">
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
        <style>
            :root {
                --font-family: "Calibri", sans-serif;
                --sidebar-width: 250px;
                --sidebar-collapsed-width: 70px;
                --transition-speed: 0.5s;
                --primary-color: #4f46e5;
                --bg-color: #111827;         /* Dark slate */
                --text-color: #f3f4f6;       /* Light gray */
                --sidebar-bg: #1f2937;       /* Dark sidebar */
                --hover-color: #374151;      /* Darker hover */
            }

            body {
                font-family: var(--font-family);
                background-color: var(--bg-color);
                color: var(--text-color);
                margin: 0;
            }

            #sidebar-container {
                color: #fff;
                height: 100vh;
                width: var(--sidebar-width);
                position: fixed;
                top: 0;
                right: 0;
                left: unset;
                background-color: var(--sidebar-bg);
                transition: width var(--transition-speed) ease;
                box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1);
                z-index: 1000;
                overflow-x: hidden;
            }

            #sidebar-container.collapsed {
                width: var(--sidebar-collapsed-width);
            }

            #content h1, .card-title {
                font-family: var(--font-family);
            }

            #content {
                font-family: var(--font-family);
                margin-right: var(--sidebar-width);
                padding: 20px;
                transition: margin-left var(--transition-speed) ease;
            }

            #content.expanded {
                font-family: var(--font-family);
                margin-right: var(--sidebar-collapsed-width);
            }

            .sidebar-header {
                display: flex;
                align-items: center;
                justify-content: space-between;
                padding: 16px;
                border-bottom: 1px solid #e5e7eb;
            }

            .sidebar-toggle {
                background: none;
                border: none;
                color: var(--text-color);
                cursor: pointer;
                padding: 8px;
                border-radius: 4px;
            }

            .sidebar-toggle:hover {
                background-color: var(--hover-color);
            }

            .nav-item {
                color: white;
                padding: 12px 16px;
                display: flex;
                align-items: center;
                cursor: pointer;
                transition: background-color 0.2s;
                border-radius: 4px;
                margin: 4px 8px;
            }

            .nav-item:hover {
                background-color: var(--hover-color);
            }

            .nav-item.active {
                background-color: rgba(79, 70, 229, 0.1);
                color: var(--primary-color);
                font-weight: 500;
            }

            .nav-icon {
                margin-inline-end: 12px; /* works with RTL and LTR */
                width: 20px;
                text-align: center;
                display: inline-block;
            }

            .nav-text {
                color: #fff;
                white-space: nowrap;
                opacity: 1;
                transition: opacity var(--transition-speed);
            }

            #sidebar-container.collapsed .nav-text {
                opacity: 0;
                width: 0;
                display: none;
            }

            #sidebar-container.collapsed .sidebar-brand {
                color: #fff;
                display: none;
            }

            .sidebar-section {
                margin-top: 16px;
            }

            .sidebar-section-title {
                color: #fff;
                padding: 0 16px;
                margin-bottom: 8px;
                font-size: 0.75rem;
                text-transform: uppercase;
                letter-spacing: 0.05em;
                color: #6b7280;
                font-weight: 600;
            }

            #sidebar-container.collapsed .sidebar-section-title {
                opacity: 0;
                display: none;
            }
        </style>
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
'''

# Define the sidebar
sidebar = html.Div(
    [
        html.Div(
            [
                html.Span("Dashboard", className="sidebar-brand"),
                html.Button(
                    html.I(className="fas fa-bars"),
                    id="sidebar-toggle",
                    className="sidebar-toggle",
                ),
            ],
            className="sidebar-header",
        ),
        html.Div(
            [
                html.Div("القائمة الرئيسية", className="sidebar-section-title"),
                html.Div(
                    [
                        html.Div(
                            [
                                html.I(className="fas fa-home nav-icon"),
                                html.Span("لوحة البيانات", className="nav-text"),
                            ],
                            className="nav-item active",
                        ),
                        html.Div(
                            [
                                html.I(className="fas fa-chart-line nav-icon"),
                                html.Span("تحليل البيانات", className="nav-text"),
                            ],
                            className="nav-item",
                        ),
                        html.Div(
                            [
                                html.I(className="fas fa-users nav-icon"),
                                html.Span("المستخدمين", className="nav-text"),
                            ],
                            className="nav-item",
                        ),
                    ],
                    className="sidebar-section",
                ),
                html.Div("الإعدادات", className="sidebar-section-title"),
                html.Div(
                    [
                        html.Div(
                            [
                                html.I(className="fas fa-cog nav-icon"),
                                html.Span("الإعدادات", className="nav-text"),
                            ],
                            className="nav-item",
                        ),
                        html.Div(
                            [
                                html.I(className="fas fa-question-circle nav-icon"),
                                html.Span("المساعدة", className="nav-text"),
                            ],
                            className="nav-item",
                        ),
                    ],
                    className="sidebar-section",
                ),
            ],
            style={"padding": "8px 0"},
        ),
    ],
    id="sidebar-container",
)

# Define the content area
content = html.Div(
    [
        html.H1("لوحة البيانات", className="mb-4"),
        # html.P("This is your main content area. It will adjust when the sidebar is collapsed."),
        # html.Div(
        #     [
        #         dcc.Dropdown(
        #             id="theme-selector",
        #             options=[
        #                 {"label": "Light", "value": "light"},
        #                 {"label": "Calm", "value": "calm"},
        #             ],
        #             value="calm",
        #             clearable=False,
        #             style={"width": "200px"}
        #         ),
        #         html.Label("Theme", style={"marginInlineEnd": "8px"}),
        #     ],
        #     style={"display": "flex", "alignItems": "center", "marginBottom": "16px"},
        # ),

        html.Div(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.Card(
                                dbc.CardBody(
                                    [
                                        html.H4("Card 1", className="card-title"),
                                        html.P("This is some card content"),
                                    ]
                                ),
                                className="mb-4 shadow-sm",
                            ),
                            width=4,
                        ),
                        dbc.Col(
                            dbc.Card(
                                dbc.CardBody(
                                    [
                                        html.H4("Card 2", className="card-title"),
                                        html.P("This is some card content"),
                                    ]
                                ),
                                className="mb-4 shadow-sm",
                            ),
                            width=4,
                        ),
                        dbc.Col(
                            dbc.Card(
                                dbc.CardBody(
                                    [
                                        html.H4("Card 3", className="card-title"),
                                        html.P("This is some card content"),
                                    ]
                                ),
                                className="mb-4 shadow-sm",
                            ),
                            width=4,
                        ),
                    ],
                    className="mb-4",
                ),
                dbc.Row(
                    dbc.Col(
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    html.H4("Data Visualization", className="card-title"),
                                    dcc.Graph(
                                        figure={
                                            'data': [
                                                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                                                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'Montréal'},
                                            ],
                                            'layout': {
                                                'title': 'Sample Bar Chart',
                                                'plot_bgcolor': 'rgba(0,0,0,0)',
                                                'paper_bgcolor': 'rgba(0,0,0,0)',
                                            }
                                        }
                                    ),
                                ]
                            ),
                            className="shadow-sm",
                        )
                    )
                ),
            ],
            style={"marginTop": "20px"},
        ),

        html.Div(id="theme-style-injector", style={"display": "none"}),


    ],
    id="content",
)

# App layout
app.layout = html.Div([dcc.Location(id="url"), sidebar, content])

# Callback to toggle sidebar
@callback(
    [Output("sidebar-container", "className"),
     Output("content", "className")],
    [Input("sidebar-toggle", "n_clicks")],
    [State("sidebar-container", "className")]
)
def toggle_sidebar(n_clicks, sidebar_class):
    if n_clicks:
        if sidebar_class == "collapsed":
            return "", ""
        else:
            return "collapsed", "expanded"
    return "", ""


# @callback(
#     Output("theme-style-injector", "children"),
#     Input("theme-selector", "value")
# )
# def update_theme_css(theme):
#     if theme == "light":
#         style = {"--bg-color": "#f9fafb"}
#     elif theme == "calm":
#         style = {"--bg-color": "#233A51"}
#     else:
#         style = {}  # Default or handle other themes

#     return html.Div(style=style)


# Run the app
if __name__ == "__main__":
    app.run(debug=True)