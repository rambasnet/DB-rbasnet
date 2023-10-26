all: test clean

run:
	python gradebook.py

test:
	pytest --verbose --color=yes .

clean:
	rm -rf __pycache__
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	rm -rf .hypothesis
	rm -rf __pycache__
	rm -rf .pytest_cache
	rm -rf test_utility/__pycache__
	rm -rf utility/__pycache__

