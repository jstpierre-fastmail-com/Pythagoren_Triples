import math


# return every pythagorean triples as his simplest form and without repeating it.
def get_pythagorean_triples(n):
    
    
    output = ''
    num_list = []
    for i in range(1, n + 1):
        for j in range(1, round(i * (2 * i / 3))):
            if math.sqrt(i ** 2 + j ** 2) == round(math.sqrt(i ** 2 + j ** 2)):
                if str(i) + ',' + str(j) in num_list or str(j) + ',' + str(i) in num_list:
                    continue
                else:
                    output += (str(i) + '^2 + ' + str(j) + '^2 = ' + str(
                        round(math.sqrt(i ** 2 + j ** 2))) + '^2' + "\n")
                    for k in range(1, round(n / i) + 1):
                        num_list.append(str(j * k) + ',' + str(i * k))
    return output


num_input = int(input("Until which number do you want to get Pythagorean Triples ?\n"))
pythagorean_triples_string = get_pythagorean_triples(num_input)
pythagorean_triples_length = len(pythagorean_triples_string.split('\n')) - 1

print(f"\nHere's every pythagorean triples below the number {num_input}.\n\n" + pythagorean_triples_string + '\n')

print(f'that makes {pythagorean_triples_length} of them')
