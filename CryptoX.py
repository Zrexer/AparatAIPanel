#!/usr/bin/env python3 
"""
Aparat Library

Developer and Writed: CryptoX, Host1let

License: 

Copyright 2024 CryptoX For Aparat API Library Private

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

import requests
import os
import hashlib
import certifi
import urllib.parse
import urllib3
import sys
import platform

os.system("")

class colors:
    red = '\033[91m'
    green = '\033[92m'
    blue = '\033[94m'
    yellow = '\033[93m'
    magenta = '\033[95m'
    cyan = '\033[96m'
    white = '\033[97m'
    bold = '\033[1m'
    underline = '\033[4m'
    black='\033[30m'
    Backsilver='\033[100m'
    silver='\033[90m'
    Backwhite='\033[3m'
    Backgreen='\033[42m'
    Backyellow='\033[43m'
    BackBlue='\033[44m'
    Backpink='\033[45m'
    Backcyan='\033[46m'
    BackRed='\033[41m'
    green = '\033[32m' 
    red = '\033[31m' 
    blue = '\033[36m' 
    pink = '\033[35m' 
    yellow = '\033[93m' 
    darkblue = '\033[34m' 
    white = '\033[00m'
    bluo = '\033[34m'
    red_p = '\033[41m'
    green_p = '\033[42m'
    bluo_p = '\033[44m'
    pink_p = '\033[45m'
    blue_p = '\033[46m'
    white_p = '\033[47m'
    rd = '\033[91m'
    black='\033[30m'
    bold = '\033[1m'
    underline = '\033[4m'
    magenta = '\033[95m'

#The Base and The Form Class and uploadPost Function is copied from Aparat Library
class Base(object):
    def __init__(self, dic):
        self.dic = dic
        for key in dic.keys():
            setattr(self, key, dic[key])

class Form(Base):
    def __init__(self, dic):
        super().__init__(dic)

#--------------------------------
class Encryption(object):
    def __init__(self, passwordKey):
        self.password = str(passwordKey)
        
    def changeType(self):
        md5 = hashlib.md5()
        sha1 = hashlib.sha1()
        encodedPassword = self.password.encode("utf-8")
        md5.update(encodedPassword)
        sha1.update(md5.hexdigest().encode("utf-8"))
        return sha1.hexdigest()
    
    def urlType(self):
        return urllib.parse.quote(self.password)


class Client(object):
    """Client Class for Aparat
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    ```
    from CryptoX import Client 
    
    myUsername = "imA_User"
    myPassword = "1234"
    
    app = Client()
    data = app.loginSession(myUsername, myPassword)
    print(data)
    ```
    
    """
    def __init__(self):
        self.etcApi = "https://www.aparat.com/etc/api/"
        self.liveApi = "http://api.aparat.com/fa/v1/live/live"
    
    def loginSession(self, username: str = None, password: str = None):
        if (username == None or password == None):
            raise ValueError(f"{colors.white}[ {colors.yellow}username {colors.green}, {colors.yellow}password {colors.white}]{colors.red} parameters cannot be empty in {colors.green}' loginSession ' {colors.red}Method{colors.white}")
        else:
            try:
                passwordToUse = Encryption(passwordKey=password).changeType()
                return dict(requests.get(f"{self.etcApi}login/luser/{username}/lpass/{passwordToUse}").json())
            except Exception as e:
                return {"error" : e}
                pass
    
    def userProfileInfo(self, username: str = None):
        if (username == None):
            raise ValueError(f"{colors.white}[ {colors.yellow}username {colors.white}]{colors.red} parameter cannot be empty in {colors.green}' userProfileInfo ' {colors.red}Method{colors.white}")
        else:
            try:
                return dict(requests.get(f"{self.etcApi}profile/username/{username}").json())
            except Exception as e:
                return {"error" : e}
            
    def userBySearch(self, perpage : int = 1, text : str = None):
        if (text == None):
            raise ValueError(f"{colors.white}[{colors.yellow} text {colors.white}]{colors.red} parameter cannot be empty in {colors.green}' userBySearch '{colors.red} Method{colors.white}")
        else:
            if (len(text) <= 3):
                raise ValueError(f"{colors.white}the {colors.green}{text}{colors.white} is {colors.red}more than 3 letters{colors.white}")
            else:
                try:
                    textToUse = Encryption(text).urlType()
                    print(textToUse)
                    return dict(requests.get(f"{self.etcApi}userBySearch/text/{textToUse}/perpage/{str(perpage)}").json())
                except Exception as e:
                    return {"error" : e}
                
    def profileCategories(self, username : str = None):
        if (username == None):
            raise ValueError(f"{colors.white}[{colors.yellow} username{colors.white} ]{colors.red} cannot be empty for {colors.green}' profileCategories ' {colors.red}Method{colors.white}")
        else:
            try:
                return dict(requests.get(f"{self.etcApi}profilecategories/username/{username}").json())
            except Exception as e:
                return {"error" : e}
            
    def getVideoInformation(self, videoHashUID : str = None):
        if (videoHashUID == None):
            raise ValueError(f"{colors.white}[{colors.yellow} videoHashUID {colors.white}]{colors.red} parameter cannot be empty in {colors.green}' getVideoInformation '{colors.red} Method{colors.white}")
        else:
            try:
                return dict(requests.get(f"{self.etcApi}video/videohash/{videoHashUID}").json())
            except Exception as e:
                return {"error" : e}
            
    def categoryVideos(self, perpage: int = 3, cat: int = 3):
        try:
            return dict(requests.get(f"{self.etcApi}categoryVideos/cat/{cat}/perpage/{perpage}").json())
        except Exception as e:
            return {"error" : e}
        
    def getVideoByUsername(self, username : str = None, perpage : int = 1):
        if (username == None):
            raise ValueError(f"{colors.white}[{colors.yellow} username {colors.white}]{colors.red} parameter cannot be empty in {colors.green}' getVideoByUsername '{colors.red} Method{colors.white}")
        else:
            try:
                return dict(requests.get(f"{self.etcApi}videoByUser/username/{username}/perpage/{perpage}").json())
            except Exception as e:
                return {"error" : e}
            
    def commentByVideos(self, videoHashUID : str = None, perpage : int = 1):
        if (videoHashUID == None):
            raise ValueError(f"{colors.white}[{colors.yellow} videoHashUID {colors.white}]{colors.red} parameter cannot be empty in {colors.green}' commentByVideos '{colors.red} Method{colors.white}")
        else:
            try:
                return dict(requests.get(f"{self.etcApi}commentByVideos/videohash/{videoHashUID}/perpage/{perpage}").json())
            except Exception as e:
                return {"error" : e}
            
    def videoBySearch(self, text: str = None, perpage : int = 1):
        if (text == None):
            raise ValueError(f"{colors.white}[{colors.yellow} text {colors.white}]{colors.red} parameter cannot be empty in {colors.green}' videoBySearch '{colors.red} Method{colors.white}")
        else:
            try:
                return dict(requests.get(f"{self.etcApi}videoBySearch/text/{text}/perpage/{perpage}").json())
            except Exception as e:
                return {"error" : e}
            
    def searchVideoByTag(self, text: str = None):
        if (text == None):
            raise ValueError(f"{colors.white}[{colors.yellow} text {colors.white}]{colors.red} parameter cannot be empty in {colors.green}' searchVideoByTag '{colors.red} Method{colors.white}")
        else:
            try:
                return dict(requests.get(f"{self.etcApi}videoByTag/text/{text}").json())
            except Exception as e:
                return {"error" : e}
            
    def uploadForm(self, usernameToSend: str = None, tokenByLogin : str = None):
        if (usernameToSend == None or tokenByLogin == None):
            raise ValueError(f"{colors.white}[{colors.yellow} usernameToSend {colors.green},{colors.yellow} tokenByLogin {colors.white}]{colors.red} parameter cannot be empty in {colors.green}' uploadForm '{colors.red} Method{colors.white}")
        else:
            try:
                return dict(requests.get(f"{self.etcApi}uploadForm/luser/{usernameToSend}/ltoken/{tokenByLogin}").json())
            except Exception as e:
                return {"error" : e}
            
    def uploadPost(
            self, 
            video_path: str, 
            title: str, 
            category: int, 
            form: Form, 
            tags: 'list[str]' = None,
            allow_comment: bool = None, 
            descreption: str = None, 
            video_pass: bool = None
        ):

        url = f"{self.etcApi}"
        with open(video_path, 'rb') as f:
            video_data = f.read()

        data = {
            'frm-id': form.frm_id,
            'data[title]': title,
            'data[category]': category
        }

        if tags:
            data['data[tags]'] = ','.join(tags)
        if allow_comment is not None:
            data['data[comment]'] = allow_comment
        if descreption is not None:
            data['data[descr]'] = descreption
        if video_pass is not None:
            data['data[video_pass]'] = video_pass

        urllib_http = urllib3.PoolManager(ca_certs=certifi.where())
        resp = urllib_http.request("POST", url, fields={
            "video": (video_path, video_data),
            **data
        })

        if resp.status != 200:
            raise Exception("Upload failed")

        try:
            response_data = dict(resp.data.decode('utf-8'))
        except Exception as ex:
            raise Exception("Upload failed")

        videohash = response_data['uploadpost']['uid']
        return self.video(videohash)

    def deleteVideoLink(self, usernameToWork : str = None, tokenByLogin : str = None, videoHashUID : str = None):
        if (usernameToWork == None or tokenByLogin == None or videoHashUID == None):
            raise ValueError(f"{colors.white}[{colors.yellow} usernameToWork {colors.green},{colors.yellow} tokenByLogin {colors.green},{colors.yellow} videoHashUID {colors.white}]{colors.red} parameter cannot be empty in {colors.green}' deleteVideoLink '{colors.red} Method{colors.white}")
        else:
            try:
                return dict(requests.get(f"{self.etcApi}deleteVideoLink/luser/{usernameToWork}/ltoken/{tokenByLogin}/videohash/{videoHashUID}").json())
            except Exception as e:
                return {"error" : e}
            
    def startLive(self, username : str = None, token : str = None):
        if (username == None or token == None):
            raise ValueError(f"{colors.white}[{colors.yellow} username {colors.green},{colors.yellow} token {colors.white}]{colors.red} parameter cannot be empty in {colors.green}' startLive '{colors.red} Method{colors.white}")
        else:
            try:
                return dict(requests.get(f"{self.liveApi}init/luser/{username}/ltoken/{token}").json())
            except Exception as e:
                return {"error" : e}
            
    def listOfLives(self):
        try:
            return dict(requests.get(f"{self.liveApi}list").json())
        except Exception as e:
            return {"error" : e}
        
    def aparatCategories(self):
        try:
            return dict(requests.get("https://www.aparat.com/etc/api/categories").json())
        except Exception as e:
            return {"error" : e}

class ConsoleHandler(object):
    def __init__(self, mode: str):
        self.mode = mode
        
    @property
    def prepare(self):
        if self.mode == "version-mode":
            return "2.5.8"

        if self.mode == "dev-mode":
            return "H:Paradise"
        
        if self.mode == "show-me-path-mode":
            return os.getcwd()
        
        if self.mode == "os-mode":
            return platform.system()

        if self.mode == "help-mode":
            namef = sys.argv[0].split(".")[0]
            return f"Command Options Usage for {namef}\n(-v, --version): show version of {namef}\n(-d, --dev, --developer): person who created {namef}\n(-p, --path): show the path directory starter\n(-o, --os, --os-type): os type of system [Windows, Linux, ...]\n(-h, --help): show this message to help the user"

if "-v" in sys.argv or "--version" in sys.argv:
    print(ConsoleHandler("version-mode").prepare)
    
if "-d" in sys.argv or "--developer" in sys.argv or "--dev" in sys.argv:
    print(ConsoleHandler('dev-mode').prepare)
    
if "-p" in sys.argv or "--path" in sys.argv:
    print(ConsoleHandler("show-me-path-mode").prepare)
    
if "-o" in sys.argv or "--os-type" in sys.argv or "--os" in sys.argv:
    print(ConsoleHandler('os-mode').prepare)
    
if "-h" in sys.argv or "--help" in sys.argv:
    print(ConsoleHandler("help-mode").prepare)