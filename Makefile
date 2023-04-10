makev:
	docker compose up --wait --verbose

make:
	docker compose up -d --wait

down:
	docker compose down

run:
	poetry run dotenv run -- python -m conduit