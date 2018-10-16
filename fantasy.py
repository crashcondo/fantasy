import csv
from decimal import *
TWOPLACES = Decimal(10) ** -2

wr=[]
qb=[]
rb=[]
te=[]
defense=[]

#Inputs csv of known player data (playerlist.csv) from Fanduel and sorts and splits out based on position to representative
#*.csv files.  It also creates representative multidimeninonal lists, each named after each position.
#Each written/generated row will contain players injury designation,fullname,proj fantasy points, cost, and matchup
#in that order.  It also removes any players which have been assigned a PFF of less than 1.
#Later added decimal quantizing to control text output for two significant decimal places
with open('playerlist.csv','rt') as plistin, open ('wr.csv','w') as wrout, open ('qb.csv','w') as qbout, open ('rb.csv','w') as rbout, open ('te.csv','w') as teout, open ('defense.csv','w') as defout:
    wrwriter = csv.writer(wrout)
    qbwriter = csv.writer(qbout)
    rbwriter = csv.writer(rbout)
    tewriter = csv.writer(teout)
    defwriter = csv.writer(defout)
    for row in csv.reader(plistin):
        if row[1] == 'WR' and float(row[5])>1:
             wrwriter.writerow([row[11],row[3],Decimal(row[5]).quantize(TWOPLACES),int(row[7]),row[8]])
             wr.append([row[11],row[3],Decimal(row[5]).quantize(TWOPLACES),int(row[7]),row[8]])
        elif row[1] == 'QB' and float(row[5])>1:
             qbwriter.writerow([row[11],row[3],round(float(row[5]),2),int(row[7]),row[8]])
             qb.append([row[11],row[3],Decimal(row[5]).quantize(TWOPLACES),int(row[7]),row[8]])       	
        elif row[1] == 'RB' and float(row[5])>1:
             rbwriter.writerow([row[11],row[3],round(float(row[5]),2),int(row[7]),row[8]])
             rb.append([row[11],row[3],Decimal(row[5]).quantize(TWOPLACES),int(row[7]),row[8]])
        elif row[1] == 'TE' and float(row[5])>1:
             tewriter.writerow([row[11],row[3],round(float(row[5]),2),int(row[7]),row[8]])
             te.append([row[11],row[3],Decimal(row[5]).quantize(TWOPLACES),int(row[7]),row[8]])
        elif row[1] == 'D' and float(row[5])>1:
             defwriter.writerow([row[11],row[3],round(float(row[5]),2),int(row[7]),row[8]])
             defense.append([row[11],row[3],Decimal(row[5]).quantize(TWOPLACES),int(row[7]),row[8]]) 

#defines statsortpadmake(x, csvlabel) function which expects a list input (x) and csv file label (csvlabel)
#generates and appends the $/FP stat to each player record in that same row.
#it then returns a list sorted by this new $/FP stat.
#it then adds padding to each row:column entry for better csv file viewing.
#it then generates a csv file with name csvlabel which you have to enter during function call.
def statsortpadmake(x, csvlabel):
    #generates $/FP stat and appends it to same row
    for i in range(len(x)):
        x[i].append((round(x[i][3]/x[i][2],2)))

    #sorts list via new $/FP stat
    x = sorted(x,key=lambda z:(z[5]))

    #cell padding code
    for i in range(len(x)):
        for j in range(len(x[i])):
            if j == 0:
                x[i][j]=(f"{x[i][j]:3}")
            elif j == 1:
                x[i][j]=(f"{x[i][j]:25}").replace('\'', ' ') #removes ' from names so they don't get escaped during csv processing
            elif j == 2 or j == 3:
                x[i][j]=(f"{x[i][j]:6}")
            elif j == 4:
                x[i][j]=(f"{x[i][j]:8}")
            elif j == 5:
                x[i][j]=(f"{x[i][j]:8}")  
            else:
                return

    #Outputs sorted and padded lists to custom generated csv files.
    with open(f'{csvlabel}.csv', 'w') as myfile:
        scrib = csv.writer(myfile,quoting=csv.QUOTE_NONE,delimiter="\n",escapechar='\\')
        scrib.writerow(x)
    print(f"{csvlabel}.csv created...")
    return


#Processes raw lists read in from playerlist.csv via statsortpadmake(x, csvlabel) function
statsortpadmake(wr,"sorted_WR")
statsortpadmake(qb,"sorted_QB")
statsortpadmake(rb,"sorted_RB")
statsortpadmake(te,"sorted_TE")
statsortpadmake(defense,"sorted_DEF")
print("All done!")



