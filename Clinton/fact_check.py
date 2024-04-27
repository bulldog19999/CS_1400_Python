"""
Name: Michael Brumwell
Date: 4/27/2024

README:
This is fact_check.py, below are instructions on how to properly use this file
1. Create a folder which only contains fact_check.py, Presidents.txt, and BLS_Private.csv
2. Ensure Presidents.txt and BLS_Private.csv are spelled correctly, otherwise the program will error out
2.A. Ensure BLS_Private is downloaded directly from the BUreau of Labor Statistics website: 1961-2012, csv, private jobs, seasonally adjusted
3. The Contents of Presidents.txt is formatted as the following: President_Last_Name Year Party_Status
3.A. Party Status is represented as a Letter, D or R
4. Repeat Steps 2 and 3, this program is designed for the correctly named files are in the SAME WORKING DIRECTORY as the python file
5. This program does not write output to Conclusions.md, but the data printed at the end is used to form my conclusions

!!!The purpose of this program is to use BLS_Private and Presidents.txt to check Bill Clinton's statement, summerized below:
-66000000 (66 Million) jobs were created between 1961 and 2012 (Dems 42 million jobs / Rep 24 million jobs)

"""

import csv

def main():
    yearly_jobs = {}               #A dictionary where years are keys and values is a LIST of job values per month
    yearly_party_status = []       #A set of sets containing the year(or date) and party status - parties may change between years - update as needed

    job_data = "BLS_private.csv"
    president_data = "Presidents.txt"

    def determine_party_status(p_data):
        """
        This function is responsible for:
        1. Reading Presidents.txt
        2. splitting each line
        3. storing a set of information into the list yearly_party_status
        3.A. The data is stored as a set containing a year and a letter representing party status (D or R)
        """
        
        try:
            with open(p_data, "r") as pres_data:
                for line in pres_data:
                    info = line.split()
                    yearly_party_status.append((info[1], info[2]))
        except:
            print(f'{president_data} was not found')
            quit()
    
    def get_job_numbers(j_data):
        """
        This function is responsible three things:
        1. Reading the job csv file
        2. Spliting each value by commas -> creating a list of data
        3. Popping the first element of every row -> they are years and need to be removed from this data for calculation purposes
        """
        
        try:
            with open(j_data, "r") as jobs_data:
                jobs_by_year = csv.reader(jobs_data, delimiter=' ')
                for month in jobs_by_year:
                    for jobs in month:
                        jobs_rows = jobs.split(",")
                        yearly_jobs[jobs_rows.pop(0)] = [jobs_rows]
        except:
            print(f'{job_data} was not found')
            quit()

    def assign_job_numbers(yearly_job_data, yearly_party_data):
        """
        With a set to store party data (yearly_party_data) and a dict to store job numbers (yearly_job_data), the funciton works like this:
        -Access the set which contains a year and party assignment
        -Use the year as a key to read the values of the job data dict
        --Because the dictionary values are a list within a list, they will be access like this -> yearly_job_data[p_data[0]][0]
        --p_data[0] is the year owned by democrates or republicans, which is also the key for job data (yearly_data)

        -the jobs will be assigned to a total and to a party bases on the party data's second value (D or R)
        """
        democrat_jobs = 0
        republican_jobs = 0
        total_jobs = 0

        #get party information from set
        for p_data in yearly_party_data:
            for jobs in yearly_job_data[p_data[0]][0]:
                total_jobs += int(jobs)

                #Add jobs to appropriate party
                if(p_data[1] == "D"):
                    democrat_jobs += int(jobs)
                else:
                    republican_jobs += int(jobs)

        
        print(f'Total private sector jobs created between 1961-2012: {total_jobs}')
        print(f'Jobs created while a democrat was president: {democrat_jobs}')
        print(f'Jobs created while a republican was president: {republican_jobs}')
        print(f'Total private sector jobs created * 1000 between 1961-2012: {total_jobs * 1000}')
        print(f'Jobs created * 1000 while a democrat was president: {democrat_jobs * 1000}')
        print(f'Jobs created * 1000 while a republican was president: {republican_jobs * 1000}')
        print(f'Percentage of jobs created vs Clinton\'s statement of 66 million jobs produced: {(total_jobs/66000000)*100:.2f}%')
        print(f'Percentage of Democrat "produced" jobs created vs Clinton\'s statement of 42 million: {(democrat_jobs/42000000)*100:.2f}%')
        print(f'Percentage of Republican "produced" jobs created vs Clinton\'s statement of 24 million: {(republican_jobs/24000000)*100:.2f}%')
        print(f'Percentage of jobs created * 1000 vs Clinton\'s statement of 66 million jobs produced: {((total_jobs * 1000)/66000000)*100:.2f}%')
        print(f'Percentage of Democrat "produced" jobs created * 1000 vs Clinton\'s statement of 42 million: {((democrat_jobs*1000)/42000000)*100:.2f}%')
        print(f'Percentage of Republican "produced" jobs created * 1000 vs Clinton\'s statement of 24 million: {((republican_jobs*1000)/24000000)*100:.2f}%')

    determine_party_status(president_data)
    get_job_numbers(job_data)
    assign_job_numbers(yearly_jobs, yearly_party_status)

if(__name__ == "__main__"):
    main()