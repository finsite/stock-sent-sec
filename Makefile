.PHONY: requirements

requirements:
	pip-compile --upgrade requirements.in
	pip-compile --upgrade requirements-dev.in
