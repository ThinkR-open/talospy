# TalosPy <img src="assets/logo.png" align="right" alt="talospy logo" style="height: 140px;"></a>

[![Cookiecutter](https://img.shields.io/badge/Templating%20app%20with-Cookiecutter-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter)
![Python](https://img.shields.io/badge/Language-Python-blue)

Install [pipx](https://pipx.pypa.io/stable/installation/)

1. Install cookiecutter

```bash
pipx install cookiecutter
```

2. Use a Github template

```bash
pipx run cookiecutter gh:ThinkR-open/talospy
```

3. Answer the questions

4. Install and use poetry shell

```bash
poetry self add poetry-plugin-shell
```

```bash
cd name_of_your_project
poetry shell
```

5. Install the dependencies

```bash
poetry install
```

6. Run the application

```bash
poe runshiny
```
