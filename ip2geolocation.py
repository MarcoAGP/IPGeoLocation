#!/usr/bin/env python3
# encoding: UTF-8

"""
    IPGeoLocation - Retrieve IP Geolocation information 
    Powered by http://ip-api.com
    Copyright (C) 2015 @maldevel

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

__author__ = 'maldevel'

import argparse, sys
from argparse import RawTextHelpFormatter
from geolocation.IpGeoLocationLib import IpGeoLocationLib
import webbrowser

VERSION = '1.2'


if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description=""" 
IPGeoLocation {} - Retrieve IP Geolocation information
Powered by http://ip-api.com
    """.format(VERSION), formatter_class=RawTextHelpFormatter)
    
    parser.add_argument('-t', metavar='IP', type=str, dest='ip', default=None, help='IP Address')
    parser.add_argument('-u', metavar='User_Agent', type=str, dest='useragent', default=None, help='User Agent string.')
    parser.add_argument('-ru', help='Pick User Agent strings randomly.', action='store_true')
    parser.add_argument('-ulist', metavar='User_Agent_List', type=str, dest='useragentfilelist', default=None, help='User Agent File List. Each User Agent string in a new line.')
    parser.add_argument('--proxy', metavar='Proxy', type=str, dest='proxy', default=None, help='Proxy (ex. http://127.0.0.1:8080)')
    parser.add_argument('-gm', help='Open IP location in Google maps with default browser.', action='store_true')
    
    args = parser.parse_args()
    
    if(args.ru and args.useragentfilelist is None):
        print('You have to provide a file with User Agent strings. Each User agent string should be in a new line.')
        sys.exit(2)
        
    ipGeoLocRequest = IpGeoLocationLib()
    IpGeoLocObj = ipGeoLocRequest.GetInfo(args.ip, args.useragent, args.ru, args.useragentfilelist, args.proxy)
        
    if IpGeoLocObj:
        if args.gm:
            if type(IpGeoLocObj.Longtitude) == float and type(IpGeoLocObj.Latitude) == float:
                webbrowser.open('http://www.google.com/maps/place/{},{}/@{},{},16z'.
                            format(IpGeoLocObj.Latitude, IpGeoLocObj.Longtitude, IpGeoLocObj.Latitude, IpGeoLocObj.Longtitude))

        print("""
IPGeoLocation {} - Retrieve IP Geolocation information
Powered by http://ip-api.com

Results
        
    IP: {}
    ASN: {}
    City: {}
    Country: {}
    Country Code: {}
    ISP: {}
    Latitude: {}
    Longtitude: {}
    Organization: {}
    Region Code: {}
    Region Name: {}
    Timezone: {}
    Zip Code: {}
            """.format(VERSION,
                   IpGeoLocObj.IP,
                   IpGeoLocObj.ASN,
                   IpGeoLocObj.City, 
                   IpGeoLocObj.Country,
                   IpGeoLocObj.CountryCode,
                   IpGeoLocObj.ISP,
                   IpGeoLocObj.Latitude,
                   IpGeoLocObj.Longtitude,
                   IpGeoLocObj.Organization,
                   IpGeoLocObj.Region,
                   IpGeoLocObj.RegionName,
                   IpGeoLocObj.Timezone,
                   IpGeoLocObj.Zip)#.encode('cp737', errors='replace').decode('cp737')
               )