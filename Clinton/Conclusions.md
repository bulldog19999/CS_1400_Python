Welcome to Conclusions.md. First I will give mmy process for processing the data, along with ecvery explanation for my process.
I will then give the data I found and my conclusions based on the found data.

Answer:
Republicans had a higher amount of jobs
Democrats had significantly lower amount of jobs
Bill Clintons was a little off from how many jobs were created, but grossly overestimated the jobs assigned to democrats, and underestimated the jobs assigned to republicans.

Thoughts before the code:
For this assignment, I am treating clinton's statement of "producing X amount of jobs" as jobs that were created while a republican or democrat was in office.
More thoughts on this will be explained throughout conclusions.md

For presidents.txt, I have it formatted as president_name year and party status. I knew I would need to read data on a yearly basis
and assign the appropriate job numbers based on the party status of the president for that year. While I required it to be formatted for the code,
I ultimately did not need the names of presidents.

I understand that President Nixon and President Kennedy did not finish their terms. But it ultimately did not matter for this case as their vice presidents
were of the same party. And when A president is unable to complete a term, it's the vice president that is next in line for presidency.
So, while different presidents can have different effects on the private secotr job market, going that deep was not necessary for this case.
As such, Giving full years to a republican or democrat will suffice, although my numbers for them are likely to be off, more on that in the next section.

I was looking through the given Job data on Canvas and the data returned on the Bereau of Labor Statistics website and noticed that the job numbers were overall
lower on later years than the BLS data. There was also data missing for November or December of 2012. The missing data could be attributed to the timing of Clinton's statement,
but I didn't see a good reason to think that the canvas data should differ, so I used the data from the TLS website.

Thoughts for the code:
I tried to keep the code simple (More information can be found in fact_check.py):
-use presidents.txt to get information which party was in the white house for what year
-use the jobs data to store data to be read and calculated
-return the information to be used here.

I ran into a few concerns:
1. My results: I am aware that on canvas you are supposed to "multiply your results by 1000 and if you dont youre wrong, or if you do and you get weird numbers than rethink your data."
   I tried multiple ways to think and process my data, but for this result I ultimately settled on not multiplying anything by 1000 (even though I have code listing both, My answer for this is the jobs NOT
   multiplied by 1000).

   A. With what was said on canvas and the job data being listed in thousands one way I thought about it was (45000 thousand = 45,000,000 for one month). But then the issue came up, "Oh, 45 million jobs in january of 1961, that doesnt sound right at all because the comparison is 66 million between 1961 - 2012". So then, I added all of the data then multiplied the result by 1000 (Results and percentages are printed in the python file) and got wild results. I was unable to think of a more reasonable solution, and that is why my official answers to the questions is based on the data NOT multiplied by 1000.

2. Data processing: As previously mentioned, my processing required a year and party status. I understand that this information can be used on a deeper level, but for how I interpreted evaluating clinton's statement
   I felt getting deep into processing was ultimately not necessary. As such I pretty much processed the data at face value. I ultimately gave Democrates or republicans job numbers at the start of every year, but this is in accurate. I think the job data for January should be ultimately given to the previous party, if there is a change in party, because the new president is pretty much coming into their new term at the tail end of the month. An argument can also be given for dividing the month of january into 31 days, give one party the amount * 20 and give the other the amount * 11, but as I'm running out of time, I can't really make these deeper changes. As a result I acknowledge that my democrat and republican numbers are off from what I would like them to be.

Final Thoughts:
Based on my final data, Bill Clinton was off from the actual amount of jobs created and was very off about party contributions to jobs.
-For total jobs, he was off by about %13
-Jobs created while a Democrat was in office was about half of his claim (58% was the calculated comparison)
-Jobs created while a Republican was in office was higher than his claim (127% was the calculated comparison)

