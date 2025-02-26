from shiny import App, Inputs, Outputs, Session, ui
from modules import mod_welcome as welcome
from pathlib import Path

current_dir = Path(__file__).parent

app_ui = ui.div(
    ui.page_fixed(
        ui.head_content(
            ui.tags.title("{{ cookiecutter.project_name }}"),
            ui.tags.link(
                rel="icon",
                href="logo.png",
            ),
        ),
        welcome.welcome_talospy_ui("welcome"), 
    ),
)


def server(input: Inputs, output: Outputs, session: Session):
  pass


app = App(app_ui, server, static_assets=current_dir / "www", debug=False)
