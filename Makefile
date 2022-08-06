TMP = .tmp

FUNCY_DIR = $(TMP)/funcy
FUNCY_VERSION = 1.17

FUNCY_STUBS_DIR = funcy-stubs

update-funcy: 
	mkdir -p $(TMP)
	git -C $(FUNCY_DIR) checkout tags/$(FUNCY_VERSION) || git clone https://github.com/Suor/funcy.git $(FUNCY_DIR)

stubtest: update-funcy
	cp -r $(FUNCY_STUBS_DIR)/* $(FUNCY_DIR)
	cd $(TMP) && python -m mypy funcy