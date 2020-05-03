# algo-generator

Library to automatically generate the underlying algorithm of a Python script.

#### Instructions to run the code -
1. Clone the repo
2. Create a virtual environment and install the dependencies present in requirements.txt
3. Run the **algo_generator.py** script and pass the path of the python file for which the algorithm has to be generated (as a command line argument)

eg - python algo_generator.py /home/ubuntu/some_random_script.py

#### Configurations -
The file **configurations.py** can be used to configure the behaviour of the library.

1. To export the generated algorithm in a text file, set **EXPORT_TO_FILE = True**
2. To generate an audio of the algorithm, set **GENERATE_AUDIO = True**
3. To display line numbers for the output algorithm, set **SET_LINE_NUMBER = True**
