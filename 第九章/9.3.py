class Stock:
    """Stock Information Class"""
    def __init__(self,sCode,sName,priceYesterday,priceToday):
        self.sCode = sCode
        self.sName = sName
        self.priceYesterday = priceYesterday
        self.priceToday = priceToday
        
    def getName(self):
        return self.sName
    
    def getCode(self):
        return self.sCode
    
    def getPriceYesterday(self):
        return self.priceYesterday
    
    def setPriceYesterday(self,priceYesterday):
        self.priceYesterday = priceYesterday
    
    def getPriceToday(self):
        return self.priceToday
    
    def getChangePercent(self):
        return (self.priceToday - self.priceYesterday) / self.priceYesterday * 100
    
