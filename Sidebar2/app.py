import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, 'assets/style.css'])

sidebar = html.Aside(
    className="sidebar",
    children=[
        html.Header(
            className="sidebar-header",
            children=[
                html.Img(src="assets/logo.svg", className="logo-img"),
                html.I(className="logo-icon bx bxl-instagram"),
            ],
        ),
        html.Nav(
            children=[
                dcc.Link(
                    html.Button(
                        children=[
                            html.Span(
                                children=[
                                    html.I(className="bx bx-home"),
                                    html.Span("Home"),
                                ]
                            )
                        ],
                        className="w-100",  # Add w-100 class here
                        style={"textAlign": "left"} # Align text to the left within the full-width button
                    ),
                    href="/",
                    className="w-100 p-0",
                    style={"textDecoration": "none"}
                ),
                dcc.Link(
                    html.Button(
                        children=[
                            html.Span(
                                children=[
                                    html.I(className="bx bx-search"),
                                    html.Span("Search"),
                                ]
                            )
                        ],
                        className="w-100",  # Add w-100 class here
                        style={"textAlign": "left"}
                    ),
                    href="/search",
                    className="w-100 p-0",
                    style={"textDecoration": "none"}
                ),
                dcc.Link(
                    html.Button(
                        children=[
                            html.Span(
                                children=[
                                    html.I(className="bx bx-compass"),
                                    html.Span("Explore"),
                                ]
                            )
                        ],
                        className="w-100",  # Add w-100 class here
                        style={"textAlign": "left"}
                    ),
                    href="/explore",
                    className="w-100 p-0",
                    style={"textDecoration": "none"}
                ),
                dcc.Link(
                    html.Button(
                        children=[
                            html.Span(
                                children=[
                                    html.I(className="bx bxl-telegram", children=[html.Span("13")]),
                                    html.Span("Messages"),
                                ]
                            )
                        ],
                        className="w-100",  # Add w-100 class here
                        style={"textAlign": "left"}
                    ),
                    href="/messages",
                    className="w-100 p-0",
                    style={"textDecoration": "none"}
                ),
                dcc.Link(
                    html.Button(
                        children=[
                            html.Span(
                                children=[
                                    html.I(className="bx bx-heart", children=[html.Em()]),
                                    html.Span("Notifications"),
                                ]
                            )
                        ],
                        className="w-100",  # Add w-100 class here
                        style={"textAlign": "left"}
                    ),
                    href="/notifications",
                    className="w-100 p-0",
                    style={"textDecoration": "none"}
                ),
                dcc.Link(
                    html.Button(
                        children=[
                            html.Span(
                                children=[
                                    html.I(className="bx bx-plus-circle"),
                                    html.Span("Create"),
                                ]
                            )
                        ],
                        className="w-100",  # Add w-100 class here
                        style={"textAlign": "left"}
                    ),
                    href="/create",
                    className="w-100 p-0",
                    style={"textDecoration": "none"}
                ),
                dcc.Link(
                    html.Button(
                        children=[
                            html.Span(
                                children=[
                                    html.Img(src="assets/logo.png"),
                                    html.Span("Profile"),
                                ]
                            )
                        ],
                        className="w-100",  # Add w-100 class here
                        style={"textAlign": "left"}
                    ),
                    href="/profile",
                    className="w-100 p-0",
                    style={"textDecoration": "none"}
                ),
            ]
        ),
    ]
)

content = html.Div(id="page-content", style={"margin-left": "250px", "padding": "20px"})

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])

@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return html.P("This is the Home page content.")
    elif pathname == "/search":
        return html.P("This is the Search page content.")
    elif pathname == "/explore":
        return html.P("This is the Explore page content.")
    elif pathname == "/messages":
        return html.P("This is the Messages page content.")
    elif pathname == "/notifications":
        return html.P("This is the Notifications page content.")
    elif pathname == "/create":
        return html.P("This is the Create page content.")
    elif pathname == "/profile":
        return html.P("This is the Profile page content.")
    return html.P("404: Page not found!")

if __name__ == "__main__":
    app.run(debug=True)