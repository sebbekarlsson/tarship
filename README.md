# tarship
> Deploy `.tar.gz` files along with a `bash` script to any remote.

## Usage
### Configuring your project
> To use this tool you must first make sure that your project has a  
> `instructions.sh` file at the top root of the directory. This file will
> be executed once the `.tar.gz` file has reached the remote.

### Using the CLI
> Now to use the cli, stand where your `instructions.sh` file is and run:

    tarship --host=<ip> --user=<user>

> This will create a neat `.tar.gz` package for you and send it to the host,  
> and execute the `instructions.sh` on the host.


## Installation
> To install tarship, you can just clone down this repository and run:

    python setup.py install
