from shiny import Inputs, Outputs, Session, module, ui
from faicons import icon_svg


@module.ui
def welcome_talospy_ui():
    return (
        ui.div(
            ui.div(
                icon_svg("python", height="50px"),
                ui.tags.a("{talospy}", href="https://github.com/ThinkR-open/talospy", target="_blank"),
                class_="container-fluid",
            ),
        ),
    )


@module.server
def welcome_talospy_server(input: Inputs, output: Outputs, session: Session):
    pass
