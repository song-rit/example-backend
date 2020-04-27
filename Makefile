.PHONY: run
run:
	@uwsgi --http-socket 0.0.0.0:8080 --home ~/.virtualenvs/playground --chdir hello_world --module hello_world.wsgi:application --check-static ./
