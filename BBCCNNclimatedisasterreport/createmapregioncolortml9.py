
import csv
import pandas as pd
import ast
import operator

path = '../Dataanalysiscode/codecreate/BBCCNNcombine/'
path2 = './2countryrate/wholehtml/'

### merge all weather issue together for US, just try first ###
weatherlist = ['hurricane','drought','snow','earthquake','flood','allweat']

for eachweather in weatherlist:
    weatherissue = eachweather
    #print('weatherissue:',weatherissue)
    
    #1,create a html file to write
    fw = open(path2 + 'BBCCNN' + weatherissue +"countryrate.html","w")

    #2,write the html template header
    fh = open("./2countryrate/headpart.html","r")
    header = fh.readlines()
    fh.close()
    fw.writelines(header)

    #3,write data part---country rate
    #(1)read each weather issue 'countryrate6.txt' to list of list
    countryratef = open(path + 'BBCCNN' + weatherissue + 'countryrate6.txt', "r")
    lines = countryratef.read()
    countryratelist = ast.literal_eval(lines)
    countryratef.close()
    #(2)convert list of list to dict
    countryratedict = dict(countryratelist)
    #(3)sort dict by value (1:sort by value,0:sort by key)
    countryratedictsort = sorted(countryratedict.items(), key=operator.itemgetter(1),reverse=True)
    #print('countryratedictsort:',countryratedictsort)
    for eachcountrynum in countryratedictsort:
        if eachcountrynum == countryratedictsort[-1]:
            fw.write(str(list(eachcountrynum)) + '\n')
        else:
            fw.write(str(list(eachcountrynum)) + ',\n')

    #4,write foot part
    ff = open("./2countryrate/footpart.html","r")
    footer = ff.readlines()
    ff.close()
    fw.writelines(footer)
    fw.close()


    


    




    

    

    


    

    

'''
    path2 = 'E:/Project/visualclimate/monthchange3/zingchart_trial/success try/wholehtml/'
    for eachcountry in top2countrylist:
        ########## create whole html file ######### 
        #1,create a html filt to write
        fw = open(path2 + eachcountry + weatherissue +"wholehtml.html","w")

        #2,write the html template header
        fh = open("headpart.html","r")
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
        ff1 = open("footpart1.html","r")
        footer1 = ff1.readlines()
        ff1.close()
        fw.writelines(footer1)

        #5,write country,weather issue title
        if eachcountry == 'US':
            eachcountry = 'America'
        titlestr = eachcountry + ' ' + weatherissue.title()
        fw.write(titlestr)

        #6,write the html template footer2
        ff2 = open("footpart2.html","r")
        footer2 = ff2.readlines()
        ff2.close()
        fw.writelines(footer2)

        fw.close()
'''

