# webscrapper-boilerplate using: selenium 4, chromedriver, beautifulsoup4

## Reference

Selenium-webdriver: https://www.selenium.dev/documentation/webdriver/

beautifulsoup4: https://www.crummy.com/software/BeautifulSoup/bs4/doc/

chromedriver: https://chromedriver.chromium.org

## Setup

### environment

1. Clone this repo

2. create environment & install packages

    ```bash
    conda env create -f environment
    ```

3. use the environment

    ```bash
    conda activate webscrapper
    ```

### chromedriver

1. Check your version of Chrome 
2. download suitable version of chromedriver from [[https://chromedriver.chromium.org/downloads]]
3. unzip it as chromedriver
4. run the chromedriver (permission may asked if on Mac)

    terminal should be shown as below

    ```bash
    Starting ChromeDriver 108.0.5359.71 (1e0e3868ee06e91ad636a874420e3ca3ae3756ac-refs/branch-heads/5359@{#1016}) on port 9515
    Only local connections are allowed.
    Please see https://chromedriver.chromium.org/security-considerations for suggestions on keeping ChromeDriver safe.
    ChromeDriver was started successfully.
    ```

    stop it (cltr c) and close the terminal

## Run

```bash
python scapper.py
```
