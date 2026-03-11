# How to run:
## Virtual environment setup
1. Create a virtual environment with `python3 -m venv venv_name`
2. Activate the virtual environment with `source ./venv_name/bin/activate` on macos/linux. IDK what it is on windows tbh.
3. Install dependencies (just numpy) with `pip install -r requirements.txt`

## Providing input
Input is in the form of JSON files
There are some test cases in ./test_cases/ 
To create your own test case, create a JSON file `touch <file_name>.json` and 
fill it with whatever configuration you'd like to test. The format matches 
The spec from the assignment. Look at the provided test cases to see the exact 
format.

## Running the program
With the virtual environment activated, run with:
```
python3 main.py [-v] <filepath>
```
Where file path is the path of the json file you'd like to test.
The optional `[-v]` flag allows for verbose output.
Example:
```
python3 main.py -v ./test_cases/input3.json
```
