IMAGE_NAME=givemesomecredit_aldisf

build_dev:
	docker build -t $(IMAGE_NAME)_dev:latest -f Dockerfile-analysis .

run_jupyter_dev:build_dev
	docker run --rm -it -p 127.0.0.1:8889:8889 $(IMAGE_NAME)_dev:latest

start_server:
	uvicorn main:app --port 8888

build_serving:
	docker build -t $(IMAGE_NAME)_serving:latest -f Dockerfile-serving .

serve:build_serving
	docker run --rm -it -p 8888:80 $(IMAGE_NAME)_serving:latest
