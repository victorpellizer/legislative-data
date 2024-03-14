from src.ChallengeService import ChallengeService
from src.GetInputData import get_data


def main():
    """
    Starts the robot execution
    """
    print("Execution started")
    input_data = get_data()

    robot = ChallengeService()
    response = robot.exec(payload=input_data)

    html_file = open('output/result.html','w', encoding="utf-8")
    html_file.write(response)
    html_file.close()

main()
