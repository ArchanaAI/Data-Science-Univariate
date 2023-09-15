class univariate():

    def Quanqual(dataset):
        quan=[]
        qual=[]
        for columnName in dataset.columns:
            print(columnName)
            if(dataset[columnName].dtype=='O'):
                print("qual")
                qual.append(columnName)
            else:
                print("quan")
                quan.append(columnName)
        return quan,qual
    def freqTable(colunmName,dataset):
        freqTable=pd.DataFrame(columns=["unique_values","Frequency","Relative_Frequency","Cumsum"])
        freqTable["unique_values"]=dataset[columnName].value_counts().index
        freqTable["Frequency"]=dataset[columnName].value_counts().values
        freqTable["Relative_Frequency"]=(freqTable["Frequency"]/103)
        freqTable["Cumsum"]=freqTable["Relative_Frequency"].cumsum()
        return freqTable

    def univariate(dataset,quan):
        descriptive=pd.DataFrame(index=["Mean","Median","Mode","Q1:25%","Q2:50%","Q3:75%","99%","Q4:100%","IQR","1.5rule","Lesser","Greater","min","max"],columns=quan)
        for colunmName in quan:
            descriptive[colunmName]["Mean"]=dataset[colunmName].mean()
            descriptive[colunmName]["Median"]=dataset[colunmName].median()
            descriptive[colunmName]["Mode"]=dataset[colunmName].mode()[0]
            descriptive[colunmName]["Q1:25%"]=dataset.describe()[colunmName]["25%"]
            descriptive[colunmName]["Q2:50%"]=dataset.describe()[colunmName]["50%"]
            descriptive[colunmName]["Q3:75%"]=dataset.describe()[colunmName]["75%"]
            descriptive[colunmName]["99%"]=np.percentile(dataset[colunmName],99)
            descriptive[colunmName]["Q4:100%"]=dataset.describe()[colunmName]["max"]
            descriptive[colunmName]["IQR"]=descriptive[colunmName]["Q3:75%"]-descriptive[colunmName]["Q1:25%"]
            descriptive[colunmName]["1.5rule"]=1.5*descriptive[colunmName]["IQR"]
            descriptive[colunmName]["Lesser"]=descriptive[colunmName]["Q1:25%"]-descriptive[colunmName]["1.5rule"]
            descriptive[colunmName]["Greater"]=descriptive[colunmName]["Q3:75%"]+descriptive[colunmName]["1.5rule"]
            descriptive[colunmName]["min"]=dataset[colunmName].min()
            descriptive[colunmName]["max"]=dataset[colunmName].max()
        return descriptive
    
    def outlier_colunmName():
        Lesser=[]
        Greater=[]
        for colunmName in quan:
            if(descriptive[colunmName]["min"]<descriptive[colunmName]["Lesser"]):
                Lesser.append(colunmName)
            if(descriptive[colunmName]["max"]>descriptive[colunmName]["Greater"]):
                Greater.append(colunmName)
        return [colunmName]
    def replacing_outlier():
        for colunmName in Lesser:
            dataset[colunmName][dataset[colunmName]<descriptive[colunmName]["Lesser"]]=descriptive[colunmName]["Lesser"]
        for colunmName in Greater:
            dataset[colunmName][dataset[colunmName]>descriptive[colunmName]["Greater"]]=descriptive[colunmName]["Greater"]
        return descriptive