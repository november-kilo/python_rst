import argparse

from problems.problem_4_04 import Problem404
from problems.problem_4_05 import Problem405
from problems.problem_4_06 import Problem406
from problems.problem_4_07 import Problem407
from problems.problem_4_08 import Problem408
from problems.problem_4_09 import Problem409
from problems.problem_4_10 import Problem410
from problems.problem_4_11 import Problem411

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-p', '--problems', nargs='+')

    for _, value in arg_parser.parse_args()._get_kwargs():
        if value is not None:
            problems = []

            if '404' in value:
                problems.append(Problem404())

            if '405' in value:
                problems.append(Problem405())

            if '406' in value:
                problems.append(Problem406())

            if '407' in value:
                problems.append(Problem407())

            if '408' in value:
                problems.append(Problem408())

            if '408' in value:
                problems.append(Problem409())

            if '410' in value:
                problems.append(Problem410())

            if '411' in value:
                problems.append(Problem411())

            for problem in problems:
                problem.do_problem()
