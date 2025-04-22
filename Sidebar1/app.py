import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, 'assets/style.css'])

sidebar = html.Nav(
    className="sidebar",
    children=[
        html.Div(
            className="sidebar-inner",
            children=[
                html.Header(
                    className="sidebar-header",
                    children=[
                        html.Button(
                            type="button",
                            className="sidebar-burger",
                            id="sidebar-toggle",
                            children=[
                                html.I(className="bx bx-menu"),
                            ],
                        ),
                        html.Img(src="assets/logo.png", alt="", className="sidebar-logo"),
                    ],
                ),
                html.Nav(
                    className="sidebar-menu",
                    children=[
                        dcc.Link(
                            html.Button(
                                type="button",
                                children=[
                                    html.I(className="bx bx-home"),
                                    html.Span("Home"),
                                ],
                            ),
                            href="/home",
                            className="w-100 p-0",
                            style={"textDecoration": "none"},
                        ),
                        dcc.Link(
                            html.Button(
                                type="button",
                                children=[
                                    html.I(className="bx bx-user"),
                                    html.Span("Accounts"),
                                ],
                            ),
                            href="/accounts",
                            className="w-100 p-0",
                            style={"textDecoration": "none"},
                        ),
                        dcc.Link(
                            html.Button(
                                type="button",
                                className="has-border",
                                children=[
                                    html.I(className="bx bx-cog"),
                                    html.Span("Settings"),
                                ],
                            ),
                            href="/settings",
                            className="w-100 p-0",
                            style={"textDecoration": "none"},
                        ),
                        dcc.Link(
                            html.Button(
                                type="button",
                                children=[
                                    html.I(className="bx bx-shape-circle"),
                                    html.Span("Blockchain"),
                                ],
                            ),
                            href="/blockchain",
                            className="w-100 p-0",
                            style={"textDecoration": "none"},
                        ),
                        dcc.Link(
                            html.Button(
                                type="button",
                                children=[
                                    html.I(className="bx bx-data"),
                                    html.Span("Databases"),
                                ],
                            ),
                            href="/databases",
                            className="w-100 p-0",
                            style={"textDecoration": "none"},
                        ),
                        dcc.Link(
                            html.Button(
                                type="button",
                                children=[
                                    html.I(className="bx bx-speaker"),
                                    html.Span("AudioVibe"),
                                ],
                            ),
                            href="/audiovibe",
                            className="w-100 p-0",
                            style={"textDecoration": "none"},
                        ),
                        dcc.Link(
                            html.Button(
                                type="button",
                                className="has-border",
                                children=[
                                    html.I(className="bx bx-music"),
                                    html.Span("Soundblast"),
                                ],
                            ),
                            href="/soundblast",
                            className="w-100 p-0",
                            style={"textDecoration": "none"},
                        ),
                        dcc.Link(
                            html.Button(
                                type="button",
                                children=[
                                    html.I(className="bx bx-folder"),
                                    html.Span("Folders"),
                                ],
                            ),
                            href="/folders",
                            className="w-100 p-0",
                            style={"textDecoration": "none"},
                        ),
                        dcc.Link(
                            html.Button(
                                type="button",
                                children=[
                                    html.I(className="bx bx-layer"),
                                    html.Span("Levels"),
                                ],
                            ),
                            href="/levels",
                            className="w-100 p-0",
                            style={"textDecoration": "none"},
                        ),
                        dcc.Link(
                            html.Button(
                                type="button",
                                children=[
                                    html.I(className="bx bx-lock"),
                                    html.Span("Security"),
                                ],
                            ),
                            href="/security",
                            className="w-100 p-0",
                            style={"textDecoration": "none"},
                        ),
                    ],
                ),
            ],
        ),
    ]
)

content = html.Div(id="page-content", style={"margin-left": "75px", "transition": "margin-left 0.4s"})

app.layout = html.Div(
    id="app-wrapper",
    children=[
        dcc.Location(id="url"),
        sidebar,
        content
    ]
)

app.clientside_callback(
    """
    function(n_clicks) {
        const wrapper = document.getElementById('app-wrapper');
        if (!wrapper) return;
        if (n_clicks % 2 === 1) {
            wrapper.classList.add('open');
        } else {
            wrapper.classList.remove('open');
        }
        return window.getComputedStyle(document.getElementById("page-content")).style;
    }
    """,
    Output("page-content", "style"),
    Input("sidebar-toggle", "n_clicks")
)


@app.callback(
    Output("page-content", "children"), 
    [Input("url", "pathname")]
)
def render_page_content(pathname):
    if pathname == "/home":
        return html.P("This is the Home page content.")
    elif pathname == "/accounts":
        return html.P("This is the Accounts page content.")
    elif pathname == "/settings":
        return html.P("This is the Settings page content.")
    elif pathname == "/blockchain":
        return html.P("This is the Blockchain page content.")
    elif pathname == "/databases":
        return html.P("This is the Databases page content.")
    elif pathname == "/audiovibe":
        return html.P("This is the AudioVibe page content.")
    elif pathname == "/soundblast":
        return html.P("This is the Soundblast page content.")
    elif pathname == "/folders":
        return html.P("This is the Folders page content.")
    elif pathname == "/levels":
        return html.P("This is the Levels page content.")
    elif pathname == "/security":
        return html.P("This is the Security page content.")
    else:
        return html.P("This is the default content.")

if __name__ == "__main__":
    app.run(debug=True)