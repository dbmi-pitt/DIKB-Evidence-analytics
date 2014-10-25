
make-log:
	vim `tla make-log` 

start-ddi-search-engine:
	/usr/bin/env twistd web --port 2022 --logfile /home/boycerd/DI_DIR/python/ddi_search_engine/twistd.log --path /home/boycerd/DI_DIR/python/ddi_search_engine

stop-ddi-search-engine:
	kill `cat twistd.pid`

