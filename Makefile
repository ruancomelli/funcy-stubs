TMP = .tmp

FUNCY_DIR = $(TMP)/funcy
FUNCY_VERSION = 1.17

FUNCY_STUBS_DIR = funcy-stubs

MYPY = pdm run mypy

update-funcy: 
	mkdir -p $(TMP)
	git -C $(FUNCY_DIR) checkout tags/$(FUNCY_VERSION) \
		|| git clone https://github.com/Suor/funcy.git $(FUNCY_DIR) \
		&& git -C $(FUNCY_DIR) checkout tags/$(FUNCY_VERSION)

stubtest: update-funcy
	cp -r $(FUNCY_STUBS_DIR)/* $(FUNCY_DIR)/funcy
	$(MYPY) $(FUNCY_DIR)
