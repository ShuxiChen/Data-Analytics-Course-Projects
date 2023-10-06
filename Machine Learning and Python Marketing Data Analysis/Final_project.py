### web scraping

import pandas as pd
import requests as req
import json

def json_parsing(url):
    print("Requesting「{0}」district data between 2012.Aug and 2022.Dec".format(district)) 
    resp = req.get(url)
    data = json.loads(resp.text)
    print("Total {0} records of housing prices in Taichung City between 101.08 and 111.12 for the district {1}.".format(len(data), district))
    return data

# 只取出想要的欄位，並重新命名
def rename_col(data):
    all_cases=[]
    for case in data : # to get all cases 
        one_case={}               # dictionary used to store single case
        one_case['address'] = case['a']            #住址
        one_case['community'] = case['bn']         #社區名稱
        one_case['lon']= case['lon']               #經度
        one_case['lat']= case['lat']               #緯度     
        one_case['age'] = case['g']                #屋齡
        one_case['area'] = case['s']               #建物面積    
        one_case['build_type'] = case['b']         #建物型態 e.g.大樓,公寓,透天厝...etc    
        one_case['main_purpose'] = case['pu']      #主要用途    
        one_case['floor'] = case['f']              #樓別/樓高   
        one_case['layout'] = case['v']             #格局
        one_case['elevator'] = case['el']          #有無電梯       
        one_case['manager'] = case['m']            #有無管理員          
        one_case['parking_num'] = case['l']        #車位個數    
        one_case['build_share1'] = case['bs']      #主建物面積占建物移轉總面積（扣除車位面積）之比例   
        one_case['build_share2'] = case['es']      #主建物面積占建物移轉總面積之比例   
        one_case['note'] = case['note']            #附記, e.g. 頂加 
        one_case['deal_date'] = case['e']          #成交日期(tw)   
        one_case['unit_price'] = case['p']         #單價  
        one_case['price'] = case['tp']             #總價 (萬)
        all_cases.append(one_case.copy())
    return all_cases

cols=['address','community','lon','lat',
      'age','area','build_type','main_purpose',
      'floor','layout','elevator','manager','parking_num',
      'build_share1','build_share2','note',
      'deal_date','unit_price','price']

# 將list 轉換為 dataframe
def to_df(all_cases, cols):
    df_house = pd.DataFrame (all_cases, columns = cols)
    return df_house

# 將原始數據保存到 CSV 檔案
def to_csv(df_house, district, cols):
    df_house.to_csv('price_{0}_201208_202212.csv'.format(district), columns = cols, index = False)        
    print('price_{0}_201208_202212.csv saved successfully !'.format(district))

### 東區
district = "東區"
url = "https://lvr.land.moi.gov.tw/SERVICE/QueryPrice/f6dfdf588349cff5c638f77f6b539f14?q=VTJGc2RHVmtYMStYQStYb2tEWWk5Z1cvSm1LangreXJUem5KUEFyeFRtclU2V2N5QmpNQ0VxajBDdUdSNFpWek8yN3YwVy9aZitIMG1FMTU3M0hWWDZkSm83d2ExVlNnWEZORWFpdUo0ZUxoek9rZzZoNjJBWk5TQjlJeGhZbkdnNmZkM3IwYW5YQThIZm1rS1Y3amlRN1dHUGxNNW5SOXVuUnZybWtYNzdNbTFjRUFTTzlsK2ZhenR0VVVRNXJla1hzMm1IcWQ1aTMvdDhLMkNyOTE2a210YURNMU9aQUQvNjdGYW5Jb0pJQVNrNDkxaHhEQ3d3ZTFxZTdPR3VCVXB0QllkTEJIODU3Sisvb1plMmROd0N1Q1VNK3k2LzJXdWhpTk83YXhBWjE0dkF2dTZmb2pyY2E4bStNUDVVa09vbTdoNkhJUk5lYUYvblVJVC8yRnZBbHRpR1lZdFNMSmU1UUVXSSsyNmIrZVcyNUZ5Q2xEWGo3MlQ2bUhKUytCNjBFbStnVTNqUlpYTGxRaDJKVUVlSVpVTnNrMWlFY3R1a2VJbmdXY3VFVWhaMzRCMzFyYzdpWmpPK2dEaEVGd2E0ZGt0cDlDZElJSzFvSkFBRTZOUlNHbUI2bUFTYXJYemFveFBVUVFob1orK3hnU0JnZHM0aGlDK3lER2Jvc01QdFFIdTVkbTB1UW1vMFdJSVlmc1FhZ0grbHA0Mkk1amdyTWkrZXR4VSs2NkpkbHBuajNEUWpkeFk3NnpJb29NTGdwRGt1Uk84ZW14RWR1NEdseFhTRlZRQUhsbUNKM09EN3JxRUd2elp6UVR4ek5TMGcybkZHTGY5MHpCOEVLYnFuNEZOS0dNWXZPalVLZlUrbXdqd0RJNDM4TENHVTlxWnMzcTBvd3hEcWRJTHB1VC96akVyWFQrN1g1VWhlTUM="
data = json_parsing(url)
all_cases = rename_col(data)
df_house1 = to_df(all_cases, cols)
to_csv(df_house1, district, cols)

### 西區
district = "西區"
url = "https://lvr.land.moi.gov.tw/SERVICE/QueryPrice/e4c24ae2e9eb422e1cda49b22128fd18?q=VTJGc2RHVmtYMStMT1VWRHFsVEZUb2VFeDV2R3A5M1dPbkRkdWlXb01EL2lkUlBoTTJhWFB6V0Npa2tTbmxTYU9PZjVlU0svRElTbFhHSnczS0xqYWx2aXpCZ3lNTnkvRjJLRzZpTGYxc0czdStXOXB1ZXJEMFNoWHRZdm42QjlhVXArbkRENWtNT3drb3lYcmIxUjVqL2lKSC9tdHR1aXg0dDZLaGpkdGFYT0JTcEdVQjN6QWxTY0ZmNFAwc2dxTmlvd2JHNVREa2xZZ2U4cmU0dGQ3bjJ2YmVaa202ZmVlWTlVOVY0REdoTjdKdkJqaG1LWTBJWUtBSmcreU91VE8veVprdHh4cURXUWRVaFRhN0JoMk81bDhqWi85QVB1NWhaUm5BdUFMSW1OZ0tibERxY2t6MEtzZGV4bWxmdkw5d0FPYTJkaXUrNi9ISEt6Y2NlY0cwTFNMRkQ0MFVId2t0OEhYVm9vMlBhTHRjRE0zZjJiUmpmak9HY3VCVXU3UG1LUzVJbThzUUp3ZXFTMEhiWFJlQmxkZXVXanNjUXN5T0x2NW1Ca1dzWVpYZjdXajd2WGtDQ3cxTnNFMUc2NHpBSXcvdzJxbUh3REhRV0plUEJDZ2w5WEhsQmlWb3FKbW93dU1RdjlSNW14TWhqVVU0c3pkVXEwSHJiN0c3MnJpciswQlRIWEhsSTZZUjZXS0pJZlZRMGFKdDR1M3NkRTVuWnlObkVMbjRxSHJKeXltZXZSVWk2WmtWY2UvNzNKcTRyOXFhZkVxVEI1TGxiMkxPWmgwR0puc3d1dklHK1dXMFJYUTlSUHpLMUR6MVp2RnVjQVFyVGpqclFNbExpa3ZpbDlCM3FPWXhHZnFqUjZ1Ni9Vc3N4djVzQ00zZEczMDBDejF5U2IzV3daaHptaU0wTWxOaFRHWDIzQ2o2ZEo="
data = json_parsing(url)
all_cases = rename_col(data)
df_house2 = to_df(all_cases, cols)
to_csv(df_house2, district, cols)

### 南區
district = "南區"
url = "https://lvr.land.moi.gov.tw/SERVICE/QueryPrice/db22b201b8c716223cc415456a7ffa60?q=VTJGc2RHVmtYMS9JcDUzaDB0c3NRTVk4R3Nlb3MxSVo0QUpwdEp2OGp5bHpDbzQzS2NKOHE3aXVhY1ZPTEQxbWl5SEU0WmNNdUZtS0J5L3hKN0xPWk91Y2I4aTJ5bjRZRDk0UFQvNHFkR1VqYUJYay9hc3JpMHk4N2tuSTZadkpORzBSb1FyaVBwSVd4TUErNDBTWmRSL3E4a3JDMzVnQXVuNDRYajZZWW02Y2tMUGNxeGx1SkdQbnVVWmx4NTBwMXR4b0hWNUhpTjdhaUo0OHg1UWFoamFXNkhkQ1FoY05QZ2RpVGJqeDFIaWsyNXZHT3pPQU1jWDZ3RzZzUTcvUHE2VzdZZTBZSUE1ODNBbzJiWTFVdFREVmVUbDlXenRDMU5teHBwL3Irc016TXd3M3BGV0ZKUUI3NDd2VXpxTk0yQ1Vabkh4bE80Rnowemo1NHJSS3BlcmQvN2RaRkNEbUhORjZTZHRuOUEvZWp3NGZTS0RCZVNkZGl2UHhveXJZYVAwN3VCRkhFbGZHdUYwdGdPYjNNNVhweUhSVisyWkJaVlhtLytTVHdSQURJMFMxaFVKcmhSN0FuTkRYYW8vZFFIVzZCN2U0N2dKTkEzcWlFNTZMQXcxUjN0eUVuK2JEOUsxNzNqckhUbVpkYTgyR2NkTm1UcU5qaGdwS3FFdFRJdjhzWE5oY2laeGxoYlZDOHpHSmxUM21oRjFzS2ZYYnVibDRUa2VWUVlsNTNuRjJvd2hMT3pNTTZWem1Ba1RDcXNLTWNOV1ZDNTJ4M2RxM0thczhlNkFWYm15SDMybEFxZGY5emd6N2NscDZGYk9rMnM2Q0szYmp3Znc4WGxTNkFXTjY5eVdHS2ZMMFR5VmlncHZuRmExNk5EYm82ejgrN1NvMGZ5UTluNm5jYisvTkZOeklRVkpsZkw3UXlxVEI="
data = json_parsing(url)
all_cases = rename_col(data)
df_house3 = to_df(all_cases, cols)
to_csv(df_house3, district, cols)

### 北區
district = "北區"
url = "https://lvr.land.moi.gov.tw/SERVICE/QueryPrice/65ea05e176765a4571788aa6a535f5fb?q=VTJGc2RHVmtYMTlubS9lNzBaVG1ZcHluN0o1NVNiQVprT0lYSFBDSHhZL0pHVkpueGFYVVJSZHVRZko3S0crazE2ZXpCNEZvbW9EQ3FCaCsyMVdmeVBVcEdQR0dia0RtTitTWThwcHkvdTNNU1pOL1RkYzNuK1YrVE0yNGNZdEdGNWxnRTR2bU5aYjFoZHpkZndWeVZkWm96MUFPUVpwOEFLVVdsVUlTdVNDVzZxRUJZbmV6M1BGMzJXdTlDM21VbXpIYTJFZ1JBSWgzVWNaUnpzMUNnVnFucUN0d2JoWUFic0czaHJPaVJCcVpncHN2Y2FBbkdrQjNWR1JBRVVqRjErVWpSYXBBUGdzc1ZJQTdBWnRuUVlOODhCMmNYak9yOXlCK2hTVVZlVW9WZHNCbmdUdzRIMmtJWGw1cGpBQ2xFRHhnL3U5QVYwZk1zNG9GOXo1Smp1b1JQYUNhS3ptQzYzc3p6eHJTRW1MN1EzTGlpUVVRazFGa0xCbVpwM3ZTQUhBeXI3OHl6V2RrRGh4VXI1VGdtZ3dQRUJGMVM5dVJzWWl3M01MVnJoUXJJbm5BZ1BrQTdxNTRMMCsvYzdveTJveDRyL2k0TXJvTkI0TGROMmNMUkxMdDI0OE9lODRMV0oyQ044bEZDWGQ4aHV6QjM0ZUxGV01jTnczRW8vblF4aFRLRlA4SmFOeDUzSjdmMzJpRWQ5eExoTThUWjNHM3JCNGExanVaSFhRRXU4bDZMRmJ3dVhRZnRwMnp5Q0pwK2FxMFowV0VUUGRCT2M3NjBaNURYeUpVczEwd01zRWRKMmVIRFhyUzZPZkt1cDRXcm85SUFoMThqem5FWVFLSkRTd29DaDV6R1pIc2hCVWdFN1Z5MFZCVkY3YjFwb1B2eWNqQ1REYlZaOEJCUGl2MUtuYzFHRlQwdWxqNWo0ck0="
data = json_parsing(url)
all_cases = rename_col(data)
df_house4 = to_df(all_cases, cols)
to_csv(df_house4, district, cols)

### 中區
district = "中區"
url = "https://lvr.land.moi.gov.tw/SERVICE/QueryPrice/127a531578bc959f7f2b12bcbe700fb1?q=VTJGc2RHVmtYMThKN1BYYTFySDhxaDBzaWttYjVEWFRmN0ZVYktqNGJJZkNtK1FKZ0hkK2diT254R1N5UDRCZGx3dUxxS0YwR2ZBYlFjUVFiR3g2RndXRUgxSng4ZHpHV3R1QlV6RTcwaXkyaUxyWGFBMFQ1NUpMUU9iVEhpNVNOdmVRUVUySElGMGRQWHJaU1VMS3RCbHJscEpEc1MwYzI2OG9aY3ZiV0l5dEJBaTFhKy9GdXdvWTB3RzNVajJZSldTUDdZTmxuOHcvSnVDR3Nxd2wzUEFvY2V2TXF5ZGkzZVRGbytMUDVJTTNDV1ZNNHRuNGp3R0dYU1NvbCtKMkdERGVFNndaYlZVeHhvWTJsTmVwczJNYVc1MG1PaDEyVWdoT3hUOGZmbVM1Q3JrdEEyYXpMUTIvRHZUMTRrZzlObmprMUlhL0pKTHh6bDlnYnh1cHVTZDBvY2M0TmpnTEFtbHNlbUhRdGxZU04yelBDY2Z5QVh5ZFJRYXRZWkEzemkyckUzdHFtYmdTZnpDTHdOcTlhdHpjZzREMTBEWkJKMlhvTmNVRjZXdFBteWNLQ0VzL1h6Smx1RVNaN1lNRjkyQUNUTHg0VHZDTXJPZmcrWTkraTB6RWlCemFkRDJQcVN1OFRHMmxBWWRzVzJ0czd2T2Yya0dydy9URkZhNUdNSllTWWErVkpyNXRDMnFKQ09NQUxNdGxOZkM4c0hWdGJaSXVaNHRXR2ZjUVorS0hyYmZnM0pMVkFsVE9ObG5Eby9aUGhCalNXa1NpUDBraTA1ZzhaOUZyOVQrRHM3eFFiemNQZlJZaDRsdERTNmdKeko1c2xmQ2cwWUFWbGcxTlBEOTdpeEtNU2ZlbnlVQzUzZ2owRENJYzBUSTVsYnVsdVVxSDM5L2xkZmhCVGtxaXVwSndrdFFucU50UXpkTVk="
data = json_parsing(url)
all_cases = rename_col(data)
df_house5 = to_df(all_cases, cols)
to_csv(df_house5, district, cols)

### 西屯區
district = "西屯區"
url = "https://lvr.land.moi.gov.tw/SERVICE/QueryPrice/e1f7fb15f2569b88edbfd6a2fb7e5980?q=VTJGc2RHVmtYMTkwMXJKV2p5TmxNZjRyb3lnUDRtcStKVWZtc1dUUUtlN3lqbE5qQldWKzFTUU5RUDRCajE2ZUQxK3NCTldSRmtpc3RDcFdJSkNqdEx3UkMxb3huNFFIN0VoT2piNTY2NHJ5ejdjdkFVSVJZYnpHbFVtU25qZFhhMVRaczcvVVJiTlY3dm45MFdnM08rVTVSaU9tcHkrT1BVRFlYcW15OWwzaTRoY3BVS204N05nSXhZUjYxUEw0Y2t4NmM0Q3BJSm05Y3VjMzJsWFNXWEI2cURGdWxxSzJ4dE5VTDZtcVZDME10V3VPVTlOdVpacHAzQjdLazNESWs5RzlJRStSc3hDY3pxQUdzV3dtQWFNa2FZM25Ga1NBYzR4WUYxMXBqeWFjcGtTempzengwYUNGUm1pL3hJVzlqZVIvL3UvT3JoUUtYVFk4dU9NZzloMTNVSzM3VUxVaGovMGJVcGx3TFVVLzRMbVR2MDRpT0lYSytpMEkxZUxmczE4NTllY3dTSWVtS09NT2tDUnNyU1FZN3Z5VWZIZndSUjR2TnZIZ3FLTUNOT1liUUhIY2tUNUpzQWlKSlZPaFFZdVNwbkpqendOaXRBWTJlMzUxVkdYazJ5V1ZqL1YxSWpPNnA5N25EeUl6Qy9QempCeFR2NU5Vc0NPRkkxWk82TzBNZWliMTM1VXBCbnJkWjI0N2lFY2lXbXVvczZIZE9nZjRPczBCM2dOK3l1QkxncXdicFFuZWdVSTExSE5OeDAzUWtEbi9iaHZIVE5GUVVNTHc0Rm9zUWI5SDhIc3BNcDQ3K21rY1ZCYlNoaDBrV0JINlZhNjBqaGprVThpRlFCZEZsOENyQW5ZN05tYTlEYmRGTlFmVGlLTDhSWFhWRTJQQjNOZFdNQ3ZiWk55Zm1xWGRLd2ZPc0I2M0dwSzE="
data = json_parsing(url)
all_cases = rename_col(data)
df_house6 = to_df(all_cases, cols)
to_csv(df_house6, district, cols)

### 南屯區
district = "南屯區"
url = "https://lvr.land.moi.gov.tw/SERVICE/QueryPrice/7b8379ae48fa0927933e4d9fd3a4e712?q=VTJGc2RHVmtYMS9OcDVnK2hnNFAwMHFGNVZGSytrUDhzZS83ZTlWV3VJMHMwVE53VHkxdncxYnJDK0Z0WlZ4SDlaQ1AyQ1V5ZUMzTHgvNlFBYjUzcEpFQ1MrazhmdTZZbU93QVVqSGZiaSt1dVJzSXlMMk92RzVWMGJiSzNSZzJRQ0ZvS3BNZldxZWpFZUZUdjVsOXhZdGhwMHpjOVB2eTBNMzVncnlDNWtTQVhyTVBGRXRpSlN2RGRCKzJJMitYTkcrVXU0dUpNK3VRT1NLV0JNdFhla0lGdW4yRFNYM3JkMEhxUnFRcDhrUS9laVJVMWVvRFFqb2FtT2Nmb3lVOFJYdmRVaGtITUgrUytXMDJkWWNrRUY4bitBcnQ3TXN5SXNaL1hxSVBDLzRvd0hlcTd0bWxtbTBLVFFxMlB1ZGFjQ3V5UXhvVm12YVZ5N1NJK3UyUDRDOHZQSE80eTA1b2tQSXdrVXhUSlU1WlhCNTJpSCsxRVJNenNPTVJKWGMwS2pGZlJ5MTNlNFZhOXVYYUFHVEdRTjUvQnpSYVFlS25QZ1o5UUdRWno2ZVFmbU5rSC9sYzZVQlFzMXhDMjhwOHFGU0xiblFJR2tmOUJGK2Y4bXBHTnU4eGRYZUZMWU0veUZxcEh3ZzZ0VUxNQmVpNFRZSVpGT1FYeVZGaWVyQVJSTG5MeWRpQ2JwMWtIOWdId2hoUjlkc3U4N2VhSEpSZzBKbEFWVkRkL0QyQURPcnZ0OERjVUlJTkRUa1hxNTh4WXJjblZoRmoxL1lMSDIvTGplcGFEdDljWFN1Yk9sNHFLVDRKOGdRbUFlNUgraHdiZW1jR25RU2dmTTA0M3g4ZWowbUlvTkdrNTdaMFZFbklEVnZpSm5GbnBpejB1RG5tNVZGZ1F6dkJJSEQxMWRvZ0Y0QVc4UE1MdU9Ga0V0SFY="
data = json_parsing(url)
all_cases = rename_col(data)
df_house7 = to_df(all_cases, cols)
to_csv(df_house7, district, cols)

### 北屯區
district = "北屯區"
url = "https://lvr.land.moi.gov.tw/SERVICE/QueryPrice/415ccdc83870f122147b5dc4a4bfaea7?q=VTJGc2RHVmtYMThJczBrVVVpamFkSGZ4TWdRWC9OaWhkNmdzeXpUSkFISGRxVGhBeURBVlQxdDFQcEhBVVBWYng2cGlDQllOUkZDMzRkY3JQbDJJRlUzd1IvbVpRcTUzaTFpSnNVaW50WU9uam9INVNzUUpaNk1naXp1MFd6dDhNRk9FWVJtQi9UWFFKYWNTWWczVXIySzVLMWZkRTdqd3RJdGxMdEVyYis4N0FmOWptejByUFpqN2tHdzhSdmpxYk80SzVxMU8wWWM0ekVYRWNGWjJFWjFNc0h0empmZEVGaDJpdkVxcHJzZ2lsSHNzYVF1UktoRDhWclRrdXBZR3MvMlNLNHhtNXhwYm1iUVU0UmRibXhlNnQyVDRIZ3RxaDljWTZONm5qTWx6K3VsS0NjUzYzY1VuRUdlODBVZ3FPYzVIempMUVVzeE9JWitFaU5EL1d1YVBBcmptWUhMVGdJTGZWQmhFOXptTk4yZUgwUGRtdWFIaTRHb1o4UG5XT1JJdEYybkdESFloUXpDY2dqYjRSU291N014SzBNOHc1UmljdnZNME9wcHRGMDRZaHZhNWU4MlNWb0sxcUlIenY4YkV5L205Sm5hdnU3RUMrVzFCei8rQlJGQVVyMWlPY1V5ekdIbmVwa3RleVVsd0h6bGg3WGpzZzN5SlhpOVh4cTFXTEVOUjJoOFpCM3orMUpucEt5bjRrcDltNmtkelV6TXpEd29mSEZDOVF6d3BGcnIyUWhOODRLVE5OK2xQZ3cxZnVrMWY5eG9WZHlZS2dFMDVVeG1reU5pdjh3UWttMzNNaTZZN24yQitNT0FBS1lTSzhGcFIwR25JaUxzM1A0QWtsWGxtdzRHVkEwZ3RKVE9jeTN4bDQrbmFJTUkrMG5aYXV0V3BidzB0dkZkRVR1WFVjZEtVVloxek5jbEw="
data = json_parsing(url)
all_cases = rename_col(data)
df_house8 = to_df(all_cases, cols)
to_csv(df_house8, district, cols)

# add "district" column
df_house1.insert(0, "district", "東區")
df_house2.insert(0, "district", "西區")
df_house3.insert(0, "district", "南區")
df_house4.insert(0, "district", "北區")
df_house5.insert(0, "district", "中區")
df_house6.insert(0, "district", "西屯區")
df_house7.insert(0, "district", "南屯區")
df_house8.insert(0, "district", "北屯區")

# reset index
df_house1 = df_house1.reset_index(drop=True)
df_house2 = df_house2.reset_index(drop=True)
df_house3 = df_house3.reset_index(drop=True)
df_house4 = df_house4.reset_index(drop=True)
df_house5 = df_house5.reset_index(drop=True)
df_house6 = df_house6.reset_index(drop=True)
df_house7 = df_house7.reset_index(drop=True)
df_house8 = df_house8.reset_index(drop=True)

# concatenate all dataframe
df_house_all = pd.concat([df_house1, df_house2, df_house3, df_house4, df_house5, df_house6, df_house7, df_house8])

# export to csv
cols = ['district'] + cols
df_house_all.to_csv('price_all_201208_202212.csv', columns = cols, index = False)  



### Maching learning
import pandas as pd
import numpy as np
from collections import Counter
import seaborn as sns
from scipy.stats import pearsonr
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import matplotlib.font_manager as fm
from pandas.plotting import scatter_matrix
from datetime import datetime, timedelta
from scipy.stats import iqr
import math
import os
import re
         
# set working directory
os.chdir('/Users/xi/Desktop/python/20230411_HW2')
df = pd.read_csv('price_all_201208_202212.csv')

# set option to display all columns
pd.set_option('display.max_columns', None)
df.head(10)


# dataframe info
df.info()
# data types of area, build_share1, build_share2, unit_price, price should shold be numerical
# deal_date is not in date format
# year is object


## transform (area, build_share1, build_share2, unit_price, price) to numerical type
'''Could not convert string directly to float since there is 
a comma or dot in the number string.
Need to remove the comma from the string and then convert it to a float.'''
df["area"] = df["area"].str.replace(',', '').astype(float)
df["unit_price"] = df["unit_price"].str.replace(',', '').astype(float)
df["price"] = df["price"].str.replace(',', '').astype(float)
df["build_share1"] = df["build_share1"].str.replace('%', '').astype(float)/100
df["build_share2"] = df["build_share2"].str.replace('%', '').astype(float)/100

# check info again
df.info()

# take a glimpe of missing value
df.isna().sum()
# build_share2, community is undesired, will not discuss them from now on

# take a glimpe of missing value
len(df[df.duplicated()]) # 192

### EDA

## Numerical data
# dataframe description
df.describe()
# age, area, parking_num, price, unit_price seems to have outliers


# price histogram
plt.hist(df["price"][df["price"] > 0], bins=50)
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.xlim(df["price"][df["price"] > 0].min(), df["price"].max()) 
plt.ticklabel_format(style='plain', axis='x') 
plt.show() # highly skewed
# price boxplot
sns.boxplot(x = "price", data = df)
plt.ticklabel_format(style='plain', axis='x')

# unit_price histogram
plt.hist(df["unit_price"][df["unit_price"] > 0], bins=50)
plt.xlabel("Unit Price")
plt.ylabel("Frequency")
plt.xlim(df["unit_price"][df["unit_price"] > 0].min(), df["unit_price"].max()) 
plt.ticklabel_format(style='plain', axis='x') 
plt.show() # highly skewed
# unit_price boxplot
sns.boxplot(x = "unit_price", data = df)
plt.ticklabel_format(style='plain', axis='x')

# area histogram
plt.hist(df["area"], bins=50)
plt.xlabel("Area")
plt.ylabel("Frequency")
plt.xlim(df["area"].min(), df["area"].max()) 
plt.ticklabel_format(style='plain', axis='x') 
plt.show() # highly skewed
# area boxplot
sns.boxplot(x = "area", data = df)
plt.ticklabel_format(style='plain', axis='x')

# age histogram
plt.hist(df["age"], bins=50)
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.xlim(df["age"].min(), df["age"].max()) 
plt.ticklabel_format(style='plain', axis='x') 
plt.show() # highly skewed
# age boxplot
sns.boxplot(x = "age", data = df)
plt.ticklabel_format(style='plain', axis='x')

# parking_num
plt.hist(df["parking_num"], bins=50)
plt.xlabel("Parking number")
plt.ylabel("Frequency")
plt.xlim(df["parking_num"].min(), df["parking_num"].max()) 
plt.ticklabel_format(style='plain', axis='x') 
plt.show() # highly skewed
# parking_num boxplot
sns.boxplot(x = "parking_num", data = df)
plt.ticklabel_format(style='plain', axis='x')

# build_share1
plt.hist(df["build_share1"], bins=50)
plt.xlabel("Build Share1")
plt.ylabel("Frequency")
plt.xlim(df["build_share1"].min(), df["build_share1"].max()) 
plt.ticklabel_format(style='plain', axis='x') 
plt.show() # highly skewed
# unit_price boxplot
sns.boxplot(x = "build_share1", data = df)
plt.ticklabel_format(style='plain', axis='x')

## correlation
corr_matrix = df.corr()
sorted_columns = corr_matrix["price"].sort_values(ascending=False).index
sns.heatmap(df[sorted_columns].corr(), annot=True, annot_kws={'size': 7})
# area & price, age & build share1

# area & price
plt.scatter(x = df["area"], y = df["price"])
plt.plot(np.unique(df["area"]),
         np.poly1d(np.polyfit(df["area"], df["price"], 1))
         (np.unique(df["area"])), color='red')
plt.ticklabel_format(style='plain', axis='y')
plt.xlabel("Area")
plt.ylabel("Price")
plt.show()

# age & build_share1
sns.scatterplot(x='age', y='build_share1', data=df)
sns.regplot(x='age', y='build_share1', data=df, scatter=False, color='red')
plt.ticklabel_format(style='plain', axis='y')
plt.xlabel('Age')
plt.ylabel('Build Share1')
plt.show()


### Categorical data(average with median, boxplot)

# district
# barchart (with percentages)
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
counts = df["district"].value_counts()
percentages = counts / counts.sum() * 100
x = counts.index
fig, ax = plt.subplots()
ax.bar(x, counts.values, width=0.4, color='b', align='center')
plt.title('District Counts')
plt.xlabel('District')
plt.ylabel('Count')
for i, v in enumerate(counts.values):
    ax.text(i, v + 1, str(round(percentages.values[i], 2)) + '%', ha='center')
plt.show()
# average and median price by district
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
df1 = df.groupby("district")["price"].mean().reset_index()
df_median = df.groupby("district")["price"].median().reset_index()
plt.figure(figsize=(10,6))
sns.barplot(x="district", y="price", data=df1)
plt.plot(df_median["district"], df_median["price"], '-o', color='red')
plt.ticklabel_format(style='plain', axis='y')
plt.title("Average Price by District")
plt.xlabel("District")
plt.ylabel("Price(NTD)")
for i, v in enumerate(df1["price"].values):
    plt.text(i, v+10, '{:,.0f}'.format(v), ha='center')
plt.show()
# average and median unit price by district
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
df1 = df.groupby("district")["unit_price"].mean().reset_index()
df_median = df.groupby("district")["unit_price"].median().reset_index()
plt.figure(figsize=(10,6))
sns.barplot(x="district", y="unit_price", data=df1)
plt.plot(df_median["district"], df_median["unit_price"], '-o', color='red')
plt.ticklabel_format(style='plain', axis='y')
plt.title("Average Unit Price by District")
plt.xlabel("District")
plt.ylabel("Unit Price(NTD)")
for i, v in enumerate(df1["unit_price"].values):
    plt.text(i, v+10, '{:,.0f}'.format(v), ha='center')
plt.show()


# elevator
# barchart (with percentages)
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
counts = df["elevator"].value_counts()
percentages = counts / counts.sum() * 100
x = counts.index
fig, ax = plt.subplots()
ax.bar(x, counts.values, width=0.4, color='b', align='center')
plt.title('Elevator Counts')
plt.xlabel('Elevator')
plt.ylabel('Count')
for i, v in enumerate(counts.values):
    ax.text(i, v + 1, str(round(percentages.values[i], 2)) + '%', ha='center')
plt.show()
# average and median price by elevator
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
df1 = df.groupby("elevator")["price"].mean().reset_index()
df_median = df.groupby("elevator")["price"].median().reset_index()
plt.figure(figsize=(10,6))
sns.barplot(x="elevator", y="price", data=df1)
plt.plot(df_median["elevator"], df_median["price"], '-o', color='red')
plt.ticklabel_format(style='plain', axis='y')
plt.title("Average Price by Elevator")
plt.xlabel("Elevator")
plt.ylabel("Price(NTD)")
for i, v in enumerate(df1["price"].values):
    plt.text(i, v+10, '{:,.0f}'.format(v), ha='center')
plt.show()
# average and median unit price by elevator
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
df1 = df.groupby("elevator")["unit_price"].mean().reset_index()
df_median = df.groupby("elevator")["unit_price"].median().reset_index()
plt.figure(figsize=(10,6))
sns.barplot(x="elevator", y="unit_price", data=df1)
plt.plot(df_median["elevator"], df_median["unit_price"], '-o', color='red')
plt.ticklabel_format(style='plain', axis='y')
plt.title("Average Unit Price by Elevator")
plt.xlabel("Elevator")
plt.ylabel("Unit Price(NTD)")
for i, v in enumerate(df1["unit_price"].values):
    plt.text(i, v+10, '{:,.0f}'.format(v), ha='center')
plt.show()


# manager
# barchart (with percentages)
counts = df["manager"].value_counts()
percentages = counts / counts.sum() * 100
x = counts.index
fig, ax = plt.subplots()
ax.bar(x, counts.values, width=0.4, color='b', align='center')
plt.title('Manager Counts')
plt.xlabel('Manager')
plt.ylabel('Count')
for i, v in enumerate(counts.values):
    ax.text(i, v + 1, str(round(percentages.values[i], 2)) + '%', ha='center')
plt.show()
# average and median price by manager
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
df1 = df.groupby("manager")["price"].mean().reset_index()
df_median = df.groupby("manager")["price"].median().reset_index()
plt.figure(figsize=(10,6))
sns.barplot(x="manager", y="price", data=df1)
plt.plot(df_median["manager"], df_median["price"], '-o', color='red')
plt.ticklabel_format(style='plain', axis='y')
plt.title("Average Price by Manager")
plt.xlabel("Manager")
plt.ylabel("Price(NTD)")
for i, v in enumerate(df1["price"].values):
    plt.text(i, v+10, '{:,.0f}'.format(v), ha='center')
plt.show()
# average and median unit price by manager
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
df1 = df.groupby("manager")["unit_price"].mean().reset_index()
df_median = df.groupby("manager")["unit_price"].median().reset_index()
plt.figure(figsize=(10,6))
sns.barplot(x="manager", y="unit_price", data=df1)
plt.plot(df_median["manager"], df_median["unit_price"], '-o', color='red')
plt.ticklabel_format(style='plain', axis='y')
plt.title("Average Unit Price by Manager")
plt.xlabel("Manager")
plt.ylabel("Unit Price(NTD)")
for i, v in enumerate(df1["unit_price"].values):
    plt.text(i, v+10, '{:,.0f}'.format(v), ha='center')
plt.show()


# build_type
# top 5 categories
df["build_type"].value_counts()
build_type_shorten = {"住宅大樓(11層含以上有電梯)": "住宅大樓", "華廈(10層含以下有電梯)": "華廈", "公寓(5樓含以下無電梯)": "公寓", "套房(1房(1廳)1衛)": "套房"}
df["build_type"] = df["build_type"].replace(build_type_shorten)
top_build_type = df[df["build_type"].isin(df["build_type"].value_counts().index.tolist()[:5])].copy()
# barchart (with percentages)
counts = df["build_type"].value_counts()
percentages = counts / counts.sum() * 100
x = counts.index
fig, ax = plt.subplots()
ax.bar(x, counts.values, width=0.4, color='b', align='center')
plt.title('Building Type Counts')
plt.xlabel('Building Type')
plt.ylabel('Count')
for i, v in enumerate(counts.values):
    ax.text(i, v + 1, str(round(percentages.values[i], 2)) + '%', ha='center')
plt.show()
# average and median price by build_type
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
df1 = top_build_type.groupby("build_type")["price"].mean().reset_index()
df_median = top_build_type.groupby("build_type")["price"].median().reset_index()
plt.figure(figsize=(10,6))
sns.barplot(x="build_type", y="price", data=df1)
plt.plot(df_median["build_type"], df_median["price"], '-o', color='red')
plt.ticklabel_format(style='plain', axis='y')
plt.title("Average Price by Build Type")
plt.xlabel("Biuld Type")
plt.ylabel("Price(NTD)")
for i, v in enumerate(df1["price"].values):
    plt.text(i, v+10, '{:,.0f}'.format(v), ha='center')
plt.show()
# average and median unit price by build_type
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
df1 = top_build_type.groupby("build_type")["unit_price"].mean().reset_index()
df_median = top_build_type.groupby("build_type")["unit_price"].median().reset_index()
plt.figure(figsize=(10,6))
sns.barplot(x="build_type", y="unit_price", data=df1)
plt.plot(df_median["build_type"], df_median["unit_price"], '-o', color='red')
plt.ticklabel_format(style='plain', axis='y')
plt.title("Average Unit Price by Build Type")
plt.xlabel("Build Type")
plt.ylabel("Unit Price(NTD)")
for i, v in enumerate(df1["unit_price"].values):
    plt.text(i, v+10, '{:,.0f}'.format(v), ha='center')
plt.show()

# main_purpose
df["main_purpose"].value_counts() # only keep "住家用" in the following analysis


### data preprocessing

## duplicated data
len(df[df.duplicated()]) # 192
df = df.drop_duplicates().reset_index(drop = True)

# extract "road name" from "address" and create a new column
def extract_road(address):
    pattern = re.compile(r'^[\u4e00-\u9fa5]+')
    match = pattern.search(address)
    if match:
        return match.group(0)
    else:
        return ""
df["road_name"] = df["address"].apply(extract_road)


## extract bedroom, hall, bathroom from layout and store them in new columns
df[["bedroom_num", "hall_num", "bathroom_num"]] = df["layout"].str.extract(r'(\d+)房(\d+)廳(\d+)衛')
df[["bedroom_num", "hall_num", "bathroom_num"]] = df[["bedroom_num", "hall_num", "bathroom_num"]].fillna(0).astype(int)
# bedroom
df1 = df["bedroom_num"].value_counts().reset_index()
df1 = df1.sort_values(by = "index")
df1 = df1.rename(columns = {"index" : "bedroom_num", "bedroom_num":"count"})
# bedrooms bar chart
plt.bar(df1["bedroom_num"], df1["count"])
plt.title("Frequency of Bedrooms")
plt.xlabel("Bedroom")
plt.ylabel("Frequency")
plt.show()
# bedrooms < 25 vs. price
df1 = df.loc[df['bedroom_num'] < 25]
plt.scatter(x=df1["bedroom_num"], y=df1["price"])
plt.plot(np.unique(df1["bedroom_num"]),
         np.poly1d(np.polyfit(df1["bedroom_num"], df1["price"], 1))
         (np.unique(df1["bedroom_num"])), color='red')
plt.ticklabel_format(style='plain', axis='y')
plt.title("Price by Bedrooms less than 25")
plt.xlabel("Bedroom")
plt.ylabel("Price")
plt.show()
# bedrooms < 25 vs. unit price
df1 = df[~df["unit_price"].isna()]
df1 = df1.loc[df['bedroom_num'] < 25]
plt.scatter(x=df1["bedroom_num"], y=df1["unit_price"])
plt.plot(np.unique(df1["bedroom_num"]),
         np.poly1d(np.polyfit(df1["bedroom_num"], df1["unit_price"], 1))
         (np.unique(df1["bedroom_num"])), color='red')
plt.ticklabel_format(style='plain', axis='y')
plt.title("Unit Price by Bedrooms less than 25")
plt.xlabel("Bedroom")
plt.ylabel("Unit Price")
plt.show()

# hall
df1 = df["hall_num"].value_counts().reset_index()
df1 = df1.sort_values(by = "index")
df1 = df1.rename(columns = {"index" : "hall_num", "hall_num":"count"})
# halls bar chart
plt.bar(df1["hall_num"], df1["count"])
plt.title("Frequency of Halls")
plt.xlabel("Hall")
plt.ylabel("Frequency")
plt.show()
# hall < 20 vs. price
df1 = df.loc[df['hall_num'] < 20]
plt.scatter(x=df1["hall_num"], y=df1["price"])
plt.plot(np.unique(df1["hall_num"]),
         np.poly1d(np.polyfit(df1["hall_num"], df1["price"], 1))
         (np.unique(df1["hall_num"])), color='red')
plt.ticklabel_format(style='plain', axis='y')
tick_locs = np.arange(0, 21, 5)
tick_labels = [str(int(x)) for x in tick_locs]
plt.xticks(tick_locs, tick_labels)
plt.title("Price by Halls less than 20")
plt.xlabel("Hall")
plt.ylabel("Price")
plt.show()
# hall < 20 vs. unit price
df1 = df[~df["unit_price"].isna()]
df1 = df1.loc[df['hall_num'] < 25]
plt.scatter(x=df1["hall_num"], y=df1["unit_price"])
plt.plot(np.unique(df1["hall_num"]),
         np.poly1d(np.polyfit(df1["hall_num"], df1["unit_price"], 1))
         (np.unique(df1["hall_num"])), color='red')
plt.ticklabel_format(style='plain', axis='y')
plt.title("Unit Price by Halls less than 20")
plt.xlabel("Hall")
plt.ylabel("Unit Price")
plt.show()

# bathroom
df1 = df["bathroom_num"].value_counts().reset_index()
df1 = df1.sort_values(by = "index")
df1 = df1.rename(columns = {"index" : "bathroom_num", "bathroom_num":"count"})
# bathrooms bar chart
plt.bar(df1["bathroom_num"], df1["count"])
plt.title("Frequency of Bathrooms")
plt.xlabel("Bathroom")
plt.ylabel("Frequency")
plt.show()
# bathrooms < 20 vs. price
df1 = df.loc[df['bathroom_num'] < 20]
plt.scatter(x=df1["bathroom_num"], y=df1["price"])
plt.plot(np.unique(df1["bathroom_num"]),
         np.poly1d(np.polyfit(df1["bathroom_num"], df1["price"], 1))
         (np.unique(df1["bathroom_num"])), color='red')
tick_locs = np.arange(0, 21, 5)
tick_labels = [str(int(x)) for x in tick_locs]
plt.xticks(tick_locs, tick_labels)
plt.ticklabel_format(style='plain', axis='y')
plt.title("Price by Bathrooms less than 20")
plt.xlabel("Bathroom")
plt.ylabel("Price")
plt.show()
# bathrooms < 20 vs. unit price
df1 = df[~df["unit_price"].isna()]
df1 = df1.loc[df['bathroom_num'] < 20]
plt.scatter(x=df1["bathroom_num"], y=df1["unit_price"])
plt.plot(np.unique(df1["bathroom_num"]),
         np.poly1d(np.polyfit(df1["bathroom_num"], df1["unit_price"], 1))
         (np.unique(df1["bathroom_num"])), color='red')
tick_locs = np.arange(0, 21, 5)
tick_labels = [str(int(x)) for x in tick_locs]
plt.xticks(tick_locs, tick_labels)
plt.ticklabel_format(style='plain', axis='y')
plt.title("Unit Price by Bathrooms less than 20")
plt.xlabel("Bathroom")
plt.ylabel("Unit Price")
plt.show()


## extract "floor_extracted", "story" from "floor" and create new columns
df[["floor_extracted", "story"]]= df["floor"].str.split('/', expand=True)
# convert story to numeric
df["story"].unique()
floor_dict = {
  1: '一層', 2: '二層', 3: '三層', 4: '四層', 5: '五層', 6: '六層', 7: '七層', 8: '八層',
  9: '九層', 10: '十層', 11: '十一層', 12: '十二層', 13: '十三層', 14: '十四層', 
  15: '十五層', 16: '十六層', 17: '十七層', 18: '十八層', 19: '十九層', 20: '二十層',
  21: '二十一層', 22: '二十二層', 23: '二十三層', 24: '二十四層', 25: '二十五層', 
  26: '二十六層', 27: '二十七層', 28: '二十八層', 29: '二十九層', 30: '三十層', 31: '三十一層',
  32: '三十二層', 33: '三十三層', 34: '三十四層', 35: '三十五層', 36: '三十六層', 37: '三十七層',
  38: '三十八層', 39: '三十九層',40: '四十層', 41: '四十一層', 42: '四十二層', 43: '四十三層',
  None: '(空白)'}
df["story"] = df["story"].map({v: k for k, v in floor_dict.items()})


# split floor_extracted
floor_extracted_list = df["floor_extracted"].str.split(',')
floor_extracted_items = [item for inner_list in floor_extracted_list for item in inner_list]
item_counts = Counter(floor_extracted_items) 
filtered_counts = {k: v for k, v in item_counts.items() if k not in floor_dict.values()}
print(filtered_counts) # ”全“、”地下“ are important

# only consider 全、地下 and above-ground floors, delete other type of floor
drop_floor_items = ['見其他登記事項', '夾層', '屋頂突出物', '見其它登記事項', '走廊', 
              '電梯樓梯間', '瞭望室', '通道', '防空避難室', '平台', '騎樓', '']
new_floor_extracted_list = [[item for item in inner_list if item not in drop_floor_items] for inner_list in floor_extracted_list]
# check element in new_floor_extracted_list are removed
for inner_list in new_floor_extracted_list:
    for item in inner_list:
        if item in drop_floor_items:
            print("Failed: {} was not removed".format(item))
            break
    else:
        continue
    break
else:
    print("Successful")
# calculate total deal floor (above-ground and basement floor), basement floor counts as one floor
# create total deal floor column according to len of the new_floor_extracted_list
df["total_deal_floor"] = [len(item) for item in new_floor_extracted_list]
df.loc[df["floor_extracted"] == "全", "total_deal_floor"] = df["story"]
# do not consider the total deal floor of 透天厝
df.loc[(df["floor_extracted"] == "全") & (df["build_type"] == "透天厝"), "total_deal_floor"] = 0

# Create floor_sold to store the value of floor sold. 
# If a deal contains more than one floors, assign its mean value to the floor_sold.
# drop all items not in floor_dict
target_floor = dict(Counter([item for item in floor_extracted_items if item not in floor_dict.values()]))
target_floor = dict(sorted(target_floor.items(), key=lambda item: item[1], reverse = True))
drop_floor_items_for_cal = list(target_floor.keys())
new_floor_extracted_list_for_cal = [[item for item in inner_list 
                                     if item not in drop_floor_items_for_cal] 
                                    for inner_list in floor_extracted_list]
# check element in new_floor_extracted_list_for_col are removed
for inner_list in new_floor_extracted_list_for_cal:
    for item in inner_list:
        if item in drop_floor_items_for_cal:
            print("Failed: {} was not removed".format(item))
            break
    else:
        continue
    break
else:
    print("Successful")
# assign value to new_floor_extracted_list_for_cal    
cal_floor = [[list(floor_dict.keys())[list(floor_dict.values()).index(item)] 
              for item in inner_list] 
             for inner_list in new_floor_extracted_list_for_cal]
# find the mean for each inner_list of cal_floor
floor_sold = []
for inner_list in cal_floor:
    if len(inner_list) > 0:
        floor_sold.append(sum(inner_list) / len(inner_list))
    else:
        floor_sold.append("")
# add them to df and name the column "floor_sold" 
df["floor_sold"] = floor_sold
df['floor_sold'] = df['floor_sold'].replace('', 0).astype(float)
# fill in the mean of "全"
df.loc[df["floor_extracted"] == "全", "floor_sold"] = df["story"] / 2
# assign 0 to 透天厝
df.loc[(df["floor_extracted"] == "全") & (df["build_type"] == "透天厝"), "floor_sold"] = 0

# overview
df[["story", "total_deal_floor", "floor_sold"]].describe()
# story
df1 = df["story"].value_counts().reset_index()
df1 = df1.sort_values(by = "index")
df1 = df1.rename(columns = {"index" : "story", "story":"count"})
# story bar chart
plt.bar(df1["story"], df1["count"])
plt.title("Frequency of Building Stories")
plt.xlabel("Building Story")
plt.ylabel("Frequency")
plt.show()
# total_deal_floor
df1 = df["total_deal_floor"].value_counts().reset_index()
df1 = df1.sort_values(by = "index")
df1 = df1.rename(columns = {"index" : "total_deal_floor", "total_deal_floor":"count"})
# total_deal_floor bar chart
plt.bar(df1["total_deal_floor"], df1["count"])
plt.title("Frequency of Total Floor Transfered")
plt.xlabel("Total Floor Transfered")
plt.ylabel("Frequency")
plt.show()
# floor_sold
df1 = df["floor_sold"].value_counts().reset_index()
df1 = df1.sort_values(by = "index")
df1 = df1.rename(columns = {"index" : "floor_sold", "floor_sold":"count"})
# floor_sold bar chart
plt.bar(df1["floor_sold"], df1["count"])
plt.title("Frequency of Floor")
plt.xlabel("Floor")
plt.ylabel("Frequency")
plt.show()
# correlation with price and unit price
corr_matrix = df[["story", "total_deal_floor", "floor_sold", "price", "unit_price"]].corr()
sorted_columns = corr_matrix["price"].sort_values(ascending=False).index
sns.heatmap(df[sorted_columns].corr(), annot=True, annot_kws={'size': 7})


## note column manipulation
# 特殊交易：by不動產成交案件實際資訊申報書(買賣) 備註欄位選項
# https://news.591.com.tw/news/7610
# delete rows contain unnormal transaction
del_notes = ["親友、員工、共有人或其他特殊關係間之交易", "建商與地主合建案", 
         "陽台外推", "頂樓加蓋", "夾層", "其他增建", "未登記建物",
         "農作物", "機電設備", "農業設施", "急買急賣", "民情風俗",
         "瑕疵物件", "含租約", "毛胚屋", "具重建或重劃、都更等效益", 
         "畸零地", "借名登記", "受債權債務影響或債務抵償之交易", 
         "雙方合意解除契約", "土地交易案件之價格含未來興建房屋成本", 
         "地上權房屋", "市場攤位", "公共設施保留", "政府機關標讓售", 
         "地清或未辦繼承標售", "水利地承購", "協議價購", "僅車位交易", 
         "預售屋、或土地及建物分件登記案件", "親等","等親","親友","親屬",
         "血親","親人","親戚","姻親","親子","親朋","夫妻","父子","父女",
         "母子","子母","母女","兄弟","兄妹","姊弟","姊妹","姐弟","姐妹",
         "大伯","大嫂","女兒","小叔","小孩","父親","母親","弟媳","叔侄",
         "妹妹","妻舅","姊夫","姊姊","姐姐","姑姑","直系","表哥","近親",
         "姪女","祖孫","婚姻","甥舅","媳婦","朋友"]
df["note"].str.contains('|'.join(del_notes)).sum() # 47852 rows
df = df[~df['note'].fillna('').str.contains('|'.join(del_notes)) | df['note'].isna()].reset_index(drop = True)


## delete main_purpose other than 住家用
len(df[df["main_purpose"] != "住家用"]) # 21048
df = df[df["main_purpose"] == "住家用"].reset_index(drop=True)


## delete build_type other than 住宅大樓、華廈、透天厝、套房、公寓
len(df[~df["build_type"].isin(df["build_type"].value_counts()[:5].index)]) # 475
df = df[df["build_type"].isin(df["build_type"].value_counts()[:5].index)].reset_index(drop=True)


## create new data frame
new_df_cols = ['district','road_name', 'lon', 'lat', 'age', 'area', 'build_type', 
               'bedroom_num', 'hall_num', 'bathroom_num', 'story',
               'total_deal_floor', 'floor_sold','elevator', 'manager', 'parking_num',
               'build_share1', 'unit_price', 'price', 'deal_date']
df_new = df[new_df_cols]



### Split data into training and testing sets
from sklearn.model_selection import train_test_split
from matplotlib.font_manager import FontProperties

# extract year out for splitting data 
year_month_day = []
for date in df["deal_date"]:
    year, month, day = date.split("/")
    new_year = int(year) + 1911
    year_month_day.append((str(new_year), month, day))
# create year features for df_new
time = []
for inner_list in year_month_day:
    time.append(inner_list[0])
df_new["year"] = time
df_new["year"].isna().sum() # 0
df_new["year"] = df_new["year"].astype(int)

# model 1: total_price / unit_price
X_1 = df_new.drop("price", axis=1)
y_1 = df_new.price
X_train, X_test_1, y_train, y_test_1 = train_test_split(X_1, y_1, test_size=0.2, random_state=42)
X_train_1, X_val_1, y_train_1, y_val_1 = train_test_split(X_train, y_train, test_size=0.2, random_state=42)
df_train_1 = pd.concat([X_train_1, y_train_1], axis=1) #105396
df_val_1 = pd.concat([X_val_1, y_val_1], axis=1) #26350
df_test_1 = pd.concat([X_test_1, y_test_1], axis=1) #32937

# model 2: total_price / unit_price
# split by year
pre_covid = df_new[df_new["year"] <= 2019]
post_covid = df_new[df_new["year"] > 2019]
X_2 = pre_covid.drop("price", axis = 1)
y_2 = pre_covid.price
X_test_2 = post_covid.drop("price", axis = 1)
y_test_2 = post_covid.price
X_train_2, X_val_2, y_train_2, y_val_2 = train_test_split(X_2, y_2, test_size = 0.2, random_state = 42)
df_train_2 = pd.concat([X_train_2, y_train_2], axis = 1) #103342
df_val_2 = pd.concat([X_val_2, y_val_2], axis = 1) #25836
df_test_2 = pd.concat([X_test_2, y_test_2], axis = 1) #35505



### Model_1 training data
len(df_train_1[df_train_1["lon"] == 0]) # 1
len(df_train_1[df_train_1["lat"] == 0]) # 1
# nan was replaced with "" in previous manipulation
len(df_train_1[df_train_1["road_name"] == ""]) # 1670
# it seems wierd that bedroom_num, hall_num and bathroom_num be 0 at the same time
len(df_train_1[(df_train_1["bedroom_num"] == 0) & (df_train_1["hall_num"] == 0) & (df_train_1["bathroom_num"] == 0)]) # 2362
zero_counts = {}
for build_type in df_train_1["build_type"].unique():
    zero_counts[build_type] = {}
    for col in ["bedroom_num", "hall_num", "bathroom_num"]:
        zero_count = len(df_train_1[(df_train_1[col] == 0) & (df_train_1["build_type"] == build_type)])
        zero_counts[build_type][col] = zero_count
# 0 is normal in total_deal_floor and floor_sold of "透天厝" 
len(df_train_1[(df_train_1["total_deal_floor"] == 0) & (df_train_1["build_type"] != "透天厝")]) # 340
len(df_train_1[(df_train_1["floor_sold"] == 0) & (df_train_1["build_type"] != "透天厝")]) # 411


## road_name first(the following imputation heavily depend on road_name)
'''imputing the road_name with the road which has the median of price 
with which price of “” has the smallest distance'''
road_name_median = df_train_1[df_train_1["road_name"] != ""].groupby(["district","road_name"])["price"].median()
for index in df_train_1[df_train_1["road_name"] == ""].index:
    district_medians = road_name_median[road_name_median.index.get_level_values("district") == df_train_1.loc[index, "district"]]
    distances = []
    for median in district_medians:
        distances.append(np.absolute(df_train_1.loc[index, "price"] - median))
    j = distances.index(min(distances))
    df_train_1.loc[index, "road_name"] = district_medians.index[j][1]
# check all blank be filled in road_name
len(df_train_1[df_train_1["road_name"] == ""]) 


## price outliers
sns.boxplot(x = "price", data = df_train_1)
df_train_1["price"].describe()
Q1 = df_train_1['price'].quantile(0.25)
Q3 = df_train_1['price'].quantile(0.75)
IQR = Q3 - Q1
len(df_train_1[df_train_1["price"]> Q3 + 3*IQR]) # 3444
# transformed to the median groupby road_name
df_train_1 = df_train_1.reset_index(drop=True)
roadname_buildtype_median = df_train_1.groupby(["road_name", "build_type"])["price"].median()
for i, price in enumerate(df_train_1["price"]):
    if price > Q3 + 3*IQR:
        road_name = df_train_1.loc[i, "road_name"]
        build_type = df_train_1.loc[i, "build_type"]
        df_train_1.loc[i, "price"] = roadname_buildtype_median[(road_name, build_type)]
# delete rows greater than 3IQR after being transformed to the median
Q1 = df_train_1['price'].quantile(0.25)
Q3 = df_train_1['price'].quantile(0.75)
IQR = Q3 - Q1
len(df_train_1[df_train_1["price" ] > Q3 + 3*IQR]) # 2074
df_train_1 = df_train_1[~(df_train_1["price"] > Q3 + 3*IQR) | df_train_1["price"].isna()].reset_index(drop = True)
sns.boxplot(x = "price", data = df_train_1)


## unit_price outliers
df_train_1["unit_price"].describe()
sns.boxplot(x = "unit_price", data = df_train_1)
Q1 = df_train_1['unit_price'].quantile(0.25)
Q3 = df_train_1['unit_price'].quantile(0.75)
IQR = Q3 - Q1
len(df_train_1[df_train_1["unit_price"]> Q3 + 3*IQR]) # 57
# transformed to the median groupby road_name
roadname_buildtype_median = df_train_1.groupby(["road_name", "build_type"])["unit_price"].median()
for i, price in enumerate(df_train_1["unit_price"]):
    if price > Q3 + 3*IQR:
        road_name = df_train_1.loc[i, "road_name"]
        build_type = df_train_1.loc[i, "build_type"]
        df_train_1.loc[i, "unit_price"] = roadname_buildtype_median[(road_name, build_type)]
# delete rows greater than 3IQR after being transformed to the median groupby road_name
Q1 = df_train_1['unit_price'].quantile(0.25)
Q3 = df_train_1['unit_price'].quantile(0.75)
IQR = Q3 - Q1
len(df_train_1[df_train_1["unit_price"] > Q3 + 3*IQR]) # 1
df_train_1 = df_train_1[~(df_train_1["unit_price"] > Q3 + 3*IQR) | df_train_1["unit_price"].isna()].reset_index(drop = True)
# fill NaN with roadname_buildtype_median in unit_price
district_buildtype_median = df_train_1.dropna(subset = ["unit_price"]).groupby(["district", "build_type"])["unit_price"].median()
for i, unit_price in enumerate(df_train_1["unit_price"]):
    if math.isnan(unit_price):
        if df_train_1.loc[i, "build_type"] == "透天厝":
            df_train_1.loc[i, "unit_price"] = 0
        elif df_train_1.loc[i, "road_name"] in roadname_buildtype_median:
            df_train_1.loc[i, "unit_price"] = roadname_buildtype_median[(roadname_buildtype_median.index.get_level_values("road_name") == df_train_1.loc[i, "road_name"]) & (roadname_buildtype_median.index.get_level_values("build_type") == df_train_1.loc[i, "build_type"])].values[0]
        else:
            df_train_1.loc[i, "unit_price"] = district_buildtype_median[(district_buildtype_median.index.get_level_values("district") == df_train_1.loc[i, "district"]) & (district_buildtype_median.index.get_level_values("build_type") == df_train_1.loc[i, "build_type"])].values[0]
# check no NA
df_train_1["unit_price"].isna().sum() # 1
df_train_1.loc[df_train_1.unit_price.isna(), "unit_price"] = 191015
sns.boxplot(x = "unit_price", data = df_train_1)


## age outliers: it is possible for house age to be older than applicable limit (60 years)
sns.boxplot(x = "age", data = df_train_1)
plt.hist(df_train_1["age"].dropna(), bins=50)
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.xlim(df_train_1["age"].dropna().min(), df_train_1["age"].dropna().max()) 
plt.ticklabel_format(style='plain', axis='x') 
plt.show() 
# fill NaN with median age groupby road_name & build_type
len(df_train_1[df_train_1["age"].isna()]) # 21305
age_df = df_train_1[~df_train_1["age"].isna()]
roadname_buildtype_median = age_df.groupby(["road_name", "build_type"])["age"].median()
district_buildtype_median = df_train_1.groupby(["district", "build_type"])["age"].median()
for i, age in enumerate(df_train_1["age"]):
    if math.isnan(age):
        district = df_train_1.loc[i, "district"]
        road_name = df_train_1.loc[i, "road_name"]
        build_type = df_train_1.loc[i, "build_type"]
        if (road_name, build_type) in roadname_buildtype_median.index:
            df_train_1.loc[i, "age"] = roadname_buildtype_median[(road_name, build_type)]
        else:
            df_train_1.loc[i, "age"] = district_buildtype_median[(district, build_type)]
# check no NA
df_train_1["age"].isna().sum()
sns.boxplot(x = "age", data = df_train_1)


## area outliers
sns.boxplot(x = "area", data = df_train_1)
Q1 = df_train_1['area'].quantile(0.25)
Q3 = df_train_1['area'].quantile(0.75)
IQR = Q3 - Q1
len(df_train_1[df_train_1["area"]> Q3 + 3*IQR]) # 681
# transformed to the median groupby road_name, buil_type
roadname_buildtype_median = age_df.groupby(["road_name", "build_type"])["area"].median()
district_buildtype_median = age_df.groupby(["road_name", "build_type"])["area"].median()
for i, area in enumerate(df_train_1["area"]):
    if area > Q3 + 3*IQR:
        road_name = df_train_1.loc[i, "road_name"]
        build_type = df_train_1.loc[i, "build_type"]
        if (road_name, build_type) in roadname_buildtype_median:
            df_train_1.loc[i, "area"] = roadname_buildtype_median[(road_name, build_type)]
        elif (district, build_type) in district_buildtype_median:
            district = df_train_1.loc[i, "district"]
            df_train_1.loc[i, "area"] = district_buildtype_median[(district, build_type)]
# delete rows greater than 3IQR after being transformed to the median groupby road_name, buil_type
Q1 = df_train_1['area'].quantile(0.25)
Q3 = df_train_1['area'].quantile(0.75)
IQR = Q3 - Q1
len(df_train_1[df_train_1["area"] > Q3 + 3*IQR]) # 89
df_train_1 = df_train_1[~(df_train_1["area"] > Q3 + 3*IQR) | df_train_1["area"].isna()].reset_index(drop = True)


## build_share1 NaN: build_share1 of 透天厝 should be 0
len(df_train_1[df_train_1["build_share1"].isna()]) # 8835
len(df_train_1[df_train_1["build_share1"].isna() & (df_train_1["build_type"] == "透天厝")]) # 8243
# fill NaN with median build_share1 groupby road_name & build_type
share_buildtype_df = df_train_1[~(df_train_1["build_share1"].isna()) & (df_train_1["build_type"] != "透天厝")]
roadname_buildtype_median = share_buildtype_df.groupby(["road_name", "build_type"])["build_share1"].median()
district_buildtype_median = df_train_1.groupby(["district", "build_type"])["build_share1"].median()
for i, share in enumerate(df_train_1["build_share1"]):
    if math.isnan(share):
        road_name = df_train_1.loc[i, "road_name"]
        build_type = df_train_1.loc[i, "build_type"]
        if build_type == "透天厝":
            df_train_1.loc[i, "build_share1"] = 0
        elif (road_name, build_type) in roadname_buildtype_median.index:
            df_train_1.loc[i, "build_share1"] = roadname_buildtype_median[(road_name, build_type)]
        else: 
            df_train_1.loc[i, "build_share1"] = district_buildtype_median[(district, build_type)]
# check no NA
df_train_1["build_share1"].isna().sum()
sns.boxplot(x = "build_share1", data = df_train_1)

# it is unreasonable for bedroom_num, hall_num and bathroom_num all be 0
len(df_train_1[(df_train_1["bedroom_num"] == 0) & (df_train_1["hall_num"] == 0) & (df_train_1["bathroom_num"] == 0)]) # 1887
# fill mode after groupby road_name&build_type, if there is multiple modes, then fill in with mean
df_train_1.loc[(df_train_1["bedroom_num"] == 0) & (df_train_1["hall_num"] == 0) & (df_train_1["bathroom_num"] == 0), ["bedroom_num", "hall_num", "bathroom_num"]] = np.nan
df_train_1 = df_train_1[(df_train_1["bedroom_num"].notna()) & (df_train_1["hall_num"].notna()) & (df_train_1["bathroom_num"].notna())].reset_index(drop = True)


## do not consider 0 in total_deal_floor and floor_sold of "透天厝" 
# total_deal_floor
len(df_train_1[(df_train_1["total_deal_floor"] == 0) & (df_train_1["build_type"] != "透天厝")]) # 301
df_train_1.loc[(df_train_1["total_deal_floor"] == 0) & (df_train_1["build_type"] != "透天厝"), "total_deal_floor"] = np.nan
df_train_1["total_deal_floor"].isna().sum() #378
type_totalfloor = df_train_1[df_train_1["build_type"] != "透天厝"]
type_totalfloor = type_totalfloor[type_totalfloor["total_deal_floor"].notna()]
buildtype_median = type_totalfloor.groupby("build_type")["total_deal_floor"].median()
for i, total in enumerate(df_train_1["total_deal_floor"]):
    if math.isnan(total) :
        df_train_1.loc[i, "total_deal_floor"] = buildtype_median[df_train_1.loc[i, "build_type"]]
# check no NA
df_train_1["total_deal_floor"].isna().sum()


# floor_sold
len(df_train_1[(df_train_1["floor_sold"] == 0) & (df_train_1["build_type"] != "透天厝")]) # 362
df_train_1.loc[(df_train_1["floor_sold"] == 0) & (df_train_1["build_type"] != "透天厝"), "floor_sold"] = np.nan
df_train_1["floor_sold"].isna().sum() # 362
floor_sold = df_train_1[df_train_1["build_type"] != "透天厝"]
floor_sold = floor_sold[floor_sold["floor_sold"].notna()]
floor_median = floor_sold.groupby("build_type")["floor_sold"].median()
for i, floor in enumerate(df_train_1["floor_sold"]):
    if math.isnan(floor) :
        df_train_1.loc[i, "floor_sold"] = floor_median[df_train_1.loc[i, "build_type"]]
# check no NA
df_train_1["floor_sold"].isna().sum()


## story
df_train_1["story"].isna().sum() # 32
story_median = df_train_1.dropna().groupby("build_type")["story"].median()
for i, story in enumerate(df_train_1["story"]):
    if math.isnan(story) :
        df_train_1.loc[i, "story"] = story_median[df_train_1.loc[i, "build_type"]]
# check no NA
df_train_1["story"].isna().sum()


## lon, lat both be 0 in the row 
df_train_1[(df_train_1["lon"] == 0) | (df_train_1["lat"] == 0)]
lon_index = df_train_1[(df_train_1["lon"] == 0) | (df_train_1["lat"] == 0)].index
df_train_1.loc[lon_index, "lon"] = round(df_train_1[(df_train_1["road_name"] == "廣興巷") & (df_train_1["lon"] != 0)]["lon"].mean(), 4)
df_train_1.loc[lon_index, "lat"] = round(df_train_1[(df_train_1["road_name"] == "廣興巷") & (df_train_1["lat"] != 0)]["lat"].mean(), 4)


## convert deal_date to date type
df_train_1["deal_date"] = pd.to_datetime(df_train_1["deal_date"], format='%Y/%m/%d') # wrong dates exist
# split and count frequencies
df_date_split = df_train_1["deal_date"].str.split("/", expand = True)
df_date_split.columns = ["year", "month", "day"]
df_date_split["year"].value_counts()
df_date_split["month"].value_counts() # 00 month, replace it with 3ed mode = 10
df_date_split["day"].value_counts() 
# replace 00 month with the mode 10
df_train_1["deal_date"] = df_train_1["deal_date"].str.replace(r'(?<=\/)00(?=\/)', '10', regex=True)
# transform date format 
year_month_day = []
for date in df_train_1["deal_date"]:
    year, month, day = date.split("/")
    new_year = int(year) + 1911
    year_month_day.append(str(new_year) + '-' + month + '-' + day)
df_train_1["deal_date"] = year_month_day
# extract "month" from "deal year" and create a new column
df_train_1["month"] = pd.to_datetime(df_train_1['deal_date']).dt.month


### Model_1 validating data set
len(df_val_1[df_val_1["lon"] == 0]) # 0
len(df_val_1[df_val_1["lat"] == 0]) # 0
# nan was replaced with "" in previous manipulation
len(df_val_1[df_val_1["road_name"] == ""]) # 439
# it seems wierd that bedroom_num, hall_num and bathroom_num be 0 at the same time
len(df_val_1[(df_val_1["bedroom_num"] == 0) & (df_val_1["hall_num"] == 0) & (df_val_1["bathroom_num"] == 0)]) # 552
zero_counts = {}
for build_type in df_val_1["build_type"].unique():
    zero_counts[build_type] = {}
    for col in ["bedroom_num", "hall_num", "bathroom_num"]:
        zero_count = len(df_val_1[(df_val_1[col] == 0) & (df_val_1["build_type"] == build_type)])
        zero_counts[build_type][col] = zero_count
# 0 is normal in total_deal_floor and floor_sold of "透天厝" 
len(df_val_1[(df_val_1["total_deal_floor"] == 0) & (df_val_1["build_type"] != "透天厝")]) # 64
len(df_val_1[(df_val_1["floor_sold"] == 0) & (df_val_1["build_type"] != "透天厝")]) # 75


## road_name first(the following imputation heavily depend on road_name)
''' imputing the road_name with the road which has the median of price 
with which price of “” has the smallest distance'''
road_name_median = df_val_1[df_val_1["road_name"] != ""].groupby(["district","road_name"])["price"].median()
for index in df_val_1[df_val_1["road_name"] == ""].index:
    district_medians = road_name_median[road_name_median.index.get_level_values("district") == df_val_1.loc[index, "district"]]
    distances = []
    for median in district_medians:
        distances.append(np.absolute(df_val_1.loc[index, "price"] - median))
    j = distances.index(min(distances))
    df_val_1.loc[index, "road_name"] = district_medians.index[j][1]
# check all blank be filled in road_name
len(df_val_1[df_val_1["road_name"] == ""]) 


## price outliers
Q1 = df_val_1['price'].quantile(0.25)
Q3 = df_val_1['price'].quantile(0.75)
IQR = Q3 - Q1
len(df_val_1[df_val_1["price"]> Q3 + 3*IQR]) # 853
# transformed to the median groupby road_name
df_val_1 = df_val_1.reset_index(drop=True)
roadname_buildtype_median = df_val_1.groupby(["road_name", "build_type"])["price"].median()
for i, price in enumerate(df_val_1["price"]):
    if price > Q3 + 3*IQR:
        road_name = df_val_1.loc[i, "road_name"]
        build_type = df_val_1.loc[i, "build_type"]
        df_val_1.loc[i, "price"] = roadname_buildtype_median[(road_name, build_type)]
# delete rows greater than 3IQR after being transformed to the median
Q1 = df_val_1['price'].quantile(0.25)
Q3 = df_val_1['price'].quantile(0.75)
IQR = Q3 - Q1
len(df_val_1[df_val_1["price" ] > Q3 + 3*IQR]) # 592
df_val_1 = df_val_1[~(df_val_1["price"] > Q3 + 3*IQR) | df_val_1["price"].isna()].reset_index(drop = True)


## unit_price outliers
df_val_1["unit_price"].describe()
sns.boxplot(x = "unit_price", data = df_val_1)
Q1 = df_val_1['unit_price'].quantile(0.25)
Q3 = df_val_1['unit_price'].quantile(0.75)
IQR = Q3 - Q1
len(df_val_1[df_val_1["unit_price"]> Q3 + 3*IQR]) # 22
# transformed to the median groupby road_name
roadname_buildtype_median = df_val_1.groupby(["road_name", "build_type"])["unit_price"].median()
for i, price in enumerate(df_val_1["unit_price"]):
    if price > Q3 + 3*IQR:
        road_name = df_val_1.loc[i, "road_name"]
        build_type = df_val_1.loc[i, "build_type"]
        df_val_1.loc[i, "unit_price"] = roadname_buildtype_median[(road_name, build_type)]
# delete rows greater than 3IQR after being transformed to the median groupby road_name
Q1 = df_val_1['unit_price'].quantile(0.25)
Q3 = df_val_1['unit_price'].quantile(0.75)
IQR = Q3 - Q1
len(df_val_1[df_val_1["unit_price"] > Q3 + 3*IQR]) # 0
df_val_1 = df_val_1[~(df_val_1["unit_price"] > Q3 + 3*IQR) | df_val_1["unit_price"].isna()].reset_index(drop = True)
# fill NaN with roadname_buildtype_median in unit_price
district_buildtype_median = df_val_1.dropna(subset = ["unit_price"]).groupby(["district", "build_type"])["unit_price"].median()
for i, unit_price in enumerate(df_val_1["unit_price"]):
    if math.isnan(unit_price):
        if df_val_1.loc[i, "build_type"] == "透天厝":
            df_val_1.loc[i, "unit_price"] = 0
        elif df_val_1.loc[i, "road_name"] in roadname_buildtype_median:
            df_val_1.loc[i, "unit_price"] = roadname_buildtype_median[(roadname_buildtype_median.index.get_level_values("road_name") == df_val_1.loc[i, "road_name"]) & (roadname_buildtype_median.index.get_level_values("build_type") == df_val_1.loc[i, "build_type"])].values[0]
        else:
            df_val_1.loc[i, "unit_price"] = district_buildtype_median[(district_buildtype_median.index.get_level_values("district") == df_val_1.loc[i, "district"]) & (district_buildtype_median.index.get_level_values("build_type") == df_val_1.loc[i, "build_type"])].values[0]
# check no NA
df_val_1["unit_price"].isna().sum()


## age
# fill NaN with median age groupby road_name & build_type
len(df_val_1[df_val_1["age"].isna()]) # 5231
age_df = df_val_1[~df_val_1["age"].isna()]
roadname_buildtype_median = age_df.groupby(["road_name", "build_type"])["age"].median()
district_buildtype_median = df_val_1.groupby(["district", "build_type"])["age"].median()
for i, age in enumerate(df_val_1["age"]):
    if math.isnan(age):
        district = df_val_1.loc[i, "district"]
        road_name = df_val_1.loc[i, "road_name"]
        build_type = df_val_1.loc[i, "build_type"]
        if (road_name, build_type) in roadname_buildtype_median.index:
            df_val_1.loc[i, "age"] = roadname_buildtype_median[(road_name, build_type)]
        else:
            df_val_1.loc[i, "age"] = district_buildtype_median[(district, build_type)]
# check no NA
df_val_1["age"].isna().sum()


## area outliers
Q1 = df_val_1['area'].quantile(0.25)
Q3 = df_val_1['area'].quantile(0.75)
IQR = Q3 - Q1
len(df_val_1[df_val_1["area"]> Q3 + 3*IQR]) # 143
# transformed to the median groupby road_name, buil_type
roadname_buildtype_median = age_df.groupby(["road_name", "build_type"])["area"].median()
district_buildtype_median = age_df.groupby(["road_name", "build_type"])["area"].median()
for i, area in enumerate(df_val_1["area"]):
    if area > Q3 + 3*IQR:
        road_name = df_val_1.loc[i, "road_name"]
        build_type = df_val_1.loc[i, "build_type"]
        if (road_name, build_type) in roadname_buildtype_median:
            df_val_1.loc[i, "area"] = roadname_buildtype_median[(road_name, build_type)]
        elif (district, build_type) in district_buildtype_median:
            district = df_val_1.loc[i, "district"]
            df_val_1.loc[i, "area"] = district_buildtype_median[(district, build_type)]
# delete rows greater than 3IQR after being transformed to the median groupby road_name, buil_type
Q1 = df_val_1['area'].quantile(0.25)
Q3 = df_val_1['area'].quantile(0.75)
IQR = Q3 - Q1
len(df_val_1[df_val_1["area"] > Q3 + 3*IQR]) # 28
df_val_1 = df_val_1[~(df_val_1["area"] > Q3 + 3*IQR) | df_val_1["area"].isna()].reset_index(drop = True)


## build_share1 NaN: build_share1 of 透天厝 should be 0
len(df_val_1[df_val_1["build_share1"].isna()]) # 2209
len(df_val_1[df_val_1["build_share1"].isna() & (df_val_1["build_type"] == "透天厝")]) # 2061
# fill NaN with median build_share1 groupby road_name & build_type
share_buildtype_df = df_val_1[~(df_val_1["build_share1"].isna()) & (df_val_1["build_type"] != "透天厝")]
roadname_buildtype_median = share_buildtype_df.groupby(["road_name", "build_type"])["build_share1"].median()
district_buildtype_median = df_val_1.groupby(["district", "build_type"])["build_share1"].median()
for i, share in enumerate(df_val_1["build_share1"]):
    if math.isnan(share):
        road_name = df_val_1.loc[i, "road_name"]
        build_type = df_val_1.loc[i, "build_type"]
        if build_type == "透天厝":
            df_val_1.loc[i, "build_share1"] = 0
        elif (road_name, build_type) in roadname_buildtype_median.index:
            df_val_1.loc[i, "build_share1"] = roadname_buildtype_median[(road_name, build_type)]
        else: 
            df_val_1.loc[i, "build_share1"] = district_buildtype_median[(district, build_type)]
# check no NA
df_val_1["build_share1"].isna().sum()

# drop rows that bedroom_num, hall_num and bathroom_num all be 0
len(df_val_1[(df_val_1["bedroom_num"] == 0) & (df_val_1["hall_num"] == 0) & (df_val_1["bathroom_num"] == 0)]) # 391
# fill mode after groupby road_name&build_type, if there is multiple modes, then fill in with mean
df_val_1.loc[(df_val_1["bedroom_num"] == 0) & (df_val_1["hall_num"] == 0) & (df_val_1["bathroom_num"] == 0), ["bedroom_num", "hall_num", "bathroom_num"]] = np.nan
df_val_1 = df_val_1[(df_val_1["bedroom_num"].notna()) & (df_val_1["hall_num"].notna()) & (df_val_1["bathroom_num"].notna())].reset_index(drop = True)


## do not consider 0 in total_deal_floor and floor_sold of "透天厝" 
# total_deal_floor
len(df_val_1[(df_val_1["total_deal_floor"] == 0) & (df_val_1["build_type"] != "透天厝")]) # 60
df_val_1.loc[(df_val_1["total_deal_floor"] == 0) & (df_val_1["build_type"] != "透天厝"), "total_deal_floor"] = np.nan
df_val_1["total_deal_floor"].isna().sum() #378
type_totalfloor = df_val_1[df_val_1["build_type"] != "透天厝"]
type_totalfloor = type_totalfloor[type_totalfloor["total_deal_floor"].notna()]
buildtype_median = type_totalfloor.groupby("build_type")["total_deal_floor"].median()
for i, total in enumerate(df_val_1["total_deal_floor"]):
    if math.isnan(total) :
        df_val_1.loc[i, "total_deal_floor"] = buildtype_median[df_val_1.loc[i, "build_type"]]
# check no NA
df_val_1["total_deal_floor"].isna().sum()

# floor_sold
len(df_val_1[(df_val_1["floor_sold"] == 0) & (df_val_1["build_type"] != "透天厝")]) # 70
df_val_1.loc[(df_val_1["floor_sold"] == 0) & (df_val_1["build_type"] != "透天厝"), "floor_sold"] = np.nan
floor_sold = df_val_1[df_val_1["build_type"] != "透天厝"]
floor_sold = floor_sold[floor_sold["floor_sold"].notna()]
floor_median = floor_sold.groupby("build_type")["floor_sold"].median()
for i, floor in enumerate(df_val_1["floor_sold"]):
    if math.isnan(floor) :
        df_val_1.loc[i, "floor_sold"] = floor_median[df_val_1.loc[i, "build_type"]]
# check no NA
df_val_1["floor_sold"].isna().sum()

# story
df_val_1["story"].isna().sum() # 11
story_median = df_val_1.dropna().groupby("build_type")["story"].median()
for i, story in enumerate(df_val_1["story"]):
    if math.isnan(story) :
        df_val_1.loc[i, "story"] = story_median[df_val_1.loc[i, "build_type"]]
# check no NA
df_val_1["story"].isna().sum()


## convert deal_date to date type
# split and count frequencies
df_date_split = df_val_1["deal_date"].str.split("/", expand = True)
df_date_split.columns = ["year", "month", "day"]
df_date_split["year"].value_counts()
df_date_split["month"].value_counts() # 00 month, replace it with mode = 10
df_date_split["day"].value_counts() 
# replace 00 month with the mode 10
df_val_1["deal_date"] = df_val_1["deal_date"].str.replace(r'(?<=\/)00(?=\/)', '10', regex=True)
# replace .5 with the mode 25
df_val_1["deal_date"] = df_val_1["deal_date"].str.replace(r'\.5$', "25", regex=True)
# transform date format and replace deal_date with it
year_month_day = []
for date in df_val_1["deal_date"]:
    year, month, day = date.split("/")
    new_year = int(year) + 1911
    year_month_day.append(str(new_year) + '-' + month + '-' + day)
df_val_1["deal_date"] = year_month_day
# extract "month" from "deal year" and create a new column
df_val_1["month"] = pd.to_datetime(df_val_1['deal_date']).dt.month


### Model_1 testing data set
len(df_test_1[df_test_1["lon"] == 0]) # 0
len(df_test_1[df_test_1["lat"] == 0]) # 0
# nan was replaced with "" in previous manipulation
len(df_test_1[df_test_1["road_name"] == ""]) # 534
# it seems wierd that bedroom_num, hall_num and bathroom_num be 0 at the same time
len(df_test_1[(df_test_1["bedroom_num"] == 0) & (df_test_1["hall_num"] == 0) & (df_test_1["bathroom_num"] == 0)]) # 757
zero_counts = {}
for build_type in df_test_1["build_type"].unique():
    zero_counts[build_type] = {}
    for col in ["bedroom_num", "hall_num", "bathroom_num"]:
        zero_count = len(df_test_1[(df_test_1[col] == 0) & (df_test_1["build_type"] == build_type)])
        zero_counts[build_type][col] = zero_count
# 0 is normal in total_deal_floor and floor_sold of "透天厝" 
len(df_test_1[(df_test_1["total_deal_floor"] == 0) & (df_test_1["build_type"] != "透天厝")]) # 103
len(df_test_1[(df_test_1["floor_sold"] == 0) & (df_test_1["build_type"] != "透天厝")]) # 119


# road_name first(the following imputation heavily depend on road_name)
'''imputing the road_name with the road which has the median of price 
with which price of “” has the smallest distance'''
road_name_median = df_test_1[df_test_1["road_name"] != ""].groupby(["district","road_name"])["price"].median()
for index in df_test_1[df_test_1["road_name"] == ""].index:
    district_medians = road_name_median[road_name_median.index.get_level_values("district") == df_test_1.loc[index, "district"]]
    distances = []
    for median in district_medians:
        distances.append(np.absolute(df_test_1.loc[index, "price"] - median))
    j = distances.index(min(distances))
    df_test_1.loc[index, "road_name"] = district_medians.index[j][1]
# check all blank be filled in road_name
len(df_test_1[df_test_1["road_name"] == ""]) 


## price outliers
df_test_1["price"].describe()
Q1 = df_test_1['price'].quantile(0.25)
Q3 = df_test_1['price'].quantile(0.75)
IQR = Q3 - Q1
len(df_test_1[df_test_1["price"]> Q3 + 3*IQR]) # 1099
# transformed to the median groupby road_name
df_test_1 = df_test_1.reset_index(drop=True)
roadname_buildtype_median = df_test_1.groupby(["road_name", "build_type"])["price"].median()
for i, price in enumerate(df_test_1["price"]):
    if price > Q3 + 3*IQR:
        road_name = df_test_1.loc[i, "road_name"]
        build_type = df_test_1.loc[i, "build_type"]
        df_test_1.loc[i, "price"] = roadname_buildtype_median[(road_name, build_type)]
# delete rows greater than 3IQR after being transformed to the median
Q1 = df_test_1['price'].quantile(0.25)
Q3 = df_test_1['price'].quantile(0.75)
IQR = Q3 - Q1
len(df_test_1[df_test_1["price" ] > Q3 + 3*IQR]) # 638
df_test_1 = df_test_1[~(df_test_1["price"] > Q3 + 3*IQR) | df_test_1["price"].isna()].reset_index(drop = True)


## unit_price outliers
df_test_1["unit_price"].describe()
sns.boxplot(x = "unit_price", data = df_test_1)
Q1 = df_test_1['unit_price'].quantile(0.25)
Q3 = df_test_1['unit_price'].quantile(0.75)
IQR = Q3 - Q1
len(df_test_1[df_test_1["unit_price"]> Q3 + 3*IQR]) # 23
# transformed to the median groupby road_name
roadname_buildtype_median = df_test_1.groupby(["road_name", "build_type"])["unit_price"].median()
for i, price in enumerate(df_test_1["unit_price"]):
    if price > Q3 + 3*IQR:
        road_name = df_test_1.loc[i, "road_name"]
        build_type = df_test_1.loc[i, "build_type"]
        df_test_1.loc[i, "unit_price"] = roadname_buildtype_median[(road_name, build_type)]
# delete rows greater than 3IQR after being transformed to the median groupby road_name
Q1 = df_test_1['unit_price'].quantile(0.25)
Q3 = df_test_1['unit_price'].quantile(0.75)
IQR = Q3 - Q1
len(df_test_1[df_test_1["unit_price"] > Q3 + 3*IQR]) # 1
df_test_1 = df_test_1[~(df_test_1["unit_price"] > Q3 + 3*IQR) | df_test_1["unit_price"].isna()].reset_index(drop = True)
# fill NaN with roadname_buildtype_median in unit_price
district_buildtype_median = df_test_1.dropna(subset = ["unit_price"]).groupby(["district", "build_type"])["unit_price"].median()
for i, unit_price in enumerate(df_test_1["unit_price"]):
    if math.isnan(unit_price):
        if df_test_1.loc[i, "build_type"] == "透天厝":
            df_test_1.loc[i, "unit_price"] = 0
        elif df_test_1.loc[i, "road_name"] in roadname_buildtype_median:
            df_test_1.loc[i, "unit_price"] = roadname_buildtype_median[(roadname_buildtype_median.index.get_level_values("road_name") == df_test_1.loc[i, "road_name"]) & (roadname_buildtype_median.index.get_level_values("build_type") == df_test_1.loc[i, "build_type"])].values[0]
        else:
            df_test_1.loc[i, "unit_price"] = district_buildtype_median[(district_buildtype_median.index.get_level_values("district") == df_test_1.loc[i, "district"]) & (district_buildtype_median.index.get_level_values("build_type") == df_test_1.loc[i, "build_type"])].values[0]
# check no NA
df_test_1["unit_price"].isna().sum() # 3
df_test_1[df_test_1["unit_price"].isna()] # index: 21170, 22472, 26909
df_test_1.loc[df_test_1.index == 21170, "unit_price"] = 215180 # 北區住宅大樓
df_test_1.loc[df_test_1.index == 22472, "unit_price"] = 215180 # 北區住宅大樓
df_test_1.loc[df_test_1.index == 26909, "unit_price"] = 225002 # 南屯區住宅大樓


## age
# fill NaN with median age groupby road_name & build_type
len(df_test_1[df_test_1["age"].isna()]) # 6584
age_df = df_test_1[~df_test_1["age"].isna()]
roadname_buildtype_median = age_df.groupby(["road_name", "build_type"])["age"].median()
district_buildtype_median = df_test_1.groupby(["district", "build_type"])["age"].median()
for i, age in enumerate(df_test_1["age"]):
    if math.isnan(age):
        district = df_test_1.loc[i, "district"]
        road_name = df_test_1.loc[i, "road_name"]
        build_type = df_test_1.loc[i, "build_type"]
        if (road_name, build_type) in roadname_buildtype_median.index:
            df_test_1.loc[i, "age"] = roadname_buildtype_median[(road_name, build_type)]
        else:
            df_test_1.loc[i, "age"] = district_buildtype_median[(district, build_type)]
# check no NA
df_test_1["age"].isna().sum()


## area outliers
Q1 = df_test_1['area'].quantile(0.25)
Q3 = df_test_1['area'].quantile(0.75)
IQR = Q3 - Q1
len(df_test_1[df_test_1["area"]> Q3 + 3*IQR]) # 228
# transformed to the median groupby road_name, buil_type
roadname_buildtype_median = age_df.groupby(["road_name", "build_type"])["area"].median()
district_buildtype_median = age_df.groupby(["road_name", "build_type"])["area"].median()
for i, area in enumerate(df_test_1["area"]):
    if area > Q3 + 3*IQR:
        road_name = df_test_1.loc[i, "road_name"]
        build_type = df_test_1.loc[i, "build_type"]
        if (road_name, build_type) in roadname_buildtype_median:
            df_test_1.loc[i, "area"] = roadname_buildtype_median[(road_name, build_type)]
        elif (district, build_type) in district_buildtype_median:
            district = df_test_1.loc[i, "district"]
            df_test_1.loc[i, "area"] = district_buildtype_median[(district, build_type)]
# delete rows greater than 3IQR after being transformed to the median groupby road_name, buil_type
Q1 = df_test_1['area'].quantile(0.25)
Q3 = df_test_1['area'].quantile(0.75)
IQR = Q3 - Q1
len(df_test_1[df_test_1["area"] > Q3 + 3*IQR]) # 22
df_test_1 = df_test_1[~(df_test_1["area"] > Q3 + 3*IQR) | df_test_1["area"].isna()].reset_index(drop = True)


## build_share1 NaN: build_share1 of 透天厝 should be 0
len(df_test_1[df_test_1["build_share1"].isna()]) # 2724
len(df_test_1[df_test_1["build_share1"].isna() & (df_test_1["build_type"] == "透天厝")]) # 2554
# fill NaN with median build_share1 groupby road_name & build_type
share_buildtype_df = df_test_1[~(df_test_1["build_share1"].isna()) & (df_test_1["build_type"] != "透天厝")]
roadname_buildtype_median = share_buildtype_df.groupby(["road_name", "build_type"])["build_share1"].median()
district_buildtype_median = df_test_1.groupby(["district", "build_type"])["build_share1"].median()
for i, share in enumerate(df_test_1["build_share1"]):
    if math.isnan(share):
        road_name = df_test_1.loc[i, "road_name"]
        build_type = df_test_1.loc[i, "build_type"]
        if build_type == "透天厝":
            df_test_1.loc[i, "build_share1"] = 0
        elif (road_name, build_type) in roadname_buildtype_median.index:
            df_test_1.loc[i, "build_share1"] = roadname_buildtype_median[(road_name, build_type)]
        else: 
            df_test_1.loc[i, "build_share1"] = district_buildtype_median[(district, build_type)]
# check no NA
df_test_1["build_share1"].isna().sum()

## drop rows that bedroom_num, hall_num and bathroom_num all be 0
len(df_test_1[(df_test_1["bedroom_num"] == 0) & (df_test_1["hall_num"] == 0) & (df_test_1["bathroom_num"] == 0)]) # 613
# fill mode after groupby road_name&build_type, if there is multiple modes, then fill in with mean
df_test_1.loc[(df_test_1["bedroom_num"] == 0) & (df_test_1["hall_num"] == 0) & (df_test_1["bathroom_num"] == 0), ["bedroom_num", "hall_num", "bathroom_num"]] = np.nan
df_test_1 = df_test_1[(df_test_1["bedroom_num"].notna()) & (df_test_1["hall_num"].notna()) & (df_test_1["bathroom_num"].notna())].reset_index(drop = True)


## do not consider 0 in total_deal_floor and floor_sold of "透天厝" 
# total_deal_floor
len(df_test_1[(df_test_1["total_deal_floor"] == 0) & (df_test_1["build_type"] != "透天厝")]) # 94
df_test_1.loc[(df_test_1["total_deal_floor"] == 0) & (df_test_1["build_type"] != "透天厝"), "total_deal_floor"] = np.nan
df_test_1["total_deal_floor"].isna().sum() #378
type_totalfloor = df_test_1[df_test_1["build_type"] != "透天厝"]
type_totalfloor = type_totalfloor[type_totalfloor["total_deal_floor"].notna()]
buildtype_median = type_totalfloor.groupby("build_type")["total_deal_floor"].median()
for i, total in enumerate(df_test_1["total_deal_floor"]):
    if math.isnan(total) :
        df_test_1.loc[i, "total_deal_floor"] = buildtype_median[df_test_1.loc[i, "build_type"]]
# check no NA
df_test_1["total_deal_floor"].isna().sum()

# floor_sold
len(df_test_1[(df_test_1["floor_sold"] == 0) & (df_test_1["build_type"] != "透天厝")]) # 107
df_test_1.loc[(df_test_1["floor_sold"] == 0) & (df_test_1["build_type"] != "透天厝"), "floor_sold"] = np.nan
floor_sold = df_test_1[df_test_1["build_type"] != "透天厝"]
floor_sold = floor_sold[floor_sold["floor_sold"].notna()]
floor_median = floor_sold.groupby("build_type")["floor_sold"].median()
for i, floor in enumerate(df_test_1["floor_sold"]):
    if math.isnan(floor) :
        df_test_1.loc[i, "floor_sold"] = floor_median[df_test_1.loc[i, "build_type"]]
# check no NA
df_test_1["floor_sold"].isna().sum()


## story
df_test_1["story"].isna().sum() # 15
story_median = df_test_1.dropna().groupby("build_type")["story"].median()
for i, story in enumerate(df_test_1["story"]):
    if math.isnan(story) :
        df_test_1.loc[i, "story"] = story_median[df_test_1.loc[i, "build_type"]]
# check no NA
df_test_1["story"].isna().sum()


## convert deal_date to date type
# split and count frequencies
df_date_split = df_test_1["deal_date"].str.split("/", expand = True)
df_date_split.columns = ["year", "month", "day"]
df_date_split["year"].value_counts()
df_date_split["month"].value_counts()
df_date_split["day"].value_counts() 
# transform date format and replace deal_date with it
year_month_day = []
for date in df_test_1["deal_date"]:
    year, month, day = date.split("/")
    new_year = int(year) + 1911
    year_month_day.append(str(new_year) + '-' + month + '-' + day)
df_test_1["deal_date"] = year_month_day
# extract "month" from "deal year" and create a new column
df_test_1["month"] = pd.to_datetime(df_test_1['deal_date']).dt.month


### Model_2 training data
len(df_train_2[df_train_2["lon"] == 0]) # 1
len(df_train_2[df_train_2["lat"] == 0]) # 1
# nan was replaced with "" in previous manipulation
len(df_train_2[df_train_2["road_name"] == ""]) # 1518
# it seems wierd that bedroom_num, hall_num and bathroom_num be 0 at the same time
len(df_train_2[(df_train_2["bedroom_num"] == 0) & (df_train_2["hall_num"] == 0) & (df_train_2["bathroom_num"] == 0)]) # 2407
zero_counts = {}
for build_type in df_train_2["build_type"].unique():
    zero_counts[build_type] = {}
    for col in ["bedroom_num", "hall_num", "bathroom_num"]:
        zero_count = len(df_train_2[(df_train_2[col] == 0) & (df_train_2["build_type"] == build_type)])
        zero_counts[build_type][col] = zero_count
# 0 is normal in total_deal_floor and floor_sold of "透天厝" 
len(df_train_2[(df_train_2["total_deal_floor"] == 0) & (df_train_2["build_type"] != "透天厝")]) # 405
len(df_train_2[(df_train_2["floor_sold"] == 0) & (df_train_2["build_type"] != "透天厝")]) # 475


## road_name first(the following imputation heavily depend on road_name)
'''imputing the road_name with the road which has the median of price 
with which price of “” has the smallest distance'''
road_name_median = df_train_2[df_train_2["road_name"] != ""].groupby(["district","road_name"])["price"].median()
for index in df_train_2[df_train_2["road_name"] == ""].index:
    district_medians = road_name_median[road_name_median.index.get_level_values("district") == df_train_2.loc[index, "district"]]
    distances = []
    for median in district_medians:
        distances.append(np.absolute(df_train_2.loc[index, "price"] - median))
    j = distances.index(min(distances))
    df_train_2.loc[index, "road_name"] = district_medians.index[j][1]
# check all blank be filled in road_name
len(df_train_2[df_train_2["road_name"] == ""]) 


## price outliers
sns.boxplot(x = "price", data = df_train_2)
df_train_2["price"].describe()
Q1 = df_train_2['price'].quantile(0.25)
Q3 = df_train_2['price'].quantile(0.75)
IQR = Q3 - Q1
len(df_train_2[df_train_2["price"]> Q3 + 3*IQR]) # 3338
# transformed to the median groupby road_name
df_train_2 = df_train_2.reset_index(drop=True)
roadname_buildtype_median = df_train_2.groupby(["road_name", "build_type"])["price"].median()
for i, price in enumerate(df_train_2["price"]):
    if price > Q3 + 3*IQR:
        road_name = df_train_2.loc[i, "road_name"]
        build_type = df_train_2.loc[i, "build_type"]
        df_train_2.loc[i, "price"] = roadname_buildtype_median[(road_name, build_type)]
## delete rows greater than 3IQR after being transformed to the median
Q1 = df_train_2['price'].quantile(0.25)
Q3 = df_train_2['price'].quantile(0.75)
IQR = Q3 - Q1
len(df_train_2[df_train_2["price" ] > Q3 + 3*IQR]) # 2016
df_train_2 = df_train_2[~(df_train_2["price"] > Q3 + 3*IQR) | df_train_2["price"].isna()].reset_index(drop = True)
sns.boxplot(x = "price", data = df_train_2)


## unit_price outliers
df_train_2["unit_price"].describe()
sns.boxplot(x = "unit_price", data = df_train_2)
Q1 = df_train_2['unit_price'].quantile(0.25)
Q3 = df_train_2['unit_price'].quantile(0.75)
IQR = Q3 - Q1
len(df_train_2[df_train_2["unit_price"]> Q3 + 3*IQR]) # 124
# transformed to the median groupby road_name
roadname_buildtype_median = df_train_2.groupby(["road_name", "build_type"])["unit_price"].median()
for i, price in enumerate(df_train_2["unit_price"]):
    if price > Q3 + 3*IQR:
        road_name = df_train_2.loc[i, "road_name"]
        build_type = df_train_2.loc[i, "build_type"]
        df_train_2.loc[i, "unit_price"] = roadname_buildtype_median[(road_name, build_type)]
# delete rows greater than 3IQR after being transformed to the median groupby road_name
Q1 = df_train_2['unit_price'].quantile(0.25)
Q3 = df_train_2['unit_price'].quantile(0.75)
IQR = Q3 - Q1
len(df_train_2[df_train_2["unit_price"] > Q3 + 3*IQR]) # 0
df_train_2 = df_train_2[~(df_train_2["unit_price"] > Q3 + 3*IQR) | df_train_2["unit_price"].isna()].reset_index(drop = True)
# fill NaN with roadname_buildtype_median in unit_price
district_buildtype_median = df_train_2.dropna(subset = ["unit_price"]).groupby(["district", "build_type"])["unit_price"].median()
for i, unit_price in enumerate(df_train_2["unit_price"]):
    if math.isnan(unit_price):
        if df_train_2.loc[i, "build_type"] == "透天厝":
            df_train_2.loc[i, "unit_price"] = 0
        elif df_train_2.loc[i, "road_name"] in roadname_buildtype_median:
            df_train_2.loc[i, "unit_price"] = roadname_buildtype_median[(roadname_buildtype_median.index.get_level_values("road_name") == df_train_2.loc[i, "road_name"]) & (roadname_buildtype_median.index.get_level_values("build_type") == df_train_2.loc[i, "build_type"])].values[0]
        else:
            df_train_2.loc[i, "unit_price"] = district_buildtype_median[(district_buildtype_median.index.get_level_values("district") == df_train_2.loc[i, "district"]) & (district_buildtype_median.index.get_level_values("build_type") == df_train_2.loc[i, "build_type"])].values[0]
# check no NA
df_train_2["unit_price"].isna().sum()
df_train_2[df_train_2["unit_price"].isna()] # index = 14225
df_train_2.loc[df_train_2.unit_price.isna(), "unit_price"] = 180792
sns.boxplot(x = "unit_price", data = df_train_2)


## age outliers: it is possible for house age to be older than applicable limit (60 years)
sns.boxplot(x = "age", data = df_train_2)
plt.hist(df_train_2["age"].dropna(), bins=50)
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.xlim(df_train_2["age"].dropna().min(), df_train_2["age"].dropna().max()) 
plt.ticklabel_format(style='plain', axis='x') 
plt.show() 
# fill NaN with median age groupby road_name & build_type
len(df_train_2[df_train_2["age"].isna()]) # 24485
age_df = df_train_2[~df_train_2["age"].isna()]
roadname_buildtype_median = age_df.groupby(["road_name", "build_type"])["age"].median()
district_buildtype_median = df_train_2.groupby(["district", "build_type"])["age"].median()
for i, age in enumerate(df_train_2["age"]):
    if math.isnan(age):
        district = df_train_2.loc[i, "district"]
        road_name = df_train_2.loc[i, "road_name"]
        build_type = df_train_2.loc[i, "build_type"]
        if (road_name, build_type) in roadname_buildtype_median.index:
            df_train_2.loc[i, "age"] = roadname_buildtype_median[(road_name, build_type)]
        else:
            df_train_2.loc[i, "age"] = district_buildtype_median[(district, build_type)]
# check no NA
df_train_2["age"].isna().sum()
sns.boxplot(x = "age", data = df_train_2)


## area 
# outliers
sns.boxplot(x = "area", data = df_train_2)
Q1 = df_train_2['area'].quantile(0.25)
Q3 = df_train_2['area'].quantile(0.75)
IQR = Q3 - Q1
len(df_train_2[df_train_2["area"]> Q3 + 3*IQR]) # 688
# transformed to the median groupby road_name, buil_type
roadname_buildtype_median = age_df.groupby(["road_name", "build_type"])["area"].median()
district_buildtype_median = age_df.groupby(["road_name", "build_type"])["area"].median()
for i, area in enumerate(df_train_2["area"]):
    if area > Q3 + 3*IQR:
        road_name = df_train_2.loc[i, "road_name"]
        build_type = df_train_2.loc[i, "build_type"]
        if (road_name, build_type) in roadname_buildtype_median:
            df_train_2.loc[i, "area"] = roadname_buildtype_median[(road_name, build_type)]
        elif (district, build_type) in district_buildtype_median:
            district = df_train_2.loc[i, "district"]
            df_train_2.loc[i, "area"] = district_buildtype_median[(district, build_type)]
# delete rows greater than 3IQR after being transformed to the median groupby road_name, buil_type
Q1 = df_train_2['area'].quantile(0.25)
Q3 = df_train_2['area'].quantile(0.75)
IQR = Q3 - Q1
len(df_train_2[df_train_2["area"] > Q3 + 3*IQR]) # 75
df_train_2 = df_train_2[~(df_train_2["area"] > Q3 + 3*IQR) | df_train_2["area"].isna()].reset_index(drop = True)


## build_share1 NaN: build_share1 of 透天厝 should be 0
len(df_train_2[df_train_2["build_share1"].isna()]) # 9085
len(df_train_2[df_train_2["build_share1"].isna() & (df_train_2["build_type"] == "透天厝")]) # 8429
# fill NaN with median build_share1 groupby road_name & build_type
share_buildtype_df = df_train_2[~(df_train_2["build_share1"].isna()) & (df_train_2["build_type"] != "透天厝")]
roadname_buildtype_median = share_buildtype_df.groupby(["road_name", "build_type"])["build_share1"].median()
district_buildtype_median = df_train_2.groupby(["district", "build_type"])["build_share1"].median()
for i, share in enumerate(df_train_2["build_share1"]):
    if math.isnan(share):
        road_name = df_train_2.loc[i, "road_name"]
        build_type = df_train_2.loc[i, "build_type"]
        if build_type == "透天厝":
            df_train_2.loc[i, "build_share1"] = 0
        elif (road_name, build_type) in roadname_buildtype_median.index:
            df_train_2.loc[i, "build_share1"] = roadname_buildtype_median[(road_name, build_type)]
        else: 
            df_train_2.loc[i, "build_share1"] = district_buildtype_median[(district, build_type)]
# check no NA
df_train_2["build_share1"].isna().sum()
sns.boxplot(x = "build_share1", data = df_train_2)


## drop rows that bedroom_num, hall_num and bathroom_num all be 0
len(df_train_2[(df_train_2["bedroom_num"] == 0) & (df_train_2["hall_num"] == 0) & (df_train_2["bathroom_num"] == 0)]) # 1776
# fill mode after groupby road_name&build_type, if there is multiple modes, then fill in with mean
df_train_2.loc[(df_train_2["bedroom_num"] == 0) & (df_train_2["hall_num"] == 0) & (df_train_2["bathroom_num"] == 0), ["bedroom_num", "hall_num", "bathroom_num"]] = np.nan
df_train_2 = df_train_2[(df_train_2["bedroom_num"].notna()) & (df_train_2["hall_num"].notna()) & (df_train_2["bathroom_num"].notna())].reset_index(drop = True)


## do not consider 0 in total_deal_floor and floor_sold of "透天厝" 
# total_deal_floor
len(df_train_2[(df_train_2["total_deal_floor"] == 0) & (df_train_2["build_type"] != "透天厝")]) # 371
df_train_2.loc[(df_train_2["total_deal_floor"] == 0) & (df_train_2["build_type"] != "透天厝"), "total_deal_floor"] = np.nan
df_train_2["total_deal_floor"].isna().sum() #378
type_totalfloor = df_train_2[df_train_2["build_type"] != "透天厝"]
type_totalfloor = type_totalfloor[type_totalfloor["total_deal_floor"].notna()]
buildtype_median = type_totalfloor.groupby("build_type")["total_deal_floor"].median()
for i, total in enumerate(df_train_2["total_deal_floor"]):
    if math.isnan(total) :
        df_train_2.loc[i, "total_deal_floor"] = buildtype_median[df_train_2.loc[i, "build_type"]]
# check no NA
df_train_1["total_deal_floor"].isna().sum()

# floor_sold
len(df_train_2[(df_train_2["floor_sold"] == 0) & (df_train_2["build_type"] != "透天厝")]) # 431
df_train_2.loc[(df_train_2["floor_sold"] == 0) & (df_train_2["build_type"] != "透天厝"), "floor_sold"] = np.nan
floor_sold = df_train_2[df_train_2["build_type"] != "透天厝"]
floor_sold = floor_sold[floor_sold["floor_sold"].notna()]
floor_median = floor_sold.groupby("build_type")["floor_sold"].median()
for i, floor in enumerate(df_train_2["floor_sold"]):
    if math.isnan(floor) :
        df_train_2.loc[i, "floor_sold"] = floor_median[df_train_2.loc[i, "build_type"]]
# check no NA
df_train_2["floor_sold"].isna().sum()


## story
df_train_2["story"].isna().sum() # 43
story_median = df_train_2.dropna().groupby("build_type")["story"].median()
for i, story in enumerate(df_train_2["story"]):
    if math.isnan(story) :
        df_train_2.loc[i, "story"] = story_median[df_train_2.loc[i, "build_type"]]
# check no NA
df_train_2["story"].isna().sum()


## convert deal_date to date type
# split and count frequencies
df_date_split = df_train_2["deal_date"].str.split("/", expand = True)
df_date_split.columns = ["year", "month", "day"]
df_date_split["year"].value_counts()
df_date_split["month"].value_counts() # 00 month, replace it with 2nd mode = 10
df_date_split["day"].value_counts() 
# replace 00 month with the mode 10
df_train_2["deal_date"] = df_train_2["deal_date"].str.replace(r'(?<=\/)00(?=\/)', '10', regex=True)
# transform date format and replace deal_date with it
year_month_day = []
for date in df_train_2["deal_date"]:
    year, month, day = date.split("/")
    new_year = int(year) + 1911
    year_month_day.append(str(new_year) + '-' + month + '-' + day)
df_train_2["deal_date"] = year_month_day
# extract "month" from "deal year" and create a new column
df_train_2["month"] = pd.to_datetime(df_train_2['deal_date']).dt.month


### Model_2 validating data set
len(df_val_2[df_val_2["lon"] == 0]) # 0
len(df_val_2[df_val_2["lat"] == 0]) # 0
# nan was replaced with "" in previous manipulation
len(df_val_2[df_val_2["road_name"] == ""]) # 380
# it seems wierd that bedroom_num, hall_num and bathroom_num be 0 at the same time
len(df_val_2[(df_val_2["bedroom_num"] == 0) & (df_val_2["hall_num"] == 0) & (df_val_2["bathroom_num"] == 0)]) # 622
zero_counts = {}
for build_type in df_val_2["build_type"].unique():
    zero_counts[build_type] = {}
    for col in ["bedroom_num", "hall_num", "bathroom_num"]:
        zero_count = len(df_val_2[(df_val_2[col] == 0) & (df_val_2["build_type"] == build_type)])
        zero_counts[build_type][col] = zero_count
# 0 is normal in total_deal_floor and floor_sold of "透天厝" 
len(df_val_2[(df_val_2["total_deal_floor"] == 0) & (df_val_2["build_type"] != "透天厝")]) # 99
len(df_val_2[(df_val_2["floor_sold"] == 0) & (df_val_2["build_type"] != "透天厝")]) # 111


## road_name first(the following imputation heavily depend on road_name)
'''imputing the road_name with the road which has the median of price 
 with which price of “” has the smallest distance '''
road_name_median = df_val_2[df_val_2["road_name"] != ""].groupby(["district","road_name"])["price"].median()
for index in df_val_2[df_val_2["road_name"] == ""].index:
    district_medians = road_name_median[road_name_median.index.get_level_values("district") == df_val_2.loc[index, "district"]]
    distances = []
    for median in district_medians:
        distances.append(np.absolute(df_val_2.loc[index, "price"] - median))
    j = distances.index(min(distances))
    df_val_2.loc[index, "road_name"] = district_medians.index[j][1]
# check all blank be filled in road_name
len(df_val_2[df_val_2["road_name"] == ""]) 


# price outliers
df_val_2["price"].describe()
Q1 = df_val_2['price'].quantile(0.25)
Q3 = df_val_2['price'].quantile(0.75)
IQR = Q3 - Q1
len(df_val_2[df_val_2["price"]> Q3 + 3*IQR]) # 836
# transformed to the median groupby road_name
df_val_2 = df_val_2.reset_index(drop=True)
roadname_buildtype_median = df_val_2.groupby(["road_name", "build_type"])["price"].median()
for i, price in enumerate(df_val_2["price"]):
    if price > Q3 + 3*IQR:
        road_name = df_val_2.loc[i, "road_name"]
        build_type = df_val_2.loc[i, "build_type"]
        df_val_2.loc[i, "price"] = roadname_buildtype_median[(road_name, build_type)]
# delete rows greater than 3IQR after being transformed to the median
Q1 = df_val_2['price'].quantile(0.25)
Q3 = df_val_2['price'].quantile(0.75)
IQR = Q3 - Q1
len(df_val_2[df_val_2["price" ] > Q3 + 3*IQR]) # 517
df_val_2 = df_val_2[~(df_val_2["price"] > Q3 + 3*IQR) | df_val_2["price"].isna()].reset_index(drop = True)


## unit_price outliers
Q1 = df_val_2['unit_price'].quantile(0.25)
Q3 = df_val_2['unit_price'].quantile(0.75)
IQR = Q3 - Q1
len(df_val_2[df_val_2["unit_price"]> Q3 + 3*IQR]) # 37
# transformed to the median groupby road_name
roadname_buildtype_median = df_val_2.groupby(["road_name", "build_type"])["unit_price"].median()
for i, price in enumerate(df_val_2["unit_price"]):
    if price > Q3 + 3*IQR:
        road_name = df_val_2.loc[i, "road_name"]
        build_type = df_val_2.loc[i, "build_type"]
        df_val_2.loc[i, "unit_price"] = roadname_buildtype_median[(road_name, build_type)]
# delete rows greater than 3IQR after being transformed to the median groupby road_name
Q1 = df_val_2['unit_price'].quantile(0.25)
Q3 = df_val_2['unit_price'].quantile(0.75)
IQR = Q3 - Q1
len(df_val_2[df_val_2["unit_price"] > Q3 + 3*IQR]) # 0
df_val_2 = df_val_2[~(df_val_2["unit_price"] > Q3 + 3*IQR) | df_val_2["unit_price"].isna()].reset_index(drop = True)
# fill NaN with roadname_buildtype_median in unit_price
district_buildtype_median = df_val_2.dropna(subset = ["unit_price"]).groupby(["district", "build_type"])["unit_price"].median()
for i, unit_price in enumerate(df_val_2["unit_price"]):
    if math.isnan(unit_price):
        if df_val_2.loc[i, "build_type"] == "透天厝":
            df_val_2.loc[i, "unit_price"] = 0
        elif df_val_2.loc[i, "road_name"] in roadname_buildtype_median:
            df_val_2.loc[i, "unit_price"] = roadname_buildtype_median[(roadname_buildtype_median.index.get_level_values("road_name") == df_val_2.loc[i, "road_name"]) & (roadname_buildtype_median.index.get_level_values("build_type") == df_val_2.loc[i, "build_type"])].values[0]
        else:
            df_val_2.loc[i, "unit_price"] = district_buildtype_median[(district_buildtype_median.index.get_level_values("district") == df_val_2.loc[i, "district"]) & (district_buildtype_median.index.get_level_values("build_type") == df_val_2.loc[i, "build_type"])].values[0]
# check no NA
df_val_2["unit_price"].isna().sum()


## age outliers
# fill NaN with median age groupby road_name & build_type
len(df_val_2[df_val_2["age"].isna()]) # 5978
age_df = df_val_2[~df_val_2["age"].isna()]
roadname_buildtype_median = age_df.groupby(["road_name", "build_type"])["age"].median()
district_buildtype_median = df_val_2.groupby(["district", "build_type"])["age"].median()
for i, age in enumerate(df_val_2["age"]):
    if math.isnan(age):
        district = df_val_2.loc[i, "district"]
        road_name = df_val_2.loc[i, "road_name"]
        build_type = df_val_2.loc[i, "build_type"]
        if (road_name, build_type) in roadname_buildtype_median.index:
            df_val_2.loc[i, "age"] = roadname_buildtype_median[(road_name, build_type)]
        else:
            df_val_2.loc[i, "age"] = district_buildtype_median[(district, build_type)]
# check no NA
df_val_2["age"].isna().sum()


## area outliers
Q1 = df_val_2['area'].quantile(0.25)
Q3 = df_val_2['area'].quantile(0.75)
IQR = Q3 - Q1
len(df_val_2[df_val_2["area"]> Q3 + 3*IQR]) # 152
# transformed to the median groupby road_name, buil_type
roadname_buildtype_median = age_df.groupby(["road_name", "build_type"])["area"].median()
district_buildtype_median = age_df.groupby(["road_name", "build_type"])["area"].median()
for i, area in enumerate(df_val_2["area"]):
    if area > Q3 + 3*IQR:
        road_name = df_val_2.loc[i, "road_name"]
        build_type = df_val_2.loc[i, "build_type"]
        if (road_name, build_type) in roadname_buildtype_median:
            df_val_2.loc[i, "area"] = roadname_buildtype_median[(road_name, build_type)]
        elif (district, build_type) in district_buildtype_median:
            district = df_val_2.loc[i, "district"]
            df_val_2.loc[i, "area"] = district_buildtype_median[(district, build_type)]
# delete rows greater than 3IQR after being transformed to the median groupby road_name, buil_type
Q1 = df_val_2['area'].quantile(0.25)
Q3 = df_val_2['area'].quantile(0.75)
IQR = Q3 - Q1
len(df_val_2[df_val_2["area"] > Q3 + 3*IQR]) # 20
df_val_2 = df_val_2[~(df_val_2["area"] > Q3 + 3*IQR) | df_val_2["area"].isna()].reset_index(drop = True)


## build_share1 NaN: build_share1 of 透天厝 should be 0
len(df_val_2[df_val_2["build_share1"].isna()]) # 2236
len(df_val_2[df_val_2["build_share1"].isna() & (df_val_2["build_type"] == "透天厝")]) # 2035
# fill NaN with median build_share1 groupby road_name & build_type
share_buildtype_df = df_val_2[~(df_val_2["build_share1"].isna()) & (df_val_2["build_type"] != "透天厝")]
roadname_buildtype_median = share_buildtype_df.groupby(["road_name", "build_type"])["build_share1"].median()
district_buildtype_median = df_val_2.groupby(["district", "build_type"])["build_share1"].median()
for i, share in enumerate(df_val_2["build_share1"]):
    if math.isnan(share):
        road_name = df_val_2.loc[i, "road_name"]
        build_type = df_val_2.loc[i, "build_type"]
        if build_type == "透天厝":
            df_val_2.loc[i, "build_share1"] = 0
        elif (road_name, build_type) in roadname_buildtype_median.index:
            df_val_2.loc[i, "build_share1"] = roadname_buildtype_median[(road_name, build_type)]
        else: 
            df_val_2.loc[i, "build_share1"] = district_buildtype_median[(district, build_type)]
# check no NA
df_val_2["build_share1"].isna().sum()


## drop rows that bedroom_num, hall_num and bathroom_num all be 0
len(df_val_2[(df_val_2["bedroom_num"] == 0) & (df_val_2["hall_num"] == 0) & (df_val_2["bathroom_num"] == 0)]) # 481
# fill mode after groupby road_name&build_type, if there is multiple modes, then fill in with mean
df_val_2.loc[(df_val_2["bedroom_num"] == 0) & (df_val_2["hall_num"] == 0) & (df_val_2["bathroom_num"] == 0), ["bedroom_num", "hall_num", "bathroom_num"]] = np.nan
df_val_2 = df_val_2[(df_val_2["bedroom_num"].notna()) & (df_val_2["hall_num"].notna()) & (df_val_2["bathroom_num"].notna())].reset_index(drop = True)


''' do not consider 0 in total_deal_floor and floor_sold of "透天厝" '''
## total_deal_floor
len(df_val_2[(df_val_2["total_deal_floor"] == 0) & (df_val_2["build_type"] != "透天厝")]) # 83
df_val_2.loc[(df_val_2["total_deal_floor"] == 0) & (df_val_2["build_type"] != "透天厝"), "total_deal_floor"] = np.nan
df_val_2["total_deal_floor"].isna().sum() #378
type_totalfloor = df_val_2[df_val_2["build_type"] != "透天厝"]
type_totalfloor = type_totalfloor[type_totalfloor["total_deal_floor"].notna()]
buildtype_median = type_totalfloor.groupby("build_type")["total_deal_floor"].median()
for i, total in enumerate(df_val_2["total_deal_floor"]):
    if math.isnan(total) :
        df_val_2.loc[i, "total_deal_floor"] = buildtype_median[df_val_2.loc[i, "build_type"]]
# check no NA
df_val_2["total_deal_floor"].isna().sum()


## floor_sold
len(df_val_2[(df_val_2["floor_sold"] == 0) & (df_val_2["build_type"] != "透天厝")]) # 93
df_val_2.loc[(df_val_2["floor_sold"] == 0) & (df_val_2["build_type"] != "透天厝"), "floor_sold"] = np.nan
floor_sold = df_val_2[df_val_2["build_type"] != "透天厝"]
floor_sold = floor_sold[floor_sold["floor_sold"].notna()]
floor_median = floor_sold.groupby("build_type")["floor_sold"].median()
for i, floor in enumerate(df_val_2["floor_sold"]):
    if math.isnan(floor) :
        df_val_2.loc[i, "floor_sold"] = floor_median[df_val_2.loc[i, "build_type"]]
# check no NA
df_val_2["floor_sold"].isna().sum()


## story
df_val_2["story"].isna().sum() # 11
story_median = df_val_2.dropna().groupby("build_type")["story"].median()
for i, story in enumerate(df_val_2["story"]):
    if math.isnan(story) :
        df_val_2.loc[i, "story"] = story_median[df_val_2.loc[i, "build_type"]]
# check no NA
df_val_2["story"].isna().sum()


## convert deal_date to date type
# split and count frequencies
df_date_split = df_val_2["deal_date"].str.split("/", expand = True)
df_date_split.columns = ["year", "month", "day"]
df_date_split["year"].value_counts()
df_date_split["month"].value_counts()
df_date_split["day"].value_counts() 
# transform date format and replace deal_date with it
year_month_day = []
for date in df_val_2["deal_date"]:
    year, month, day = date.split("/")
    new_year = int(year) + 1911
    year_month_day.append(str(new_year) + '-' + month + '-' + day)
df_val_2["deal_date"] = year_month_day
# extract "month" from "deal year" and create a new column
df_val_2["month"] = pd.to_datetime(df_val_2['deal_date']).dt.month


### Model_2 testing data set
len(df_test_2[df_test_2["lon"] == 0]) # 1
len(df_test_2[df_test_2["lat"] == 0]) # 1
# nan was replaced with "" in previous manipulation
len(df_test_2[df_test_2["road_name"] == ""]) # 745
# it seems wierd that bedroom_num, hall_num and bathroom_num be 0 at the same time
len(df_test_2[(df_test_2["bedroom_num"] == 0) & (df_test_2["hall_num"] == 0) & (df_test_2["bathroom_num"] == 0)]) # 642
zero_counts = {}
for build_type in df_test_2["build_type"].unique():
    zero_counts[build_type] = {}
    for col in ["bedroom_num", "hall_num", "bathroom_num"]:
        zero_count = len(df_test_2[(df_test_2[col] == 0) & (df_test_2["build_type"] == build_type)])
        zero_counts[build_type][col] = zero_count
# 0 is normal in total_deal_floor and floor_sold of "透天厝" 
len(df_test_2[(df_test_2["total_deal_floor"] == 0) & (df_test_2["build_type"] != "透天厝")]) # 3
len(df_test_2[(df_test_2["floor_sold"] == 0) & (df_test_2["build_type"] != "透天厝")]) # 19


## road_name first(the following imputation heavily depend on road_name)
'''imputing the road_name with the road which has the median of price 
 with which price of “” has the smallest distance '''
road_name_median = df_test_2[df_test_2["road_name"] != ""].groupby(["district","road_name"])["price"].median()
for index in df_test_2[df_test_2["road_name"] == ""].index:
    district_medians = road_name_median[road_name_median.index.get_level_values("district") == df_test_2.loc[index, "district"]]
    distances = []
    for median in district_medians:
        distances.append(np.absolute(df_test_2.loc[index, "price"] - median))
    j = distances.index(min(distances))
    df_test_2.loc[index, "road_name"] = district_medians.index[j][1]
# check all blank be filled in road_name
len(df_test_2[df_test_2["road_name"] == ""]) 


# price outliers
Q1 = df_test_2['price'].quantile(0.25)
Q3 = df_test_2['price'].quantile(0.75)
IQR = Q3 - Q1
len(df_test_2[df_test_2["price"]> Q3 + 3*IQR]) # 1131
# transformed to the median groupby road_name
df_test_2 = df_test_2.reset_index(drop=True)
roadname_buildtype_median = df_test_2.groupby(["road_name", "build_type"])["price"].median()
for i, price in enumerate(df_test_2["price"]):
    if price > Q3 + 3*IQR:
        road_name = df_test_2.loc[i, "road_name"]
        build_type = df_test_2.loc[i, "build_type"]
        df_test_2.loc[i, "price"] = roadname_buildtype_median[(road_name, build_type)]
# delete rows greater than 3IQR after being transformed to the median
Q1 = df_test_2['price'].quantile(0.25)
Q3 = df_test_2['price'].quantile(0.75)
IQR = Q3 - Q1
len(df_test_2[df_test_2["price" ] > Q3 + 3*IQR]) # 639
df_test_2 = df_test_2[~(df_test_2["price"] > Q3 + 3*IQR) | df_test_2["price"].isna()].reset_index(drop = True)


# unit_price outliers
Q1 = df_test_2['unit_price'].quantile(0.25)
Q3 = df_test_2['unit_price'].quantile(0.75)
IQR = Q3 - Q1
len(df_test_2[df_test_2["unit_price"]> Q3 + 3*IQR]) # 107
# transformed to the median groupby road_name
roadname_buildtype_median = df_test_2.groupby(["road_name", "build_type"])["unit_price"].median()
for i, price in enumerate(df_test_2["unit_price"]):
    if price > Q3 + 3*IQR:
        road_name = df_test_2.loc[i, "road_name"]
        build_type = df_test_2.loc[i, "build_type"]
        df_test_2.loc[i, "unit_price"] = roadname_buildtype_median[(road_name, build_type)]
# delete rows greater than 3IQR after being transformed to the median groupby road_name
Q1 = df_test_2['unit_price'].quantile(0.25)
Q3 = df_test_2['unit_price'].quantile(0.75)
IQR = Q3 - Q1
len(df_test_2[df_test_2["unit_price"] > Q3 + 3*IQR]) # 0
df_test_2 = df_test_2[~(df_test_2["unit_price"] > Q3 + 3*IQR) | df_test_2["unit_price"].isna()].reset_index(drop = True)
# fill NaN with roadname_buildtype_median in unit_price
district_buildtype_median = df_test_2.dropna(subset = ["unit_price"]).groupby(["district", "build_type"])["unit_price"].median()
for i, unit_price in enumerate(df_test_2["unit_price"]):
    if math.isnan(unit_price):
        if df_test_2.loc[i, "build_type"] == "透天厝":
            df_test_2.loc[i, "unit_price"] = 0
        elif df_test_2.loc[i, "road_name"] in roadname_buildtype_median:
            df_test_2.loc[i, "unit_price"] = roadname_buildtype_median[(roadname_buildtype_median.index.get_level_values("road_name") == df_test_2.loc[i, "road_name"]) & (roadname_buildtype_median.index.get_level_values("build_type") == df_test_2.loc[i, "build_type"])].values[0]
        else:
            df_test_2.loc[i, "unit_price"] = district_buildtype_median[(district_buildtype_median.index.get_level_values("district") == df_test_2.loc[i, "district"]) & (district_buildtype_median.index.get_level_values("build_type") == df_test_2.loc[i, "build_type"])].values[0]
# check no NA
df_test_2["unit_price"].isna().sum() # 0


# age outliers
# fill NaN with median age groupby road_name & build_type
len(df_test_2[df_test_2["age"].isna()]) # 2700
age_df = df_test_2[~df_test_2["age"].isna()]
roadname_buildtype_median = age_df.groupby(["road_name", "build_type"])["age"].median()
district_buildtype_median = df_test_2.groupby(["district", "build_type"])["age"].median()
for i, age in enumerate(df_test_2["age"]):
    if math.isnan(age):
        district = df_test_2.loc[i, "district"]
        road_name = df_test_2.loc[i, "road_name"]
        build_type = df_test_2.loc[i, "build_type"]
        if (road_name, build_type) in roadname_buildtype_median.index:
            df_test_2.loc[i, "age"] = roadname_buildtype_median[(road_name, build_type)]
        else:
            df_test_2.loc[i, "age"] = district_buildtype_median[(district, build_type)]
# check no NA
df_test_2["age"].isna().sum()

# area outliers
Q1 = df_test_2['area'].quantile(0.25)
Q3 = df_test_2['area'].quantile(0.75)
IQR = Q3 - Q1
len(df_test_2[df_test_2["area"]> Q3 + 3*IQR]) # 268
# transformed to the median groupby road_name, buil_type
roadname_buildtype_median = age_df.groupby(["road_name", "build_type"])["area"].median()
district_buildtype_median = age_df.groupby(["road_name", "build_type"])["area"].median()
for i, area in enumerate(df_test_2["area"]):
    if area > Q3 + 3*IQR:
        road_name = df_test_2.loc[i, "road_name"]
        build_type = df_test_2.loc[i, "build_type"]
        if (road_name, build_type) in roadname_buildtype_median:
            df_test_2.loc[i, "area"] = roadname_buildtype_median[(road_name, build_type)]
        elif (district, build_type) in district_buildtype_median:
            district = df_test_2.loc[i, "district"]
            df_test_2.loc[i, "area"] = district_buildtype_median[(district, build_type)]
# delete rows greater than 3IQR after being transformed to the median groupby road_name, buil_type
Q1 = df_test_2['area'].quantile(0.25)
Q3 = df_test_2['area'].quantile(0.75)
IQR = Q3 - Q1
len(df_test_2[df_test_2["area"] > Q3 + 3*IQR]) # 26
df_test_2 = df_test_2[~(df_test_2["area"] > Q3 + 3*IQR) | df_test_2["area"].isna()].reset_index(drop = True)


# build_share1 NaN: build_share1 of 透天厝 should be 0
len(df_test_2[df_test_2["build_share1"].isna()]) # 2498
len(df_test_2[df_test_2["build_share1"].isna() & (df_test_2["build_type"] == "透天厝")]) # 2444
# fill NaN with median build_share1 groupby road_name & build_type
share_buildtype_df = df_test_2[~(df_test_2["build_share1"].isna()) & (df_test_2["build_type"] != "透天厝")]
roadname_buildtype_median = share_buildtype_df.groupby(["road_name", "build_type"])["build_share1"].median()
district_buildtype_median = df_test_2.groupby(["district", "build_type"])["build_share1"].median()
for i, share in enumerate(df_test_2["build_share1"]):
    if math.isnan(share):
        road_name = df_test_2.loc[i, "road_name"]
        build_type = df_test_2.loc[i, "build_type"]
        if build_type == "透天厝":
            df_test_2.loc[i, "build_share1"] = 0
        elif (road_name, build_type) in roadname_buildtype_median.index:
            df_test_2.loc[i, "build_share1"] = roadname_buildtype_median[(road_name, build_type)]
        else: 
            df_test_2.loc[i, "build_share1"] = district_buildtype_median[(district, build_type)]
# check no NA
df_test_2["build_share1"].isna().sum()

# drop rows that bedroom_num, hall_num and bathroom_num all be 0
len(df_test_2[(df_test_2["bedroom_num"] == 0) & (df_test_2["hall_num"] == 0) & (df_test_2["bathroom_num"] == 0)]) # 613
# fill mode after groupby road_name&build_type, if there is multiple modes, then fill in with mean
df_test_2.loc[(df_test_2["bedroom_num"] == 0) & (df_test_2["hall_num"] == 0) & (df_test_2["bathroom_num"] == 0), ["bedroom_num", "hall_num", "bathroom_num"]] = np.nan
df_test_2 = df_test_2[(df_test_2["bedroom_num"].notna()) & (df_test_2["hall_num"].notna()) & (df_test_2["bathroom_num"].notna())].reset_index(drop = True)

# do not consider 0 in total_deal_floor and floor_sold of "透天厝" 
# total_deal_floor
len(df_test_2[(df_test_2["total_deal_floor"] == 0) & (df_test_2["build_type"] != "透天厝")]) # 528
df_test_2.loc[(df_test_2["total_deal_floor"] == 0) & (df_test_2["build_type"] != "透天厝"), "total_deal_floor"] = np.nan
df_test_2["total_deal_floor"].isna().sum() #378
type_totalfloor = df_test_2[df_test_2["build_type"] != "透天厝"]
type_totalfloor = type_totalfloor[type_totalfloor["total_deal_floor"].notna()]
buildtype_median = type_totalfloor.groupby("build_type")["total_deal_floor"].median()
for i, total in enumerate(df_test_2["total_deal_floor"]):
    if math.isnan(total) :
        df_test_2.loc[i, "total_deal_floor"] = buildtype_median[df_test_2.loc[i, "build_type"]]
# check no NA
df_test_2["total_deal_floor"].isna().sum()

# floor_sold
len(df_test_2[(df_test_2["floor_sold"] == 0) & (df_test_2["build_type"] != "透天厝")]) # 19
df_test_2.loc[(df_test_2["floor_sold"] == 0) & (df_test_2["build_type"] != "透天厝"), "floor_sold"] = np.nan
floor_sold = df_test_2[df_test_2["build_type"] != "透天厝"]
floor_sold = floor_sold[floor_sold["floor_sold"].notna()]
floor_median = floor_sold.groupby("build_type")["floor_sold"].median()
for i, floor in enumerate(df_test_2["floor_sold"]):
    if math.isnan(floor) :
        df_test_2.loc[i, "floor_sold"] = floor_median[df_test_2.loc[i, "build_type"]]
# check no NA
df_test_2["floor_sold"].isna().sum()

# story
df_test_2["story"].isna().sum() # 6
story_median = df_test_2.dropna().groupby("build_type")["story"].median()
for i, story in enumerate(df_test_2["story"]):
    if math.isnan(story) :
        df_test_2.loc[i, "story"] = story_median[df_test_2.loc[i, "build_type"]]
# check no NA
df_test_2["story"].isna().sum()

# lon, lat both be 0 in the row 
df_test_2[(df_test_2["lon"] == 0) | (df_test_2["lat"] == 0)] # index = 13402
lon_index = df_test_2[(df_test_2["lon"] == 0) | (df_test_2["lat"] == 0)].index
df_test_2.loc[lon_index, "lon"] = round(df_test_2[(df_test_2["road_name"] == "廣興巷") & (df_test_2["lon"] != 0)]["lon"].mean(), 4)
df_test_2.loc[lon_index, "lat"] = round(df_test_2[(df_test_2["road_name"] == "廣興巷") & (df_test_2["lat"] != 0)]["lat"].mean(), 4)

# convert deal_date to date type
# split and count frequencies
df_date_split = df_test_2["deal_date"].str.split("/", expand = True)
df_date_split.columns = ["year", "month", "day"]
df_date_split["year"].value_counts()
df_date_split["month"].value_counts() # 00 month, replace it with 10
df_date_split["day"].value_counts() 
# replace 00 month with the mode 10
df_test_2["deal_date"] = df_test_2["deal_date"].str.replace(r'(?<=\/)00(?=\/)', '10', regex=True)
# replace .5 with the mode 25
df_test_2["deal_date"] = df_test_2["deal_date"].str.replace(r'\.5$', "25", regex=True)
# transform date format and replace deal_date with it
year_month_day = []
for date in df_test_2["deal_date"]:
    year, month, day = date.split("/")
    new_year = int(year) + 1911
    year_month_day.append(str(new_year) + '-' + month + '-' + day)
df_test_2["deal_date"] = year_month_day
# extract "month" from "deal year" and create a new column
df_test_2["month"] = pd.to_datetime(df_test_2['deal_date']).dt.month


### merge with macro-ecomomic indicators
os.chdir('/Users/xi/Desktop/python/house_price_project/merge_economy_data')
m1 = pd.read_csv('M1b_Supply.csv')
mortgage = pd.read_csv('Avg_Mortgage_Rate.csv', encoding='utf-8')
gdp = pd.read_csv('Real_GDP_Growth.csv')
inflation = pd.read_csv('CPI_Growth.csv')


# m1: convert date column
df_date_split = m1["時間"].str.split("/", expand = True)
df_date_split.columns = ["year", "month"]
df_date_split["year"].value_counts()
df_date_split["month"].value_counts()
# transform date format and replace deal_date with it
year_month = []
for date in m1["時間"]:
    year, month = date.split("/")
    new_year = int(year) + 1911
    year_month.append(str(new_year) + '-' + month)
m1["時間"] = year_month
# extract "month" from "deal year" and create a new column
m1["year"] = pd.to_datetime(m1["時間"]).dt.year
m1["month"] = pd.to_datetime(m1["時間"]).dt.month
# drop column
m1 = m1.drop(["時間"], axis = 1)
# rename column
m1.rename(columns={'M1b貨幣供給額(億元)' : 'M1b'}, inplace=True)


# mortgage: convert date column
df_date_split = mortgage["時間"].str.split("/", expand = True)
df_date_split.columns = ["year", "month"]
df_date_split["year"].value_counts()
df_date_split["month"].value_counts()
# transform date format and replace deal_date with it
year_month = []
for date in mortgage["時間"]:
    year, month = date.split("/")
    new_year = int(year) + 1911
    year_month.append(str(new_year) + '-' + month)
mortgage["時間"] = year_month
# extract "month" from "deal year" and create a new column
mortgage["year"] = pd.to_datetime(mortgage["時間"]).dt.year
mortgage["month"] = pd.to_datetime(mortgage["時間"]).dt.month
# drop column
mortgage = mortgage.drop(["時間"], axis = 1)
# rename column
mortgage.rename(columns={'五大行庫平均房貸利率(%)' : 'mortgage_rate'}, inplace=True)


# inflation: convert date column
inflation = inflation[~inflation["總指數"].isna()]
inflation[['year', 'month']] = inflation['統計期'].str.split('年', expand=True)
inflation['year'] = inflation['year'].astype(int)
inflation['year'] = inflation['year'] + 1911
inflation = inflation[inflation["month"] != ""]
inflation['month'] = inflation['month'].str.replace('月', '').astype(int)
# drop column
inflation = inflation.drop(["統計期"], axis = 1)
# rename column
inflation.rename(columns={'總指數' : 'CPI%'}, inplace=True)


# gdp: convert date column
gdp[['year', 'quarter']] = gdp['統計期'].str.split('年', expand=True)
gdp = gdp[~gdp["經濟成長率(%)"].isna()]
gdp = gdp[gdp["quarter"] != ""]
gdp['year'] = gdp['year'].astype(int)
gdp['year'] = gdp['year'] + 1911
gdp['quarter'] = gdp['quarter'].apply(lambda x: int(re.findall(r'\d+', x)[0]))
d_map={1 : "Q1", 2 : "Q2", 3 : "Q3", 4 : "Q4"}
gdp['quarter'] = gdp['quarter'].map(d_map)
# quater month conversion
month_quarter = {"Q1": [1, 2, 3], "Q2": [4, 5, 6], "Q3": [7, 8, 9], "Q4": [10, 11, 12]}
months = [month for quarter in month_quarter.values() for month in quarter]
years = range(2012, 2023)
dates = pd.date_range(start=f"{years[0]}-{months[0]}", end=f"{years[-1]}-{months[-1]}", freq="MS")
gdp_month = pd.DataFrame({"year": dates.year, "month": dates.month})
gdp_month["quarter"] = ""
for q, months in month_quarter.items():
    gdp_month.loc[gdp_month["month"].isin(months), "quarter"] = q
gdp_month = gdp_month.drop(df.index[:7])
gdp_conv = gdp_month.merge(gdp, on=['year', 'quarter'], how='left')
gdp_conv = gdp_conv.drop(["quarter", "統計期"], axis = 1)
# rename column
gdp_conv.rename(columns={'經濟成長率(%)': 'GDP%'}, inplace=True)


# merge all economical data
add = gdp_conv.merge(inflation, on = ["year", "month"], how = "left")
add = add.merge(m1, on = ["year", "month"], how = "left")
add = add.merge(mortgage, on = ["year", "month"], how = "left")

# merge to house data
df_train_1 = df_train_1.merge(add, on = ["year", "month"], how = "left")
df_val_1 = df_val_1.merge(add, on = ["year", "month"], how = "left")
df_test_1 = df_test_1.merge(add, on = ["year", "month"], how = "left")
df_train_2 = df_train_2.merge(add, on = ["year", "month"], how = "left")
df_val_2 = df_val_2.merge(add, on = ["year", "month"], how = "left")
df_test_2 = df_test_2.merge(add, on = ["year", "month"], how = "left")

# export to csv
# df_train_1.to_csv('df_train_1.csv', columns = df_train_1.columns, index = False) 
# df_val_1.to_csv('df_val_1.csv', columns = df_val_1.columns, index = False) 
# df_test_1.to_csv('df_test_1.csv', columns = df_test_1.columns, index = False) 
# df_train_2.to_csv('df_train_2.csv', columns = df_train_2.columns, index = False) 
# df_val_2.to_csv('df_val_2.csv', columns = df_val_2.columns, index = False) 
# df_test_2.to_csv('df_test_2.csv', columns = df_test_2.columns, index = False) 

os.chdir('/Users/xi/Desktop/python/house_price_project')
df_train_1 = pd.read_csv('df_train_1.csv')
df_val_1 = pd.read_csv('df_val_1.csv')
df_test_1 = pd.read_csv('df_test_1.csv')
df_train_2 = pd.read_csv('df_train_2.csv')
df_val_2 = pd.read_csv('df_val_2.csv')
df_test_2 = pd.read_csv('df_test_2.csv')


### check correlation and skewness again
## correlation
# Model_1
corr_matrix = df_train_1.corr()
sorted_columns = corr_matrix["price"].sort_values(ascending=False).index
sns.heatmap(df_train_1[sorted_columns].corr(), annot=True, annot_kws={'size': 7})
# price vs. area; bathroom vs. bedroom; total_deal_floor vs. 透天厝; m1b vs. elevator; 
# build_share1 vs. 透天厝; year vs. m1b; year vs. mortgage_rate; mortgage_rate vs. m1b

# Model_2
corr_matrix = df_train_2.corr()
sorted_columns = corr_matrix["price"].sort_values(ascending=False).index
sns.heatmap(df_train_2[sorted_columns].corr(), annot=True, annot_kws={'size': 7})


## skewness check
from scipy.stats import skew
# Model_1: GDP%
plt.hist(df_train_1["GDP%"][df_train_1["GDP%"] > 0])
plt.xlabel("GDP%")
plt.ylabel("Frequency")
plt.title("Model_1 GDP%")
plt.xlim(df_train_1["GDP%"][df_train_1["GDP%"] > 0].min(), df_train_1["GDP%"].max()) 
plt.ticklabel_format(style='plain', axis='x') 
plt.show() 
# GDP% boxplot
sns.boxplot(x = "GDP%", data = df_train_1)
plt.ticklabel_format(style='plain', axis='x')
plt.title("Model_1 GDP%")
plt.show()
print('Original Skewness:', skew(df_train_1["GDP%"])) # 0.4854

# Model_2: GDP%
plt.hist(df_train_2["GDP%"][df_train_2["GDP%"] > 0])
plt.xlabel("GDP%")
plt.ylabel("Frequency")
plt.title("Model_2 GDP%")
plt.xlim(df_train_2["GDP%"][df_train_2["GDP%"] > 0].min(), df_train_2["GDP%"].max()) 
plt.ticklabel_format(style='plain', axis='x') 
plt.show() 
# GDP% boxplot
sns.boxplot(x = "GDP%", data = df_train_2)
plt.ticklabel_format(style='plain', axis='x')
plt.title("Model_2 GDP%")
plt.show()
print('Original Skewness:', skew(df_train_2["GDP%"])) # -0.6595

# Model_1: CPI%
plt.hist(df_train_1["CPI%"][df_train_1["CPI%"] > 0])
plt.xlabel("CPI%")
plt.ylabel("Frequency")
plt.title("Model_1 CPI%")
plt.xlim(df_train_1["CPI%"][df_train_1["CPI%"] > 0].min(), df_train_1["CPI%"].max()) 
plt.ticklabel_format(style='plain', axis='x') 
plt.show() 
# CPI% boxplot
sns.boxplot(x = "CPI%", data = df_train_1)
plt.ticklabel_format(style='plain', axis='x')
plt.title("Model_1 CPI%")
plt.show()
print('Original Skewness:', skew(df_train_1["CPI%"])) # 0.2467

# Model_2: CPI%
plt.hist(df_train_2["CPI%"][df_train_2["CPI%"] > 0])
plt.xlabel("CPI%")
plt.ylabel("Frequency")
plt.title("Model_2 CPI%")
plt.xlim(df_train_2["CPI%"][df_train_2["CPI%"] > 0].min(), df_train_2["CPI%"].max()) 
plt.ticklabel_format(style='plain', axis='x') 
plt.show() 
# CPI% boxplot
sns.boxplot(x = "CPI%", data = df_train_2)
plt.ticklabel_format(style='plain', axis='x')
plt.title("Model_2 CPI%")
plt.show()
print('Original Skewness:', skew(df_train_2["CPI%"])) # 0.2227

# Model_1: mortgage_rate
plt.hist(df_train_1["mortgage_rate"][df_train_1["mortgage_rate"] > 0])
plt.xlabel("mortgage_rate")
plt.ylabel("Frequency")
plt.title("Model_1 mortgage_rate")
plt.xlim(df_train_1["mortgage_rate"][df_train_1["mortgage_rate"] > 0].min(), df_train_1["mortgage_rate"].max()) 
plt.ticklabel_format(style='plain', axis='x') 
plt.show() # highly skewed
# mortgage_rate boxplot
sns.boxplot(x = "mortgage_rate", data = df_train_1)
plt.ticklabel_format(style='plain', axis='x')
plt.title("Model_1 mortgage_rate")
plt.show()
print('Original Skewness:', skew(df_train_1["mortgage_rate"])) # -0.3991

# Model_2: mortgage_rate
plt.hist(df_train_2["mortgage_rate"][df_train_2["mortgage_rate"] > 0])
plt.xlabel("mortgage_rate")
plt.ylabel("Frequency")
plt.title("Model_2 mortgage_rate")
plt.xlim(df_train_2["mortgage_rate"][df_train_2["mortgage_rate"] > 0].min(), df_train_2["mortgage_rate"].max()) 
plt.ticklabel_format(style='plain', axis='x') 
plt.show() # highly skewed
# mortgage_rate boxplot
sns.boxplot(x = "mortgage_rate", data = df_train_2)
plt.ticklabel_format(style='plain', axis='x')
plt.title("Model_2 mortgage_rate")
plt.show()
print('Original Skewness:', skew(df_train_2["mortgage_rate"])) # -0.1754

# Model_1: M1b
plt.hist(df_train_1["M1b"][df_train_1["M1b"] > 0])
plt.xlabel("M1b")
plt.ylabel("Frequency")
plt.title("Model_1 M1b")
plt.xlim(df_train_1["M1b"][df_train_1["M1b"] > 0].min(), df_train_1["M1b"].max()) 
plt.ticklabel_format(style='plain', axis='x') 
plt.show() # highly skewed
# M1b boxplot
sns.boxplot(x = "M1b", data = df_train_1)
plt.ticklabel_format(style='plain', axis='x')
plt.title("Model_1 M1b")
plt.show()
print('Original Skewness:', skew(df_train_1["M1b"])) # 0.9029

# Model_2: M1b
plt.hist(df_train_2["M1b"][df_train_2["M1b"] > 0])
plt.xlabel("M1b")
plt.ylabel("Frequency")
plt.title("Model_2 M1b")
plt.xlim(df_train_2["M1b"][df_train_2["M1b"] > 0].min(), df_train_2["M1b"].max()) 
plt.ticklabel_format(style='plain', axis='x') 
plt.show() # highly skewed
# M1b boxplot
sns.boxplot(x = "M1b", data = df_train_2)
plt.ticklabel_format(style='plain', axis='x')
plt.title("Model_2 M1b")
plt.show()
print('Original Skewness:', skew(df_train_2["M1b"])) # 0.2316


from scipy.stats import boxcox
# Model_1: total_price
plt.hist(df_train_1["price"][df_train_1["price"] > 0])
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.title("Model_1 Price")
plt.xlim(df_train_1["price"][df_train_1["price"] > 0].min(), df_train_1["price"].max()) 
plt.ticklabel_format(style='plain', axis='x') 
plt.show() # highly skewed
# price boxplot
sns.boxplot(x = "price", data = df_train_1)
plt.ticklabel_format(style='plain', axis='x')
plt.title("Model_1 Price")
plt.show()
# skewness
print('Original Skewness:', skew(df_train_1["price"])) # 1.4220 > 1
# Box-Cox Transformation(is not defined for zero or negative values)
df_train_1[df_train_1["price"] <= 0]  # 0
x_boxcox, lam = boxcox(df_train_1["price"])
print('Box-Cox Transformed Skewness:', skew(x_boxcox)) # -0.0099
plt.hist(x_boxcox[x_boxcox > 0])
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.title("Model_1 Price(Box-Cox Transformation)")
plt.xlim(x_boxcox[x_boxcox > 0].min(), x_boxcox.max()) 
plt.ticklabel_format(style='plain', axis='x') 
plt.show()


# Model_2: total_price
plt.hist(df_train_2["price"][df_train_2["price"] > 0])
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.title("Model_2 Price")
plt.xlim(df_train_2["price"][df_train_2["price"] > 0].min(), df_train_2["price"].max()) 
plt.ticklabel_format(style='plain', axis='x') 
plt.show() # highly skewed
# price boxplot
sns.boxplot(x = "price", data = df_train_2)
plt.ticklabel_format(style='plain', axis='x')
plt.title("Model_2 Price")
plt.show()
# skewness
print('Original Skewness:', skew(df_train_2["price"])) # 1.4221 > 1
# Box-Cox Transformation(is not defined for zero or negative values)
df_train_2[df_train_2["price"] <= 0]  # 0
x_boxcox, lam = boxcox(df_train_2["price"])
print('Box-Cox Transformed Skewness:', skew(x_boxcox)) # -0.0124
plt.hist(x_boxcox[x_boxcox > 0])
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.title("Model_2 Price(Box-Cox Transformation)")
plt.xlim(x_boxcox[x_boxcox > 0].min(), x_boxcox.max()) 
plt.ticklabel_format(style='plain', axis='x') 
plt.show()


# Model_1: unit_price
plt.hist(df_train_1["unit_price"][df_train_1["unit_price"] > 0])
plt.xlabel("Unit Price")
plt.ylabel("Frequency")
plt.title("Model_1 unit_price")
plt.xlim(df_train_1["unit_price"][df_train_1["unit_price"] > 0].min(), df_train_1["unit_price"].max()) 
plt.ticklabel_format(style='plain', axis='x') 
plt.show()
# unit_price boxplot
sns.boxplot(x = "unit_price", data = df_train_1)
plt.ticklabel_format(style='plain', axis='x')
plt.title("Model_1 Unit Price")
plt.show()
# skewness
print('Original Skewness:', skew(df_train_1["unit_price"])) # 0.0075


# Model_2: unit_price
plt.hist(df_train_2["unit_price"][df_train_2["unit_price"] > 0])
plt.xlabel("Unit Price")
plt.ylabel("Frequency")
plt.title("Model_2 unit_price")
plt.xlim(df_train_2["unit_price"][df_train_2["unit_price"] > 0].min(), df_train_2["unit_price"].max()) 
plt.ticklabel_format(style='plain', axis='x') 
plt.show()
# unit_price boxplot
sns.boxplot(x = "unit_price", data = df_train_2)
plt.ticklabel_format(style='plain', axis='x')
plt.title("Model_2 Unit Price")
plt.show()
# skewness
print('Original Skewness:', skew(df_train_2["unit_price"])) # 0.0008


# Model_1: age
plt.hist(df_train_1["age"])
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.title("Model_1 Age") 
plt.ticklabel_format(style='plain', axis='x') 
plt.show() 
# age boxplot
sns.boxplot(x = "age", data = df_train_1)
plt.ticklabel_format(style='plain', axis='x')
plt.title("Model_1 Age")
plt.show()
# skewness
print('Original Skewness:', skew(df_train_1["age"])) # 0.5529

# Model_2: age
plt.hist(df_train_2["age"])
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.title("Model_2 Age") 
plt.ticklabel_format(style='plain', axis='x') 
plt.show() 
# age boxplot
sns.boxplot(x = "age", data = df_train_2)
plt.ticklabel_format(style='plain', axis='x')
plt.title("Model_2 Age")
plt.show()
# skewness
print('Original Skewness:', skew(df_train_2["age"])) # 0.6402


# Model_1: area
plt.hist(df_train_1["area"])
plt.xlabel("area")
plt.ylabel("Frequency")
plt.title("Model_1 Area") 
plt.ticklabel_format(style='plain', axis='x') 
plt.show() 
# area boxplot
sns.boxplot(x = "area", data = df_train_1)
plt.ticklabel_format(style='plain', axis='x')
plt.title("Model_1 Area")
plt.show()
# skewness
print('Original Skewness:', skew(df_train_1["area"])) # 0.8837

# Model_2: area
plt.hist(df_train_2["area"])
plt.xlabel("area")
plt.ylabel("Frequency")
plt.title("Model_2 Area") 
plt.ticklabel_format(style='plain', axis='x') 
plt.show() 
# area boxplot
sns.boxplot(x = "area", data = df_train_2)
plt.ticklabel_format(style='plain', axis='x')
plt.title("Model_2 Area")
plt.show()
# skewness
print('Original Skewness:', skew(df_train_2["area"])) # 0.8629


# Model_1: parking_num
plt.hist(df_train_1["parking_num"])
plt.xlabel("parking_num")
plt.ylabel("Frequency")
plt.title("Model_1 parking_num") 
plt.ticklabel_format(style='plain', axis='x') 
plt.show() 
# parking_num boxplot
sns.boxplot(x = "parking_num", data = df_train_1)
plt.ticklabel_format(style='plain', axis='x')
plt.title("Model_1 parking_num")
plt.show()
# skewness
print('Original Skewness:', skew(df_train_1["parking_num"])) # 1.2050 > 1

# Model_2: parking_num
plt.hist(df_train_2["parking_num"])
plt.xlabel("parking_num")
plt.ylabel("Frequency")
plt.title("Model_2 parking_num") 
plt.ticklabel_format(style='plain', axis='x') 
plt.show() 
# parking_num boxplot
sns.boxplot(x = "parking_num", data = df_train_2)
plt.ticklabel_format(style='plain', axis='x')
plt.title("Model_2 parking_num")
plt.show()
# skewness
print('Original Skewness:', skew(df_train_2["parking_num"])) # 1.1326 > 1


# Model_1: build_share1
plt.hist(df_train_1["build_share1"])
plt.xlabel("build_share1")
plt.ylabel("Frequency")
plt.title("Model_1 build_share1") 
plt.ticklabel_format(style='plain', axis='x') 
plt.show() 
# build_share1 boxplot
sns.boxplot(x = "build_share1", data = df_train_1)
plt.ticklabel_format(style='plain', axis='x')
plt.title("Model_1 build_share1")
plt.show()
# skewness
print('Original Skewness:', skew(df_train_1["build_share1"])) # -0.7469

# Model_2: build_share1
plt.hist(df_train_2["build_share1"])
plt.xlabel("build_share1")
plt.ylabel("Frequency")
plt.title("Model_2 build_share1") 
plt.ticklabel_format(style='plain', axis='x') 
plt.show() 
# build_share1 boxplot
sns.boxplot(x = "build_share1", data = df_train_2)
plt.ticklabel_format(style='plain', axis='x')
plt.title("Model_2 build_share1")
plt.show()
# skewness
print('Original Skewness:', skew(df_train_2["build_share1"])) # -0.7846

# the skewness of total price and parking numbers should be corrected


### skewness correction

## Box-Cox transformation
# Model_1(train): total_price
df_train_1[df_train_1["price"] <= 0]  # 0
x_boxcox, lam = boxcox(df_train_1["price"])
df_train_1["price_norm"] = x_boxcox
# Model_1(val): total_price
df_val_1[df_val_1["price"] <= 0]  # 0
x_boxcox, lam = boxcox(df_val_1["price"])
df_val_1["price_norm"] = x_boxcox
# Model_1(test): total_price
df_test_1[df_test_1["price"] <= 0]  # 0
x_boxcox, lam = boxcox(df_test_1["price"])
df_test_1["price_norm"] = x_boxcox
# Model_2(train): total_price
df_train_2[df_train_2["price"] <= 0]  # 0
x_boxcox, lam = boxcox(df_train_2["price"])
df_train_2["price_norm"] = x_boxcox
# Model_2(val): total_price
df_val_2[df_val_2["price"] <= 0]  # 0
x_boxcox, lam = boxcox(df_val_2["price"])
df_val_2["price_norm"] = x_boxcox
# Model_2(test): total_price
df_test_2[df_test_2["price"] <= 0]  # 0
x_boxcox, lam = boxcox(df_test_2["price"])
df_test_2["price_norm"] = x_boxcox


## power transformation
from sklearn.preprocessing import PowerTransformer
# Model_1(train): parking_num
len(df_train_1[df_train_1["parking_num"] <= 0]) # 38718 (Box-cox is not usable for <= 0)
pt = PowerTransformer(method = 'yeo-johnson', standardize = False)
pt_trans = pt.fit_transform(df_train_1[["parking_num"]])
df_train_1["parking_num_norm"] = pt_trans
print(df_train_1["parking_num_norm"].skew())
# Model_1(val): parking_num
pt = PowerTransformer(method = 'yeo-johnson', standardize = False)
pt_trans = pt.fit_transform(df_val_1[["parking_num"]])
df_val_1["parking_num_norm"] = pt_trans
# Model_1(test): parking_num
pt = PowerTransformer(method = 'yeo-johnson', standardize = False)
pt_trans = pt.fit_transform(df_test_1[["parking_num"]])
df_test_1["parking_num_norm"] = pt_trans

# Model_2: parking_num
len(df_train_2[df_train_2["parking_num"] <= 0])  # 36940 
pt_trans = pt.fit_transform(df_train_2[["parking_num"]])
df_train_2["parking_num_norm"] = pt_trans
print(df_train_2["parking_num_norm"].skew())
# Model_2(val): parking_num
pt = PowerTransformer(method = 'yeo-johnson', standardize = False)
pt_trans = pt.fit_transform(df_val_2[["parking_num"]])
df_val_2["parking_num_norm"] = pt_trans
# Model_2(test): parking_num
pt = PowerTransformer(method = 'yeo-johnson', standardize = False)
pt_trans = pt.fit_transform(df_test_2[["parking_num"]])
df_test_2["parking_num_norm"] = pt_trans


### plot categorical data to check if feature need pairwise t-test to reduce the levels
# Model_1: district vs. price(t-test)
sns.boxplot(x = 'district', y = 'price', data = df_train_1)
plt.title("Mode_1 District vs. Price")
plt.show()

# Model_1: district vs. unit_price(t-test)
sns.boxplot(x = 'district', y = 'unit_price', data = df_train_1)
plt.title("Mode_1 District vs. Unit Price")
plt.show()

# Model_1: build_type vs. price
sns.boxplot(x = 'build_type', y = 'price', data = df_train_1)
plt.title("Mode_1 Build Type vs. Price")
plt.show()

# Model_1: build_type vs. unit_price (t-test)
sns.boxplot(x = 'build_type', y = 'unit_price', data = df_train_1)
plt.title("Mode_1 Build Type vs. Unit Price")
plt.show()

# Model_1: elevator vs. price (t-test)
sns.boxplot(x = 'elevator', y = 'price', data = df_train_1)
plt.title("Mode_1 Elevator vs. Price")
plt.show()

# Model_1: elevator vs. unit_price
sns.boxplot(x = 'elevator', y = 'unit_price', data = df_train_1)
plt.title("Mode_1 Elevator vs. Unit Price")
plt.show()

# Model_1: manager vs. price (t-test)
sns.boxplot(x = 'manager', y = 'price', data = df_train_1)
plt.title("Mode_1 Manager vs. Price")
plt.show()

# Model_1: manager vs. price
sns.boxplot(x = 'manager', y = 'unit_price', data = df_train_1)
plt.title("Mode_1 Manager vs. Unit Price")
plt.show()


# Model_2: district vs. price(t-test)
sns.boxplot(x = 'district', y = 'price', data = df_train_2)
plt.title("Mode_2 District vs. Price")
plt.show()

# Model_2: district vs. unit_price(t-test)
sns.boxplot(x = 'district', y = 'unit_price', data = df_train_2)
plt.title("Mode_2 District vs. Unit Price")
plt.show()

# Model_2: build_type vs. price
sns.boxplot(x = 'build_type', y = 'price', data = df_train_2)
plt.title("Mode_2 Build Type vs. Price")
plt.show()

# Model_2: build_type vs. unit_price (t-test)
sns.boxplot(x = 'build_type', y = 'unit_price', data = df_train_2)
plt.title("Mode_2 Build Type vs. Unit Price")
plt.show()

# Model_2: elevator vs. price 
sns.boxplot(x = 'elevator', y = 'price', data = df_train_2)
plt.title("Mode_2 Elevator vs. Price")
plt.show()

# Model_2: elevator vs. unit_price
sns.boxplot(x = 'elevator', y = 'unit_price', data = df_train_2)
plt.title("Mode_2 Elevator vs. Unit Price")
plt.show()

# Model_2: manager vs. price (t-test)
sns.boxplot(x = 'manager', y = 'price', data = df_train_2)
plt.title("Mode_2 Manager vs. Price")
plt.show()

# Model_2: manager vs. price
sns.boxplot(x = 'manager', y = 'unit_price', data = df_train_2)
plt.title("Mode_2 Manager vs. Unit Price")
plt.show()


## scaling
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
non_scaled_cols = ["district", "road_name", "build_type", "elevator", "manager", "deal_date", "year", "month"]
# df_train_1
scaled_cols = df_train_1.columns.difference(non_scaled_cols)
scaler.fit(df_train_1[scaled_cols])
df_train_1_scale = scaler.transform(df_train_1[scaled_cols])
df_train_1_scale = pd.DataFrame(df_train_1_scale, columns = scaled_cols)
df_train_1_scale = pd.concat([df_train_1_scale, df_train_1[non_scaled_cols]], axis=1)
# df_val_1
scaled_cols = df_val_1.columns.difference(non_scaled_cols)
scaler.fit(df_val_1[scaled_cols])
df_val_1_scale = scaler.transform(df_val_1[scaled_cols])
df_val_1_scale = pd.DataFrame(df_val_1_scale, columns = scaled_cols)
df_val_1_scale = pd.concat([df_val_1_scale, df_val_1[non_scaled_cols]], axis=1)
# df_test_1
sscaled_cols = df_test_1.columns.difference(non_scaled_cols)
scaler.fit(df_test_1[scaled_cols])
df_test_1_scale = scaler.transform(df_test_1[scaled_cols])
df_test_1_scale = pd.DataFrame(df_test_1_scale, columns = scaled_cols)
df_test_1_scale = pd.concat([df_test_1_scale, df_test_1[non_scaled_cols]], axis=1)
# df_train_2
scaled_cols = df_train_2.columns.difference(non_scaled_cols)
scaler.fit(df_train_2[scaled_cols])
df_train_2_scale = scaler.transform(df_train_2[scaled_cols])
df_train_2_scale = pd.DataFrame(df_train_2_scale, columns = scaled_cols)
df_train_2_scale = pd.concat([df_train_2_scale, df_train_2[non_scaled_cols]], axis=1)
# df_val_2
scaled_cols = df_val_2.columns.difference(non_scaled_cols)
scaler.fit(df_val_2[scaled_cols])
df_val_2_scale = scaler.transform(df_val_2[scaled_cols])
df_val_2_scale = pd.DataFrame(df_val_2_scale, columns = scaled_cols)
df_val_2_scale = pd.concat([df_val_2_scale, df_val_2[non_scaled_cols]], axis=1)
# df_test_2
sscaled_cols = df_test_2.columns.difference(non_scaled_cols)
scaler.fit(df_test_2[scaled_cols])
df_test_2_scale = scaler.transform(df_test_2[scaled_cols])
df_test_2_scale = pd.DataFrame(df_test_2_scale, columns = scaled_cols)
df_test_2_scale = pd.concat([df_test_2_scale, df_test_2[non_scaled_cols]], axis=1)


## combine levels based on t-test result
from scipy import stats
import statsmodels.stats.multicomp as mc
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# Model_1: district vs. price(t-test) 北屯區&西屯區, 南區&西區, 東區&西區
comp1 = mc.MultiComparison(df_train_1_scale["price_norm"], df_train_1_scale["district"])
comp1.allpairtest(stats.ttest_ind, method= "bonf")
# Model_1: district vs. unit_price(t-test) 南屯&西屯, 北屯&南區
comp1 = mc.MultiComparison(df_train_1_scale["unit_price"], df_train_1_scale["district"])
comp1.allpairtest(stats.ttest_ind, method= "bonf")
# Model_1: build_type vs. unit_price (t-test) 公寓&套房
comp1 = mc.MultiComparison(df_train_1_scale["unit_price"], df_train_1_scale["build_type"])
comp1.allpairtest(stats.ttest_ind, method= "bonf")
# Model_1: elevator vs. price (t-test)
comp1 = mc.MultiComparison(df_train_1_scale["price_norm"], df_train_1_scale["elevator"])
comp1.allpairtest(stats.ttest_ind, method= "bonf")
# Model_1: manager vs. price (t-test)
comp1 = mc.MultiComparison(df_train_1_scale["price_norm"], df_train_1_scale["manager"])
comp1.allpairtest(stats.ttest_ind, method= "bonf")
# Model_2: district vs. price(t-test) 北屯區&西屯區, 南區&西區, 東區&西區
comp1 = mc.MultiComparison(df_train_2_scale["price_norm"], df_train_2_scale["district"])
comp1.allpairtest(stats.ttest_ind, method= "bonf")
# Model_2: district vs. unit_price(t-test) 北區&北屯, 北區&南區, 北屯&南區, 南屯&西屯
comp1 = mc.MultiComparison(df_train_2_scale["unit_price"], df_train_2_scale["district"])
comp1.allpairtest(stats.ttest_ind, method= "bonf")
# Model_2: build_type vs. unit_price (t-test)
comp1 = mc.MultiComparison(df_train_2_scale["unit_price"], df_train_2_scale["build_type"])
comp1.allpairtest(stats.ttest_ind, method= "bonf")
# Model_2: manager vs. price (t-test)
comp1 = mc.MultiComparison(df_train_2_scale["price_norm"], df_train_2_scale["manager"])
comp1.allpairtest(stats.ttest_ind, method= "bonf")


## combine categories based on t-test result for feature reduction purpose

# Model_1: train
df_train_1_scale["district_price_norm"] = df_train_1_scale["district"]
df_train_1_scale.district_price_norm[df_train_1_scale.district_price_norm == "西屯區"] = "北屯區"
df_train_1_scale.district_price_norm[df_train_1_scale.district_price_norm == "北屯區"] = "西屯北屯區"
df_train_1_scale.district_price_norm[df_train_1_scale.district_price_norm == "東區"] = "西區"
df_train_1_scale.district_price_norm[df_train_1_scale.district_price_norm == "南區"] = "西區"
df_train_1_scale.district_price_norm[df_train_1_scale.district_price_norm == "西區"] = "東西南區"
df_train_1_scale["district_unitprice"] = df_train_1_scale["district"]
df_train_1_scale.district_unitprice[df_train_1_scale.district_unitprice == "西屯區"] = "南屯區"
df_train_1_scale.district_unitprice[df_train_1_scale.district_unitprice == "南屯區"] = "西屯南屯區"
df_train_1_scale.district_unitprice[df_train_1_scale.district_unitprice == "北屯區"] = "南區"
df_train_1_scale.district_unitprice[df_train_1_scale.district_unitprice == "南區"] = "北屯南區"
df_train_1_scale["build_type_unitprice"] = df_train_1_scale["build_type"]
df_train_1_scale.build_type_unitprice[df_train_1_scale.build_type_unitprice == "公寓"] = "套房"
df_train_1_scale.build_type_unitprice[df_train_1_scale.build_type_unitprice == "套房"] = "公寓套房"

# Model_1: val
df_val_1_scale["district_price_norm"] = df_val_1_scale["district"]
df_val_1_scale.district_price_norm[df_val_1_scale.district_price_norm == "西屯區"] = "北屯區"
df_val_1_scale.district_price_norm[df_val_1_scale.district_price_norm == "北屯區"] = "西屯北屯區"
df_val_1_scale.district_price_norm[df_val_1_scale.district_price_norm == "東區"] = "西區"
df_val_1_scale.district_price_norm[df_val_1_scale.district_price_norm == "南區"] = "西區"
df_val_1_scale.district_price_norm[df_val_1_scale.district_price_norm == "西區"] = "東西南區"
df_val_1_scale["district_unitprice"] = df_val_1_scale["district"]
df_val_1_scale.district_unitprice[df_val_1_scale.district_unitprice == "西屯區"] = "南屯區"
df_val_1_scale.district_unitprice[df_val_1_scale.district_unitprice == "南屯區"] = "西屯南屯區"
df_val_1_scale.district_unitprice[df_val_1_scale.district_unitprice == "北屯區"] = "南區"
df_val_1_scale.district_unitprice[df_val_1_scale.district_unitprice == "南區"] = "北屯南區"
df_val_1_scale["build_type_unitprice"] = df_val_1_scale["build_type"]
df_val_1_scale.build_type_unitprice[df_val_1_scale.build_type_unitprice == "公寓"] = "套房"
df_val_1_scale.build_type_unitprice[df_val_1_scale.build_type_unitprice == "套房"] = "公寓套房"

# Model_1: test
df_test_1_scale["district_price_norm"] = df_test_1_scale["district"]
df_test_1_scale.district_price_norm[df_test_1_scale.district_price_norm == "西屯區"] = "北屯區"
df_test_1_scale.district_price_norm[df_test_1_scale.district_price_norm == "北屯區"] = "西屯北屯區"
df_test_1_scale.district_price_norm[df_test_1_scale.district_price_norm == "東區"] = "西區"
df_test_1_scale.district_price_norm[df_test_1_scale.district_price_norm == "南區"] = "西區"
df_test_1_scale.district_price_norm[df_test_1_scale.district_price_norm == "西區"] = "東西南區"
df_test_1_scale["district_unitprice"] = df_test_1_scale["district"]
df_test_1_scale.district_unitprice[df_test_1_scale.district_unitprice == "西屯區"] = "南屯區"
df_test_1_scale.district_unitprice[df_test_1_scale.district_unitprice == "南屯區"] = "西屯南屯區"
df_test_1_scale.district_unitprice[df_test_1_scale.district_unitprice == "北屯區"] = "南區"
df_test_1_scale.district_unitprice[df_test_1_scale.district_unitprice == "南區"] = "北屯南區"
df_test_1_scale["build_type_unitprice"] = df_test_1_scale["build_type"]
df_test_1_scale.build_type_unitprice[df_test_1_scale.build_type_unitprice == "公寓"] = "套房"
df_test_1_scale.build_type_unitprice[df_test_1_scale.build_type_unitprice == "套房"] = "公寓套房"

# Model_2: train
df_train_2_scale["district_price_norm"] = df_train_2_scale["district"]
df_train_2_scale.district_price_norm[df_train_2_scale.district_price_norm == "西屯區"] = "北屯區"
df_train_2_scale.district_price_norm[df_train_2_scale.district_price_norm == "北屯區"] = "西屯北屯區"
df_train_2_scale.district_price_norm[df_train_2_scale.district_price_norm == "東區"] = "西區"
df_train_2_scale.district_price_norm[df_train_2_scale.district_price_norm == "南區"] = "西區"
df_train_2_scale.district_price_norm[df_train_2_scale.district_price_norm == "西區"] = "東西南區"
df_train_2_scale["district_unitprice"] = df_train_2_scale["district"]
df_train_2_scale.district_unitprice[df_train_2_scale.district_unitprice == "北區"] = "北屯區"
df_train_2_scale.district_unitprice[df_train_2_scale.district_unitprice == "南區"] = "北屯區"
df_train_2_scale.district_unitprice[df_train_2_scale.district_unitprice == "北屯區"] = "北屯北南區"
df_train_2_scale.district_unitprice[df_train_2_scale.district_unitprice == "南屯區"] = "西屯區"
df_train_2_scale.district_unitprice[df_train_2_scale.district_unitprice == "西屯區"] = "西屯南屯區"

# Model_2: val
df_val_2_scale["district_price_norm"] = df_val_2_scale["district"]
df_val_2_scale.district_price_norm[df_val_2_scale.district_price_norm == "西屯區"] = "北屯區"
df_val_2_scale.district_price_norm[df_val_2_scale.district_price_norm == "北屯區"] = "西屯北屯區"
df_val_2_scale.district_price_norm[df_val_2_scale.district_price_norm == "東區"] = "西區"
df_val_2_scale.district_price_norm[df_val_2_scale.district_price_norm == "南區"] = "西區"
df_val_2_scale.district_price_norm[df_val_2_scale.district_price_norm == "西區"] = "東西南區"
df_val_2_scale["district_unitprice"] = df_val_2_scale["district"]
df_val_2_scale.district_unitprice[df_val_2_scale.district_unitprice == "北區"] = "北屯區"
df_val_2_scale.district_unitprice[df_val_2_scale.district_unitprice == "南區"] = "北屯區"
df_val_2_scale.district_unitprice[df_val_2_scale.district_unitprice == "北屯區"] = "北屯北南區"
df_val_2_scale.district_unitprice[df_val_2_scale.district_unitprice == "南屯區"] = "西屯區"
df_val_2_scale.district_unitprice[df_val_2_scale.district_unitprice == "西屯區"] = "西屯南屯區"

# Model_2: test
df_test_2_scale["district_price_norm"] = df_test_2_scale["district"]
df_test_2_scale.district_price_norm[df_test_2_scale.district_price_norm == "西屯區"] = "北屯區"
df_test_2_scale.district_price_norm[df_test_2_scale.district_price_norm == "北屯區"] = "西屯北屯區"
df_test_2_scale.district_price_norm[df_test_2_scale.district_price_norm == "東區"] = "西區"
df_test_2_scale.district_price_norm[df_test_2_scale.district_price_norm == "南區"] = "西區"
df_test_2_scale.district_price_norm[df_test_2_scale.district_price_norm == "西區"] = "東西南區"
df_test_2_scale["district_unitprice"] = df_test_2_scale["district"]
df_test_2_scale.district_unitprice[df_test_2_scale.district_unitprice == "北區"] = "北屯區"
df_test_2_scale.district_unitprice[df_test_2_scale.district_unitprice == "南區"] = "北屯區"
df_test_2_scale.district_unitprice[df_test_2_scale.district_unitprice == "北屯區"] = "北屯北南區"
df_test_2_scale.district_unitprice[df_test_2_scale.district_unitprice == "南屯區"] = "西屯區"
df_test_2_scale.district_unitprice[df_test_2_scale.district_unitprice == "西屯區"] = "西屯南屯區"


## encoding categorical data
# Model_1: train
d_map={"無" : 0, "有" : 1}
df_train_1_scale["elevator"] = df_train_1_scale["elevator"].map(d_map)
df_train_1_scale["manager"] = df_train_1_scale["manager"].map(d_map)
# one-hot encoding: district_price_norm(dummy base: 中區_price_norm)
dummy = pd.get_dummies(df_train_1_scale["district_price_norm"])
df_train_1_scale = pd.concat((df_train_1_scale, dummy), axis=1)
df_train_1_scale.isna().sum()
df_train_1_scale = df_train_1_scale.drop(["中區"], axis=1)
# one-hot encoding: district_unitprice (dummy base: 中區_unitprice)
dummy = pd.get_dummies(df_train_1_scale["district_unitprice"])
df_train_1_scale = pd.concat((df_train_1_scale, dummy), axis=1)
df_train_1_scale.isna().sum()
df_train_1_scale = df_train_1_scale.drop(["中區"], axis=1)
# one-hot encoding: build_type (dummy base: 透天厝_price_norm)
dummy = pd.get_dummies(df_train_1_scale["build_type"])
df_train_1_scale = pd.concat((df_train_1_scale, dummy), axis=1)
df_train_1_scale.isna().sum()
df_train_1_scale = df_train_1_scale.drop(["透天厝"], axis=1)
# one-hot encoding: build_type_unitprice(dummy base: 透天厝_unitprice)
dummy = pd.get_dummies(df_train_1_scale["build_type_unitprice"])
df_train_1_scale = pd.concat((df_train_1_scale, dummy), axis=1)
df_train_1_scale.isna().sum()
df_train_1_scale = df_train_1_scale.drop(["透天厝"], axis=1)
df_train_1_scale.columns = ['CPI%', 'GDP%', 'M1b', 'age', 'area', 'bathroom_num', 'bedroom_num',
       'build_share1', 'floor_sold', 'hall_num', 'lat', 'lon',
       'mortgage_rate', 'parking_num', 'parking_num_norm', 'price',
       'price_norm', 'story', 'total_deal_floor', 'unit_price', 'district',
       'road_name', 'build_type', 'elevator', 'manager',
       'deal_date', 'year', 'month', 'district_price_norm', 'district_unitprice',
       'build_type_unitprice', '北區_price_norm', '南屯區_price_norm',
       '東西南區_price_norm', '西屯北屯區_price_norm', '北區_unitprice', '北屯南區_unitprice',
       '東區_unitprice', '西區_unitprice', '西屯南屯區_unitprice', '住宅大樓_price_norm',
       '公寓_price_norm', '套房_price_norm', '華廈_price_norm', '住宅大樓_unitprice',
       '公寓套房_unitprice', '華廈_unitprice']
df_train_1_scale.drop(["district", "road_name", "build_type", "district_price_norm", 
                       "district_unitprice", "build_type_unitprice"], axis=1, inplace = True)

# Model_1: val
d_map={"無" : 0, "有" : 1}
df_val_1_scale["elevator"] = df_val_1_scale["elevator"].map(d_map)
df_val_1_scale["manager"] = df_val_1_scale["manager"].map(d_map)
# one-hot encoding: district_price_norm(dummy base: 中區_price_norm)
dummy = pd.get_dummies(df_val_1_scale["district_price_norm"])
df_val_1_scale = pd.concat((df_val_1_scale, dummy), axis=1)
df_val_1_scale.isna().sum()
df_val_1_scale = df_val_1_scale.drop(["中區"], axis=1)
# one-hot encoding: district_unitprice(dummy base: 中區_unitprice)
dummy = pd.get_dummies(df_val_1_scale["district_unitprice"])
df_val_1_scale = pd.concat((df_val_1_scale, dummy), axis=1)
df_val_1_scale.isna().sum()
df_val_1_scale = df_val_1_scale.drop(["中區"], axis=1)
# one-hot encoding: build_type(dummy base: 透天厝_price_norm)
dummy = pd.get_dummies(df_val_1_scale["build_type"])
df_val_1_scale = pd.concat((df_val_1_scale, dummy), axis=1)
df_val_1_scale.isna().sum()
df_val_1_scale = df_val_1_scale.drop(["透天厝"], axis=1)
# one-hot encoding: build_type_unitprice(dummy base: 透天厝_unitprice)
dummy = pd.get_dummies(df_val_1_scale["build_type_unitprice"])
df_val_1_scale = pd.concat((df_val_1_scale, dummy), axis=1)
df_val_1_scale.isna().sum()
df_val_1_scale = df_val_1_scale.drop(["透天厝"], axis=1)
df_val_1_scale.columns = ['CPI%', 'GDP%', 'M1b', 'age', 'area', 'bathroom_num', 'bedroom_num',
       'build_share1', 'floor_sold', 'hall_num', 'lat', 'lon',
       'mortgage_rate', 'parking_num', 'parking_num_norm', 'price',
       'price_norm', 'story', 'total_deal_floor', 'unit_price', 'district',
       'road_name', 'build_type', 'elevator', 'manager',
       'deal_date', 'year', 'month', 'district_price_norm', 'district_unitprice',
       'build_type_unitprice', '北區_price_norm', '南屯區_price_norm',
       '東西南區_price_norm', '西屯北屯區_price_norm', '北區_unitprice', '北屯南區_unitprice',
       '東區_unitprice', '西區_unitprice', '西屯南屯區_unitprice', '住宅大樓_price_norm',
       '公寓_price_norm', '套房_price_norm', '華廈_price_norm', '住宅大樓_unitprice',
       '公寓套房_unitprice', '華廈_unitprice']
df_val_1_scale.drop(["district", "road_name", "build_type", "district_price_norm", 
                       "district_unitprice", "build_type_unitprice"], axis=1, inplace = True)

# Model_1: test
d_map={"無" : 0, "有" : 1}
df_test_1_scale["elevator"] = df_test_1_scale["elevator"].map(d_map)
df_test_1_scale["manager"] = df_test_1_scale["manager"].map(d_map)
# one-hot encoding: district_price_norm(dummy base: 中區_price_norm)
dummy = pd.get_dummies(df_test_1_scale["district_price_norm"])
df_test_1_scale = pd.concat((df_test_1_scale, dummy), axis=1)
df_test_1_scale.isna().sum()
df_test_1_scale = df_test_1_scale.drop(["中區"], axis=1)
# one-hot encoding: district_unitprice(dummy base: 中區_unitprice)
dummy = pd.get_dummies(df_test_1_scale["district_unitprice"])
df_test_1_scale = pd.concat((df_test_1_scale, dummy), axis=1)
df_test_1_scale.isna().sum()
df_test_1_scale = df_test_1_scale.drop(["中區"], axis=1)
# one-hot encoding: build_type(dummy base: 透天厝_price_norm)
dummy = pd.get_dummies(df_test_1_scale["build_type"])
df_test_1_scale = pd.concat((df_test_1_scale, dummy), axis=1)
df_test_1_scale.isna().sum()
df_test_1_scale = df_test_1_scale.drop(["透天厝"], axis=1)
# one-hot encoding: build_type_unitprice(dummy base: 透天厝_unitprice)
dummy = pd.get_dummies(df_test_1_scale["build_type_unitprice"])
df_test_1_scale = pd.concat((df_test_1_scale, dummy), axis=1)
df_test_1_scale.isna().sum()
df_test_1_scale = df_test_1_scale.drop(["透天厝"], axis=1)
df_test_1_scale.columns = ['CPI%', 'GDP%', 'M1b', 'age', 'area', 'bathroom_num', 'bedroom_num',
       'build_share1', 'floor_sold', 'hall_num', 'lat', 'lon',
       'mortgage_rate', 'parking_num', 'parking_num_norm', 'price',
       'price_norm', 'story', 'total_deal_floor', 'unit_price', 'district',
       'road_name', 'build_type', 'elevator', 'manager',
       'deal_date', 'year', 'month', 'district_price_norm', 'district_unitprice',
       'build_type_unitprice', '北區_price_norm', '南屯區_price_norm',
       '東西南區_price_norm', '西屯北屯區_price_norm', '北區_unitprice', '北屯南區_unitprice',
       '東區_unitprice', '西區_unitprice', '西屯南屯區_unitprice', '住宅大樓_price_norm',
       '公寓_price_norm', '套房_price_norm', '華廈_price_norm', '住宅大樓_unitprice',
       '公寓套房_unitprice', '華廈_unitprice']
df_test_1_scale.drop(["district", "road_name", "build_type", "district_price_norm", 
                       "district_unitprice", "build_type_unitprice"], axis=1, inplace = True)

# Model_2: train
d_map={"無" : 0, "有" : 1}
df_train_2_scale["elevator"] = df_train_2_scale["elevator"].map(d_map)
df_train_2_scale["manager"] = df_train_2_scale["manager"].map(d_map)
# one-hot encoding: district_price_norm(dummy base: 中區_price_norm)
dummy = pd.get_dummies(df_train_2_scale["district_price_norm"])
df_train_2_scale = pd.concat((df_train_2_scale, dummy), axis=1)
df_train_2_scale.isna().sum()
df_train_2_scale = df_train_2_scale.drop(["中區"], axis=1)
# one-hot encoding: district_unitprice(dummy base: 中區_unitprice)
dummy = pd.get_dummies(df_train_2_scale["district_unitprice"])
df_train_2_scale = pd.concat((df_train_2_scale, dummy), axis=1)
df_train_2_scale.isna().sum()
df_train_2_scale = df_train_2_scale.drop(["中區"], axis=1)
# one-hot encoding: build_type(dummy base: 透天厝)
dummy = pd.get_dummies(df_train_2_scale["build_type"])
df_train_2_scale = pd.concat((df_train_2_scale, dummy), axis=1)
df_train_2_scale.isna().sum()
df_train_2_scale = df_train_2_scale.drop(["透天厝"], axis=1)
df_train_2_scale.columns = ['CPI%', 'GDP%', 'M1b', 'age', 'area', 'bathroom_num', 'bedroom_num',
       'build_share1', 'floor_sold', 'hall_num', 'lat', 'lon', 'mortgage_rate',
       'parking_num', 'parking_num_norm', 'price', 'price_norm', 'story',
       'total_deal_floor', 'unit_price', 'district', 'road_name', 'build_type',
       'elevator', 'manager', 'deal_date', 'year', 'month',
       'district_price_norm', 'district_unitprice', '北區_price_norm', '南屯區_price_norm',
       '東西南區_price_norm', '西屯北屯區_price_norm', '北屯北南區_unitprice', '東區_unitprice',
       '西區_unitprice', '西屯南屯區_unitprice', '住宅大樓', '公寓', '套房', '華廈']
df_train_2_scale.drop(["district", "road_name", "build_type", "district_price_norm", 
                       "district_unitprice"], axis=1, inplace = True)

# Model_2: val
d_map={"無" : 0, "有" : 1}
df_val_2_scale["elevator"] = df_val_2_scale["elevator"].map(d_map)
df_val_2_scale["manager"] = df_val_2_scale["manager"].map(d_map)
# one-hot encoding: district_price_norm(dummy base: 中區_price_norm)
dummy = pd.get_dummies(df_val_2_scale["district_price_norm"])
df_val_2_scale = pd.concat((df_val_2_scale, dummy), axis=1)
df_val_2_scale.isna().sum()
df_val_2_scale = df_val_2_scale.drop(["中區"], axis=1)
# one-hot encoding: district_unitprice(dummy base: 中區_unitprice)
dummy = pd.get_dummies(df_val_2_scale["district_unitprice"])
df_val_2_scale = pd.concat((df_val_2_scale, dummy), axis=1)
df_val_2_scale.isna().sum()
df_val_2_scale = df_val_2_scale.drop(["中區"], axis=1)
# one-hot encoding: build_type(dummy base: 透天厝)
dummy = pd.get_dummies(df_val_2_scale["build_type"])
df_val_2_scale = pd.concat((df_val_2_scale, dummy), axis=1)
df_val_2_scale.isna().sum()
df_val_2_scale = df_val_2_scale.drop(["透天厝"], axis=1)
df_val_2_scale.columns = ['CPI%', 'GDP%', 'M1b', 'age', 'area', 'bathroom_num', 'bedroom_num',
       'build_share1', 'floor_sold', 'hall_num', 'lat', 'lon', 'mortgage_rate',
       'parking_num', 'parking_num_norm', 'price', 'price_norm', 'story',
       'total_deal_floor', 'unit_price', 'district', 'road_name', 'build_type',
       'elevator', 'manager', 'deal_date', 'year', 'month',
       'district_price_norm', 'district_unitprice', '北區_price_norm', '南屯區_price_norm',
       '東西南區_price_norm', '西屯北屯區_price_norm', '北屯北南區_unitprice', '東區_unitprice',
       '西區_unitprice', '西屯南屯區_unitprice', '住宅大樓', '公寓', '套房', '華廈']
df_val_2_scale.drop(["district", "road_name", "build_type", "district_price_norm", 
                       "district_unitprice"], axis=1, inplace = True)

# Model_2: test
d_map={"無" : 0, "有" : 1}
df_test_2_scale["elevator"] = df_test_2_scale["elevator"].map(d_map)
df_test_2_scale["manager"] = df_test_2_scale["manager"].map(d_map)
# one-hot encoding: district_price_norm(dummy base: 中區_price_norm)
dummy = pd.get_dummies(df_test_2_scale["district_price_norm"])
df_test_2_scale = pd.concat((df_test_2_scale, dummy), axis=1)
df_test_2_scale.isna().sum()
df_test_2_scale = df_test_2_scale.drop(["中區"], axis=1)
# one-hot encoding: district_unitprice(dummy base: 中區_unitprice)
dummy = pd.get_dummies(df_test_2_scale["district_unitprice"])
df_test_2_scale = pd.concat((df_test_2_scale, dummy), axis=1)
df_test_2_scale.isna().sum()
df_test_2_scale = df_test_2_scale.drop(["中區"], axis=1)
# one-hot encoding: build_type(dummy base: 透天厝)
dummy = pd.get_dummies(df_test_2_scale["build_type"])
df_test_2_scale = pd.concat((df_test_2_scale, dummy), axis=1)
df_test_2_scale.isna().sum()
df_test_2_scale = df_test_2_scale.drop(["透天厝"], axis=1)
df_test_2_scale.columns = ['CPI%', 'GDP%', 'M1b', 'age', 'area', 'bathroom_num', 'bedroom_num',
       'build_share1', 'floor_sold', 'hall_num', 'lat', 'lon', 'mortgage_rate',
       'parking_num', 'parking_num_norm', 'price', 'price_norm', 'story',
       'total_deal_floor', 'unit_price', 'district', 'road_name', 'build_type',
       'elevator', 'manager', 'deal_date', 'year', 'month',
       'district_price_norm', 'district_unitprice', '北區_price_norm', '南屯區_price_norm',
       '東西南區_price_norm', '西屯北屯區_price_norm', '北屯北南區_unitprice', '東區_unitprice',
       '西區_unitprice', '西屯南屯區_unitprice', '住宅大樓', '公寓', '套房', '華廈']
df_test_2_scale.drop(["district", "road_name", "build_type", "district_price_norm", 
                       "district_unitprice"], axis=1, inplace = True)


df_train_1_scale['deal_date'] = pd.to_datetime(df_train_1_scale['deal_date']).dt.date
df_val_1_scale['deal_date'] = pd.to_datetime(df_val_1_scale['deal_date']).dt.date
df_test_1_scale['deal_date'] = pd.to_datetime(df_test_1_scale['deal_date']).dt.date
df_train_2_scale['deal_date'] = pd.to_datetime(df_train_2_scale['deal_date']).dt.date
df_val_2_scale['deal_date'] = pd.to_datetime(df_val_2_scale['deal_date']).dt.date
df_test_2_scale['deal_date'] = pd.to_datetime(df_test_2_scale['deal_date']).dt.date

# export to csv
# df_train_1_scale.to_csv('df_train_1_scale.csv', columns = df_train_1_scale.columns, index = False) 
# df_val_1_scale.to_csv('df_val_1_scale.csv', columns = df_val_1_scale.columns, index = False) 
# df_test_1_scale.to_csv('df_test_1_scale.csv', columns = df_test_1_scale.columns, index = False) 
# df_train_2_scale.to_csv('df_train_2_scale.csv', columns = df_train_2_scale.columns, index = False) 
# df_val_2_scale.to_csv('df_val_2_scale.csv', columns = df_val_2_scale.columns, index = False) 
# df_test_2_scale.to_csv('df_test_2_scale.csv', columns = df_test_2_scale.columns, index = False) 

df_train_1_scale = pd.read_csv('df_train_1_scale.csv')
df_val_1_scale = pd.read_csv('df_val_1_scale.csv')
df_test_1_scale = pd.read_csv('df_test_1_scale.csv')
df_train_2_scale = pd.read_csv('df_train_2_scale.csv')
df_val_2_scale = pd.read_csv('df_val_2_scale.csv')
df_test_2_scale = pd.read_csv('df_test_2_scale.csv')


## splitting data (with deal_date for time series detection)
import pandas as pd
# Model_1: total_price
X_train_1_1_scale1 = df_train_1_scale.drop(['parking_num', 'price', 'price_norm', 'unit_price', '北區_unitprice', 
                                           '北屯南區_unitprice', '東區_unitprice','西區_unitprice', 
                                           '西屯南屯區_unitprice', '住宅大樓_unitprice', '公寓套房_unitprice', 
                                           '華廈_unitprice', 'year', 'month'], axis = 1)
y_train_1_1_scale1 = df_train_1_scale.price_norm
X_train_1_1_scale1.set_index('deal_date', inplace=True)
y_train_1_1_scale1.index = df_train_1_scale['deal_date']

X_val_1_1_scale1 = df_val_1_scale.drop(['parking_num', 'price', 'price_norm', 'unit_price', '北區_unitprice', 
                                           '北屯南區_unitprice', '東區_unitprice','西區_unitprice', 
                                           '西屯南屯區_unitprice', '住宅大樓_unitprice', '公寓套房_unitprice', 
                                           '華廈_unitprice', 'year', 'month'], axis = 1)
y_val_1_1_scale1 = df_val_1_scale.price_norm
X_val_1_1_scale1.set_index('deal_date', inplace=True)
y_val_1_1_scale1.index = df_val_1_scale['deal_date']

X_test_1_1_scale1 = df_test_1_scale.drop(['parking_num', 'price', 'price_norm', 'unit_price', '北區_unitprice', 
                                           '北屯南區_unitprice', '東區_unitprice','西區_unitprice', 
                                           '西屯南屯區_unitprice', '住宅大樓_unitprice', '公寓套房_unitprice', 
                                           '華廈_unitprice', 'year', 'month'], axis = 1)
y_test_1_1_scale1 = df_test_1_scale.price_norm
X_test_1_1_scale1.set_index('deal_date', inplace=True)
y_test_1_1_scale1.index = df_test_1_scale['deal_date']

# Model_1: unit_price
X_train_1_2_scale1 = df_train_1_scale.drop(['parking_num', 'price_norm', 'unit_price', 'price',
                                            '北區_price_norm', '南屯區_price_norm', '東西南區_price_norm', 
                                           '西屯北屯區_price_norm', '住宅大樓_price_norm', '公寓_price_norm', 
                                           '套房_price_norm', '華廈_price_norm', 'year', 
                                           'month'], axis = 1)
y_train_1_2_scale1 = df_train_1_scale.unit_price
X_train_1_2_scale1.set_index('deal_date', inplace=True)
y_train_1_2_scale1.index = df_train_1_scale['deal_date']

X_val_1_2_scale1 = df_val_1_scale.drop(['parking_num', 'price_norm', 'unit_price', 'price',
                                            '北區_price_norm', '南屯區_price_norm', '東西南區_price_norm', 
                                           '西屯北屯區_price_norm', '住宅大樓_price_norm', '公寓_price_norm', 
                                           '套房_price_norm', '華廈_price_norm', 'year', 
                                           'month'], axis = 1)
y_val_1_2_scale1 = df_val_1_scale.unit_price
X_val_1_2_scale1.set_index('deal_date', inplace=True)
y_val_1_2_scale1.index = df_val_1_scale['deal_date']

X_test_1_2_scale1 = df_test_1_scale.drop(['parking_num', 'price_norm', 'unit_price', 'price',
                                            '北區_price_norm', '南屯區_price_norm', '東西南區_price_norm', 
                                           '西屯北屯區_price_norm', '住宅大樓_price_norm', '公寓_price_norm', 
                                           '套房_price_norm', '華廈_price_norm', 'year', 
                                           'month'], axis = 1)
y_test_1_2_scale1 = df_test_1_scale.unit_price
X_test_1_2_scale1.set_index('deal_date', inplace=True)
y_test_1_2_scale1.index = df_test_1_scale['deal_date']

# Model_2: total price
X_train_2_1_scale1 = df_train_2_scale.drop(['parking_num', 'price_norm', 'unit_price', 'price',
                                            '北屯北南區_unitprice', '東區_unitprice', '西區_unitprice',
                                           '西屯南屯區_unitprice', 'year', 'month'], axis = 1)
y_train_2_1_scale1 = df_train_2_scale.price_norm
X_train_2_1_scale1.set_index('deal_date', inplace=True)
y_train_2_1_scale1.index = df_train_2_scale['deal_date']

X_val_2_1_scale1 = df_val_2_scale.drop(['parking_num', 'price_norm', 'unit_price', 'price',
                                            '北屯北南區_unitprice', '東區_unitprice', '西區_unitprice',
                                           '西屯南屯區_unitprice', 'year', 'month'], axis = 1)
y_val_2_1_scale1 = df_val_2_scale.price_norm
X_val_2_1_scale1.set_index('deal_date', inplace=True)
y_val_2_1_scale1.index = df_val_2_scale['deal_date']

X_test_2_1_scale1 = df_test_2_scale.drop(['parking_num', 'price_norm', 'unit_price', 'price',
                                            '北屯北南區_unitprice', '東區_unitprice', '西區_unitprice',
                                           '西屯南屯區_unitprice', 'year', 'month'], axis = 1)
y_test_2_1_scale1 = df_test_2_scale.price_norm
X_test_2_1_scale1.set_index('deal_date', inplace=True)
y_test_2_1_scale1.index = df_test_2_scale['deal_date']

# Model_2: unit_price
X_train_2_2_scale1 = df_train_2_scale.drop(['parking_num', 'price_norm', 'unit_price', 'price',
                                            '北區_price_norm', '南屯區_price_norm', '東西南區_price_norm',
                                           '西屯北屯區_price_norm', 'year', 'month'], axis = 1)
y_train_2_2_scale1 = df_train_2_scale.unit_price
X_train_2_2_scale1.set_index('deal_date', inplace=True)
y_train_2_2_scale1.index = df_train_2_scale['deal_date']

X_val_2_2_scale1 = df_val_2_scale.drop(['parking_num', 'price_norm', 'unit_price', 'price',
                                            '北區_price_norm', '南屯區_price_norm', '東西南區_price_norm',
                                           '西屯北屯區_price_norm', 'year', 'month'], axis = 1)
y_val_2_2_scale1 = df_val_2_scale.unit_price
X_val_2_2_scale1.set_index('deal_date', inplace=True)
y_val_2_2_scale1.index = df_val_2_scale['deal_date']

X_test_2_2_scale1 = df_test_2_scale.drop(['parking_num', 'price_norm', 'unit_price', 'price',
                                            '北區_price_norm', '南屯區_price_norm', '東西南區_price_norm',
                                           '西屯北屯區_price_norm', 'year', 'month'], axis = 1)
y_test_2_2_scale1 = df_test_2_scale.unit_price
X_test_2_2_scale1.set_index('deal_date', inplace=True)
y_test_2_2_scale1.index = df_test_2_scale['deal_date']


### Time series or not?
# autocorrelation check
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Model_1: total_price
# Fit a linear regression model to the time series
model = sm.OLS(y_train_1_1_scale1, X_train_1_1_scale1).fit()
# Compute the residuals of the model
residuals = model.resid
# Compute the Durbin-Watson test statistic
dw_test = sm.stats.stattools.durbin_watson(residuals)
print("Durbin-Watson test statistic:", dw_test) # 1.9956873587193238
# Plot the residuals against the time index
plt.plot(X_train_1_1_scale1.index, residuals, 'o')
plt.xlabel('Time')
plt.ylabel('Residuals')
plt.title('Residuals vs. Time')
plt.show()

# Model_1: unit_price
# Fit a linear regression model to the time series
model = sm.OLS(y_train_1_2_scale1, X_train_1_2_scale1).fit()
# Compute the residuals of the model
residuals = model.resid
# Compute the Durbin-Watson test statistic
dw_test = sm.stats.stattools.durbin_watson(residuals)
print("Durbin-Watson test statistic:", dw_test) # 2.0040303174085103
# Plot the residuals against the time index
plt.plot(X_train_1_2_scale1.index, residuals, 'o')
plt.xlabel('Time')
plt.ylabel('Residuals')
plt.title('Residuals vs. Time')
plt.show()

# Model_2: total_price
# Fit a linear regression model to the time series
model = sm.OLS(y_train_2_1_scale1, X_train_2_1_scale1).fit()
# Compute the residuals of the model
residuals = model.resid
# Compute the Durbin-Watson test statistic
dw_test = sm.stats.stattools.durbin_watson(residuals)
print("Durbin-Watson test statistic:", dw_test) # 1.9879150798444414
# Plot the residuals against the time index
plt.plot(X_train_2_1_scale1.index, residuals, 'o')
plt.xlabel('Time')
plt.ylabel('Residuals')
plt.title('Residuals vs. Time')
plt.show()

# Model_2: unit_price
# Fit a linear regression model to the time series
model = sm.OLS(y_train_2_2_scale1, X_train_2_2_scale1).fit()
# Compute the residuals of the model
residuals = model.resid
# Compute the Durbin-Watson test statistic
dw_test = sm.stats.stattools.durbin_watson(residuals)
print("Durbin-Watson test statistic:", dw_test) # 1.9928693606097327
# Plot the residuals against the time index
plt.plot(X_train_2_2_scale1.index, residuals, 'o')
plt.xlabel('Time')
plt.ylabel('Residuals')
plt.title('Residuals vs. Time')
plt.show()

''' autocorrelation is NOT significant, i'm not gonna use time series model'''


## categorize time columns
# do not consider year, replace month with "quarter" in time feature for feature reduction purpose
quarter_dict = {1:"Q1", 2:"Q1", 3:"Q1", 4:"Q2", 5:"Q2", 6:"Q2", 7:"Q3", 8:"Q3",
                9:"Q3", 10:"Q4", 11:"Q4", 12:"Q4"}
df_train_1_scale['quarter'] = df_train_1_scale['month'].map(quarter_dict)
df_val_1_scale['quarter'] = df_val_1_scale['month'].map(quarter_dict)
df_test_1_scale['quarter'] = df_test_1_scale['month'].map(quarter_dict)
df_train_2_scale['quarter'] = df_train_2_scale['month'].map(quarter_dict)
df_val_2_scale['quarter'] = df_val_2_scale['month'].map(quarter_dict)
df_test_2_scale['quarter'] = df_test_2_scale['month'].map(quarter_dict)

# quarter encoding(dummy base: Q1)
dummy = pd.get_dummies(df_train_1_scale["quarter"])
df_train_1_scale = pd.concat((df_train_1_scale, dummy), axis=1)
df_train_1_scale.isna().sum()
df_train_1_scale = df_train_1_scale.drop(["Q1"], axis=1)

dummy = pd.get_dummies(df_val_1_scale["quarter"])
df_val_1_scale = pd.concat((df_val_1_scale, dummy), axis=1)
df_val_1_scale.isna().sum()
df_val_1_scale = df_val_1_scale.drop(["Q1"], axis=1)

dummy = pd.get_dummies(df_test_1_scale["quarter"])
df_test_1_scale = pd.concat((df_test_1_scale, dummy), axis=1)
df_test_1_scale.isna().sum()
df_test_1_scale = df_test_1_scale.drop(["Q1"], axis=1)

dummy = pd.get_dummies(df_train_2_scale["quarter"])
df_train_2_scale = pd.concat((df_train_2_scale, dummy), axis=1)
df_train_2_scale.isna().sum()
df_train_2_scale = df_train_2_scale.drop(["Q1"], axis=1)

dummy = pd.get_dummies(df_val_2_scale["quarter"])
df_val_2_scale = pd.concat((df_val_2_scale, dummy), axis=1)
df_val_2_scale.isna().sum()
df_val_2_scale = df_val_2_scale.drop(["Q1"], axis=1)

dummy = pd.get_dummies(df_test_2_scale["quarter"])
df_test_2_scale = pd.concat((df_test_2_scale, dummy), axis=1)
df_test_2_scale.isna().sum()
df_test_2_scale = df_test_2_scale.drop(["Q1"], axis=1)


# splitting data
# Model_1: total price
X_train_1_1_scale = df_train_1_scale.drop(['parking_num', 'price_norm', 'unit_price', '北區_unitprice', 
                                           '北屯南區_unitprice', '東區_unitprice','西區_unitprice', 
                                           '西屯南屯區_unitprice', '住宅大樓_unitprice', 
                                           '公寓套房_unitprice', '華廈_unitprice', 'year', 
                                           'deal_date', 'month', 'quarter', 'price'], axis = 1)
y_train_1_1_scale = df_train_1_scale.price_norm
X_val_1_1_scale = df_val_1_scale.drop(['parking_num', 'price_norm', 'unit_price', '北區_unitprice', 
                                           '北屯南區_unitprice', '東區_unitprice','西區_unitprice', 
                                           '西屯南屯區_unitprice', '住宅大樓_unitprice', 
                                           '公寓套房_unitprice', '華廈_unitprice', 'year', 
                                           'deal_date', 'month', 'quarter', 'price'], axis = 1)
y_val_1_1_scale = df_val_1_scale.price_norm
X_test_1_1_scale = df_test_1_scale.drop(['parking_num', 'price_norm', 'unit_price', '北區_unitprice', 
                                           '北屯南區_unitprice', '東區_unitprice','西區_unitprice', 
                                           '西屯南屯區_unitprice', '住宅大樓_unitprice', 
                                           '公寓套房_unitprice', '華廈_unitprice', 'year', 
                                           'deal_date', 'month', 'quarter', 'price'], axis = 1)
y_test_1_1_scale = df_test_1_scale.price_norm

# Model_1: unit_price
X_train_1_2_scale = df_train_1_scale.drop(['parking_num', 'price_norm', 'unit_price', '北區_price_norm', 
                                           '南屯區_price_norm', '東西南區_price_norm', 
                                           '西屯北屯區_price_norm', '住宅大樓_price_norm', 
                                           '公寓_price_norm', '套房_price_norm', 
                                           '華廈_price_norm', 'year', 'deal_date', 'month', 
                                           'quarter', 'price'], axis = 1)
y_train_1_2_scale = df_train_1_scale.unit_price
X_val_1_2_scale = df_val_1_scale.drop(['parking_num', 'price_norm', 'unit_price', '北區_price_norm', 
                                           '南屯區_price_norm', '東西南區_price_norm', 
                                           '西屯北屯區_price_norm', '住宅大樓_price_norm', 
                                           '公寓_price_norm', '套房_price_norm', 
                                           '華廈_price_norm', 'year', 'deal_date', 'month', 
                                           'quarter', 'price'], axis = 1)
y_val_1_2_scale = df_val_1_scale.unit_price
X_test_1_2_scale = df_test_1_scale.drop(['parking_num', 'price_norm', 'unit_price', '北區_price_norm', 
                                           '南屯區_price_norm', '東西南區_price_norm', 
                                           '西屯北屯區_price_norm', '住宅大樓_price_norm', 
                                           '公寓_price_norm', '套房_price_norm', 
                                           '華廈_price_norm', 'year', 'deal_date', 'month', 
                                           'quarter', 'price'], axis = 1)
y_test_1_2_scale = df_test_1_scale.unit_price

# Model_2: total price
X_train_2_1_scale = df_train_2_scale.drop(['parking_num', 'price_norm', 'unit_price', '北屯北南區_unitprice', 
                                           '東區_unitprice', '西區_unitprice', '西屯南屯區_unitprice', 
                                           'year', 'deal_date', 'month', 'quarter', 'price'], axis = 1)
y_train_2_1_scale = df_train_2_scale.price_norm
X_val_2_1_scale = df_val_2_scale.drop(['parking_num', 'price_norm', 'unit_price', '北屯北南區_unitprice', 
                                           '東區_unitprice', '西區_unitprice', '西屯南屯區_unitprice', 
                                           'year', 'deal_date', 'month', 'quarter', 'price'], axis = 1)
y_val_2_1_scale = df_val_2_scale.price_norm
X_test_2_1_scale = df_test_2_scale.drop(['parking_num', 'price_norm', 'unit_price', '北屯北南區_unitprice', 
                                           '東區_unitprice', '西區_unitprice', '西屯南屯區_unitprice', 
                                           'year', 'deal_date', 'month', 'quarter', 'price'], axis = 1)
y_test_2_1_scale = df_test_2_scale.price_norm

# Model_2: unit_price
X_train_2_2_scale = df_train_2_scale.drop(['parking_num', 'price_norm', 'unit_price', '北區_price_norm', 
                                           '南屯區_price_norm', '東西南區_price_norm',
                                           '西屯北屯區_price_norm', 'year', 'deal_date', 
                                           'month', 'quarter', 'price'], axis = 1)
y_train_2_2_scale = df_train_2_scale.unit_price
X_val_2_2_scale = df_val_2_scale.drop(['parking_num', 'price_norm', 'unit_price', '北區_price_norm', 
                                           '南屯區_price_norm', '東西南區_price_norm',
                                           '西屯北屯區_price_norm', 'year', 'deal_date', 
                                           'month', 'quarter', 'price'], axis = 1)
y_val_2_2_scale = df_val_2_scale.unit_price
X_test_2_2_scale = df_test_2_scale.drop(['parking_num', 'price_norm', 'unit_price', '北區_price_norm', 
                                           '南屯區_price_norm', '東西南區_price_norm',
                                           '西屯北屯區_price_norm', 'year', 'deal_date', 
                                           'month', 'quarter', 'price'], axis = 1)
y_test_2_2_scale = df_test_2_scale.unit_price



## normality test (all models are non-linear)
from sklearn import metrics
from scipy.stats import probplot
import statsmodels.api as sm
import scipy.stats as stats
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Model_1: total_price
model = LinearRegression() 
model.fit(X_train_1_1_scale, y_train_1_1_scale)
y_pred = model.predict(X_val_1_1_scale)
r2 = metrics.r2_score(y_val_1_1_scale, y_pred)
n = len(X_val_1_1_scale)
p = X_val_1_1_scale.shape[1]
adj_r2 = 1 - (1 - r2) * (n - 1) / (n - p - 1)
mse = metrics.mean_squared_error(y_val_1_1_scale, y_pred)
rmse = metrics.mean_squared_error(y_val_1_1_scale, y_pred, squared=False)
mae = metrics.mean_absolute_error(y_val_1_1_scale, y_pred)
print("adj_r2:", round(adj_r2, 4))
print("MAE:", round(mae, 4))
print("MSE:", round(mse, 4))
print("RMSE:", round(rmse, 4))
residuals = y_val_1_1_scale - y_pred
# Perform normality test with Shapiro-Wilk test
shapiro_results = stats.shapiro(residuals)
print("Shapiro-Wilk test:")
print("Test statistic: {:.4f}, p-value: {:.4f}".format(shapiro_results[0], shapiro_results[1]))
# Plot QQ plot of residuals
probplot(residuals, plot=plt)
plt.title("QQ Plot of Residuals")
plt.show()
# Plot residuals vs predicted values
plt.scatter(y_pred, residuals)
plt.xlabel("Predicted Values")
plt.ylabel("Residuals")
plt.title("Residual Plot")
plt.show()


# Model_1: unit_price
model = LinearRegression() 
model.fit(X_train_1_2_scale, y_train_1_2_scale)
y_pred = model.predict(X_val_1_2_scale)
r2 = metrics.r2_score(y_val_1_2_scale, y_pred)
n = len(X_val_1_2_scale)
p = X_val_1_2_scale.shape[1]
adj_r2 = 1 - (1 - r2) * (n - 1) / (n - p - 1)
mse = metrics.mean_squared_error(y_val_1_2_scale, y_pred)
rmse = metrics.mean_squared_error(y_val_1_2_scale, y_pred, squared=False)
mae = metrics.mean_absolute_error(y_val_1_2_scale, y_pred)
print("adj_r2:", round(adj_r2, 4))
print("MAE:", round(mae, 4))
print("MSE:", round(mse, 4))
print("RMSE:", round(rmse, 4))
residuals = y_val_1_2_scale - y_pred
# Perform normality test with Shapiro-Wilk test
shapiro_results = stats.shapiro(residuals)
print("Shapiro-Wilk test:")
print("Test statistic: {:.4f}, p-value: {:.4f}".format(shapiro_results[0], shapiro_results[1]))
# Plot QQ plot of residuals
probplot(residuals, plot=plt)
plt.title("QQ Plot of Residuals")
plt.show()
# Plot residuals vs predicted values
plt.scatter(y_pred, residuals)
plt.xlabel("Predicted Values")
plt.ylabel("Residuals")
plt.title("Residual Plot")
plt.show()

# Model_2: total_price
model = LinearRegression() 
model.fit(X_train_2_1_scale, y_train_2_1_scale)
y_pred = model.predict(X_val_2_1_scale)
r2 = metrics.r2_score(y_val_2_1_scale, y_pred)
n = len(X_val_2_1_scale)
p = X_val_2_1_scale.shape[1]
adj_r2 = 1 - (1 - r2) * (n - 1) / (n - p - 1)
mse = metrics.mean_squared_error(y_val_2_1_scale, y_pred)
rmse = metrics.mean_squared_error(y_val_2_1_scale, y_pred, squared=False)
mae = metrics.mean_absolute_error(y_val_2_1_scale, y_pred)
print("adj_r2:", round(adj_r2, 4))
print("MAE:", round(mae, 4))
print("MSE:", round(mse, 4))
print("RMSE:", round(rmse, 4))
residuals = y_val_2_1_scale - y_pred
# Perform normality test with Shapiro-Wilk test
shapiro_results = stats.shapiro(residuals)
print("Shapiro-Wilk test:")
print("Test statistic: {:.4f}, p-value: {:.4f}".format(shapiro_results[0], shapiro_results[1]))
# Plot QQ plot of residuals
probplot(residuals, plot=plt)
plt.title("QQ Plot of Residuals")
plt.show()
# Plot residuals vs predicted values
plt.scatter(y_pred, residuals)
plt.xlabel("Predicted Values")
plt.ylabel("Residuals")
plt.title("Residual Plot")
plt.show()

# Model_2: unit_price
model = LinearRegression() 
model.fit(X_train_2_2_scale, y_train_2_2_scale)
y_pred = model.predict(X_val_2_2_scale)
r2 = metrics.r2_score(y_val_2_2_scale, y_pred)
n = len(X_val_2_2_scale)
p = X_val_2_2_scale.shape[1]
adj_r2 = 1 - (1 - r2) * (n - 1) / (n - p - 1)
mse = metrics.mean_squared_error(y_val_2_2_scale, y_pred)
rmse = metrics.mean_squared_error(y_val_2_2_scale, y_pred, squared=False)
mae = metrics.mean_absolute_error(y_val_2_2_scale, y_pred)
print("adj_r2:", round(adj_r2, 4))
print("MAE:", round(mae, 4))
print("MSE:", round(mse, 4))
print("RMSE:", round(rmse, 4))
residuals = y_val_2_2_scale - y_pred
# Perform normality test with Shapiro-Wilk test
shapiro_results = stats.shapiro(residuals)
print("Shapiro-Wilk test:")
print("Test statistic: {:.4f}, p-value: {:.4f}".format(shapiro_results[0], shapiro_results[1]))
# Plot QQ plot of residuals
probplot(residuals, plot=plt)
plt.title("QQ Plot of Residuals")
plt.show()
# Plot residuals vs predicted values
plt.scatter(y_pred, residuals)
plt.xlabel("Predicted Values")
plt.ylabel("Residuals")
plt.title("Residual Plot")
plt.show()


### feature selection

## SelectFpr: false positive rate test
from sklearn.feature_selection import SelectFpr, f_regression
# Model_1: total_price
selector = SelectFpr(f_regression, alpha=0.05)
selector.fit_transform(X_train_1_1_scale, y_train_1_1_scale)
new_feat_fpr = selector.get_feature_names_out() 
# dropped items
dropped_items = [col for col in X_train_1_1_scale.columns if col not in new_feat_fpr]
print(dropped_items)
# calculate features' f-value & p-value
def Calculate_pvalue(feat, target):
        fvalue, pval=f_regression(feat, target)
        i = 0
        print('\nfeatures    p value')
        print('==========  =======')
        for p in pval:
            print('{0:<12}\t{1:.4f}'.format(feat.columns[i], p))
            i += 1
        i = 0
        print('\nfeatures    f value')
        print('==========  =======')
        for f in fvalue:
            print('{0:<12}\t{1:.4f}'.format(feat.columns[i], f))
            i+=1
Calculate_pvalue(X_train_1_1_scale, y_train_1_1_scale) # ['CPI%', 'Q2', 'Q3', 'Q4']
v1_train_1_1 = X_train_1_1_scale.drop(['CPI%', 'Q2', 'Q3', 'Q4'], axis = 1)
v1_val_1_1 = X_val_1_1_scale.drop(['CPI%', 'Q2', 'Q3', 'Q4'], axis = 1)
v1_test_1_1 = X_test_1_1_scale.drop(['CPI%', 'Q2', 'Q3', 'Q4'], axis = 1)

# Model_1: unit_price
selector = SelectFpr(f_regression, alpha=0.05)
selector.fit_transform(X_train_1_2_scale, y_train_1_2_scale) 
new_feat_fpr = selector.get_feature_names_out() 
# dropped items
dropped_items = [col for col in X_train_1_2_scale.columns if col not in new_feat_fpr]
print(dropped_items)
# calculate features' f-value & p-value
def Calculate_pvalue(feat, target):
        fvalue, pval=f_regression(feat, target)
        i = 0
        print('\nfeatures    p value')
        print('==========  =======')
        for p in pval:
            print('{0:<12}\t{1:.4f}'.format(feat.columns[i], p))
            i += 1
        i = 0
        print('\nfeatures    f value')
        print('==========  =======')
        for f in fvalue:
            print('{0:<12}\t{1:.4f}'.format(feat.columns[i], f))
            i+=1
Calculate_pvalue(X_train_1_2_scale, y_train_1_2_scale)

# Model_2: total_price
selector = SelectFpr(f_regression, alpha=0.05)
selector.fit_transform(X_train_2_1_scale, y_train_2_1_scale)
new_feat_fpr = selector.get_feature_names_out() 
# dropped items
dropped_items = [col for col in X_train_2_1_scale.columns if col not in new_feat_fpr]
print(dropped_items)
# calculate features' f-value & p-value
def Calculate_pvalue(feat, target):
        fvalue, pval=f_regression(feat, target)
        i = 0
        print('\nfeatures    p value')
        print('==========  =======')
        for p in pval:
            print('{0:<12}\t{1:.4f}'.format(feat.columns[i], p))
            i += 1
        i = 0
        print('\nfeatures    f value')
        print('==========  =======')
        for f in fvalue:
            print('{0:<12}\t{1:.4f}'.format(feat.columns[i], f))
            i+=1
Calculate_pvalue(X_train_2_1_scale, y_train_2_1_scale) # ['Q3', 'Q4']
v1_train_2_1 = X_train_2_1_scale.drop(['Q3', 'Q4'], axis = 1)
v1_val_2_1 = X_val_2_1_scale.drop(['Q3', 'Q4'], axis = 1)
v1_test_2_1 = X_test_2_1_scale.drop(['Q3', 'Q4'], axis = 1)

# Model_2: unit_price
selector = SelectFpr(f_regression, alpha=0.05)
selector.fit_transform(X_train_2_2_scale, y_train_2_2_scale)
new_feat_fpr = selector.get_feature_names_out() 
# dropped items
dropped_items = [col for col in X_train_2_2_scale.columns if col not in new_feat_fpr]
print(dropped_items)
# calculate features' f-value & p-value
def Calculate_pvalue(feat, target):
        fvalue, pval=f_regression(feat, target)
        i = 0
        print('\nfeatures    p value')
        print('==========  =======')
        for p in pval:
            print('{0:<12}\t{1:.4f}'.format(feat.columns[i], p))
            i += 1
        i = 0
        print('\nfeatures    f value')
        print('==========  =======')
        for f in fvalue:
            print('{0:<12}\t{1:.4f}'.format(feat.columns[i], f))
            i+=1
Calculate_pvalue(X_train_2_2_scale, y_train_2_2_scale) # ['GDP%', 'Q3']
v1_train_2_2 = X_train_2_2_scale.drop(['GDP%', 'Q3'], axis = 1)
v1_val_2_2 = X_val_2_2_scale.drop(['GDP%', 'Q3'], axis = 1)
v1_test_2_2 = X_test_2_2_scale.drop(['GDP%', 'Q3'], axis = 1)



## SelectKBest: false positive rate test
from sklearn.model_selection import cross_val_score
from sklearn.feature_selection import SelectKBest
from sklearn.linear_model import LinearRegression 
# Model_1: total_price
k_values = range(1, len(X_train_1_1_scale.columns)+1) # Set the range of values for k
# Initialize the list to store the cross-validation scores
cv_scores = []
# Loop over the range of values for k
for k in k_values:
    # Create the SelectKBest object
    selector = SelectKBest(f_regression, k=k)
    # Fit the selector on the training data
    X_train_kbest = selector.fit_transform(X_train_1_1_scale, y_train_1_1_scale)
    # Compute the cross-validation score on the transformed data
    cv_score = np.mean(cross_val_score(LinearRegression(),
                                       X_train_kbest,
                                       y_train_1_1_scale,
                                       cv=5,
                                       scoring='r2'))
    # Append the cross-validation score to the list
    cv_scores.append(cv_score)
# Plot the relationship between k and the validation score
plt.plot(k_values, cv_scores)
plt.xticks(range(min(k_values), max( k_values)+1, 2))
plt.xlabel('Number of Features')
plt.ylabel('Validation Score')
plt.show()
# k = 18
selector = SelectKBest(f_regression, k = 18)
selector.fit_transform(X_train_1_1_scale, y_train_1_1_scale)
new_feat_kbest = selector.get_feature_names_out() 
# dropped items
dropped_items = [col for col in X_train_1_1_scale.columns if col not in new_feat_kbest]
print(dropped_items)
# ['CPI%', 'GDP%', 'lat', 'lon', 'mortgage_rate', 'elevator', 'manager', '東西南區_price_norm', 'Q2', 'Q3', 'Q4']
v2_train_1_1 = X_train_1_1_scale.drop(['CPI%', 'GDP%', 'lat', 'lon', 'mortgage_rate', 'elevator', 'manager', 
                                 '東西南區_price_norm', 'Q2', 'Q3', 'Q4'], axis = 1)
v2_val_1_1 = X_val_1_1_scale.drop(['CPI%', 'GDP%', 'lat', 'lon', 'mortgage_rate', 'elevator', 'manager', 
                                 '東西南區_price_norm', 'Q2', 'Q3', 'Q4'], axis = 1)
v2_test_1_1 = X_test_1_1_scale.drop(['CPI%', 'GDP%', 'lat', 'lon', 'mortgage_rate', 'elevator', 'manager', 
                                 '東西南區_price_norm', 'Q2', 'Q3', 'Q4'], axis = 1)


# Model_1: unit_price
k_values = range(1, len(X_train_1_2_scale.columns)+1)
cv_scores = []
for k in k_values:
    selector = SelectKBest(f_regression, k=k)
    X_train_kbest = selector.fit_transform(X_train_1_2_scale, y_train_1_2_scale)
    cv_score = np.mean(cross_val_score(LinearRegression(),
                                       X_train_kbest,
                                       y_train_1_2_scale,
                                       cv=5,
                                       scoring='r2'))
    cv_scores.append(cv_score)
# Plot the relationship between k and the validation score
plt.plot(k_values, cv_scores)
plt.xticks(range(min(k_values), max( k_values)+1, 2))
plt.xlabel('Number of Features')
plt.ylabel('Validation Score')
plt.show()
# k = 22
selector = SelectKBest(f_regression, k = 22)
selector.fit_transform(X_train_1_2_scale, y_train_1_2_scale)
new_feat_kbest = selector.get_feature_names_out() 
# dropped items
dropped_items = [col for col in X_train_1_2_scale.columns if col not in new_feat_kbest]
print(dropped_items)
# ['hall_num', 'lat', '北區_unitprice', '西區_unitprice', 'Q2', 'Q3', 'Q4']
v2_train_1_2 = X_train_1_2_scale.drop(['hall_num', 'lat', '北區_unitprice', '西區_unitprice', 
                                 'Q2', 'Q3', 'Q4'], axis = 1)
v2_val_1_2 = X_val_1_2_scale.drop(['hall_num', 'lat', '北區_unitprice', '西區_unitprice', 
                                 'Q2', 'Q3', 'Q4'], axis = 1)
v2_test_1_2 = X_test_1_2_scale.drop(['hall_num', 'lat', '北區_unitprice', '西區_unitprice', 
                                 'Q2', 'Q3', 'Q4'], axis = 1)


# Model_2: total_price
k_values = range(1, len(X_train_2_1_scale.columns)+1) # Set the range of values for k
# Initialize the list to store the cross-validation scores
cv_scores = []
# Loop over the range of values for k
for k in k_values:
    # Create the SelectKBest object
    selector = SelectKBest(f_regression, k=k)
    # Fit the selector on the training data
    X_train_kbest = selector.fit_transform(X_train_2_1_scale, y_train_2_1_scale)
    # Compute the cross-validation score on the transformed data
    cv_score = np.mean(cross_val_score(LinearRegression(),
                                       X_train_kbest,
                                       y_train_2_1_scale,
                                       cv=5,
                                       scoring='r2'))
    # Append the cross-validation score to the list
    cv_scores.append(cv_score)
# Plot the relationship between k and the validation score
plt.plot(k_values, cv_scores)
plt.xticks(range(min(k_values), max( k_values)+1, 2))
plt.xlabel('Number of Features')
plt.ylabel('Validation Score')
plt.show()
# k = 21
selector = SelectKBest(f_regression, k = 21)
selector.fit_transform(X_train_2_1_scale, y_train_2_1_scale)
new_feat_kbest = selector.get_feature_names_out() 
# dropped items
dropped_items = [col for col in X_train_2_1_scale.columns if col not in new_feat_kbest]
print(dropped_items)
# ['CPI%', 'GDP%', 'lat', 'mortgage_rate', 'manager', 'Q2', 'Q3', 'Q4']
v2_train_2_1 = X_train_2_1_scale.drop(['CPI%', 'GDP%', 'lat', 'mortgage_rate', 'manager', 
                                 'Q2', 'Q3', 'Q4'], axis = 1)
v2_val_2_1 = X_val_2_1_scale.drop(['CPI%', 'GDP%', 'lat', 'mortgage_rate', 'manager', 
                                 'Q2', 'Q3', 'Q4'], axis = 1)
v2_test_2_1 = X_test_2_1_scale.drop(['CPI%', 'GDP%', 'lat', 'mortgage_rate', 'manager', 
                                 'Q2', 'Q3', 'Q4'], axis = 1)


# Model_2: unit_price
k_values = range(1, len(X_train_2_2_scale.columns)+1)
cv_scores = []
for k in k_values:
    selector = SelectKBest(f_regression, k=k)
    X_train_kbest = selector.fit_transform(X_train_2_2_scale, y_train_2_2_scale)
    cv_score = np.mean(cross_val_score(LinearRegression(),
                                       X_train_kbest,
                                       y_train_2_2_scale,
                                       cv=5,
                                       scoring='r2'))
    cv_scores.append(cv_score)
# Plot the relationship between k and the validation score
plt.plot(k_values, cv_scores)
plt.xticks(range(min(k_values), max( k_values)+1, 2))
plt.xlabel('Number of Features')
plt.ylabel('Validation Score')
plt.show()
# k = 22
selector = SelectKBest(f_regression, k = 22)
selector.fit_transform(X_train_2_2_scale, y_train_2_2_scale)
new_feat_kbest = selector.get_feature_names_out() 
# dropped items
dropped_items = [col for col in X_train_2_2_scale.columns if col not in new_feat_kbest]
print(dropped_items)
# ['GDP%', 'hall_num', 'lat', '西區_unitprice', 'Q2', 'Q3', 'Q4']
v2_train_2_2 = X_train_2_2_scale.drop(['GDP%', 'hall_num', 'lat', '西區_unitprice', 'Q2', 
                                 'Q3', 'Q4'], axis = 1)
v2_val_2_2 = X_val_2_2_scale.drop(['GDP%', 'hall_num', 'lat', '西區_unitprice', 'Q2', 
                                 'Q3', 'Q4'], axis = 1)
v2_test_2_2 = X_test_2_2_scale.drop(['GDP%', 'hall_num', 'lat', '西區_unitprice', 'Q2', 
                                 'Q3', 'Q4'], axis = 1)



## forward selection
from sklearn.feature_selection import SequentialFeatureSelector as SFS
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR

# Model_1: total_price
# Set the range of the number of features to select
num_features = range(5, len(X_train_1_1_scale.columns))
# Initialize the list to store the cross-validation scores
cv_scores = []
# Loop over the range of the number of features to select
for num in num_features:
    # Create the sequential feature selector object
    sfs = SFS(estimator = LinearRegression(),
              n_features_to_select = num,
              direction = 'forward',
              scoring ='r2',
              cv = 5,
              n_jobs = 4)
    # Fit the sequential feature selector on the training data
    sfs.fit(X_train_1_1_scale, y_train_1_1_scale)
    # Compute the cross-validation score on the selected features
    cv_score = np.mean(cross_val_score(LinearRegression(),
                                        X_train_1_1_scale.iloc[:, list(sfs.support_)],
                                        y_train_1_1_scale,
                                        cv=5,
                                        scoring='r2'))
    # Append the cross-validation score to the list
    cv_scores.append(cv_score)
# Plot the cross-validation scores as a function of the number of selected features
plt.plot(num_features, cv_scores)
plt.xticks(range(min(num_features), 28, 2))
plt.xlabel('Number of features')
plt.ylabel('Cross-validation R^2 score')
plt.title('Optimal number of features')
plt.show()
# n = 11
sfs = SFS(estimator = LinearRegression(),  
          n_features_to_select = 11,
          direction = 'forward', 
          scoring = 'r2',
          cv = 5, 
          n_jobs = 4)
sfs = sfs.fit(X_train_1_1_scale, y_train_1_1_scale)
new_feat_SFS = sfs.get_feature_names_out()
print(new_feat_SFS) 
# drop: ['CPI%', 'GDP%', 'bathroom_num', 'floor_sold', 'lat', 'mortgage_rate', 'total_deal_floor', 
#'elevator', '北區_price_norm', '南屯區_price_norm', '東西南區_price_norm', '西屯北屯區_price_norm', 
#'住宅大樓_price_norm', '公寓_price_norm', '華廈_price_norm', 'Q2', 'Q3', 'Q4']
v3_train_1_1 = X_train_1_1_scale[['M1b', 'age', 'area', 'bedroom_num', 'build_share1', 'hall_num', 'lon',
 'parking_num_norm', 'story', 'manager', '套房_price_norm']]
v3_val_1_1 = X_val_1_1_scale[['M1b', 'age', 'area', 'bedroom_num', 'build_share1', 'hall_num', 'lon',
 'parking_num_norm', 'story', 'manager', '套房_price_norm']]
v3_test_1_1 = X_test_1_1_scale[['M1b', 'age', 'area', 'bedroom_num', 'build_share1', 'hall_num', 'lon',
 'parking_num_norm', 'story', 'manager', '套房_price_norm']]


# Model_1: unit_price
# Set the range of the number of features to select
num_features = range(5, len(X_train_1_2_scale.columns))
# Initialize the list to store the cross-validation scores
cv_scores = []
# Loop over the range of the number of features to select
for num in num_features:
    
    sfs = SFS(estimator = LinearRegression(),
              n_features_to_select = num,
              direction = 'forward',
              scoring ='r2',
              cv = 5,
              n_jobs = 4)
    
    sfs.fit(X_train_1_2_scale, y_train_1_2_scale)
   
    cv_score = np.mean(cross_val_score(LinearRegression(),
                                        X_train_1_2_scale.iloc[:, list(sfs.support_)],
                                        y_train_1_2_scale,
                                        cv=5,
                                        scoring='r2'))
    cv_scores.append(cv_score)
# Plot the cross-validation scores as a function of the number of selected features
plt.plot(num_features, cv_scores)
plt.xticks(range(min(num_features), 28, 2))
plt.xlabel('Number of features')
plt.ylabel('Cross-validation R^2 score')
plt.title('Optimal number of features')
plt.show() 
# n = 19
sfs = SFS(estimator = LinearRegression(),  
          n_features_to_select = 19,
          direction = 'forward', 
          scoring = 'r2',
          cv = 5, 
          n_jobs = 4)
sfs = sfs.fit(X_train_1_2_scale, y_train_1_2_scale)
new_feat_SFS = sfs.get_feature_names_out()
print(new_feat_SFS) 
# drop: ['CPI%', 'GDP%', 'bedroom_num', 'hall_num', 'lat', 'lon', 'elevator', 'Q2', 'Q3', 'Q4']
v3_train_1_2 = X_train_1_2_scale[['M1b', 'age', 'area', 'bathroom_num', 'build_share1', 'floor_sold',
 'mortgage_rate', 'parking_num_norm', 'story', 'total_deal_floor', 'manager',
 '北區_unitprice', '北屯南區_unitprice', '東區_unitprice', '西區_unitprice',
 '西屯南屯區_unitprice', '住宅大樓_unitprice', '公寓套房_unitprice', '華廈_unitprice']]
v3_val_1_2 = X_val_1_2_scale[['M1b', 'age', 'area', 'bathroom_num', 'build_share1', 'floor_sold',
 'mortgage_rate', 'parking_num_norm', 'story', 'total_deal_floor', 'manager',
 '北區_unitprice', '北屯南區_unitprice', '東區_unitprice', '西區_unitprice',
 '西屯南屯區_unitprice', '住宅大樓_unitprice', '公寓套房_unitprice', '華廈_unitprice']]
v3_test_1_2 = X_test_1_2_scale[['M1b', 'age', 'area', 'bathroom_num', 'build_share1', 'floor_sold',
 'mortgage_rate', 'parking_num_norm', 'story', 'total_deal_floor', 'manager',
 '北區_unitprice', '北屯南區_unitprice', '東區_unitprice', '西區_unitprice',
 '西屯南屯區_unitprice', '住宅大樓_unitprice', '公寓套房_unitprice', '華廈_unitprice']]

# Model_2: total_price
num_features = range(5, len(X_train_2_1_scale.columns))
cv_scores = []
for num in num_features:
    
    sfs = SFS(estimator = LinearRegression(),
              n_features_to_select = num,
              direction = 'forward',
              scoring ='r2',
              cv = 5,
              n_jobs = 4)
    
    sfs.fit(X_train_2_1_scale, y_train_2_1_scale)
   
    cv_score = np.mean(cross_val_score(LinearRegression(),
                                        X_train_2_1_scale.iloc[:, list(sfs.support_)],
                                        y_train_2_1_scale,
                                        cv=5,
                                        scoring='r2'))
    cv_scores.append(cv_score)
# Plot the cross-validation scores as a function of the number of selected features
plt.plot(num_features, cv_scores)
plt.xticks(range(min(num_features), 28, 2))
plt.xlabel('Number of features')
plt.ylabel('Cross-validation R^2 score')
plt.title('Optimal number of features')
plt.show()
# n = 12
sfs = SFS(estimator = LinearRegression(),  
          n_features_to_select = 12,
          direction = 'forward', 
          scoring = 'r2',
          cv = 5, 
          n_jobs = 4)
sfs = sfs.fit(X_train_2_1_scale, y_train_2_1_scale)
new_feat_SFS = sfs.get_feature_names_out()
print(new_feat_SFS) 
# drop: ['CPI%', 'GDP%', 'bathroom_num', 'floor_sold', 'lat', 'mortgage_rate', 'elevator', 
# '北區_price_norm', '南屯區_price_norm', '東西南區_price_norm', '西屯北屯區_price_norm', '住宅大樓', 
# '公寓', '華廈', 'Q2', 'Q3', 'Q4']
v3_train_2_1 = X_train_2_1_scale[['M1b', 'age', 'area', 'bedroom_num', 'build_share1', 'hall_num', 'lon',
 'parking_num_norm', 'story', 'total_deal_floor', 'manager', '套房']]
v3_val_2_1 = X_val_2_1_scale[['M1b', 'age', 'area', 'bedroom_num', 'build_share1', 'hall_num', 'lon',
 'parking_num_norm', 'story', 'total_deal_floor', 'manager', '套房']]
v3_test_2_1 = X_test_2_1_scale[['M1b', 'age', 'area', 'bedroom_num', 'build_share1', 'hall_num', 'lon',
 'parking_num_norm', 'story', 'total_deal_floor', 'manager', '套房']]


# Model_2: unit_price
num_features = range(5, len(X_train_2_2_scale.columns))
cv_scores = []
for num in num_features:
    
    sfs = SFS(estimator = LinearRegression(),
              n_features_to_select = num,
              direction = 'forward',
              scoring ='r2',
              cv = 5,
              n_jobs = 4)
    
    sfs.fit(X_train_2_2_scale, y_train_2_2_scale)
   
    cv_score = np.mean(cross_val_score(LinearRegression(),
                                        X_train_2_2_scale.iloc[:, list(sfs.support_)],
                                        y_train_2_2_scale,
                                        cv=5,
                                        scoring='r2'))
    cv_scores.append(cv_score)  
# Plot the cross-validation scores as a function of the number of selected features
plt.plot(num_features, cv_scores)
plt.xticks(range(min(num_features), 28, 2))
plt.xlabel('Number of features')
plt.ylabel('Cross-validation R^2 score')
plt.title('Optimal number of features')
plt.show()
# n = 14
sfs = SFS(estimator = LinearRegression(),  
          n_features_to_select = 14,
          direction = 'forward', 
          scoring = 'r2',
          cv = 5, 
          n_jobs = 4)
sfs = sfs.fit(X_train_2_2_scale, y_train_2_2_scale)
new_feat_SFS = sfs.get_feature_names_out()
print(new_feat_SFS) 
# drop: ['CPI%', 'GDP%', 'area', 'bathroom_num', 'floor_sold', 'hall_num', 'lat', 'lon', 
# 'mortgage_rate', 'manager', '北屯北南區_unitprice', '東區_unitprice', 'Q2', 'Q3', 'Q4']
v3_train_2_2 = X_train_2_2_scale[['M1b', 'age', 'bedroom_num', 'build_share1', 'parking_num_norm', 'story',
                            'total_deal_floor', 'elevator', '西區_unitprice', '西屯南屯區_unitprice', 
                            '住宅大樓','公寓', '套房', '華廈']]
v3_val_2_2 = X_val_2_2_scale[['M1b', 'age', 'bedroom_num', 'build_share1', 'parking_num_norm', 'story',
                            'total_deal_floor', 'elevator', '西區_unitprice', '西屯南屯區_unitprice', 
                            '住宅大樓','公寓', '套房', '華廈']]
v3_test_2_2 = X_test_2_2_scale[['M1b', 'age', 'bedroom_num', 'build_share1', 'parking_num_norm', 'story',
                            'total_deal_floor', 'elevator', '西區_unitprice', '西屯南屯區_unitprice', 
                            '住宅大樓','公寓', '套房', '華廈']]


## backward selection
# Model_1: total_price
num_features = range(5, len(X_train_1_1_scale.columns))
cv_scores = []
for num in num_features:

    sfs = SFS(estimator = LinearRegression(),
              n_features_to_select = num,
              direction = 'backward',
              scoring ='r2',
              cv = 5,
              n_jobs = 4)

    sfs.fit(X_train_1_1_scale, y_train_1_1_scale)

    cv_score = np.mean(cross_val_score(LinearRegression(),
                                        X_train_1_1_scale.iloc[:, list(sfs.support_)],
                                        y_train_1_1_scale,
                                        cv=5,
                                        scoring='r2'))
    cv_scores.append(cv_score)
# Plot the cross-validation scores as a function of the number of selected features
plt.plot(num_features, cv_scores)
plt.xticks(range(min(num_features), 28, 2))
plt.xlabel('Number of features')
plt.ylabel('Cross-validation R^2 score')
plt.title('Optimal number of features')
plt.show()
# n = 12
sfs = SFS(estimator = LinearRegression(),  
          n_features_to_select = 12,
          direction = 'backward', 
          scoring = 'r2',
          cv = 5, 
          n_jobs = 4)
sfs = sfs.fit(X_train_1_1_scale, y_train_1_1_scale)
new_feat_SFS = sfs.get_feature_names_out()
print(new_feat_SFS) 
# drop: ['CPI%', 'GDP%', 'bathroom_num', 'build_share1', 'floor_sold', 'lat', 'mortgage_rate', 
# 'total_deal_floor', 'elevator', 'manager', '北區_price_norm', '南屯區_price_norm', 
# '東西南區_price_norm', '西屯北屯區_price_norm', 'Q2', 'Q3', 'Q4']
v4_train_1_1 = X_train_1_1_scale.drop(['CPI%', 'GDP%', 'bathroom_num', 'build_share1', 'floor_sold', 'lat', 
                                 'mortgage_rate', 'total_deal_floor', 'elevator', 'manager', 
                                 '北區_price_norm', '南屯區_price_norm', '東西南區_price_norm', 
                                 '西屯北屯區_price_norm', 'Q2', 'Q3', 'Q4'], axis = 1)
v4_val_1_1 = X_val_1_1_scale.drop(['CPI%', 'GDP%', 'bathroom_num', 'build_share1', 'floor_sold', 'lat', 
                                 'mortgage_rate', 'total_deal_floor', 'elevator', 'manager', 
                                 '北區_price_norm', '南屯區_price_norm', '東西南區_price_norm', 
                                 '西屯北屯區_price_norm', 'Q2', 'Q3', 'Q4'], axis = 1)
v4_test_1_1 = X_test_1_1_scale.drop(['CPI%', 'GDP%', 'bathroom_num', 'build_share1', 'floor_sold', 'lat', 
                                 'mortgage_rate', 'total_deal_floor', 'elevator', 'manager', 
                                 '北區_price_norm', '南屯區_price_norm', '東西南區_price_norm', 
                                 '西屯北屯區_price_norm', 'Q2', 'Q3', 'Q4'], axis = 1)


# Model_1: unit_price
num_features = range(5, len(X_train_1_2_scale.columns))
cv_scores = []
for num in num_features:
    
    sfs = SFS(estimator = LinearRegression(),
              n_features_to_select = num,
              direction = 'backward',
              scoring ='r2',
              cv = 5,
              n_jobs = 4)
    
    sfs.fit(X_train_1_2_scale, y_train_1_2_scale)
   
    cv_score = np.mean(cross_val_score(LinearRegression(),
                                        X_train_1_2_scale.iloc[:, list(sfs.support_)],
                                        y_train_1_2_scale,
                                        cv=5,
                                        scoring='r2'))
    cv_scores.append(cv_score)
# Plot the cross-validation scores as a function of the number of selected features
plt.plot(num_features, cv_scores)
plt.xticks(range(min(num_features), 28, 2))
plt.xlabel('Number of features')
plt.ylabel('Cross-validation R^2 score')
plt.title('Optimal number of features')
plt.show()
# n = 11
sfs = SFS(estimator = LinearRegression(),  
          n_features_to_select = 11,
          direction = 'backward', 
          scoring = 'r2',
          cv = 5, 
          n_jobs = 4)
sfs = sfs.fit(X_train_1_2_scale, y_train_1_2_scale)
new_feat_SFS = sfs.get_feature_names_out()
print(new_feat_SFS) 
# drop: ['CPI%', 'GDP%', 'area', 'bathroom_num', 'bedroom_num', 'build_share1', 'floor_sold',
#   'hall_num', 'lat', 'lon', 'mortgage_rate', 'total_deal_floor', 'elevator', '北屯南區_unitprice', 
# '東區_unitprice', 'Q2', 'Q3', 'Q4']
v4_train_1_2 = X_train_1_2_scale.drop(['CPI%', 'GDP%', 'area', 'bathroom_num', 'bedroom_num', 'build_share1', 
                                 'floor_sold','hall_num', 'lat', 'lon', 'mortgage_rate', 
                                 'total_deal_floor', 'elevator', '北屯南區_unitprice', '東區_unitprice', 
                                 'Q2', 'Q3', 'Q4'], axis = 1)
v4_val_1_2 = X_val_1_2_scale.drop(['CPI%', 'GDP%', 'area', 'bathroom_num', 'bedroom_num', 'build_share1', 
                                 'floor_sold','hall_num', 'lat', 'lon', 'mortgage_rate', 
                                 'total_deal_floor', 'elevator', '北屯南區_unitprice', '東區_unitprice', 
                                 'Q2', 'Q3', 'Q4'], axis = 1)
v4_test_1_2 = X_test_1_2_scale.drop(['CPI%', 'GDP%', 'area', 'bathroom_num', 'bedroom_num', 'build_share1', 
                                 'floor_sold','hall_num', 'lat', 'lon', 'mortgage_rate', 
                                 'total_deal_floor', 'elevator', '北屯南區_unitprice', '東區_unitprice', 
                                 'Q2', 'Q3', 'Q4'], axis = 1)


# Model_2: total_price
num_features = range(5, len(X_train_2_1_scale.columns))
cv_scores = []
for num in num_features:
    
    sfs = SFS(estimator = LinearRegression(),
              n_features_to_select = num,
              direction = 'backward',
              scoring ='r2',
              cv = 5,
              n_jobs = 4)
    
    sfs.fit(X_train_2_1_scale, y_train_2_1_scale)
   
    cv_score = np.mean(cross_val_score(LinearRegression(),
                                        X_train_2_1_scale.iloc[:, list(sfs.support_)],
                                        y_train_2_1_scale,
                                        cv=5,
                                        scoring='r2'))
    cv_scores.append(cv_score)
# Plot the cross-validation scores as a function of the number of selected features
plt.plot(num_features, cv_scores)
plt.xticks(range(min(num_features), 28, 2))
plt.xlabel('Number of features')
plt.ylabel('Cross-validation R^2 score')
plt.title('Optimal number of features')
plt.show()
# n = 9
sfs = SFS(estimator = LinearRegression(),  
          n_features_to_select = 9,
          direction = 'backward', 
          scoring = 'r2',
          cv = 5, 
          n_jobs = 4)
sfs = sfs.fit(X_train_2_1_scale, y_train_2_1_scale)
new_feat_SFS = sfs.get_feature_names_out()
print(new_feat_SFS) 
# drop: ['CPI%', 'GDP%', 'bathroom_num', 'bedroom_num', 'build_share1', 'floor_sold', 'hall_num', 
# 'lat', 'mortgage_rate', 'story', 'total_deal_floor', 'elevator', 'manager', '北區_price_norm', 
# '南屯區_price_norm', '東西南區_price_norm', '西屯北屯區_price_norm', 'Q2', 'Q3', 'Q4']
v4_train_2_1 = X_train_2_1_scale.drop(['CPI%', 'GDP%', 'bathroom_num', 'bedroom_num', 'build_share1', 
                                 'floor_sold', 'hall_num', 'lat', 'mortgage_rate', 'story', 
                                 'total_deal_floor', 'elevator', 'manager', '北區_price_norm', 
                                 '南屯區_price_norm', '東西南區_price_norm', '西屯北屯區_price_norm', 
                                 'Q2', 'Q3', 'Q4'], axis = 1)
v4_val_2_1 = X_val_2_1_scale.drop(['CPI%', 'GDP%', 'bathroom_num', 'bedroom_num', 'build_share1', 
                                 'floor_sold', 'hall_num', 'lat', 'mortgage_rate', 'story', 
                                 'total_deal_floor', 'elevator', 'manager', '北區_price_norm', 
                                 '南屯區_price_norm', '東西南區_price_norm', '西屯北屯區_price_norm', 
                                 'Q2', 'Q3', 'Q4'], axis = 1)
v4_test_2_1 = X_test_2_1_scale.drop(['CPI%', 'GDP%', 'bathroom_num', 'bedroom_num', 'build_share1', 
                                 'floor_sold', 'hall_num', 'lat', 'mortgage_rate', 'story', 
                                 'total_deal_floor', 'elevator', 'manager', '北區_price_norm', 
                                 '南屯區_price_norm', '東西南區_price_norm', '西屯北屯區_price_norm', 
                                 'Q2', 'Q3', 'Q4'], axis = 1)

# Model_2: unit_price
num_features = range(5, len(X_train_2_2_scale.columns))
cv_scores = []
for num in num_features:
    
    sfs = SFS(estimator = LinearRegression(),
              n_features_to_select = num,
              direction = 'backward',
              scoring ='r2',
              cv = 5,
              n_jobs = 4)
    
    sfs.fit(X_train_2_2_scale, y_train_2_2_scale)
   
    cv_score = np.mean(cross_val_score(LinearRegression(),
                                        X_train_2_2_scale.iloc[:, list(sfs.support_)],
                                        y_train_2_2_scale,
                                        cv=5,
                                        scoring='r2'))
    cv_scores.append(cv_score)
# Plot the cross-validation scores as a function of the number of selected features
plt.plot(num_features, cv_scores)
plt.xticks(range(min(num_features), 28, 2))
plt.xlabel('Number of features')
plt.ylabel('Cross-validation R^2 score')
plt.title('Optimal number of features')
plt.show()
# n = 11
sfs = SFS(estimator = LinearRegression(),  
          n_features_to_select = 11,
          direction = 'backward', 
          scoring = 'r2',
          cv = 5, 
          n_jobs = 4)
sfs = sfs.fit(X_train_2_2_scale, y_train_2_2_scale)
new_feat_SFS = sfs.get_feature_names_out()
print(new_feat_SFS) 
# drop: ['CPI%', 'GDP%', 'area', 'bathroom_num', 'bedroom_num', 'build_share1', 'floor_sold',
#   'hall_num', 'lat', 'lon', 'mortgage_rate', 'total_deal_floor', 'manager', '北屯北南區_unitprice',
#   '東區_unitprice', 'Q2', 'Q3', 'Q4']
v4_train_2_2 = X_train_2_2_scale.drop(['CPI%', 'GDP%', 'area', 'bathroom_num', 'bedroom_num', 'build_share1',
                                 'floor_sold','hall_num', 'lat', 'lon', 'mortgage_rate', 
                                 'total_deal_floor', 'manager', '北屯北南區_unitprice','東區_unitprice', 
                                 'Q2', 'Q3', 'Q4'], axis = 1)
v4_val_2_2 = X_val_2_2_scale.drop(['CPI%', 'GDP%', 'area', 'bathroom_num', 'bedroom_num', 'build_share1',
                                 'floor_sold','hall_num', 'lat', 'lon', 'mortgage_rate', 
                                 'total_deal_floor', 'manager', '北屯北南區_unitprice','東區_unitprice', 
                                 'Q2', 'Q3', 'Q4'], axis = 1)
v4_test_2_2 = X_test_2_2_scale.drop(['CPI%', 'GDP%', 'area', 'bathroom_num', 'bedroom_num', 'build_share1',
                                 'floor_sold','hall_num', 'lat', 'lon', 'mortgage_rate', 
                                 'total_deal_floor', 'manager', '北屯北南區_unitprice','東區_unitprice', 
                                 'Q2', 'Q3', 'Q4'], axis = 1)


## regression coefficients
from sklearn.feature_selection import SelectFromModel
model = SelectFromModel(LinearRegression())
# Model_1: price
model.fit(X_train_1_1_scale, y_train_1_1_scale)
selected_feat = X_train_1_1_scale.columns[(model.get_support())]
cols = set(X_train_1_1_scale) - set(selected_feat)
print('dropped features: {0}'.format(cols))
print("")
print('selected features: {0}'.format(selected_feat))
v5_train_1_1 = X_train_1_1_scale[['M1b', 'age', 'area', 'bathroom_num', 'bedroom_num', 'hall_num', 
                            'parking_num_norm', '套房_price_norm']]
v5_val_1_1 = X_val_1_1_scale[['M1b', 'age', 'area', 'bathroom_num', 'bedroom_num', 'hall_num', 
                            'parking_num_norm', '套房_price_norm']]
v5_test_1_1 = X_test_1_1_scale[['M1b', 'age', 'area', 'bathroom_num', 'bedroom_num', 'hall_num', 
                            'parking_num_norm', '套房_price_norm']]

# Model_1: unit_price
model.fit(X_train_1_2_scale, y_train_1_2_scale)
selected_feat = X_train_1_2_scale.columns[(model.get_support())]
cols = set(X_train_1_2_scale) - set(selected_feat)
print('dropped features: {0}'.format(cols))
print("")
print('selected features: {0}'.format(selected_feat))
v5_train_1_2 = X_train_1_2_scale[['M1b', 'age', 'parking_num_norm', 'story', '住宅大樓_unitprice', 
                            '公寓套房_unitprice', '華廈_unitprice']]
v5_val_1_2 = X_val_1_2_scale[['M1b', 'age', 'parking_num_norm', 'story', '住宅大樓_unitprice', 
                            '公寓套房_unitprice', '華廈_unitprice']]
v5_test_1_2 = X_test_1_2_scale[['M1b', 'age', 'parking_num_norm', 'story', '住宅大樓_unitprice', 
                            '公寓套房_unitprice', '華廈_unitprice']]

# Model_2: price
model.fit(X_train_2_1_scale, y_train_2_1_scale)
selected_feat = X_train_2_1_scale.columns[(model.get_support())]
cols = set(X_train_2_1_scale) - set(selected_feat)
print('dropped features: {0}'.format(cols))
print("")
print('selected features: {0}'.format(selected_feat))
v5_train_2_1 = X_train_2_1_scale[['M1b', 'age', 'area', 'bedroom_num', 'hall_num', 'parking_num_norm', 
                              '住宅大樓', '套房', '華廈']]
v5_val_2_1 = X_val_2_1_scale[['M1b', 'age', 'area', 'bedroom_num', 'hall_num', 'parking_num_norm', 
                              '住宅大樓', '套房', '華廈']]
v5_test_2_1 = X_test_2_1_scale[['M1b', 'age', 'area', 'bedroom_num', 'hall_num', 'parking_num_norm', 
                              '住宅大樓', '套房', '華廈']]

# Model_2: unit_price
model.fit(X_train_2_2_scale, y_train_2_2_scale)
selected_feat = X_train_2_2_scale.columns[(model.get_support())]
cols = set(X_train_2_2_scale) - set(selected_feat)
print('dropped features: {0}'.format(cols))
print("")
print('selected features: {0}'.format(selected_feat))
v5_train_2_2 = X_train_2_2_scale[['M1b', 'age', 'bedroom_num', 'hall_num', 'parking_num_norm', 'story', 
                            '住宅大樓', '公寓', '套房', '華廈']]
v5_val_2_2 = X_val_2_2_scale[['M1b', 'age', 'bedroom_num', 'hall_num', 'parking_num_norm', 'story', 
                            '住宅大樓', '公寓', '套房', '華廈']]
v5_test_2_2 = X_test_2_2_scale[['M1b', 'age', 'bedroom_num', 'hall_num', 'parking_num_norm', 'story', 
                            '住宅大樓', '公寓', '套房', '華廈']]


## feature importance                    
from sklearn.ensemble import RandomForestRegressor
# Model_1: price
model = SelectFromModel(RandomForestRegressor(random_state = 42))
model.fit(X_train_1_1_scale, y_train_1_1_scale)
importances = list(model.estimator_.feature_importances_)
feature_list = list(X_train_1_1_scale.columns)
list1, list2 = (list(t) for t in zip(*sorted(zip(importances, feature_list))))
x_values = list(range(len(importances))) 
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
plt.figure(figsize=(10,6))
plt.barh(x_values, list1, linewidth = 1.2)
plt.yticks(x_values, list2, rotation='horizontal')
plt.ylabel('Features')
plt.xlabel('Importance')
plt.title('Model_1 (Target:Price) Feature Importances')
plt.tight_layout()
plt.show()
v6_train_1_1 = X_train_1_1_scale[['area', 'build_share1', 'age', 'lon', 'M1b', 'lat', 'story', 'floor_sold',
                            'CPI%', 'bathroom_num']]
v6_val_1_1 = X_val_1_1_scale[['area', 'build_share1', 'age', 'lon', 'M1b', 'lat', 'story', 'floor_sold',
                            'CPI%', 'bathroom_num']]
v6_test_1_1 = X_test_1_1_scale[['area', 'build_share1', 'age', 'lon', 'M1b', 'lat', 'story', 'floor_sold',
                            'CPI%', 'bathroom_num']]

# Model_1: unit_price
model = SelectFromModel(RandomForestRegressor(random_state = 42))
model.fit(X_train_1_2_scale, y_train_1_2_scale)
importances = list(model.estimator_.feature_importances_)
feature_list = list(X_train_1_2_scale.columns)
list1, list2 = (list(t) for t in zip(*sorted(zip(importances, feature_list))))
x_values = list(range(len(importances))) 
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
plt.figure(figsize=(10,6))
plt.barh(x_values, list1, linewidth = 1.2)
plt.yticks(x_values, list2, rotation='horizontal')
plt.ylabel('Features')
plt.xlabel('Importance')
plt.title('Model_1 (Target: Unit Price) Feature Importances')
plt.tight_layout()
plt.show()
v6_train_1_2= X_train_1_2_scale[['build_share1', 'age', 'lon', 'M1b', 'elevator', 'story', 'lat', 
                           'area', 'floor_sold', '北屯南區_unitprice']]
v6_val_1_2= X_val_1_2_scale[['build_share1', 'age', 'lon', 'M1b', 'elevator', 'story', 'lat', 
                           'area', 'floor_sold', '北屯南區_unitprice']]
v6_test_1_2= X_test_1_2_scale[['build_share1', 'age', 'lon', 'M1b', 'elevator', 'story', 'lat', 
                           'area', 'floor_sold', '北屯南區_unitprice']]

# Model_2: price
model = SelectFromModel(RandomForestRegressor(random_state = 42))
model.fit(X_train_2_1_scale, y_train_2_1_scale)
importances = list(model.estimator_.feature_importances_)
feature_list = list(X_train_2_1_scale.columns)
list1, list2 = (list(t) for t in zip(*sorted(zip(importances, feature_list))))
x_values = list(range(len(importances))) 
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
plt.figure(figsize=(10,6))
plt.barh(x_values, list1, linewidth = 1.2)
plt.yticks(x_values, list2, rotation='horizontal')
plt.ylabel('Features')
plt.xlabel('Importance')
plt.title('Model_2 (Target:Price) Feature Importances')
plt.tight_layout()
plt.show()
v6_train_2_1 = X_train_2_1_scale[['area', 'build_share1', 'age', 'lon', 'M1b', 'lat', 'story', 'floor_sold',
                            'CPI%', 'bathroom_num']]
v6_val_2_1 = X_val_2_1_scale[['area', 'build_share1', 'age', 'lon', 'M1b', 'lat', 'story', 'floor_sold',
                            'CPI%', 'bathroom_num']]
v6_test_2_1 = X_test_2_1_scale[['area', 'build_share1', 'age', 'lon', 'M1b', 'lat', 'story', 'floor_sold',
                            'CPI%', 'bathroom_num']]

# Model_2: unit_price
model = SelectFromModel(RandomForestRegressor(random_state = 42))
model.fit(X_train_2_2_scale, y_train_2_2_scale)
importances = list(model.estimator_.feature_importances_)
feature_list = list(X_train_2_2_scale.columns)
list1, list2 = (list(t) for t in zip(*sorted(zip(importances, feature_list))))
x_values = list(range(len(importances))) 
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
plt.figure(figsize=(10,6))
plt.barh(x_values, list1, linewidth = 1.2)
plt.yticks(x_values, list2, rotation='horizontal')
plt.ylabel('Features')
plt.xlabel('Importance')
plt.title('Model_2 (Target: Unit Price) Feature Importances')
plt.tight_layout()
plt.show()
v6_train_2_2= X_train_2_2_scale[['build_share1', 'age', 'lon', 'M1b', 'elevator', 'story', 'lat', 
                           'area', 'floor_sold', '西屯南屯區_unitprice']]
v6_val_2_2= X_val_2_2_scale[['build_share1', 'age', 'lon', 'M1b', 'elevator', 'story', 'lat', 
                           'area', 'floor_sold', '西屯南屯區_unitprice']]
v6_test_2_2= X_test_2_2_scale[['build_share1', 'age', 'lon', 'M1b', 'elevator', 'story', 'lat', 
                           'area', 'floor_sold', '西屯南屯區_unitprice']]


### VIF analysis 
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor
# Model_1: total_price
vif_df = pd.DataFrame(columns=['feature', 'VIF'])
for i, feature in enumerate(v6_train_1_1.columns):
    vif_score = variance_inflation_factor(v6_train_1_1.values, i)
    vif_df = vif_df.append({'feature': feature, 'VIF': vif_score}, ignore_index=True)
print(vif_df)
# drop columns and VIF
vif_df = pd.DataFrame(columns=['feature', 'VIF'])
for i, feature in enumerate(v6_train_1_1.drop(['story'], axis = 1).columns):
    vif_score = variance_inflation_factor(v6_train_1_1.drop(['story'], axis = 1).values, i)
    vif_df = vif_df.append({'feature': feature, 'VIF': vif_score}, ignore_index=True)
print(vif_df)
# drop
v1_train_1_1.drop(['住宅大樓_price_norm', 'total_deal_floor', '西屯北屯區_price_norm', 'bedroom_num'],
                  axis = 1, inplace = True)
v1_val_1_1.drop(['住宅大樓_price_norm', 'total_deal_floor', '西屯北屯區_price_norm', 'bedroom_num'],
                  axis = 1, inplace = True)
v1_test_1_1.drop(['住宅大樓_price_norm', 'total_deal_floor', '西屯北屯區_price_norm', 'bedroom_num'],
                  axis = 1, inplace = True)
v2_train_1_1.drop(['住宅大樓_price_norm', 'total_deal_floor', 'bedroom_num'], axis = 1, inplace = True)
v2_val_1_1.drop(['住宅大樓_price_norm', 'total_deal_floor', 'bedroom_num'], axis = 1, inplace = True)
v2_test_1_1.drop(['住宅大樓_price_norm', 'total_deal_floor', 'bedroom_num'], axis = 1, inplace = True)
v4_train_1_1.drop(['住宅大樓_price_norm'], axis = 1, inplace = True)
v4_val_1_1.drop(['住宅大樓_price_norm'], axis = 1, inplace = True)
v4_test_1_1.drop(['住宅大樓_price_norm'], axis = 1, inplace = True)
v5_train_1_1.drop(['bedroom_num'], axis = 1, inplace = True)
v5_val_1_1.drop(['bedroom_num'], axis = 1, inplace = True)
v5_test_1_1.drop(['bedroom_num'], axis = 1, inplace = True)
v6_train_1_1.drop(['story'], axis = 1, inplace = True)
v6_val_1_1.drop(['story'], axis = 1, inplace = True)
v6_test_1_1.drop(['story'], axis = 1, inplace = True)

# Model_1:unit_price
vif_df = pd.DataFrame(columns=['feature', 'VIF'])
for i, feature in enumerate(v6_train_1_1.columns):
    vif_score = variance_inflation_factor(v6_train_1_1.values, i)
    vif_df = vif_df.append({'feature': feature, 'VIF': vif_score}, ignore_index=True)
print(vif_df)
# drop columns
vif_df = pd.DataFrame(columns=['feature', 'VIF'])
for i, feature in enumerate(v6_train_1_1.drop(['story'], axis = 1).columns):
    vif_score = variance_inflation_factor(v6_train_1_1.drop(['story'], axis = 1).values, i)
    vif_df = vif_df.append({'feature': feature, 'VIF': vif_score}, ignore_index=True)
print(vif_df)

# Model_2:total_price
vif_df = pd.DataFrame(columns=['feature', 'VIF'])
for i, feature in enumerate(v6_train_2_1.columns):
    vif_score = variance_inflation_factor(v6_train_2_1.values, i)
    vif_df = vif_df.append({'feature': feature, 'VIF': vif_score}, ignore_index=True)
print(vif_df)
# drop columns
vif_df = pd.DataFrame(columns=['feature', 'VIF'])
for i, feature in enumerate(v6_train_2_1.drop(['total_deal_floor'], axis = 1).columns):
    vif_score = variance_inflation_factor(v6_train_2_1.drop(['total_deal_floor'], axis = 1).values, i)
    vif_df = vif_df.append({'feature': feature, 'VIF': vif_score}, ignore_index=True)
print(vif_df)
v1_train_2_1.drop(['住宅大樓', 'total_deal_floor', '西屯北屯區_price_norm',  'bedroom_num'],
                  axis = 1, inplace = True)
v1_val_2_1.drop(['住宅大樓', 'total_deal_floor', '西屯北屯區_price_norm',  'bedroom_num'],
                  axis = 1, inplace = True)
v1_test_2_1.drop(['住宅大樓', 'total_deal_floor', '西屯北屯區_price_norm',  'bedroom_num'],
                  axis = 1, inplace = True)
v2_train_2_1.drop(['住宅大樓', 'total_deal_floor', 'bedroom_num'], axis = 1, inplace = True)
v2_val_2_1.drop(['住宅大樓', 'total_deal_floor', 'bedroom_num'], axis = 1, inplace = True)
v2_test_2_1.drop(['住宅大樓', 'total_deal_floor', 'bedroom_num'], axis = 1, inplace = True)
v3_train_2_1.drop(['total_deal_floor'], axis = 1, inplace = True)
v3_val_2_1.drop(['total_deal_floor'], axis = 1, inplace = True)
v3_test_2_1.drop(['total_deal_floor'], axis = 1, inplace = True)


# Model_2:unit_price
vif_df = pd.DataFrame(columns=['feature', 'VIF'])
for i, feature in enumerate(v6_train_2_2.columns):
    vif_score = variance_inflation_factor(v6_train_2_2.values, i)
    vif_df = vif_df.append({'feature': feature, 'VIF': vif_score}, ignore_index=True)
print(vif_df)
# drop columns and VIF test
vif_df = pd.DataFrame(columns=['feature', 'VIF'])
for i, feature in enumerate(v6_train_2_2.drop(['住宅大樓'], axis = 1).columns):
    vif_score = variance_inflation_factor(v6_train_2_2.drop(['住宅大樓'], axis = 1).values, i)
    vif_df = vif_df.append({'feature': feature, 'VIF': vif_score}, ignore_index=True)
print(vif_df)
v1_train_2_2.drop(['住宅大樓', 'total_deal_floor', '北屯北南區_unitprice', 'bedroom_num'],
                  axis = 1, inplace = True)
v1_val_2_2.drop(['住宅大樓', 'total_deal_floor', '北屯北南區_unitprice', 'bedroom_num'],
                  axis = 1, inplace = True)
v1_test_2_2.drop(['住宅大樓', 'total_deal_floor', '北屯北南區_unitprice', 'bedroom_num'],
                  axis = 1, inplace = True)
v2_train_2_2.drop(['住宅大樓', 'total_deal_floor', 'bedroom_num'], axis = 1, inplace = True)
v2_val_2_2.drop(['住宅大樓', 'total_deal_floor', 'bedroom_num'], axis = 1, inplace = True)
v2_test_2_2.drop(['住宅大樓', 'total_deal_floor', 'bedroom_num'], axis = 1, inplace = True)
v3_train_2_2.drop(['住宅大樓', 'total_deal_floor'], axis = 1, inplace = True)
v3_val_2_2.drop(['住宅大樓', 'total_deal_floor'], axis = 1, inplace = True)
v3_test_2_2.drop(['住宅大樓', 'total_deal_floor'], axis = 1, inplace = True)
v4_train_2_2.drop(['住宅大樓'], axis = 1, inplace = True)
v4_val_2_2.drop(['住宅大樓'], axis = 1, inplace = True)
v4_test_2_2.drop(['住宅大樓'], axis = 1, inplace = True)
v5_train_2_2.drop(['住宅大樓'], axis = 1, inplace = True)
v5_val_2_2.drop(['住宅大樓'], axis = 1, inplace = True)
v5_test_2_2.drop(['住宅大樓'], axis = 1, inplace = True)


### modeling and evaluation

## Linear Regression
# Model_1: total_price
model = LinearRegression() 
model.fit(v1_train_1_1, y_train_1_1_scale)
y_pred = model.predict(v1_val_1_1)
r2 = metrics.r2_score(y_val_1_1_scale, y_pred)
n = len(v1_val_1_1)
p = v1_val_1_1.shape[1]
adj_r2 = 1 - (1 - r2) * (n - 1) / (n - p - 1)
mse = metrics.mean_squared_error(y_val_1_1_scale, y_pred)
print("adj_r2:", round(adj_r2, 4))
print("MSE:", round(mse, 4))

# Model_1: unit_price
model = LinearRegression() 
model.fit(v5_train_1_2, y_train_1_2_scale)
y_pred = model.predict(v5_val_1_2)
r2 = metrics.r2_score(y_val_1_2_scale, y_pred)
n = len(v5_val_1_2)
p = v5_val_1_2.shape[1]
adj_r2 = 1 - (1 - r2) * (n - 1) / (n - p - 1)
mse = metrics.mean_squared_error(y_val_1_2_scale, y_pred)
print("adj_r2:", round(adj_r2, 4))
print("MSE:", round(mse, 4))

# Model_2: total_price
model = LinearRegression() 
model.fit(v1_train_2_1, y_train_2_1_scale)
y_pred = model.predict(v1_val_2_1)
r2 = metrics.r2_score(y_val_2_1_scale, y_pred)
n = len(v1_val_2_1)
p = v1_val_2_1.shape[1]
adj_r2 = 1 - (1 - r2) * (n - 1) / (n - p - 1)
mse = metrics.mean_squared_error(y_val_2_1_scale, y_pred)
print("adj_r2:", round(adj_r2, 4))
print("MSE:", round(mse, 4))

# Model_2: total_price
model = LinearRegression() 
model.fit(v1_train_2_2, y_train_2_2_scale)
y_pred = model.predict(v1_val_2_2)
r2 = metrics.r2_score(y_val_2_2_scale, y_pred)
n = len(v1_val_2_2)
p = v1_val_2_2.shape[1]
adj_r2 = 1 - (1 - r2) * (n - 1) / (n - p - 1)
mse = metrics.mean_squared_error(y_val_2_2_scale, y_pred)
print("adj_r2:", round(adj_r2, 4))
print("MSE:", round(mse, 4))

## polynomial regression(run origina & v1~v6)
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
import matplotlib.pyplot as plt
model = Pipeline([
    ("poly", PolynomialFeatures(degree = 2)),
    ("linreg", LinearRegression())])
model.fit(v6_train_2_2, y_train_2_2_scale)
y_pred = model.predict(v6_val_2_2)
mse = mean_squared_error(y_val_2_2_scale, y_pred)
r2 = r2_score(y_val_2_2_scale, y_pred)
n = len(v6_val_2_2)
p = v6_val_2_2.shape[1]
adj_r2 = 1 - (1 - r2) * (n - 1) / (n - p - 1)
mse = metrics.mean_squared_error(y_val_2_2_scale, y_pred)
print("adj_r2:", round(adj_r2, 4))
print("MSE:", round(mse, 4))


## SVR (run origina & v1~v6)
from sklearn.svm import SVR
# v1~v6
model = SVR(kernel='rbf', C = 1.0, gamma = 0.1)
model.fit(v6_train_1_1, y_train_1_1_scale)
y_pred = model.predict(v6_val_1_1)
r2 = r2_score(y_val_1_1_scale, y_pred)
n = len(v6_val_1_1)
p = v6_val_1_1.shape[1]
adj_r2 = 1 - (1 - r2) * (n - 1) / (n - p - 1)
mse = metrics.mean_squared_error(y_val_1_1_scale, y_pred)
print("adj_r2:", round(adj_r2, 4))
print("MSE:", round(mse, 4))


## Desision Tree (run origina & v1~v6)
from sklearn.tree import DecisionTreeRegressor
dec_result = []
model = DecisionTreeRegressor(max_depth = 5, random_state = 42)
model.fit(X_train_1_1_scale, y_train_1_1_scale)
y_pred = model.predict(X_val_1_1_scale)
r2 = r2_score(y_val_1_1_scale, y_pred)
n = len(X_val_1_1_scale)
p = X_val_1_1_scale.shape[1]
adj_r2 = 1 - (1 - r2) * (n - 1) / (n - p - 1)
mse = metrics.mean_squared_error(y_val_1_1_scale, y_pred)
print("adj_r2:", round(adj_r2, 4))
print("MSE:", round(mse, 4))


## Random forest (run origina & v1~v6)
from sklearn.ensemble import RandomForestRegressor
dec_result = []
model = RandomForestRegressor(max_depth = 5, random_state=42)  
model.fit(X_train_1_1_scale, y_train_1_1_scale)
y_pred = model.predict(X_val_1_1_scale)
r2 = r2_score(y_val_1_1_scale, y_pred)
n = len(X_val_1_1_scale)
p = X_val_1_1_scale.shape[1]
adj_r2 = 1 - (1 - r2) * (n - 1) / (n - p - 1)
mse = metrics.mean_squared_error(y_val_1_1_scale, y_pred)
dec_result.append(("O_1_1", round(adj_r2, 4), round(mse, 4)))


## Gradient Boosting Regression(run origina & v1~v6)
import xgboost as xgb
# Define the XGB regressor and set the hyperparameters
dec_result = []
model = xgb.XGBRegressor(objective ='reg:squarederror', colsample_bytree = 0.3, learning_rate = 0.1,
                max_depth = 5, alpha = 10, n_estimators = 10) 
model.fit(X_train_1_1_scale, y_train_1_1_scale)
y_pred = model.predict(X_val_1_1_scale)
r2 = r2_score(y_val_1_1_scale, y_pred)
n = len(X_val_1_1_scale)
p = X_val_1_1_scale.shape[1]
adj_r2 = 1 - (1 - r2) * (n - 1) / (n - p - 1)
mse = metrics.mean_squared_error(y_val_1_1_scale, y_pred)
dec_result.append(("O_1_1", round(adj_r2, 4), round(mse, 4)))



### hyperparameter tuning
from sklearn.model_selection import RandomizedSearchCV

## SVR tuning
# Model_1: total_price
result = []
model = SVR(kernel='rbf')
param_svr = {
    'C': [0.1, 1, 10, 100],
    'gamma': [0.01, 0.1, 1, 10]
}
# best parameters
rs = RandomizedSearchCV(model, param_distributions = param_svr, cv = 5, n_iter = 10, random_state = 42)
rs.fit(v6_train_1_1, y_train_1_1_scale)
# performace_val
best_1_1 = rs.best_estimator_
best_1_1.fit(v6_train_1_1, y_train_1_1_scale)
y_pred = best_1_1.predict(v6_val_1_1)
r2 = r2_score(y_val_1_1_scale, y_pred)
n = len(X_val_1_1_scale)
p = X_val_1_1_scale.shape[1]
adj_r2 = 1 - (1 - r2) * (n - 1) / (n - p - 1)
mse = metrics.mean_squared_error(y_val_1_1_scale, y_pred)
result.append((rs.best_estimator_, round(adj_r2, 4), round(mse, 4)))

# Model_1: unit_price
model = SVR(kernel='rbf')
param_svr = {
    'C': [0.1, 1, 10, 100],
    'gamma': [0.01, 0.1, 1, 10]
}
# best parameters
rs = RandomizedSearchCV(model, param_distributions = param_svr, cv = 5, n_iter = 10, random_state = 42)
rs.fit(v6_train_1_2, y_train_1_2_scale)
# performace_val
best_1_2 = rs.best_estimator_
best_1_2.fit(v6_train_1_2, y_train_1_2_scale)
y_pred = best_1_2.predict(v6_val_1_2)
r2 = r2_score(y_val_1_2_scale, y_pred)
n = len(X_val_1_2_scale)
p = X_val_1_2_scale.shape[1]
adj_r2 = 1 - (1 - r2) * (n - 1) / (n - p - 1)
mse = metrics.mean_squared_error(y_val_1_2_scale, y_pred)
result.append((rs.best_estimator_, round(adj_r2, 4), round(mse, 4)))


# Model_2: total_price
model = SVR(kernel='rbf')
param_svr = {
    'C': [0.1, 1, 10, 100],
    'gamma': [0.01, 0.1, 1, 10]
}
# best parameters
rs = RandomizedSearchCV(model, param_distributions = param_svr, cv = 5, n_iter = 10, random_state = 42)
rs.fit(v6_train_2_1, y_train_2_1_scale)
# performace_val
best_2_1 = rs.best_estimator_
best_2_1.fit(v6_train_2_1, y_train_2_1_scale)
y_pred = best_2_1.predict(v6_val_2_1)
r2 = r2_score(y_val_2_1_scale, y_pred)
n = len(X_val_2_1_scale)
p = X_val_2_1_scale.shape[1]
adj_r2 = 1 - (1 - r2) * (n - 1) / (n - p - 1)
mse = metrics.mean_squared_error(y_val_2_1_scale, y_pred)
result.append((rs.best_estimator_, round(adj_r2, 4), round(mse, 4)))

# Model_1: unit_price
model = SVR(kernel='rbf')
param_svr = {'C': [0.1, 1, 10, 100],
             'gamma': [0.01, 0.1, 1, 10]}
# best parameters
rs = RandomizedSearchCV(model, param_distributions = param_svr, cv = 5, n_iter = 10, random_state = 42)
rs.fit(v6_train_2_2, y_train_2_2_scale)
# performace_val
best_2_2 = rs.best_estimator_
best_2_2.fit(v6_train_2_2, y_train_2_2_scale)
y_pred = best_2_2.predict(v6_val_2_2)
r2 = r2_score(y_val_2_2_scale, y_pred)
n = len(X_val_2_2_scale)
p = X_val_2_2_scale.shape[1]
adj_r2 = 1 - (1 - r2) * (n - 1) / (n - p - 1)
mse = metrics.mean_squared_error(y_val_2_2_scale, y_pred)
result.append((rs.best_estimator_, round(adj_r2, 4), round(mse, 4)))


## polynomial
# Model_1: toal_price
model = Pipeline([("poly", PolynomialFeatures()),
                  ("linreg", LinearRegression())])
param_poly = {'poly__degree': [1, 2, 3],
          'linreg__fit_intercept': [True, False],
          'linreg__normalize': [True, False]}
# perform the random search cross-validation
rs = RandomizedSearchCV(model, param_distributions = param_poly, cv = 5, n_iter = 10, random_state = 42)
rs.fit(v6_train_1_1, y_train_1_1_scale)
print(rs.best_params_)
# performace_val
best_1_1 = rs.best_estimator_
best_1_1.fit(v6_train_1_1, y_train_1_1_scale)
y_pred = best_1_1.predict(v6_val_1_1)
r2 = r2_score(y_val_1_1_scale, y_pred)
n = len(X_val_1_1_scale)
p = X_val_1_1_scale.shape[1]
adj_r2 = 1 - (1 - r2) * (n - 1) / (n - p - 1)
mse = metrics.mean_squared_error(y_val_1_1_scale, y_pred)
result.append((rs.best_estimator_, round(adj_r2, 4), round(mse, 4)))
# best: (Pipeline(steps=[('poly', PolynomialFeatures(degree=3)),('linreg', LinearRegression(normalize=True))])

# Model_1: unit_price
model = Pipeline([("poly", PolynomialFeatures()),
                  ("linreg", LinearRegression())])
param_poly = {'poly__degree': [1, 2, 3],
          'linreg__fit_intercept': [True, False],
          'linreg__normalize': [True, False]}
# perform the random search cross-validation
rs = RandomizedSearchCV(model, param_distributions = param_poly, cv = 5, n_iter = 10, random_state = 42)
rs.fit(v6_train_1_2, y_train_1_2_scale)
print(rs.best_params_)
# performace_val
best_1_2 = rs.best_estimator_
best_1_2.fit(v6_train_1_2, y_train_1_2_scale)
y_pred = best_1_2.predict(v6_val_1_2)
r2 = r2_score(y_val_1_2_scale, y_pred)
n = len(X_val_1_2_scale)
p = X_val_1_2_scale.shape[1]
adj_r2 = 1 - (1 - r2) * (n - 1) / (n - p - 1)
mse = metrics.mean_squared_error(y_val_1_2_scale, y_pred)
result.append((rs.best_estimator_, round(adj_r2, 4), round(mse, 4)))
# bes: (Pipeline(steps=[('poly', PolynomialFeatures(degree=3)),('linreg', LinearRegression(normalize=True))])


# Model_2: total_price
model = Pipeline([("poly", PolynomialFeatures()),
                  ("linreg", LinearRegression())])
param_poly = {'poly__degree': [1, 2, 3],
          'linreg__fit_intercept': [True, False],
          'linreg__normalize': [True, False]}
# perform the random search cross-validation
rs = RandomizedSearchCV(model, param_distributions = param_poly, cv = 5, n_iter = 10, random_state = 42)
rs.fit(v6_train_2_1, y_train_2_1_scale)
print(rs.best_params_)
# performace_val
best_2_1 = rs.best_estimator_
best_2_1.fit(v6_train_2_1, y_train_2_1_scale)
y_pred = best_2_1.predict(v6_val_2_1)
r2 = r2_score(y_val_2_1_scale, y_pred)
n = len(X_val_2_1_scale)
p = X_val_2_1_scale.shape[1]
adj_r2 = 1 - (1 - r2) * (n - 1) / (n - p - 1)
mse = metrics.mean_squared_error(y_val_2_1_scale, y_pred)
result.append((rs.best_estimator_, round(adj_r2, 4), round(mse, 4)))
# best: (Pipeline(steps=[('poly', PolynomialFeatures(degree=3)),('linreg', LinearRegression(normalize=False))])


# Model_2: unit_price
model = Pipeline([("poly", PolynomialFeatures()),
                  ("linreg", LinearRegression())])
param_poly = {'poly__degree': [1, 2, 3],
          'linreg__fit_intercept': [True, False],
          'linreg__normalize': [True, False]}
# perform the random search cross-validation
rs = RandomizedSearchCV(model, param_distributions = param_poly, cv = 5, n_iter = 10, random_state = 42)
rs.fit(v6_train_2_2, y_train_2_2_scale)
print(rs.best_params_)
# performace_val
best_2_2 = rs.best_estimator_
best_2_2.fit(v6_train_2_2, y_train_2_2_scale)
y_pred = best_2_2.predict(v6_val_2_2)
r2 = r2_score(y_val_2_2_scale, y_pred)
n = len(X_val_2_2_scale)
p = X_val_2_2_scale.shape[1]
adj_r2 = 1 - (1 - r2) * (n - 1) / (n - p - 1)
mse = metrics.mean_squared_error(y_val_2_2_scale, y_pred)
result.append((rs.best_estimator_, round(adj_r2, 4), round(mse, 4)))
# best: (Pipeline(steps=[('poly', PolynomialFeatures(degree=3)),('linreg', LinearRegression(normalize=True))])


## random forest
# Model_1: total_price
result = []
model = RandomForestRegressor(random_state = 42)
param_rf = {'n_estimators': [100, 500, 1000],
              'max_features': ['auto', 'sqrt'],
              'max_depth': [5, 10, 15],
              'min_samples_split': [2, 5, 10],
              'min_samples_leaf': [1, 2, 4],
              'bootstrap': [True, False]}
# perform the random search cross-validation
rs = RandomizedSearchCV(model, param_distributions = param_rf, cv = 5, n_iter = 10, random_state = 42)
rs.fit(v6_train_1_1, y_train_1_1_scale) 
best_1_1 = rs.best_estimator_
best_1_1.fit(v6_train_1_1, y_train_1_1_scale)
y_pred = best_1_1.predict(v6_val_1_1)
r2 = r2_score(y_val_1_1_scale, y_pred)
n = len(X_val_1_1_scale)
p = X_val_1_1_scale.shape[1]
adj_r2 = 1 - (1 - r2) * (n - 1) / (n - p - 1)
mse = metrics.mean_squared_error(y_val_1_1_scale, y_pred)
result.append((rs.best_estimator_, round(adj_r2, 4), round(mse, 4)))
# {'n_estimators': 1000, 'min_samples_split': 2, 'min_samples_leaf': 1, 'max_features': 'sqrt', 'max_depth': 15, 'bootstrap': True}


# Model_1: unit_price
model = RandomForestRegressor(random_state = 42)
param_rf = {'n_estimators': [100, 500, 1000],
              'max_features': ['auto', 'sqrt'],
              'max_depth': [5, 10, 15],
              'min_samples_split': [2, 5, 10],
              'min_samples_leaf': [1, 2, 4],
              'bootstrap': [True, False]}
# perform the random search cross-validation
rs = RandomizedSearchCV(model, param_distributions = param_rf, cv = 5, n_iter = 10, random_state = 42)
rs.fit(v6_train_1_2, y_train_1_2_scale)
best_1_2 = rs.best_estimator_
best_1_2.fit(v6_train_1_2, y_train_1_2_scale)
y_pred = best_1_2.predict(v6_val_1_2)
r2 = r2_score(y_val_1_2_scale, y_pred)
n = len(X_val_1_2_scale)
p = X_val_1_2_scale.shape[1]
adj_r2 = 1 - (1 - r2) * (n - 1) / (n - p - 1)
mse = metrics.mean_squared_error(y_val_1_2_scale, y_pred)
result.append((rs.best_estimator_, round(adj_r2, 4), round(mse, 4)))
# {'n_estimators': 100, 'min_samples_split': 2, 'min_samples_leaf': 1, 'max_features': 'auto', 'max_depth': 15, 'bootstrap': True}


# Model_2: total_price
result = []
model = RandomForestRegressor(random_state = 42)
param_rf = {'n_estimators': [100, 500, 1000],
              'max_features': ['auto', 'sqrt'],
              'max_depth': [5, 10, 15],
              'min_samples_split': [2, 5, 10],
              'min_samples_leaf': [1, 2, 4],
              'bootstrap': [True, False]}
# perform the random search cross-validation
rs = RandomizedSearchCV(model, param_distributions = param_rf, cv = 5, n_iter = 10, random_state = 42)
rs.fit(v6_train_2_1, y_train_2_1_scale)
# performace_val
best_2_1 = rs.best_estimator_
best_2_1.fit(v6_train_2_1, y_train_2_1_scale)
y_pred = best_2_1.predict(v6_val_2_1)
r2 = r2_score(y_val_2_1_scale, y_pred)
n = len(X_val_2_1_scale)
p = X_val_2_1_scale.shape[1]
adj_r2 = 1 - (1 - r2) * (n - 1) / (n - p - 1)
mse = metrics.mean_squared_error(y_val_2_1_scale, y_pred)
result.append((rs.best_estimator_, round(adj_r2, 4), round(mse, 4)))
# best: (RandomForestRegressor(max_depth=15, max_features='sqrt', n_estimators=1000)

# Model_2: unit_price
model = RandomForestRegressor(random_state = 42)
param_rf = {'n_estimators': [100, 500, 1000],
              'max_features': ['auto', 'sqrt'],
              'max_depth': [5, 10, 15],
              'min_samples_split': [2, 5, 10],
              'min_samples_leaf': [1, 2, 4],
              'bootstrap': [True, False]}
# perform the random search cross-validation
rs = RandomizedSearchCV(model, param_distributions = param_rf, cv = 5, n_iter = 10, random_state = 42)
rs.fit(v6_train_2_2, y_train_2_2_scale)
# performace_val
best_2_2 = rs.best_estimator_
best_2_2.fit(v6_train_2_2, y_train_2_2_scale)
y_pred = best_2_2.predict(v6_val_2_2)
r2 = r2_score(y_val_2_2_scale, y_pred)
n = len(X_val_2_2_scale)
p = X_val_2_2_scale.shape[1]
adj_r2 = 1 - (1 - r2) * (n - 1) / (n - p - 1)
mse = metrics.mean_squared_error(y_val_2_2_scale, y_pred)
result.append((rs.best_estimator_, round(adj_r2, 4), round(mse, 4)))
# best: (RandomForestRegressor(max_depth=15, random_state=42), 0.8998, 0.0028)

'''for 4 models, random forest are the best'''



## model testing
from sklearn.metrics import r2_score, mean_squared_error
# Model_1_1
result = []
param_rf = {'n_estimators': 1000,
              'max_features': 'sqrt',
              'max_depth': 15,
              'min_samples_split': 2,
              'min_samples_leaf': 1,
              'bootstrap': True}
model = RandomForestRegressor(**param_rf, random_state=42)  
model.fit(v6_train_1_1, y_train_1_1_scale)
y_pred = model.predict(v6_test_1_1)
r2 = r2_score(y_test_1_1_scale, y_pred)
n = len(v6_test_1_1)
p = v6_test_1_1.shape[1]
adj_r2 = 1 - (1 - r2) * (n - 1) / (n - p - 1)
mse = metrics.mean_squared_error(y_test_1_1_scale, y_pred)
result.append(("O_1_1", round(adj_r2, 4), round(mse, 4)))

# Model_1_2
param_rf = {'n_estimators': 100,
              'max_features': 'auto',
              'max_depth': 15,
              'min_samples_split': 2,
              'min_samples_leaf': 1,
              'bootstrap': True}
model = RandomForestRegressor(**param_rf, random_state=42)  
model.fit(v6_train_1_2, y_train_1_2_scale)
y_pred = model.predict(v6_test_1_2)
r2 = r2_score(y_test_1_2_scale, y_pred)
n = len(v6_test_1_2)
p = v6_test_1_2.shape[1]
adj_r2 = 1 - (1 - r2) * (n - 1) / (n - p - 1)
mse = metrics.mean_squared_error(y_test_1_2_scale, y_pred)
result.append(("O_1_2", round(adj_r2, 4), round(mse, 4)))

# Model_2_1
param_rf = {'n_estimators': 1000,
              'max_features': 'sqrt',
              'max_depth': 15}
model = RandomForestRegressor(**param_rf, random_state=42)  
model.fit(v6_train_1_2, y_train_1_2_scale)
y_pred = model.predict(v6_test_1_2)
r2 = r2_score(y_test_1_2_scale, y_pred)
n = len(v6_test_1_2)
p = v6_test_1_2.shape[1]
adj_r2 = 1 - (1 - r2) * (n - 1) / (n - p - 1)
mse = metrics.mean_squared_error(y_test_1_2_scale, y_pred)
result.append(("O_2_1", round(adj_r2, 4), round(mse, 4)))

# Model_2_2
param_rf = {'max_depth': 15}
model = RandomForestRegressor(**param_rf, random_state=42)  
model.fit(v6_train_2_2, y_train_2_2_scale)
y_pred = model.predict(v6_test_2_2)
r2 = r2_score(y_test_2_2_scale, y_pred)
n = len(v6_test_2_2)
p = v6_test_2_2.shape[1]
adj_r2 = 1 - (1 - r2) * (n - 1) / (n - p - 1)
mse = metrics.mean_squared_error(y_test_2_2_scale, y_pred)
result.append(("O_2_2", round(adj_r2, 4), round(mse, 4)))
