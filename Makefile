IMAGE_NAME=givemesomecredit_aldisf

create_conda_dev:
	conda create -n $(IMAGE_NAME)_dev python=3.9

create_conda_serving:
	conda_create -n $(IMAGE_NAME)_serving python=3.9

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

example_request:
	curl -X 'POST' \
	'http://127.0.0.1:8888/delinquency/delinquency' \
	-H 'accept: application/json' \
	-H 'Content-Type: application/json' \
	-d '{ \
	"RevolvingUtilizationOfUnsecuredLines": 0.88551908, \
	"age": 43, \
	"NumberOfTime30_59DaysPastDueNotWorse": 0, \
	"DebtRatio": 0.177512717, \
	"MonthlyIncome": 5700, \
	"NumberOfOpenCreditLinesAndLoans": 4, \
	"NumberOfTimes90DaysLate": 0, \
	"NumberRealEstateLoansOrLines": 0, \
	"NumberOfTime60_89DaysPastDueNotWorse": 0, \
	"NumberOfDependents": 0 \
	}'
