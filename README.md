# Covid-19
Introduction To The Project
COVID-19 outbreaks only affect the lives of people, they result in a negative impact on the economy of the 
country. On Jan. 30, 2020, it was declared as a health emergency for the entire globe by the World Health 
Organization (WHO). By Apr. 28, 2020, more than 3 million people were infected by this virus and there 
was no vaccine to prevent. The WHO released certain guidelines for safety, but they were only precautionary 
measures. The use of information technology with a focus on fields such as data Science and machine 
learning can help in the fight against this pandemic. It is important to have early warning methods through 
which one can forecast how much the disease will affect society, on the basis of which the government can 
take necessary actions without affecting its economy. In this chapter, we include methods for forecasting 
future cases based on existing data. Machine learning approaches are used and two solutions, one for 
predicting the chance of being infected and other for forecasting the number of positive cases, are discussed. 
A trial was done for different algorithms, and the algorithm that gave results with the best accuracy are 
covered in the report. 
In this era of automation, artificial intelligence and data science have important role in the health care 
industry. These technologies are so well-connected that medical professionals can easily manage their roles 
and patient care. All health care organizations work hard to develop an automated system that can be used 
to accept the challenges faced in health care. Scientists are working on machine learning (ML) to develop 
smart solutions to diagnose and treat disease. ML is capable of detecting disease and virus infections more 
accurately so that patients' disease can be diagnosed at an early stage, the dangerous stages of diseases can 
be avoided, and there can be fewer patients. In the same manner, ML can be used to automate the task of 
predicting COVID-19 infection and help forecast future infection tallies of COVID-19. In this project, we 
included methods for forecasting future cases based on existing data. ML approaches are used and two 
solutions, one for predicting the chances of being infected and other for forecasting the number of positive 
cases, are discussed.

• Specifications
The project deeply focuses on the DETAILS ABOUT COVID which means the Total Positive 
Cases, Death Record, Recovered Cases Records
➢ Country/Region, including all the states of India which were threatened by the global 
Pandemic and were under its impact for a long time including the present dates.
➢ Date, includes Date-wise details of the cases including time, month for specific state in India
➢ Provinces are the provinces of a specific state were covered which were affected during the 
4
pandemic
➢ Recovered Cases, the count of Recovered Cases per Province covering a certain state datewise
➢ Confirmed Cases, the count of Confirmed Cases per Province covering a certain state datewise
➢ Confirmed Deaths, the count of Confirmed Deaths per Province covering a certain state datewis

• Features
1. Live Rates
The project shall cover widely a range of “Confirmed Cases”, “Recovered Cases” and “Confirmed 
Deaths” profiles of each Province, Country according to 
➢ Date Wise Confirmed Cases, Recovered Cases and Deaths
➢ Month Wise Details 
➢ Year Wise Details
2. Covid Analysis
The project will widely range to Covid Analysis using previous predictions with the concept of Supervised 
Learning and Next Strong Support Rate. It shall also include the chances of steady rate recovery of a certain 
patient. 
Using two simple mathematical epidemiological models—the Susceptible-Infectious-Recovered model and 
the log-linear regression model, we model the daily and cumulative incidence of COVID-19.
3. Covid Prediction Graph
The methodology consists of 3 steps, first one is the data collection. We have collected the dataset from 
Kaggle, second step is to generate a dynamic map of expansion of Covid-19 from the date of 22nd January 
2020 till 7 th July 2021 globally. Basically, our study period was 3 months and we analyzed and visualized 
the spreading of the virus country-wise as well as globally during the study period with confirmed cases, 
recovered cases and deceased. Finally, we predicted the expansion of the virus globally with the help of 
plotly and prophet python library. Prediction is a typical data science exercise that helps the administration 
with function planning, objective setting, and anomaly detection. Seaborn Python library was used to 
develop a Graphs to visualize how the pandemic virus is spreading all over the globe, country-wise as well 
as continent-wise. This dynamic map will show how it varies day by day with the help of legend.
5
➢ Polynomial Regression
Polynomial Regression is a regression algorithm that models the relationship between a 
dependent(y) and independent variable(x) as nth degree polynomial. It is also called the special case of 
Multiple Linear Regression in ML. Because we add some polynomial terms to the Multiple Linear regression 
equation to convert it into Polynomial Regression The dataset used in Polynomial regression for training is 
of non-linear nature. It makes use of a linear regression model to fit the complicated and non-linear functions 
and datasets.Hence, "In Polynomial regression, the original features are converted into Polynomial features 
of required degree (2,3,..,n) and then modelled using a linear model. If we apply a linear model on a linear 
dataset, then it provides us a good result as we have seen in Simple Linear Regression, but if we apply the 
same model without any modification on a non-linear dataset, then it will produce a drastic output. Due to 
which loss function will increase, the error rate will be high, and accuracy will be decreased.
So for such cases, where data points are arranged in a non-linear fashion, we need the Polynomial Regression 
model. We can understand it in a better way using the
➢ Equation of the Polynomial Regression Model:
1. Simple Linear Regression equation: 
y = b0+b1x
2. Multiple Linear Regression equation:
 y= b0+b1x+ b2x2+ b3x3+....+ bnxn
3. Polynomial Regression equation:
 y= b0+b1x + b2x
2+ b3x
3+....+ bnx

• Home Page
It is the first page that is encountered by the user on connecting to 127.0.0.1:8000/main/. It includes all 
the other modules and the live details of Covid Patients including Recovered Cases, Confirmed Cases and 
Number of Deaths in a specified region.
It includes the following modules:
➢ World Statistics
It displays the Live information about all the countries in the world that have been affected by the 
global pandemic which is taken with reference from World Health Organization (WHO). It also 
displays the list of top 10 countries in the world in terms of Cases and respective Deaths per 
country.
➢ Visualization Menu
This is the most important section for the project. It focuses on Machine Learning Concepts like 
plotting graphs on the following topics:
• Plot For Analyzing Different Cases Of A Specified State For 2020-2021
• Plot For Analyzing Different Cases Of A Specified State For A Specified Year
• Plot For Analyzing Different Cases Of A Specified State For A Specified Month Of A 
Specified Year
• Plot For Analyzing Cases of A State Within A Given Span Of Months And Specified Year
• Plot For Analyzing Comparison of different states for selective years as per case status upto 
10 states
• Plot For Analyzing Comparison of two different states for all years as per case status
• Plot For Analyzing Comparison of 2 different states for month slots for specified year
➢ Information About Corona Virus
It includes the following points:
• How Virus Spreads
1. Human Contact
2. Air Transmission
3. Contaminated Object
• Corona Virus Symptoms
1. Coughing And Sneezing
2. Shortness Of Breath
7
3. Confusion
4. Hot Fever
5. Strong Headache
6. Sore Throat
• Corona Virus Do’s And Don’ts
➢ Top FAQ’s Regarding Covid
This Sections include all the top questions that rise about Covid 19 taken from different sources 
and answered precisely by Experts.
➢ Most Popular Blogs
It lists the most popular blogs which acknowledge the user about Covid-19 Causes, Preventions.
➢ WHO’S Director General Message
This section includes message by Dr Tedros Adhanom Ghebreyesus, Director-General of the 
World Health Organization.
➢ WorldWide Live Rates
It includes the Cases, Deaths, Recovered Cases Worldwide.
8
HARDWARE AND SOFTWARE REQUIREMENTS
• Hardware Requirements
1. Any PC Processor
2. 512 GB RAM
3. Keyboard and Mouse
4. Internet Connection
• Software Requirements
5. Any Operating System: Windows 10
6. Web Browser
7. Spyder
8. Sublime Text

• HTML
HyperText Markup Language (HTML) is a markup language for creating a webpage. Webpages are 
usually viewed in a web browser. They can include writing, links, pictures, and even sound and video. 
HTML is used to mark and describe each of these kinds of content so the web browser can display them
correctly.
• CSS3
Cascading Style Sheets, fondly referred to as CSS, is a simple design language intended to simplify 
the process of making web pages presentable.CSS handles the look and feel part of a web page. Using 
CSS, you can control the color of the text, the style of fonts, the spacing between paragraphs, how columns 
are sized and laid out, what background images or colors are used, layout designs,variations in display for 
different devices and screen sizes as well as a variety of other effects.
CSS is easy to learn and understand but it provides powerful control over the presentation of an 
HTML document. Most commonly, CSS is combined with the markup languages HTML or 
XHTML.
➢ Advantages of CSS
CSS saves time
Pages load faster
Easy maintenance
Superior styles to HTML
Multiple Device Compatibility
Global web standards
• Bootstrap
Bootstrap is the most popular front-end framework in the recent time. It is sleek, intuitive, and powerful 
mobile first front- end framework for faster and easier web development. 
10
BACK END
• PYTHON
Python is a high-level, interpreted, interactive and object-oriented scripting language. Python is 
designed to be highly readable. It uses English keywords frequently where as other languages use 
punctuation, and it has fewer syntactical constructions than other languages.
➢ Python is Interpreted − Python is processed at runtime by the interpreter. You do not need to 
compile your program before executing it. This is similar to PERL and PHP.
➢ Python is Interactive − You can actually sit at a Python prompt and interact with the
interpreter directly to write your programs.
➢ Python is Object-Oriented − Python supports Object-Oriented style or technique of 
programming that encapsulates code within objects.
➢ Python is a Beginner's Language − Python is a great language for the beginner-level 
programmers and supports the development of a wide range of applications from simple text 
processing to WWW browsers togames.
➢ Advantages:
1. Free and Open Source
2. Extensive Libraries
3. Simple and easy
4. Improves Productivity
5. Embedded
6. Readable
7. Portable
➢ Python Features:
1. Easy to code: 
Python is a high-level programming language. Python is very easy to learn the 
language as compared to other languages like C, C#, Javascript, Java, etc. It is very 
easy to code in python language and anybody can learn python basics in a few hours or 
days. It is also a developer-friendly language.
2. GUI Programming Language
Graphical User interfaces can be made using a module such as PyQt5, PyQt4, 
wxPython, or Tk in python. PyQt5 is the most popular option for creating graphical 
apps with Python.
11
3. Interpreted Language
Python is an Interpreted Language because Python code is executed line by line at a 
time. like other languages C, C++, Java, etc. there is no need to compile python code 
this makes it easier to debug our code. The source code of python is converted into an 
immediate form called bytecode.
4. Dynamically Typed Language
Python is a dynamically-typed language. That means the type (for example-int, double, 
long, etc.) for a variable is decided at run time not in advance because of this feature 
we don’t need to specify the type of variable.
• DJANGO
It is an open-source toolkit for developing with HTML, CSS, and JS. Quickly prototype your ideas 
or build your entire app with our Sass variables and mixings, responsive grid system, extensive 
prebuilt components, and powerful plugins built on query. Bootstrap is a front-end library for 
designing websites and web applications. It contains HTML and CSS based design templates for 
typography, forms, buttons, navigation and other interface components, as well as optional JavaScript 
extensions.
• CASCADING STYLE SHEETS (CSS)
CSS is a style sheet language used for describing the presentation of a document written in a 
mark-up language. Along with HTML and JavaScript, CSS is a cornerstone technology used 
by most websites to create visually engaging web pages, user interfaces for web 
applications, and user interfaces for many mobile applications.
CSS is designed primarily to enable the separation of presentation and content, including 
aspects such as the layout, colours, and fonts. This separation can improve content 
accessibility, provide more flexibility and control in the specification of presentation 
characteristics, enable multiple HTML pages to share formatting by specifying the relevant 
CSS in a separate .css file, and reduce complexity and repetition in the structural content.
12
• MACHINE LEARNING
Machine learning is about extracting knowledge from data. It is a research field at the intersectionof
statistics, artificial intelligence, and computer science and is also known as predictive analyticsor 
statistical learning. The application of machine learning methods has in recent years become
ubiquitousin everyday life. From automatic recommendations of which moviesto watch, to whatfood 
to order or which products to buy, to personalized online radio and recognizing your friendsin your
photos, many modern websites and devices have machine learning algorithms at their core.When you
look at a complex website like Facebook, Amazon, or Netflix, it is very likely that everypart of the site
contains multiple machine learning models.
✓ Why Machine Learning?
In the early days of “intelligent” applications, many systems used hand coded rules of “if” and
“else” decisionstoprocessdata or adjust to userinput.Thinkof a spam filter whose job istomove
the appropriate incomingemailmessagestoa spam folder.
You could make up a blacklist of wordsthat wouldresult in an email being marked asspam. This
would be an example of using an expert-designed rule system to design an “intelligent” 
application. Manually crafting decision rules isfeasible for some applications, particularly those 
in which humans have a good understanding of the processto model.
However, using handcoded rulesto makedecisions hastwomajor disadvantages:
• The logic required to make a decision isspecific to a single domain and task. Changingthetask
even slightly might require a rewriteof the whole system.
• Designing rules requires a deep understanding of how a decision should be made by ahuman
expert

SPYDER
Spyder is an open-source cross-platform integrated development environment(IDE) for scientific 
programming in the Python language. Spyder integrates with a number of prominent packages in the 
scientific Python stack, including NumPy,SciPy, Matplotlib, pandas,IPython,SymPy and Cython, as 
well as other open-source software. It is released under the MIT license.
➢ Features 
• An editor with syntax highlighting, introspection, code completion
• Support for multiple IPython consoles
• The ability to explore and edit variablesfrom a GUI
• A Help pane able to retrieve and render rich text documentation on functions, classes and 
methods automatically or on-demand
• A debugger linked to IPdb, for step-by-step execution
• Static code analysis, powered by Pylint
• A run-time Profiler, to benchmark code
• Project support, allowing work on multiple development efforts simultaneously
• A built-in file explorer, for interacting with the filesystem and managing projects
• A "Find in Files" feature, allowing full regular expression search over a specified scope
• SUBLIME TEXT
Sublime Text is a commercialsource code editor. It natively supports manyprogramming 
14
languages and markup languages. Users can expand its functionality with plugins, typically communitybuilt and maintained under free-software licenses. To facilitate plugins, Sublime Text features 
a Python API.
➢ Features
The following is a list of features of Sublime Text:[3]
• "Goto Anything," quick navigation to files, symbols, or lines
• "Command palette" uses adaptive matching for quick keyboard invocation of arbitrary 
commands
• Simultaneous editing: simultaneously make the same interactive changes to multiple selected 
areas
• Python-based plugin API
• Project-specific preferences
• Extensive customizability via JSON settings files, including project-specific and platformspecific settings
• Cross-platform (Windows, macOS, and Linux) and Supportive Plugins for cross-platform
• Compatible with many language grammars from TextMate
15
ESSENTIAL LIBRARIES USED
• NumPy
NumPy is one of the fundamental packages for scientific computing in Python. It contains
functionalityfor multidimensional arrays, high-levelmathematicalfunctionssuchaslinear algebra
operations and the Fourier transform, and pseudorandom numbergenerators.
In scikit-learn, the NumPy array is the fundamental data structure. scikit-learn takes in data in
the form of NumPy arrays. Any data you’re using will have to be converted to a NumPy array.
The core functionality ofNumPyis the arrayclass, a multidimensional (n-dimensional) array. All
elements of the arraymust beof the same type.
• Matplotlib
Matplotlib is the primary scientific plotting library in Python. It provides functions for making
publication- quality visualizations such as line charts, histograms, scatter plots, and so on. 
Visualizing your data and different aspects of your analysis can give you important insights, and 
we will be using matplotlib for all ourvisualizations. When workinginside the JupyterNotebook,
you can show figures directly in the browser by using the matplotlib notebook and matplotlib
inline commands.
• Pandas
It is a Python library for data wrangling and analysis. It is built around a data structure called the
DataFrame that is modeled after the R DataFrame. Simply put, a pandas DataFrame is a 
table,similar to an Excel spreadsheet. pandas provide a great range of methods to modify and
operate on this table; in particular, it allows SQL-like queries and joins of tables. Another
valuable tool provided by pandas is its ability to ingest from a great variety of file formats and
databases, like SQL, Excel files, and comma-separated values (CSV) files. Going into detail
about the functionalityofpandasis out of the scope of this book.
• Seaborn
Seaborn is a library for making statistical graphics in Python. It builds on top of matplotlib and 
integrates closely with pandas data structures. Seaborn helps you explore and understand your 
data. Its plotting functions operate on data frames and arrays containing whole datasets and 
16
internally perform the necessary semantic mapping and statistical aggregation to produce 
informative plots. Its dataset-oriented, declarative API lets you focus on what the different 
elements of your plots mean, rather than on the details of how to draw them.
