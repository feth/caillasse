ALLPY = $(wildcard *.py)
PY_ = $(filter-out %_rc.py, $(ALLPY))
PY = $(filter-out %_ui.py, $(PY_))
PYC = $(PY:.py=.pyc)
PY_TESTED = $(PY:.py=_py_tested)
UI = $(wildcard *.ui)
UIPY = $(UI:.ui=_ui.py)
QRC = $(wildcard *.qrc)
RCPY = $(QRC:.qrc=_rc.py)
FR_TS = caillasse_fr.ts
FR_QM = caillasse_fr.qm
RESOURCES = $(wildcard images/*) $(FR_QM)
DIR_NAME = $(notdir $(CURDIR))
COVER_HTML_DIR = ../cover/$(DIR_NAME)


all: $(UIPY) $(RCPY)
.PHONY: all

clean:
	@rm $(UIPY)
	@rm $(RCPY)
	@rm *.pyc
	@rm *.qm
.PHONY: clean
.IGNORE: clean

$(RCPY): $(RESOURCES)

compile: all $(PYC) $(FR_QM)
.PHONY: compile

%.del: %
	rm $^
.PHONY: %.del

%_ui.py: %.ui
	pyuic4 $< -o $@

%_rc.py: %.qrc resources $(QM_FR)
	pyrcc4 $< -o $@

%.pyc: %.py
	pycompile $< $@

#translation into french: binary embedded into qrc
%.qm: %.ts
	lrelease $< -qm $@

#translation into french: use linguist to edit
%.ts: $(UI) $(PY)
	pylupdate4 $? -ts $@
