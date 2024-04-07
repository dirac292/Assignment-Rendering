import jinja2 
import os
import sys
import subprocess


#Running this
# assignment 3B/PHYS\ 334/ PHYS\ 334 4 10
# assignment assignment_directory course_name assignment_number number_of_questions

script_dir = os.path.dirname(os.path.abspath(__file__))

env = jinja2.Environment(
    block_start_string = '\BLOCK{',
    block_end_string = '}',
    variable_start_string = '\VAR{',
    variable_end_string = '}',
    comment_start_string = '\#{',
    comment_end_string = '}',
    line_statement_prefix = '%-',
    line_comment_prefix = '%#',
    trim_blocks = True,
    autoescape = False,
    loader = jinja2.FileSystemLoader(script_dir)
)

path = sys.argv[1]
course_number = sys.argv[2]
assignment_number = sys.argv[3] 
question_number = sys.argv[4]
directory = "/Users/ms/" + path + "A" + assignment_number

output_path = directory + "/" + "document.tex"

if not os.path.exists(directory):
   print(f"Creating the directory at {directory}")
   os.mkdir(directory)
else:
    print("Exists")


my_variable_dict = {
    "assignment" : str(assignment_number),
    "course": str(course_number),
    "questions": int(question_number)
}


template = env.get_template('document.tex')

document = template.render(**my_variable_dict)

with open(output_path,'w') as output:
    output.write(document)
code = f"code {directory}"


subprocess.run(['code', directory])