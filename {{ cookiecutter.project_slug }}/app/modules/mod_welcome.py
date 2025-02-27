from shiny import Inputs, Outputs, Session, module, ui, render, reactive
from faicons import icon_svg


@module.ui
def welcome_talospy_ui():
    return ui.page_fluid(
        ui.tags.style(
            """
            body {
                background-color: #eeeeee;
            color: #f0f0f0;
            text-align: center;
            }
            .title {
                font-size: 2.5rem;
                font-weight: bold;
                color: #333;
                margin-top: 10vh;
            }
            .subtitle {
                font-size: 1.2rem;
                color: #555;
            }
            .header {
                margin-bottom: 50px;
            }
            .card {
                background-color: #ffffff;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 0 5px rgba(0, 0, 0, 0.1);
                border: 0.1px solid #ddd;
                text-align: left;
            }
            .counter {
                display: flex;
                gap: 10px;
            }
            """
        ),
        ui.div(
            ui.div(
                ui.h1("Welcome to TalosPy!", class_="title"),
                ui.h2("Your Shiny Python app is up and running.", class_="subtitle"),
                class_="header",
            ),
            ui.layout_columns(
                ui.card(
                    ui.div(
                        ui.h2("Counter: "),
                        ui.h1(ui.output_text("counter")),
                        class_="counter",
                    ),
                    ui.input_action_button(
                        id="increment",
                        label="Add",
                        icon=icon_svg("plus"),
                    ),
                ),
                ui.a(
                    ui.card(
                        ui.h2(icon_svg("book"), "Read the doc"),
                        ui.h5("Click here to read the TalosPy documentation."),
                    ),
                    href="https://thinkr-open.github.io/talospy/",
                    target="_blank",
                    style="text-decoration: none; color: #000000",
                ),
                col_widths=(6, 6),
            ),
        ),
    )


@module.server
def welcome_talospy_server(input: Inputs, output: Outputs, session: Session):
    val = reactive.value(0)

    @reactive.effect()
    @reactive.event(input.increment)
    def _():
        val.set(val() + 1)

    @render.text
    def counter():
        return val()
