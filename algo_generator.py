import os
import traceback
import sys
from gtts import gTTS
from generator_engine import AlgoGenerator
from constants import (LANGUAGE, FOR, WHILE, IF, ELSE, ELIF, IMPORT, FROM, PRINT, BREAK, CONTINUE, 
                       DEF, SPACE, TAB, CLASS)
from configurations import SET_LINE_NUMBER, EXPORT_TO_FILE, GENERATE_AUDIO

source_filename = sys.argv[1]
generator = AlgoGenerator()
algorithm = ""
line_number = 1

with open(source_filename) as f:
    for line in f:
        if SET_LINE_NUMBER:
            algorithm += str(line_number) + ' '

        line = line.rstrip()
        if not line:
            algorithm += "\n"  # If we find a blank line, we keep the blank line
        else:
            try:
                indentation_type = SPACE if line[0] == SPACE else TAB
                indentation_value = len(line) - len(line.lstrip())
                algorithm += indentation_type * indentation_value

                keyword = generator.get_keyword(line)

                if keyword in [FOR, WHILE]:
                    algorithm += generator.handle_loop(keyword, line)
                elif keyword in [IF, ELSE, ELIF]:
                    algorithm += line.strip().capitalize()
                elif keyword in [IMPORT, FROM]:
                    algorithm += line.strip().capitalize()
                elif keyword == PRINT:
                    algorithm += generator.get_the_value_to_print(line)
                elif keyword in [BREAK, CONTINUE]:
                    algorithm += line.strip().capitalize()
                elif keyword == DEF:
                    algorithm += generator.handle_function_definition(line)
                elif keyword == CLASS:
                    algorithm += generator.handle_class_declaration(line)
                elif "==" not in line and "=" in line:
                    algorithm += generator.handle_assignment(line)
                else:
                    algorithm += line.strip()

                algorithm += "\n"

            except Exception:
                traceback.print_exc()
                print("Could not translate line number {}-{}".format(line_number, line))

        line_number += 1

if EXPORT_TO_FILE:
    with open('algo_output.txt', 'w') as f_out:
        f_out.write(algorithm)
else:
    print(algorithm)

if GENERATE_AUDIO:
    myobj = gTTS(text=algorithm, lang=LANGUAGE, slow=False)
    myobj.save("algo_generated.mp3")
    os.system("mpg321 algo_generated.mp3")
