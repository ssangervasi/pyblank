export PYTHONBREAKPOINT=ipdb.set_trace

alias pe='PIPENV_DEV=1 python3.9 -m pipenv'

run() {
	pe run blank
}

tests() {
	pe run pytest "$@"
}

console() {
	pe run ipython
}

refresh() {
	source $BASH_SOURCE;
}
