app = "ach-server"

python_requirements()

python_library(
    name="lib",
    sources=rglobs("*.py", "static/*", "templates/*"),
    dependencies=[
        ":Django",
        ":dj-database-url",
    ],
    compatibility="CPython>=3",
)

# prep_command(
#     name="django-settings-path-env",
#     prep_args=["-n", "DJANGO_SETTINGS_MODULE=project2.config.settings"],
#     prep_environ=True,
#     prep_executable="echo",
#     scope="test",
# )

python_tests(
    name="tests",
    sources=rglobs("**/test_*.py"),
    # This glob is annoying, but needs to include test files and conftest.py
    dependencies=[
        # ":django-settings-path-env",
        ":lib",
        ":pytest-django",
    ],
    compatibility="CPython>=3",
)

