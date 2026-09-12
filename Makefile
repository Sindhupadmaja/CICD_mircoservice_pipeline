test:
	pytest -q

build:
	docker build -t orders-api:local .

k8s:
	kubectl apply -f k8s/
