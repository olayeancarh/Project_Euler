def get_max_prime_factor_of_a_number(num_fact):
    count = 2
    factors = []
    while num_fact != 1:
        if num_fact % count != 0:
            count += 1
        else:
            factors.append(count)
            num_fact = int(num_fact/count)
    print(max(factors))