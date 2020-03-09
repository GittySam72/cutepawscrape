#-------------------------------------------------------------------------
# importing dependencies module
import os
from requests_html import HTMLSession
from bs4 import BeautifulSoup
import urllib.request
import csv
#--------------------------------------------------------------------------



#---------------------------------------------------------------------------------
# PageNoDirectoryCreation
def dircreation():
    '''
    dircreation() will create required folders.
    '''
    for i in range(1, 297):
        dirname = f"PageNo{i}"
        parent_dir = r"C:\Users\Lenovo\Desktop\Assignment"
        path = os.path.join(parent_dir, dirname)
        os.mkdir(path)
        dirname2 = "CSV Data"
        dirname3 = "Images"
        parent_dir1 = f"C:\\Users\\Lenovo\\Desktop\\Assignment\\PageNo{i}"
        path1 = os.path.join(parent_dir1, dirname2)
        path2 = os.path.join(parent_dir1, dirname3)
        os.mkdir(path1)
        os.mkdir(path2)
        dirname4 = "AllImages"
        dirname5 = "CroppedImages"
        parent_dir2 = f"C:\\Users\\Lenovo\\Desktop\\Assignment\\PageNo{i}\\Images"
        path3 = os.path.join(parent_dir2, dirname4)
        path4 = os.path.join(parent_dir2, dirname5)
        os.mkdir(path3)
        os.mkdir(path4)
# ----------------------------------------------------------------------------


#---------------------------------------------------------------------------------
# Part -1 Scrapping Data-working on online data
def scrapedata():
    '''
    scarpedata() method will scrapedata from given url and will put that
    data into given folder.
    '''
    count = 1
    # Lists
    urls = []
    titlesList = []
    hyperList = []
    imgurls = []

    for i in range(1, 297):
        url = f"http://www.cutestpaw.com/tag/cats/page/{i}/"
        urls.append(url)


    for url in urls:
        try:
            session = HTMLSession()
            response = session.get(url).html
            source = response.html
            soup = BeautifulSoup(source, "lxml")

            # Scraping Part
            whole_box = soup.find(id="photos")
            all_boxes = whole_box.find_all("a")
            print(count)
            with open(f'C:\\Users\\Lenovo\\Desktop\\Assignment\\PageNo{count}\\CSV Data\\AllData.csv', "a") as s:
                file=csv.writer(s)
                file.writerow(("Title", 'Hyperlink'))
                
            c = 1
            for one_box in all_boxes:
                # title stuff
                title = one_box.find("img")
                title = title.attrs['title']
                titlesList.append(title + "\n")

                # Hyperlinks
                hyper = one_box.attrs['href']
                hyperList.append(hyper + '\n')

                # imageUrl
                imgurl = one_box.find("img")
                imgurl = imgurl.attrs['src']
                imgurls.append(imgurl)

                with open(f'C:\\Users\\Lenovo\\Desktop\\Assignment\\PageNo{count}\\CSV Data\\AllData.csv', "a") as s:
                    file = csv.writer(s)
                    file.writerow((title, hyper))

                urllib.request.urlretrieve(imgurl, f"C:\\Users\\Lenovo\\Desktop\\Assignment\\PageNo{count}\\Images\\AllImages\\{title}.jpg")
                print("Downloaded Image No:", c)
                c += 1

            count += 1

        except:
            pass
#---------------------------------------------------------------------------------


#---------------------------------------------------------------------------------
def main():
    '''
    Main() first will invoke dircreation() which will create required folders and then
    it will invoke scrapedata() which will scrape data and will put data into
    created folder.
    '''
    dircreation()
    scrapedata()
#---------------------------------------------------------------------------------


#---------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
#---------------------------------------------------------------------------------
