IMAGE_NAME=bball_app
DB_PATH=/app/src/data/bball.db

.PHONY=build notebook interactive run \
	db_clean db_create db_load db_rm db_interactive

COMMON_DOCKER_FLAGS= \
	-v $(shell pwd):/app/src \
	-e FLASK_DEBUG=1 \
	-e FLASK_ENV=development \
	-e DB_PATH=$(DB_PATH) \
	-e DATA_DIR=/app/src/data \

build:
	docker build . -t $(IMAGE_NAME)

interactive: build
	docker run -it \
	$(COMMON_DOCKER_FLAGS) \
	$(IMAGE_NAME) /bin/bash

notebook: build
	docker run -it -p 8888:8888 \
	$(COMMON_DOCKER_FLAGS) \
	$(IMAGE_NAME) \
	jupyter notebook --allow-root --no-browser \
	--port 8888 --ip=0.0.0.0

flask: build
	docker run -it -p 4000:5000 \
	$(COMMON_DOCKER_FLAGS) \
	$(IMAGE_NAME)

db_create: build
	docker run $(COMMON_DOCKER_FLAGS) $(IMAGE_NAME) \
		python /app/src/app/data_utils/db_manage.py db_create

db_load: build
	docker run $(COMMON_DOCKER_FLAGS) $(IMAGE_NAME) \
		python /app/src/app/data_utils/db_manage.py db_load

db_rm: build
	docker run $(COMMON_DOCKER_FLAGS) $(IMAGE_NAME) \
		python /app/src/app/data_utils/db_manage.py db_rm

db_clean: build
	docker run $(COMMON_DOCKER_FLAGS) $(IMAGE_NAME) \
		python /app/src/app/data_utils/db_manage.py db_clean

db_interactive: build
	docker run -it $(COMMON_DOCKER_FLAGS) $(IMAGE_NAME) \
	sqlite3 -column -header $(DB_PATH)

autodoc: build
	docker run -it -p 4040:4040 \
	$(COMMON_DOCKER_FLAGS) \
	$(IMAGE_NAME) \
	mkdocs serve --dev-addr 0.0.0.0:4040 -f /app/src/api-docs/mkdocs.yml

test: build
	docker run \
	$(COMMON_DOCKER_FLAGS) \
	$(IMAGE_NAME) \
	pytest --cov=app /app/src/test/test.py --cov-report=term-missing -v