lint:
	-poetry run docformatter -r --in-place --black main.py core tests || [ $$? -eq 3 ] # accept error code 3 as success
	poetry run black main.py core tests
	poetry run isort main.py core tests
	poetry run flake8 main.py core tests
	poetry run pylint main.py core

test:
	@bash -c 'poetry run pytest ; \
    EXIT_CODE=$$? ; \
    if [ -z "$$EXIT_CODE" ]; then exit 1 ; \
    elif [ $$EXIT_CODE -eq 5 ]; then exit 0 ; \
    else exit $$EXIT_CODE ; \
    fi'