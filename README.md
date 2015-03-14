# xkcd_downloader

xkcd Downloader
============
Downloads all images from XKCD

Requirements
============
pip install scrapy
* Install any other libraries which might be missing in your system.

Spider
=========
* xkcd_download_images - downloads all comic images and info to a json file

To Run
======

```scrapy crawl xkcd_download_images -o xkcd_data.json``` - Info in xkcd_data.json, Images in images folder