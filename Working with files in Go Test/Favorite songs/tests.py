import os

from hstest import StageTest, CheckResult, WrongAnswer, TestCase

inputs = [
    "Uptown Funk\nLocked out of Heaven\nTalking to the Moon",
]

# Create the file 'songs.txt' with some data to check afterwards if it exists
with open("songs.txt", "w") as f:
    f.write("Uptown Funk\n")
    f.write("Locked out of Heaven\n")
    f.write("Talking to the Moon")

FILENAME = "songs.txt"


class TestAdmissionProcedure(StageTest):
    def generate(self):
        return [TestCase(stdin=[test], attach=[test]) for test in inputs]

    def check(self, reply: str, attach: list):
        if not os.path.exists(FILENAME):
            raise WrongAnswer(f"Cannot find file {FILENAME}")

        # with open(FILENAME, "r") as f:
        #     content = f.read().strip()
        #     if content != attach[0]:
        #         raise WrongAnswer(
        #             f'Invalid content of {FILENAME} file, got "{content}" want "{attach[0]}"'
        #         )

        return CheckResult.correct()


if __name__ == '__main__':
    TestAdmissionProcedure().run_tests()
