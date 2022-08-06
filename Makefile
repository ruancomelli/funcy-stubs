TMP=.tmp
FUNCY_VERSION=1.17

update-funcy: 
	mkdir -p $(TMP)
	git -C $(TMP)/funcy checkout tags/$(FUNCY_VERSION) || git clone https://github.com/Suor/funcy.git $(TMP)/funcy

stubtest: update-funcy
	cp -r funcy $(TMP)
	cd $(TMP) && python -m mypy.stubtest funcy