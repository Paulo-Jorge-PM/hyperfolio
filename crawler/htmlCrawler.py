#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import time, os, pathlib
from requests_html import HTMLSession, HTML

class HtmlCrawler:

    def __init__(self, firstPage="", baseDomains=[], saveDir="", blockedExtensions=[], baseUrl="", rederJS="", sourceEncoding="cp1252", saveEncoding="utf8"):

        self.session = HTMLSession()
        self.sourceEncoding = sourceEncoding#utf8 / cp1252 / ISO-8859-1 etc.
        self.saveEncoding = saveEncoding#utf8 / cp1252 / ISO-8859-1 etc.

        self.BASE_DOMAINS = ["dgsi.pt"]#for checking if it is not an external link, can be more than one
        self.SAVE_DIR = pathlib.Path.cwd().joinpath("output", "html", saveDir)#"output/html/saveDir/"
        self.blockedExtensions = blockedExtensions#will only download this url endings after the last point. "" = www.xx.com/page without point
        self.RENDER_JS = rederJS
        ###LET IT EMPTY IF CRAWLING WEB. Make it "https://arquivo.pt/noFrame/replay/" if crawling arquivo.pt global links f.e.
        self.BASE_URL = baseUrl


        self.totalLinks = []
        self.homepageLinks = []
        self.savedLinks = []
        self.ignored = []

        self.end = False

        self.loadLinks()

        #IF everything empty and first time running start by the base domains
        if not self.totalLinks:
            self.totalLinks.append(firstPage)
            with open(self.SAVE_DIR.joinpath("totalLinks.txt"), "a+", encoding=self.saveEncoding) as f:
                f.write(firstPage+"\n")

        ### LET THE MAGIC BEGIN
        try:
            self.startCrawl()
        except Exception as e:
            print("Error:")
            print(e)


    def loadLinks(self):
        #Create folder if not exist
        os.makedirs(self.SAVE_DIR, exist_ok=True)
        ###a+ so it can read but also creat if not exist. f.seek(0) to simulate the read and 
        with open(self.SAVE_DIR.joinpath("homepages.txt"), "a+", encoding=self.saveEncoding) as f:
            f.seek(0)
            lines = [line.rstrip() for line in f]
            for l in lines:
                self.homepageLinks.append(l)

        with open(self.SAVE_DIR.joinpath("savedLinks.txt"), "a+", encoding=self.saveEncoding) as f:
            f.seek(0)
            lines = [line.rstrip() for line in f]
            for l in lines:
                self.savedLinks.append(l)

        with open(self.SAVE_DIR.joinpath("ignored.txt"), "a+", encoding=self.saveEncoding) as f:
            f.seek(0)
            lines = [line.rstrip() for line in f]
            for l in lines:
                self.ignored.append(l)

        with open(self.SAVE_DIR.joinpath("totalLinks.txt"), "a+", encoding=self.saveEncoding) as f:
            f.seek(0)
            lines = [line.rstrip() for line in f]
            for l in lines:
                self.totalLinks.append(l)

        for link in self.homepageLinks:
            if link not in self.totalLinks:
                self.totalLinks.append(link)
                with open(self.SAVE_DIR.joinpath("totalLinks.txt"), "a+", encoding=self.saveEncoding) as f:
                    f.write(link+"\n")


    def startCrawl(self):
        print("CRAWLING...")
        while self.end == False:

            count=0
            for link in self.totalLinks:

                if link not in self.savedLinks and link not in self.ignored:

                    try:
                        #GET HTML
                        resp = self.getHtml(link, js=self.RENDER_JS)
                        #html = resp.text
                        html = resp.html.html.encode(self.saveEncoding).decode(self.saveEncoding)

                        #SAVE HTML
                        if self.BASE_URL != "":
                            originalUrl = link.lower().split(self.BASE_URL, 1)[1]
                            domain = originalUrl.split("/", 1)[1].replace("https://", "").replace("http://", "").replace("www.", "").split("/", 1)[0]
                        else:
                            originalUrl = link.lower()
                            domain = originalUrl.replace("https://", "").replace("http://", "").replace("www.", "").split("/", 1)[0]

                        if link in self.homepageLinks:
                            save = self.SAVE_DIR.joinpath("homepages")
                        else:
                            save = self.SAVE_DIR.joinpath("sublinks", domain)

                        extension = self.getExtension(originalUrl)
                        if extension not in self.blockedExtensions:
                            #if extension == "":
                            #    extension = "html"
                            #fName = str(time.time()) + "_" + originalUrl.replace("/", "\\")[:220] + "." + extension#220 because filenames in some OS are limited to 255. \\ because / is not allowed in linux
                            fName = str(time.time()) + ".html"
                        else:
                            self.ignored.append(link)
                            with open(self.SAVE_DIR.joinpath("ignored.txt"), "a+", encoding=self.saveEncoding) as f:
                                f.write(link+"\n")
                            raise Exception('File extension not allowed')

                        #add the original link to the 1st line as comment
                        html = "<!--"+link+"-->\n" + html
                        path = self.saveHtml(html, save, fileName=fName)

                        print("3333----tesssssste a ver onde pára!")
                        #ADD TO THE SAVED LIST and LOG:
                        self.savedLinks.append(link)
                        with open(self.SAVE_DIR.joinpath("savedLinks.txt"), "a+", encoding=self.saveEncoding) as f:
                            f.write(link+"\n")

                        #self.logFile += link + " :::|::: " + path + "\n"
                        with open(self.SAVE_DIR.joinpath("log_saved_files.txt"), "a+", encoding=self.saveEncoding) as f:
                            f.write(link + " :::|:::> " + path + "\n")

                        print("1----tesssssste a ver onde pára!")
                        #EXTRACT NEW LINKS:
                        self.extractLinks(resp)
                        print("22----tesssssste a ver onde pára!")

                        count += 1
                    except Exception as e:
                        print("ERROR at: " + link + "| Error code:")
                        print(e)
                        with open(self.SAVE_DIR.joinpath("failedLinks.txt"), "a+", encoding=self.saveEncoding) as f:
                            f.write(link+"\n")

            #if no more links to work end the loop
            if count == 0:
                self.end = True
                #with open(self.SAVE_DIR + "log_saved_files.txt", "w") as f:
                #    f.write(self.logFile)
                print("*** FINISHED! ***")


    def getExtension(self, fName):
        e = fName[-5:].split(".")#search for point in the last 5 chars. e.g. .html .html .js. 5 because extensions dont have more than 4 chars (.html = 5)
        if len(e) == 1:#in case there is no extension
            extension = ""
        else:
            extension = e[-1]
        return extension

    def getHtml(self, link, js="", wait=2, sleept=4, reload=True):
        resp = self.session.get(link)
        resp.html.encoding = self.sourceEncoding
        if js:
            #resp.html.render()
            #js = '''
            #() => {
            #      $(document).ready(function() {                        
            #           $("#viewComentsButtonContainer").click();
            #      })
            #}
            #'''
            resp.html.render(wait=wait, sleep=sleep, script=js, reload=reload)
        return resp

    def saveHtml(self, data, saveDir, fileName=""):
        if not os.path.exists(saveDir):
            os.makedirs(saveDir, exist_ok=True)
        path = saveDir.joinpath(fileName)
        with open(path, "w", encoding=self.saveEncoding) as f:
            f.write(data)
            print("HTML SAVED AT: " + str(path))
        return str(path)

    def extractLinks(self, resp):
        links = resp.html.absolute_links
        print("44444----tesssssste a ver onde pára!")
        for link in links:
            if link not in self.totalLinks and link[:4] == "http":
                try:
                    if self.BASE_URL != "":
                        originalUrl = link.lower().split(self.BASE_URL, 1)[1]
                        domain = originalUrl.split("/", 1)[1].replace("https://", "").replace("http://", "").replace("www.", "").split("/", 1)[0]
                    else:
                        originalUrl = link.lower()
                        domain = originalUrl.replace("https://", "").replace("http://", "").replace("www.", "").split("/", 1)[0]
                    print("777----tesssssste a ver onde pára!")
                    #if not an external link
                    #note: can be a sub-domain like: desporto.publico.pt in the publico.pt main domain
                    for base in self.BASE_DOMAINS:
                        if base in domain:
                            self.totalLinks.append(link)
                            with open(self.SAVE_DIR.joinpath("totalLinks.txt"), "a+", encoding=self.saveEncoding) as f:
                                f.write(link+"\n")
                            print("EXTRACTED LINK: " + link)
                except Exception as e:
                    print("EXCEPTION extractLinks failed: " + link + " | Error:")
                    print(e)
                    with open(self.SAVE_DIR.joinpath("failedLinks.txt"), "a+", encoding=self.saveEncoding) as f:
                        f.write(link+"\n")



if __name__ == '__main__':
    #main = HtmlCrawler()
    pass
