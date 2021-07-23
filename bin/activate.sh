export PYTHONBREAKPOINT=ipdb.set_trace

alias pe='pipenv'
alias ped='PIPENV_DEV=1 pe'

test() {
	pe run pytest "$@"
}

console() {
	pe run ipython
}

refresh() {
	source $BASH_SOURCE;
}
