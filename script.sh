pytest Tests --alluredir=reports --screenshot=on
pytest Tests --alluredir=reports --screenshot=on --browser CHROME  -v -s --headless 1  

mkdir reports/history
cp allure-report/history/* reports/history

allure generate reports --clean reports/history
allure open
