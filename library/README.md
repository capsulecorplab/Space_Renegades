Use this folder to store development code and/or custom libraries

## trajectory_browser.py
Web scraper for https://trajbrowser.arc.nasa.gov/traj_browser.php. <br>
Submit search queries for trajectory data and return pandas DataFrames of the results.
#### Dependencies:
* dryscrape
* pandas
#### Notes:
To install dryscrape, a specific version of qmake is needed.
For Mac OS X:
```
brew install qt@5.5
brew link --force qt@5.5
which qmake
```
Then add the that directory to your path environment in ~/.bash_profile  : <br>
I added `export PATH="/usr/local/opt/qt@5.5/bin:$PATH"` to the end of my ~/.bash_profile <br>
Dryscrape can then be pip installed: `pip install dryscrape`.

For Linux:
```
sudo apt install qt5-default
sudo apt install libqt5webkit5-dev
python3 -m pip install dryscrape
python3 -m pip install pandas
```

