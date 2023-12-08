"""
Test Script for Main Code and Lib Files.
"""

from main import main
import os


def test_main():
    # count the number of files in the directory before execution
    initial_count = len(os.listdir("mlruns/0"))

    # ececute the code
    main()

    # count the number of files in the directory after execution
    final_count = len(os.listdir("mlruns/0"))

    # assert the difference
    assert final_count > initial_count


if __name__ == "__main__":
    test_main()
    pass
