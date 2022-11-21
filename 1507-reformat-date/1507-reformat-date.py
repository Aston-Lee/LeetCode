class Solution:
    def reformatDate(self, date: str) -> str:
        
        dates = date[:3]
        month = date[-8:-5]
        year = date[-4:]
        
        monthDict = {
            "Jan" : "01",
            "Feb" : "02",
            "Mar" : "03",
            "Apr" : "04",
            "May" : "05",
            "Jun" : "06",
            "Jul" : "07",
            "Aug" : "08",
            "Sep" : "09",
            "Oct" : "10",
            "Nov" : "11",
            "Dec" : "12"
        }
        monthStr = monthDict[month]
        
        num = 0
        for char in dates:
            if char.isdigit():
                num *= 10
                num += int(char)
                
        if num < 10:
            num = "0" + str(num)
        else:
            num = str(num)
                
        res = year + '-' + monthStr + '-' + num
        return res