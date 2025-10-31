from datetime import datetime,timedelta
import re
import math
def delivery_date(start, description):
    fecha=datetime.fromisoformat(start)
    
    if description=="NOW":
        return (fecha+timedelta(hours=2)).isoformat()
        
    if description=="ASAP":
        if fecha.hour<13:
            return fecha.replace(hour=17,minute=0).isoformat()
        return (fecha+timedelta(hours=24)).replace(hour=13,minute=0).isoformat()

    if description=="EOW":
        if fecha.weekday() in [0,1,2]:
            dias=(4-fecha.weekday())%7
            return (fecha+timedelta(days=dias)).replace(hour=17,minute=0).isoformat()
        else:
            dias=(6-fecha.weekday())%7
            return (fecha+timedelta(days=dias)).replace(hour=20,minute=0).isoformat()

    item=re.search(r"([0-9]+)M",description)
    if item:
        n_month=int(item.group(1))
        year=fecha.year
        
        if fecha.month>=n_month:
            year+=1

        out=fecha.replace(year=year,month=n_month,day=1,hour=8,minute=0)
        dia=1
        while out.weekday()>4:
            dia+=1
            out=fecha.replace(year=year,month=n_month,day=dia,hour=8,minute=0)
        
        return out.isoformat()
        

    item=re.search(r"Q([0-9]+)",description)
    if item:
        n_quarter=int(item.group(1))
        actual_quarter=math.ceil(fecha.month/3)

        year=fecha.year
        print(actual_quarter, n_quarter)
        if not actual_quarter<=n_quarter:
            year+=1
            
        mes=3*n_quarter
        out=fecha.replace(year=year,month=mes,day=1,hour=8,minute=0)

        dia=0
        while mes==out.month:
            if out.weekday()<5:
                dia=out.day
            out+=timedelta(days=1)
        return fecha.replace(year=year,month=mes,day=dia,hour=8,minute=0).isoformat()