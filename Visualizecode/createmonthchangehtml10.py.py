
import csv
import pandas as pd
import ast
import operator

path = '../Dataanalysiscode/codecreate/BBCCNNcombine/'
path2 = './3reportdateshow/wholehtml/'

### merge all weather issue together for US, just try first ###
weatherlist = ['hurricane','drought','snow','flood','earthquake']

for eachweather in weatherlist:
    weatherissue = eachweather
    #read each weather issue 'countryrate6.txt' to list of list
    countryratef = open(path + 'BBCCNN' + weatherissue + 'countryrate6.txt', "r")
    lines = countryratef.read()
    countryratelist = ast.literal_eval(lines)
    countryratef.close()
    #(2)convert list of list to dict
    countryratedict = dict(countryratelist)
    #(3)sort dict by value (1:sort by value,0:sort by key)
    countryratedictsort = sorted(countryratedict.items(), key=operator.itemgetter(1),reverse=True)
    #(4)get first and second top country
    firstcountry = countryratedictsort[0][0]
    secondcountry = countryratedictsort[1][0]
    top2countrylist = [firstcountry,secondcountry]

    
    for eachcountry in top2countrylist:
        ########## create whole html file ######### 
        #1,create a html filt to write
        fw = open(path2 + eachcountry + weatherissue +"index.html","w")

        #2,write the html template header
        fh = open("./3reportdateshow/headpart.html","r")
        header = fh.readlines()
        fh.close()
        fw.writelines(header)

        #3,write the middle part---the data part
        #(1)read weatherissue+'weekgroupmatrix8.csv' file (the year-week matrix)
        weekyearmatrixdf = pd.read_csv(path + eachcountry + weatherissue + 'weekyearmat8.csv',sep=',',header=None)
        noyeartitmatrdf = weekyearmatrixdf[1:]
        allweeklistlong = noyeartitmatrdf.values.tolist()

        for eachweeklist in allweeklistlong:
            weeknum = eachweeklist[0]
            reportdateindexlist = eachweeklist[1:]
            reportdateindexlistint = map(int,reportdateindexlist)
            if eachweeklist is not allweeklistlong[-1]:
                fw.write("{\n\"values\":" + str(reportdateindexlistint) + ",\n\"text\":\"" + weeknum + "\"\n},\n")
            else:
                fw.write("{\n\"values\":" + str(reportdateindexlistint) + ",\n\"text\":\"" + weeknum + "\"\n}\n")

        #4,write the html template footer1
        ff1 = open("./3reportdateshow/footpart1.html","r")
        footer1 = ff1.readlines()
        ff1.close()
        fw.writelines(footer1)

        #5,write country,weather issue title
        if eachcountry == 'US':
            eachcountry = 'America'
        titlestr = eachcountry + ' ' + weatherissue.title()
        fw.write(titlestr)

        #6,write the html template footer2
        ff2 = open("./3reportdateshow/footpart2.html","r")
        footer2 = ff2.readlines()
        ff2.close()
        fw.writelines(footer2)

        fw.close()
































































'''
for j in range(0, 64):
    images[j]["chi_en_text"].replace(">","")
    fw.write("<a class='example-image-link'" + " href='" + "./imgcache/" + images[j]["original_pic"] + "' data-lightbox='image-set'" + " title='" + str(images[j]["chi_en_text"]) + " reposts count:" + str(images[j]["reposts_count"]) + "'" + "><img class='example-image' src='" + "./resizeimg/" + images[j]["thumbnail_pic_resize"] + "'></a>\n")
'''

