# git_math_done
Hack Princeton

Inspiration

For many first years, keeping up with the course load and the fast-paced university lectures can be a challenge. For many, taking good study notes in mathematics lectures while listening to a professor can be quite challenging. To solve this problem I created the application '\Git'_Math_Done: A tool that converts technical speech into readable Latex format.

What it does

To make it short and sweet, Git_Math_Done is a translation tool that converts plain English Speech Input into readable Latex text. It incorporates algorithms that find specific mathematical symbols/terminology and converts it to Latex. Ex: Speech Input : ("Limit of X approaches 0"), Latex Text Output : {$\lim_{x\to\0}

The application reads in the speech input and tries to finds any functions/equations/mathematical terminology in the speech input stream. Once it finds possible matches, it converts parts of the string into Latex. Once the entire speech input stream has been parsed, the data is stored in a text file, the contents of the file can be copied into Microsoft Word or other applications that support Latex.

How I built it

Git_Math_Done uses Microsoft Azure's Speech Recognition API for converting the speech input stream. Git_Math_Done is written in Python and the output stream is written in Latex.

Challenges I ran into

The biggest challenge with this project was identifying an equation in an input stream. As intellectuals, most of us who have taken math courses in their lives can identify a normal mathematical equation. However, a computer might treat any equation as a regular string. The toughest challenge in this project was truly identifying functions hidden in a string. In order to solve this problem, I wrote a machine learning algorithm where the application finds the most common variable name in a given area. Using this peripheral, the application scans for more words in the input stream such as 'equals', 'of', 'function'.

Accomplishments that I'm proud of

This project can identify and 'graph' a function if the method is ever called. This allows the user to produce graphs of any functions they are working with.

What I learned

Throughout the course of this hackathon, I learned a variety of new technologies. The most exciting one was Bing Speech Recognition API, which allowed me to translate English into mathematical terms. I was also introduced to Latex, which made representing and graphing much simpler. I hope to use it more often in the future.

What's next for Git Math Done

I will be using Wolfram Alpha API to do computation when asked to compute the answer to a particular question. Lastly, I will be making a plug-in for this project, so the user can use this function in their word documents.
