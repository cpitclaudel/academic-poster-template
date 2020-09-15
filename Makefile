dist/poster.css: poster.less
	lessc --strict-units=on $< $@

dist/%/:
	mkdir -p dist/$*

dist/%/poster.css: dist/poster.css | dist/%/
	ln -f -s ../poster.css $@

dist/%/poster.html: examples/%.jinja2 poster.jinja2 dist/%/poster.css | dist/%/
	./render.py $< $@

clean:
	rm -r dist/

.SECONDARY:
