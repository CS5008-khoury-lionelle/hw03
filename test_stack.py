
import unittest
from gradescope_utils.autograder_utils.decorators import number
from neugs_utils import tier, COMMON_ONE, COMMON_TWO, COMMON_THREE
import os
import subprocess



# Double check class name, remember unit tests likes it to start with Test
class TestMyStack(unittest.TestCase):
    _file : str = "tests/test_stack.out"
    _compile_command: str = f"clang -Wall tests/stack_grading_tests.c -o {_file}"
    
    def compile_code(self) -> str:
        """Compiles the code using the compile_command. 

        Returns:
            str: the decoded string of how many warnings or errors
        """
        compiled = subprocess.run(
            self._compile_command.split(), capture_output=True)
        if (compiled.stderr):
            self.fail("Code failed to compile or had warnings\n{0}".format(compiled.stderr.decode()))
        return ''

    def run_range(self, start : int , end: int) -> None:
        """Runs subprocess passing in start and end as the first two parameters 
        
        Args:
            start (int): test id of the start test
            end (int): test id of the end test
        """
        command = subprocess.run([self._file, str(start), str(end)], capture_output=True)
        if (command.stderr):
            self.fail(command.stderr.decode())

    def setUp(self) -> None:
        if not os.path.isfile(self._file):
            self.compile_code()
        return super().setUp()

    @tier(COMMON_ONE)
    @number(2.1)
    def test_compile(self) -> None:
        """Testing to make sure mystack.h compiles"""
        pass # test happens in setup

    @tier(COMMON_ONE)
    @number(2.2)
    def test_create_stack(self) -> None:
        """Testing stack creation."""
        self.run_range(1, 1)

    @tier(COMMON_ONE)
    @number(2.3)
    def test_stack_empty(self) -> None:
        """Testing stack_empty"""
        self.run_range(2, 3)
    
    @tier(COMMON_ONE)
    @number(2.4)
    def test_stack_full(self) -> None:
        """Testing stack_full"""
        self.run_range(4, 5)

    @tier(COMMON_TWO)
    @number(4.0)
    def test_stack_enqueue(self) -> None:
        """Testing stack_enqueue (if error, check size, and adding with different stack sizes)"""
        self.run_range(6, 8)

    @tier(COMMON_TWO)
    @number(4.1)
    def test_stack_dequeue(self) -> None:
        """Testing stack_dequeue (if error, check the return value, and dequeueing with different sizes)"""
        self.run_range(9, 12)

    @tier(COMMON_THREE)
    @number(6.0)
    def test_stack_size(self) -> None:
        """Testing stack_size both empty and non_empty"""
        self.run_range(13, 14)
    
    @tier(COMMON_THREE)
    @number(6.1)
    def test_memory_leak(self) -> None:
        """Testing for a memory leak (errors code may be strange)"""
        self.run_range(-1, -1)

if __name__ == '__main__':
    print("Cleaning .out files")
    subprocess.run("rm tests/*.out", shell=True)
    unittest.main()
