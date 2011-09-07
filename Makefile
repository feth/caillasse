SCORIA=dist build caillasse.egg-info

install:
	python setup.py install

clean:
	rm -fr $(SCORIA)
