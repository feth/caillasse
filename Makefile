RECURSE_DIRS=caillasse_pyqt
SCORIA=dist build caillasse.egg-info

install: recurse
	python setup.py install

recurse: $(subst ,_recurse,$(RECURSE_DIRS))
	@echo $<

.PHONY: recurse

%_recurse: %
	make -C $<

.PHONY: %_recurse

clean:
	@rm -rf $(SCORIA)
	make -C $< clean

.PHONY: clean
.IGNORE: clean
