# feedback-collection-system
Feedback collection system using Python Tornado

## Requirements
- python3.8
- python3-pip
- python3.8-venv

install the above by running `make install-requirements`.

install mongodb using `make install-mongo-db`

please refer `Makefile` for more utils


## Installation

Install the dependencies using the bellow command.

```bash
make prepare
```

## Running with docker
```bash
docker build -t feedback-collection-system .
```

```bash
docker run --rm -d --network host feedback-collection-system
```