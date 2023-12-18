# Python Performance

## How to Run for Yourself

1. Create a virtual environment `python3 -m venv .venv`. On some systems you may be able to just use `python` instead of `python3`.
2. Activate the virtual environment `source .venv/bin/activate` on posix systems, `.venv\Scripts\activate` on Windows.
3. Install dependencies `pip install -r requirements.txt`. These are all for analysis after the fact.
4. To run the scenarios with analysis, run the `analyze_scenarios.py` file from the respective folders. For example, to run the tests with analysis from the first article, run `python cc_polymorphism/analyze_scenarios.py`. The final results, which include comparisons between the scenarios, will be in a file called `final_results.txt` under the article folder.
5. To just run the scenarios so you can do your own analysis, you can run the `run_scenarious.py` file under the article folders.
