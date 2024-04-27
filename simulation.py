import sys

def main():
    def Logistic_Equation(initial_pop, growth_rate, iterations, output_file_name = 'output.txt'):
        """
        calculates population over time
        growth_rate * pop_percent * (1 - pop_percent)
        x amount of times
        outputs to text file
        
        """

        output_file = open(f'{output_file_name}', "w")

        def recalculate_pop(population):
            #Used to find new pop and update cuttent_pop variable on lines 32-33
            new_pop = round(growth_rate * population * (1-population), 3)
            return(new_pop)

        current_pop = initial_pop
        for i in range(iterations):
            if(i == 0):
                output_file.writelines(f'{i+1} {current_pop} "\n"')
            else:
                output_file.writelines(f'{i + 1} {recalculate_pop(current_pop):.3f}\n')
                current_pop = recalculate_pop(current_pop)

        output_file.close()

    #Arguments list 1-4 and not 0-3 because "simulation.py" counts as an argument on the command line
    initial_pop = float(sys.argv[1])
    growth_rate = float(sys.argv[2])
    iterations = int(sys.argv[3])
    output_file = sys.argv[4]

    Logistic_Equation(initial_pop, growth_rate, iterations, output_file)

main()