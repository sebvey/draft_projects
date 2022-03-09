docker_build_stage1:
	@echo "BUILDING STAGE1 IMAGE ..."
	@docker build -t multi-stage1 multi-stage1

docker_build: docker_build_stage1
	@echo "BUILDING FINAL IMAGE ..."
	@docker build -t multi-final .
