env_dir = env
activate = . $(env_dir)/bin/activate
python = python3
req_file = requirements.txt
module = tcad_bot

.PHONY: run
run: | $(env_dir)
	$(activate) && python -m $(module)

$(env_dir):
	$(python) -m venv $@
	$(activate) && pip install -r $(req_file)

.PHONY: clean
clean:
	rm -rf $(env_dir)
