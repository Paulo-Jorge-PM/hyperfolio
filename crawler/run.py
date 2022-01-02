#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from htmlCrawler import HtmlCrawler

if __name__ == '__main__':
    saveDir = "dgsi"
    baseDomains = ["dgsi.pt"]
    blockedExtensions = ["pdf"]
    baseUrl = ""
    js = '''
    () => {
          $(document).ready(function() {                        
               $("#viewComentsButtonContainer").click();
          })
    }
    '''
    main = HtmlCrawler(firstPage="http://www.dgsi.pt", saveDir=saveDir, baseDomains=baseDomains, blockedExtensions=blockedExtensions, rederJS="")
