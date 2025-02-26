from shiny.run import ShinyAppProc
from playwright.sync_api import Page, expect
from shiny.pytest import create_app_fixture

app = create_app_fixture("../../app.py")


def test_app(page: Page, app: ShinyAppProc):
    page.goto(app.url)
    response = page.request.get(app.url)
    expect(response).to_be_ok()
    expect(page).to_have_title("{{ cookiecutter.project_name }}")
