# Count Renders

The script uses csv render files as input and gives render counts accourding to the given arguments.

## Getting Started

Just typing `./run.sh` should run the script once you're in the root folder. If `run.sh` does not have sudo permission on your system, 
you should use `sudo ./run.sh` or do `chmod 700 run.sh`.

## Options

-**app** *STRING* : filters output for only renders that use the given application

-**renderer** *STRING* : filters output for only renders that use the given renderer

-**failed** : includes data from failed renders in the output

## Flags

-*avgtime* : outputs the average render time in seconds

-*avgcpu* : outputs the average peak cpu

-*avgram* : outputs the average ram usage

-*maxram* : outputs the id for the render with the highest peak RAM

-*maxcpu* : outputs the id for the render with the highest peak CPU

-*summary* : outputs the result of all of the above commands, in the order listed above,
each on a separate line

## Examples
`./run.sh */path/to/files*`

`./run.sh -app *<app_name>* -avgcpu`

`./run.sh -failed -summary`
