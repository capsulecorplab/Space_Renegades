#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 11:30:56 2017

@author: Patrick Woo-Sam
"""

import dryscrape
import time
import pandas as pd
from io import StringIO


class Trajectory_browser:
    def __init__(self):
        self._url = 'https://trajbrowser.arc.nasa.gov/traj_browser.php'
        self.session = dryscrape.Session()
        self.session.set_attribute('local_storage_enabled')
        self.csv = None
        
    def search(self, **kwargs):
        '''Submit a seach query to NASA's trajectory browser.
        
        Keyword arguments:
        ------------------
        NEOs -- on or off (default on)

        NEAs -- on or off (default on)
        
        NECs -- on or off (default on)
        
        chk_maxOCC -- on or off (default on)
        
        maxMag -- int (default 25)
        
        chk_target_list -- on or off (default on)
        
        target_list -- ??? (default '')
        
        mission_class -- Mission class:  oneway or roundtrip (default oneway)
        
        mission_type -- Mission type: rendezvous or flyby (default rendezvous)
        
        LD1 -- Launch year, lower bound:  int (default 2014)
        
        LD2 -- Launch year, upper bound:  int (defualt 2016)
        
        maxDT -- float (default 7.0)
        
        min -- DV or DT (default DV)
        
        wdw_width -- int (default 0)
        '''
        kwargs = {k: str(v) for k, v in kwargs.items()}
        query = {'NEOs': 'on',
                 'NEAs': 'on',
                 'NECs': 'on',
                 'chk_maxMag': 'on',
                 'maxMag': '25',
                 'chk_maxOCC': 'on',
                 'maxOCC': '4',
                 'chk_target_list': 'on',
                 'target_list': '',
                 'mission_class': 'oneway',
                 'mission_type': 'rendezvous',
                 'LD1': '2014',
                 'LD2': '2016',
                 'maxDT': '2.0',
                 'DTunit': 'yrs',
                 'maxDV': '7.0',
                 'min': 'DV',
                 'wdw_width': '0',
                 'submit': 'Search'}
        query.update(kwargs)
        search_string = '?'
        for k, v in query.items():
            search_string += k + '=' + v + '&'
        search_string = search_string[:-1]
        self.session.visit(self._url + search_string)
    
    def download_csv(self, **kwargs):
        '''Save the csv from a query to self.csv.
        
        This method calls Trajectory_browser().search(**kwargs) and then saves 
        the trajectory data to Trajectory_browser().csv.
        
        See Trajectory_browser().search() for valid search parameters.
        '''
        self.search(**kwargs)
        self.session.at_xpath('/html/body/div[2]/button').click()
        time.sleep(2)  # sleep to allow javascript to parse data
        self.csv = StringIO(self.session.body())
        
    def get_DataFrame(self):
        '''Return pandas DataFrame for self.csv.'''
        if self.csv is not None:
            df = pd.read_csv(self.csv)
            df = df.iloc[:, :-1]
            return df
        else:
            print(('You must first download a csv! `Trajectory_browser().'
                   'download_csv()`'))
            return pd.DataFrame()


if __name__ == '__main__':
    br = Trajectory_browser()
    br.download_csv()
    df = br.get_DataFrame()
    print(df)
