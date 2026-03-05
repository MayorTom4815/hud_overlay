release:
	nuitka --onefile --clean-cache="all" --output-dir="./builds" main.py && cp default_config.toml ./builds