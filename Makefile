PROJECT=varroa
REPO=registry.rc.nectar.org.au/nectar
DESCRIBE=$(shell git describe --tags)
IMAGE_TAG := $(if $(TAG),$(TAG),$(DESCRIBE))
IMAGE=$(REPO)/$(PROJECT):$(IMAGE_TAG)
BUILDER=docker
BUILDER_ARGS=
build:
	echo "Derived image tag: $(DESCRIBE)"
	echo "Actual image tag: $(IMAGE_TAG)"
	rm -rf dist/
	python3 setup.py sdist
	$(BUILDER) build $(BUILDER_ARGS) -t $(IMAGE) .
push:
	$(BUILDER) push $(IMAGE)
.PHONY: build push
