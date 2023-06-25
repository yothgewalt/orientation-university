encoded_string: str = ""

run_length = input()
if not run_length:
    encoded_string = ""

counter: int = 1
for picker in range(1, len(run_length)):
    if run_length[picker] == run_length[picker - 1]:
        counter += 1
    else:
        encoded_string += " " + run_length[picker - 1] + " " + str(counter)
        counter = 1

encoded_string += " " + run_length[-1] + " " + str(counter)
print(encoded_string, sep=" ")
