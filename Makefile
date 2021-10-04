# remove all cached files
clean:
	find . | grep -E "(.*_cache|__pycache__|\.pyc|\.pyo$$)" | xargs rm -rf
