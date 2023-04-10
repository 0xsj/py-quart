makev:
	docker compose up --wait

make:
	docker compose up -d --wait

down:
	docker compose down

run:
	poetry run dotenv run -- python -m conduit