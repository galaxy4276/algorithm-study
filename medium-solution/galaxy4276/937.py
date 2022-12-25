from typing import List


def reorder_log_files(logs: List[str]) -> List[str]:
    letters, digits = [], []
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)
    test = letters[0]
    print(f'{test.split()[1:]}, {test.split()[0]})')
    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    digits.sort()
    return letters + digits


if __name__ == '__main__':
    logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
    result: List[str] = reorder_log_files(logs)
    print(result)
