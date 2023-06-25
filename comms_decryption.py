encrypt = str(92813912398100282033745980018127)

alphabets = {
    1: "A",
    2: "B",
    3: "C",
    4: "D",
    5: "E",
    6: "F",
    7: "G",
    8: "H",
    9: "I",
    10: "J"
}

first_dataset: str = ""
for picker in range(3, len(encrypt), 7):
    first_dataset += str(encrypt[picker])

second_dataset: str = ""
for picker in range(7, len(encrypt), 5):
    second_dataset += str(encrypt[picker])

sum_of_dataset: int = (int(first_dataset) + int(second_dataset)) + 10000

first_selected: str = str(sum_of_dataset)[-4] + str(sum_of_dataset)[-3] + str(sum_of_dataset)[-2]

unit_selected: int = 0
for picker in range(0, len(str(first_selected))):
    unit_selected += int(str(first_selected)[picker])

unit_selected = int(str(unit_selected)[-1]) + 1
if unit_selected in alphabets:
    print(first_selected + alphabets[unit_selected])
