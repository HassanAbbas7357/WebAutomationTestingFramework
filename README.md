
# Web Automation Framework


Advanced Web Automation Framework for building testcases and generating intresting reports with enhance UI framework "Allure" with Python and Pyest.



## Authors

- [@HassanAbbas7357](https://github.com/HassanAbbas7357)



## Reporting

Insert gif or link to demo


![image](https://drive.google.com/uc?export=view&id=1I6QbkmG6mDaoRIxIxoA3fyVVMQWNLZzU)


![image](https://drive.google.com/uc?export=view&id=1cIwTwVH03hH724nTcelNKeKD1dRkF-S6)


![image](https://drive.google.com/uc?export=view&id=1QmJmKJcGoGs9n_eTQnctsswWL17vvk6n)



## Usage/Examples


#### Use this command to install the required packages
```bash
pip3 install -r requirements.txt
```
#### Use this command to run your testcases
```bash
pytest Tests --alluredir=reports --screenshot=on --browser CHROME  -v -s --headless 0  
```
```bash
pytest Tests --alluredir=reports --screenshot=on --browser FIREFOX  -v -s --headless 1  
```
```bash
pytest Tests --alluredir=reports --screenshot=on --browser SAFARI  -v -s --headless 0  
```
#### Use this command to generate and preview the Allure report
```bash
allure serve reports/
```
## License

[Open Source Project]()


## Tech Stack

**Technologies:** Python, Pytest , Selenium 

**Reporting:** Allure Framework

