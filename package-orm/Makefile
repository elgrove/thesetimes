lint:
	-poetry run docformatter -r --in-place --black thesetimes_orm || [ $$? -eq 3 ] # accept error code 3 as success
	poetry run black thesetimes_orm
	poetry run isort thesetimes_orm
	poetry run flake8 thesetimes_orm
	poetry run pylint thesetimes_orm

test:
	@bash -c 'poetry run pytest ; \
    EXIT_CODE=$$? ; \
    if [ -z "$$EXIT_CODE" ]; then exit 1 ; \
    elif [ $$EXIT_CODE -eq 5 ]; then exit 0 ; \
    else exit $$EXIT_CODE ; \
    fi'