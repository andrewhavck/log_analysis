This project analyzes HTTP logs and provides statistics on session information

##Installation
1. `pip install virtualenv`
2. `virtualenv env`
3. `source venv/bin/activate`
4. `pip install -Ur requirements.txt`
5. `py.test`

##Usage
`python log_analysis/analysis.py -s data/testLog.tsv`

This will output two tsv files and an html file of a chart

- log_class.tsv - log data with IP class
- session_info.tsv - session info by IP
- status_codes.html - aggregated status codes over time using a two minute moving average